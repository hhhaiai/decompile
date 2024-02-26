//
// Load a SYM file with Dialog
// Saved the last browsed path associated with the extension in the Database
// (use with dbg2map and mapsym)
//
// History:
//
// v1.00 - This file is originally donated by David Cattley.
// v1.07 - Bugfix, improved interface, handles larger SegDefs
// v1.08 - extended for save tha last used path associaded with *.sym in the current database
//         set VAC to 0 for aktivating v1.07
//         set VAC to 1 for sym-files from IBM/Microsoft MAPSYM for OS/2 (Loadsym V1.00)
//

#include <idc.idc>

#define VERBOSE 1

// set to version before IDA 4.30, for mapsym.exe VAC, not found any informations about the last changes
#define VAC 1

static main(void)
{
        auto    symFileName, symFile;

        symFileName = AskFileEx(0,"*.sym","Choose the symbol-file");

        if(symFileName=="")
          { if(VERBOSE) msg("Operation cancelled by user.\n");
            return -1; }

        if(VERBOSE)     msg("Opening symbol file %s\n", symFileName);
        symFile = fopen(symFileName, "rb");

        if (0 != symFile)
        {
                auto nextMapDef;

                //
                // Process all of the MAPDEF's in this file.
                //
                // if(VERBOSE)     msg("%0.4x: ", ftell(symFile));
                if(VERBOSE)     msg("Processing %s\n", symFileName);

                nextMapDef = 0;

                do
                {
                        nextMapDef = DoMapDef(symFile, nextMapDef);
                }
                while (0 != nextMapDef);
        }
        else
        { if(VERBOSE) msg("Can't open symbol file:\n%s\n", symFileName);
          return -1;
        }
        if(VERBOSE) msg("Symbol file has been loaded successfully.\n");
}


static DoMapDef(File, Position)
{
        auto    ppNextMap;

        //
        // Process the specified MAPDEF structure.
        //
        fseek(File, Position, 0);

        if(VERBOSE)     msg("%0.4x: ", ftell(File));

        ppNextMap = readshort(File, 0);

        if (0 == ppNextMap)
        {
                //
                // This is the last one!  It is special.
                //
                auto release, version;

                release = fgetc(File);
                version = fgetc(File);

                if(VERBOSE)     msg("VERSION Next:%x Release:%x Version:%x\n",
                                ppNextMap,
                                release,
                                version
                                );
        }
        else
        {
                auto    bFlags, bReserved1, pSegEntry,
                                cConsts, pConstDef, cSegs, ppSegDef,
                                cbMaxSym, achModName;

                auto i, nextSegDef;

                bFlags = fgetc(File);
                bReserved1 = fgetc(File);
                pSegEntry = readshort(File, 0);
                cConsts = readshort(File, 0);
                pConstDef = readshort(File, 0);
                cSegs = readshort(File, 0);
                ppSegDef = readshort(File, 0);
                cbMaxSym = fgetc(File);
                achModName = ReadSymName(File);

                if(VERBOSE)     msg("MAPDEF Next:%x Flags:%x Entry:%x Con:%d@%x Seg:%d@%x Max:%d Mod:%s\n",
                                ppNextMap,
                                bFlags,
                                pSegEntry,
                                cConsts, pConstDef,
                                cSegs, ppSegDef,
                                cbMaxSym,
                                achModName
                                );

                //
                // Process the SEGDEFs in this MAPDEF
                //
                nextSegDef = ppSegDef << 4;

                for (i=0; i<cSegs; i=i+1)
                {
                        nextSegDef = DoSegDef(File, nextSegDef);
                }
        }

        //
        // Return the file position of the next MAPDEF
        //
        return (ppNextMap << 4);
}


static DoSegDef(File, Position)
{
        auto    ppNextSeg, cSymbols, pSymDef,
                        wSegNum, wReserved2, wReserved3, wReserved4,
                        bFlags, bReserved1, ppLineDef, bReserved2,
                        bReserved3, achSegName;

        auto i, n, symPtr, segBase;

        //
        // Process the specified SEGDEF structure.
        //
        fseek(File, Position, 0);

        if(VERBOSE)     msg("%0.4x: ", ftell(File));

        ppNextSeg = readshort(File, 0);
        cSymbols = readshort(File, 0);
        pSymDef = readshort(File, 0);
        wSegNum = readshort(File, 0);
        wReserved2 = readshort(File, 0);
        wReserved3 = readshort(File, 0);
        wReserved4 = readshort(File, 0);
        bFlags = fgetc(File);
        bReserved1 = fgetc(File);
        ppLineDef = readshort(File, 0);
        bReserved2 = fgetc(File);
        bReserved3 = fgetc(File);
        achSegName = ReadSymName(File);

        if (VAC) {
          segBase = get_segm_by_sel(wSegNum);
       // the others will access the externals, sym-files from MAPSYM contains only internals
        } else {
       // segBase = get_segm_by_sel(wSegNum); //fixed
          segBase = get_first_seg();
          for (i=wSegNum; i > 1; i=i-1) { segBase = get_next_seg(segBase); }
        }
        if(VERBOSE)     msg("SEGDEF Next:%x Sym:(%d)@%x Flags:%x Lines:%x Seg:%s [%04x %08x]\n",
                        ppNextSeg,
                        cSymbols, pSymDef,
                        bFlags,
                        ppLineDef,
                        achSegName, wSegNum, segBase
                        );

        //
        // Process the symbols in this SEGDEF
        //
        n = 2;
        if (!VAC) {
       // sym-files from MAPSYM (VAC) works with unshifted pSymDef
           pSymDef = pSymDef << (bFlags & 0xFE);
           if ((bFlags & 0xFE) != 0) n++;
        }
        for (i=0; i<cSymbols; i=i+1)
        {
             // fseek(File, Position+pSymDef+(i*2), 0); //fixed
                fseek(File, Position+pSymDef+(i*n), 0);
                if (n>2) symPtr = Position+(readlong(File, 0)&0xFFFFFF);
                else symPtr = Position+readshort(File, 0);
                DoSymDef(File, symPtr, (bFlags & 1), wSegNum);
        }

        //
        //  Return the position of the next SEGDEF
        //
        return (ppNextSeg << 4);
}


static DoSymDef(File, Position, Size, Segment)
{
        auto dwSymVal, achSymName, ea, i;

        fseek(File, Position, 0);

        if(VERBOSE)     msg("%0.4x: ", ftell(File));

        if (0 == Size)
                dwSymVal = readshort(File, 0);
        else
                dwSymVal = readlong(File, 0);

        achSymName = ReadSymName(File);

        //
        // Calculate the EA of this symbols.
        //
        if (VAC) {
          ea = get_segm_by_sel(Segment) + dwSymVal;
     // sym-files from MAPSYM contains only internals
        } else {
       // ea = get_segm_by_sel(Segment) + dwSymVal; // fixed
          ea = get_first_seg(); // This points to the externals ???
          for (i=Segment; i > 1; i=i-1) { ea = get_next_seg(ea); }
          ea = ea + dwSymVal;
        }

        if(VERBOSE)     msg("SYM%d: %04x:%08x [%08x] %s\n",
                        (16+Size*16),
                        Segment, dwSymVal, ea,
                        achSymName);

        //
        // Now go and name the location!
        //
        set_name(ea, "");
        set_name(ea, achSymName);
}


static ReadSymName(symFile)
{
        auto i, nameLen, name;

        name = "";
        nameLen = fgetc(symFile);

        for (i=0; i<nameLen; i=i+1)
        {
                name = name + fgetc(symFile);
        }

        return(name);
}

static getPath(fileName) {
	auto	pos, path;
	path = "";
	while (1) {
		pos = strstr(fileName,"\\");
		if (-1 == pos) break;
		path = path + substr(fileName,0,pos+1);
		fileName = substr(fileName,pos+1,-1);
	}
	return path;
}

static AskFileEx(forSave, ext, dialogText) {
	auto	fileName, w, p, extArrayId, lastPath, newPath, extKey;
	w = ext;
	if (substr(w,0,1) == "*") w = substr(w,1,-1);
	if (substr(w,0,1) == ".") w = substr(w,1,-1);
/* is case-sensitive */
	extKey = "DT#"+w;
	extArrayId = get_array_id("DT#EXT#Array");
	if (-1 == extArrayId)
		extArrayId = create_array("DT#EXT#Array");
	lastPath = get_hash_string(extArrayId,extKey);
/* without this, we have at first only '*' as Mask, but not "*.ext". IDA 4.20 */
	if ("" == lastPath)
		lastPath = getPath(get_input_file_path());
	w = lastPath+"*."+w;
	if(VERBOSE)	msg("--> lastPath %s\n", w);
	fileName = askfile(forSave,w,dialogText);
	if (("" == fileName) | (-1 == extArrayId))
		return fileName;
	newPath = getPath(fileName);
	if (("" != newPath) & (lastPath != newPath))
// Save the new path, associated with the extension in the Database
		set_hash_string(extArrayId, extKey, newPath);
	return fileName;
}

