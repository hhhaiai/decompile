################################################################################################
# bFLT v4 loader for IDA
#
# Identifies and sets appropriate data segments.
# Patches relocation and GOT addresses so that string and data references are resolved properly.
#
# Craig Heffner
# Tactical Network Solutions
# 06-March-2011
################################################################################################

BFLT_VERSION          = 4
BFLT_MAGIC            = b"bFLT"
BFLT_HEADER_SIZE      = 0x40
FLAGS_RAM             = 0x01
FLAGS_GOTPIC          = 0x02
FLAGS_GZIP            = 0x04
DEFAULT_CPU           = "Coldfire"
DEBUG                 = True

import struct

import idaapi
import ida_idp
import idc

def accept_file(li, filename):

        li.seek(0)

        # Make sure this is a bFLT v4 file
        if li.read(4) == BFLT_MAGIC and struct.unpack(">I", li.read(4))[0] == BFLT_VERSION:
            return {'format': "%s v%d executable" % (BFLT_MAGIC, BFLT_VERSION),
                    'processor': DEFAULT_CPU}
        return 0


def load_file(li, neflags, format):

        # Set default processor
        idaapi.set_processor_type(DEFAULT_CPU, ida_idp.SETPROC_LOADER)

        # Read in the bFLT header fields
        li.seek(0)
        (magic, version, entry, data_start, data_end, bss_end, stack_size, reloc_start, reloc_count, flags) = struct.unpack(">IIIIIIIIII", li.read(4*10))

        # Check for the GZIP flag.
        # The loader doesn't de-compress GZIP'd files, as these can be easily decompressed with external tools prior to loading the file into IDA
        if (flags & FLAGS_GZIP) == FLAGS_GZIP:
                warning("Code/data is GZIP compressed. You probably want to decompress the bFLT file with the flthdr or gunzip_bflt utilities before loading it into IDA.")

        # Load the file data into IDA
        li.file2base(BFLT_HEADER_SIZE, BFLT_HEADER_SIZE, data_end, True)

        # Add the .text .data and .bss segments
        idaapi.add_segm(0, BFLT_HEADER_SIZE, data_start, ".text", "CODE")
        idaapi.add_segm(0, data_start, data_end, ".data", "DATA")
        idaapi.add_segm(0, data_end, bss_end, ".bss", "BSS", idaapi.ADDSEG_SPARSE)

        if DEBUG:
                print("Created File Segments: ")
                print("\t.text   0x%.8X - 0x%.8X" % (BFLT_HEADER_SIZE, data_start))
                print("\t.data   0x%.8X - 0x%.8X" % (data_start, data_end))
                print("\t.bss    0x%.8X - 0x%.8X" % (data_end, bss_end))

        # Entry point is at the beginning of the .text section
        idaapi.add_entry(entry, entry, "_start", 1)

        # Explicitly set 32 bit addressing on .text segment
        idaapi.set_segm_addressing(idaapi.getseg(entry), 1)

        # prepare structure for set_fixup()
        fd = idaapi.fixup_data_t(idaapi.FIXUP_OFF32)

        # Is there a global offset table?
        if (flags & FLAGS_GOTPIC) == FLAGS_GOTPIC:

                # Add a reptable comment and name the offset so that all references to GOT are obvious
                idc.set_cmt(data_start, "GLOBAL_OFFSET_TABLE", 1)
                idc.set_name(data_start, "GOT")

                if DEBUG:
                        print("Global Offset Table detected, patching...")

                # GOT starts at the beginning of the data section; loop through the data section, patching up valid GOT entries.
                i = data_start
                while i < data_end:

                        # Get the next GOT entry
                        li.seek(i)
                        got_entry = struct.unpack("<I", li.read(4))[0]

                        # The last GOT entry is -1
                        if got_entry == 0xFFFFFFFF:
                                if DEBUG:
                                        print("Finished processing Global Offset Table.")
                                break

                        # All other non-zero entries are valid GOT entries
                        elif got_entry > 0:

                                # The actual data is located at <original GOT entry> + <BFLT_HEADER_SIZE>
                                new_entry = got_entry + BFLT_HEADER_SIZE

                                if DEBUG:
                                        print("Replacing GOT entry value 0x%.8X with 0x%.8X at offset 0x%.8X" % (got_entry, new_entry, i))

                                # Replace the GOT entry with the correct pointer
                                idaapi.put_dword(i, new_entry)
                                # add info about relocation to help analyzer
                                fd.off = new_entry
                                fd.set(i)

                        # Make each GOT entry a DWORD
                        idc.create_dword(i)

                        # Point i at the next GOT entry address
                        i = i + 4

        # Patch relocation addresses
        for i in range(0, reloc_count):
                try:
                        # Get the next relocation entry.
                        # Relocation entry = <address of bytes to be patched> - <BFLT_HEADER_SIZE>
                        li.seek(reloc_start + (i * 4))
                        reloc_offset = struct.unpack(">I", li.read(4))[0] + BFLT_HEADER_SIZE

                        # Sanity check, make sure the relocation offset is in a defined segment
                        if reloc_offset < bss_end:
                                try:
                                        # reloc_offset + base_offset == <pointer to actual data> - <BFLT_HEADER_SIZE>
                                        li.seek(reloc_offset)
                                        reloc_val = struct.unpack(">I", li.read(4))[0]
                                        if reloc_val == 0:
                                                # skip zero relocs
                                                # see fs/binfmt_flat.c
                                                if DEBUG:
                                                        print("Skipping zero reloc at (0x%.8X)" % reloc_offset)
                                                continue

                                        reloc_data_offset = reloc_val + BFLT_HEADER_SIZE

                                        if DEBUG:
                                                print("Patching reloc: (0x%.8X) == 0x%.8X" % (reloc_offset, reloc_data_offset))

                                        # Replace pointer at reloc_offset with the address of the actual data
                                        idaapi.put_dword(reloc_offset, reloc_data_offset)
                                        # add info about relocation to help analyzer
                                        fd.off = reloc_data_offset
                                        fd.set(reloc_offset)
                                except Exception as e:
                                        print("Error patching relocation entry #%d: %s" % (i, str(e)))
                        elif DEBUG:
                                print("Relocation entry #%d outside of defined file sections, skipping..." % i)
                except Exception as e:
                        print("Error processing relocation entry #%d: %s" % (i, str(e)))

        return 1
