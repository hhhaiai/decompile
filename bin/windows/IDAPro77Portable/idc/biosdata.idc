//
//      This script creates a segment at paragraph 0x40 and
//      makes comments to BIOS data area. To see mnemonical names of
//      BIOS data area variables, please use this file:
//
//        - press F2 when running IDA
//        - select this file
//

#include <idc.idc>

//-------------------------------------------------------------------------
static CW(off,name,cmt) {
  auto x;
  x = 0x400 + off;
  create_word(x);
  set_name(x,name);
  set_cmt(x,cmt, 1);
}

//-------------------------------------------------------------------------
static CD(off,name,cmt) {
  auto x;
  x = 0x400 + off;
  create_dword(x);
  set_name(x,name);
  set_cmt(x,cmt, 1);
}

//-------------------------------------------------------------------------
static CB(off,name,cmt) {
  auto x;
  x = 0x400 + off;
  create_byte(x);
  set_name(x,name);
  set_cmt(x,cmt, 1);
}

//-------------------------------------------------------------------------
static CmtBdata() {
 CW(0x000,"com_port_1","Base I/O address of 1st serial I/O port");
 CW(0x002,"com_port_2","Base I/O address of 2nd serial I/O port");
 CW(0x004,"com_port_3","Base I/O address of 3rd serial I/O port");
 CW(0x006,"com_port_4","Base I/O address of 4th serial I/O port");

 CW(0x008,"prn_port_1","Base I/O address of 1st parallel I/O port");
 CW(0x00A,"prn_port_2","Base I/O address of 2nd parallel I/O port");
 CW(0x00C,"prn_port_3","Base I/O address of 3rd parallel I/O port");
 CW(0x00E,"prn_port_4","Base I/O address of 4th parallel I/O port");

 CW(0x010,"equip_bits",         "Equipment installed info bits\n"
                                "15  14  13   12   11  10   9   8\n"
                                "\\    /      game  \\       /\n"
                                "# of print  port  # of RS-232\n"
                                "ports 0-3   used   ports 0-4\n"
                                "\n"
                                "7   6    5    4    3   2   1   0\n"
                                "\\   /    \\    /    \\   / Math  |\n"
                                "# of   video mode  RAM    uP  no\n"
                                "disk-  at boot up  00=16K    dsk\n"
                                "ettes  00=EGA/VGA  01=32K   driv\n"
                                " 1-4   01=CGA-40   10=48K   if 0\n"
                                "if bit 10=CGA-80   11=64K\n"
                                "0 = 1  11=MDA-80   (old PCs)\n"
                                "\n"
                                "Note: bit 13=modem on PC lap-tops\n"
                                "      bit 2=mouse on MCA & others");

 CB(0x012,"manufactr_test",     "Manufacturing Test get_wide_byte\n"
                                "bit 0 = 1 while in test mode\n"
                                "MCA systems use other bits\n"
                                "  during POST operations");
 CW(0x013,"base_ram_size",      "Base memory size in KBytes (0-640)");

 CB(0x015,"mtest_scratchpad",   "[AT] {Manufacturing test scratch pad}\n"
                                "[Compaq Deskpro 386] previous scan code");
 CB(0x016,"error_codes",        "[AT] {Manufacturing test scratch pad}\n"
                                "[PS/2 Mod 30] {BIOS control flags}\n"
                                "[Compaq Deskpro 386] keyclick loudness (00h-7Fh)");
 CB(0x017,"keybd_flags_1",      "Keyboard flag bits\n"
                                "  7   6   5   4    3   2   1   0\n"
                                "ins- cap num scrl alt ctl lef rig\n"
                                "sert --toggles--- --shifts down--");
 CB(0x018,"keybd_flags_2",      "Keyboard flag bits\n"
                                "   7     6     5     4   \n"
                                "insert  caps  num  scroll\n"
                                "------now depressed------\n"
                                "\n"
                                "   3     2     1     0\n"
                                " pause  sys   left right\n"
                                " lock request -alt-down-");
 CB(0x019,"keybd_alt_num",      "Alt-nnn keypad workspace");
 CW(0x01A,"keybd_q_head",       "pointer to next character in keyboard buffer");
 CW(0x01C,"keybd_q_tail",       "pointer to first free slot in keyboard buffer");
 CW(0x01E,"keybd_queue",        "Keyboard circular buffer");
 make_array(0x41E, 16 );
 CB(0x03E,"dsk_recal_stat",     "Recalibrate floppy drive bits\n"
                                "   3       2       1       0\n"
                                "drive-3 drive-2 drive-1 drive-0\n"
                                "\n"
                                "bit 7 = interrupt flag");
 CB(0x03F,"dsk_motor_stat",     "Motor running status & disk write\n"
                                " bit 7=1 disk write in progress\n"
                                " bits 6&5 = drive selected 0 to 3\n"
                                "    3       2       1       0\n"
                                " drive-3 drive-2 drive-1 drive-0\n"
                                " --------- 1=motor on-----------");
 CB(0x040,"dsk_motor_timer",    "Motor timer, at 0, turn off motor");
 CB(0x041,"dsk_ret_code",       "Controller return code\n"
                                " 00h = ok\n"
                                " 01h = bad command or parameter\n"
                                " 02h = can't find address mark\n"
                                " 03h = can't write, protected dsk\n"
                                " 04h = sector not found\n"
                                " 08h = DMA overrun\n"
                                " 09h = DMA attempt over 64K bound\n"
                                " 10h = bad CRC on disk read\n"
                                " 20h = controller failure\n"
                                " 40h = seek failure\n"
                                " 80h = timeout, no response");

 CB(0x042,"dsk_status_1",       "Status bytes-disk controller chip\n"
                                " Note: 7 info bytes returned from\n"
                                " controller are saved here. Refer\n"
                                " to the NEC uPD 765 chip manual\n"
                                " for the specific info, depending\n"
                                " on the previous command issued.");
 CB(0x043,"dsk_status_2",       "");
 CB(0x044,"dsk_status_3",       "");
 CB(0x045,"dsk_status_4",       "");
 CB(0x046,"dsk_status_5",       "");
 CB(0x047,"dsk_status_6",       "");
 CB(0x048,"dsk_status_7",       "");

 CB(0x049,"video_mode",         "Present display mode");
 CW(0x04A,"video_columns",      "Number of columns");
 CW(0x04C,"video_buf_size",     "Video buffer size in bytes\n"
                                "  Note: size may be rounded up to\n"
                                "  the nearest 2K boundary.  For\n"
                                "  example, 80x25 mode=4000 bytes,\n"
                                "  but value may be 4096.");
 CW(0x04E,"video_pageoff",      "Video page offset of the active\n"
                                "  page, from start of current \n"
                                "  video segment.");
 CW(0x050,"vid_curs_pos0",      "Cursor position page 0\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x052,"vid_curs_pos1",      "Cursor position page 1\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x054,"vid_curs_pos2",      "Cursor position page 2\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x056,"vid_curs_pos3",      "Cursor position page 3\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x058,"vid_curs_pos4",      "Cursor position page 4\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x05A,"vid_curs_pos5",      "Cursor position page 5\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x05C,"vid_curs_pos6",      "Cursor position page 6\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x05E,"vid_curs_pos7",      "Cursor position page 7\n"
                                "  bits 15-8=row, bits 7-0=column");
 CW(0x060,"vid_curs_mode",      "Active cursor, start & end lines \n"
                                "  bits 12 to 8 for starting line\n"
                                "  bits 4  to 0 for ending line");
 CB(0x062,"video_page",         "Present page");
 CW(0x063,"video_port",         "Video controller base I/O address");
 CB(0x065,"video_mode_reg",     "Hardware mode register bits");
 CB(0x066,"video_color",        "Color set in CGA modes");
 CW(0x067,"gen_use_ptr",        "General use offset pointer");
 CW(0x069,"gen_use_seg",        "General use segment pointer");
 CB(0x06B,"gen_int_occurd",     "Unused interrupt occurred\n"
                                "  value holds the IRQ bit 7-0 of\n"
                                "  the interrupt that occurred");
 CW(0x06C,"timer_low",          "Timer, low word, cnts every 55 ms");
 CW(0x06E,"timer_high",         "Timer, high word");
 CB(0x070,"timer_rolled",       "Timer overflowed, set to 1 when\n"
                                " more than 24 hours have elapsed");
 CB(0x071,"keybd_break",        "Bit 7 set if break key depressed");
 CW(0x072,"warm_boot_flag",     "Boot (reset) type\n"
                                "  1234h=warm boot, no memory test       \n"
                                "  4321h=boot & save memory");
 CB(0x074,"hdsk_status_1",      "Hard disk status\n"
                                " 00h = ok\n"
                                " 01h = bad command or parameter\n"
                                " 02h = can't find address mark\n"
                                " 03h = can't write, protected dsk\n"
                                " 04h = sector not found\n"
                                " 05h = reset failure\n"
                                " 07h = activity failure\n"
                                " 08h = DMA overrun\n"
                                " 09h = DMA attempt over 64K bound\n"
                                " 0Ah = bad sector flag\n"
                                " 0Bh = removed bad track\n"
                                " 0Dh = wrong # of sectors, format\n"
                                " 0Eh = removed control data addr\n"
                                "        mark\n"
                                " 0Fh = out of limit DMA\n"
                                "        arbitration level\n"
                                " 10h = bad CRC or ECC, disk read\n"
                                " 11h = bad ECC corrected data\n"
                                " 20h = controller failure\n"
                                " 40h = seek failure\n"
                                " 80h = timeout, no response\n"
                                " AAh = not ready\n"
                                " BBh = error occurred, undefined\n"
                                " CCh = write error, selected dsk\n"
                                " E0h = error register = 0\n"
                                " FFh = disk sense failure");
 CB(0x075,"hdsk_count",         "Number of hard disk drives");
 CB(0x076,"hdsk_head_ctrl",     "Head control (XT only)");
 CB(0x077,"hdsk_ctrl_port",     "Hard disk control port (XT only)");
 CB(0x078,"prn_timeout_1",      "Countdown timer waits for printer\n"
                                "  to respond (printer 1)");
 CB(0x079,"prn_timeout_2",      "Countdown timer waits for printer\n"
                                "  to respond (printer 2)");
 CB(0x07A,"prn_timeout_3",      "Countdown timer waits for printer\n"
                                "  to respond (printer 3)");
 CB(0x07B,"prn_timeout_4",      "Countdown timer waits for printer\n"
                                "  to respond (printer 4)");
 CB(0x07C,"rs232_timeout_1",    "Countdown timer waits for RS-232 (1)");
 CB(0x07D,"rs232_timeout_2",    "Countdown timer waits for RS-232 (2)");
 CB(0x07E,"rs232_timeout_3",    "Countdown timer waits for RS-232 (3)");
 CB(0x07F,"rs232_timeout_4",    "Countdown timer waits for RS-232 (4)");
 CW(0x080,"keybd_begin",        "Ptr to beginning of keybd queue");
 CW(0x082,"keybd_end",          "Ptr to end of keyboard queue");
 CB(0x084,"video_rows",         "Rows of characters on display - 1");
 CW(0x085,"video_pixels",       "Number of pixels per charactr * 8");
 CB(0x087,"video_options",      "Display adapter options\n"
                                "  bit 7 = clear RAM\n"
                                "  bits 6,5 = memory on adapter\n"
                                "              00 - 64K\n"
                                "              01 - 128K\n"
                                "              10 - 192K\n"
                                "              11 - 256K\n"
                                "  bit 4 = unused\n"
                                "  bit 3 = 0 if EGA/VGA active\n"
                                "  bit 2 = wait for display enable\n"
                                "  bit 1 = 1 - mono monitor\n"
                                "        = 0 - color monitor\n"
                                "  bit 0 = 0 - handle cursor, CGA");
 CB(0x088,"video_switches",     "Switch setting bits from adapter\n"
                                "  bits 7-4 = feature connector\n"
                                "  bits 3-0 = option switches");
 CB(0x089,"video_1_save",       "Video save area 1-EGA/VGA control\n"
                                "  bit 7 = 200 line mode\n"
                                "  bits 6,5 = unused\n"
                                "  bit 4 = 400 line mode\n"
                                "  bit 3 = no palette load\n"
                                "  bit 2 = mono monitor\n"
                                "  bit 1 = gray scale\n"
                                "  bit 0 = unused");
 CB(0x08A,"video_2_save",       "Video save area 2");

 CB(0x08B,"dsk_data_rate",      "Last data rate for diskette\n"
                                " bits 7 & 6 = 00 for 500K bit/sec\n"
                                "            = 01 for 300K bit/sec\n"
                                "            = 10 for 250K bit/sec\n"
                                "            = 11 for 1M bit/sec\n"
                                " bits 5 & 4 = step rate"
                                "Rate at start of operation\n"
                                " bits 3 & 2 = 00 for 500K bit/sec\n"
                                "            = 01 for 300K bit/sec\n"
                                "            = 10 for 250K bit/sec\n"
                                "            = 11 for 1M bit/sec");
 CB(0x08C,"hdsk_status_2",      "Hard disk status");
 CB(0x08D,"hdsk_error",         "Hard disk error");
 CB(0x08E,"hdsk_complete",      "When the hard disk controller's\n"
                                " task is complete, this byte is\n"
                                " set to FFh (from interrupt 76h)");
 CB(0x08F,"dsk_options",        "Diskette controller information\n"
                                " bit 6 = 1 Drv 1 type determined\n"
                                "     5 = 1 Drv 1 is multi-rate\n"
                                "     4 = 1 Drv 1 change detect\n"
                                "     2 = 1 Drv 0 type determined\n"
                                "     1 = 1 Drv 0 is multi-rate\n"
                                "     0 = 1 Drv 0 change detect");
 CB(0x090,"dsk0_media_st",      "Media state for diskette drive 0\n"
                                "    7      6      5      4\n"
                                " data xfer rate  two   media\n"
                                "  00=500K bit/s  step  known\n"
                                "  01=300K bit/s\n"
                                "  10=250K bit/s\n"
                                "  11=1M bit/sec\n"
                                "    3      2      1      0\n"
                                " unused  -----state of drive-----\n"
                                "         bits floppy  drive state\n"
                                "         000=  360K in 360K, ?\n"
                                "         001=  360K in 1.2M, ?\n"
                                "         010=  1.2M in 1.2M, ?\n"
                                "         011=  360K in 360K, ok\n"
                                "         100=  360K in 1.2M, ok\n"
                                "         101=  1.2M in 1.2M, ok\n"
                                "         111=  720K in 720K, ok\n"
                                "           or 1.44M in 1.44M\n"
                                "        (state not used for 2.88)");
 CB(0x091,"dsk1_media_st",      "Media state for diskette drive 1\n"
                                " (see dsk0_media_st)");
 CB(0x092,"dsk0_start_st",      "Starting state for drive 0");
 CB(0x093,"dsk1_start_st",      "Starting state for drive 1");
 CB(0x094,"dsk0_cylinder",      "Current track number for drive 0");
 CB(0x095,"dsk1_cylinder",      "Current track number for drive 1");
 CB(0x096,"keybd_flags_3",      "Special keyboard type and mode\n"
                                " bit 7 Reading ID of keyboard\n"
                                "     6 last char is 1st ID char\n"
                                "     5 force num lock\n"
                                "     4 101/102 key keyboard\n"
                                "     3 right alt key down\n"
                                "     2 right ctrl key down\n"
                                "     1 E0h hidden code last\n"
                                "     0 E1h hidden code last");
 CB(0x097,"keybd_flags_4",      "Keyboard Flags (advanced keybd)\n"
                                "  7      6       5     4  3 2 1 0\n"
                                "xmit   char   Resend  Ack   \   /\n"
                                "error was ID  Rec'd  Rec'd   LEDs");

 CW(0x098,"timer_waitoff",      "Ptr offset to wait done flag");
 CW(0x09A,"timer_waitseg",      "Ptr segment to wait done flag");
 CW(0x09C,"timer_clk_low",      "Timer low word, 1 microsecond clk");
 CW(0x09E,"timer_clk_high",     "Timer high word");
 CB(0x0A0,"timer_clk_flag",     "Timer flag 00h = post acknowledgd\n"
                                "           01h = busy\n"
                                "           80h = posted");
 CB(0x0A1,"lan_bytes",          "Local area network bytes (7)");
 make_array(0x4A1, 7);

 CD(0x0A8,"video_sav_tbl",      "Pointer to a save table of more\n"
                                "pointers for the video system \n"
                                "           SAVE TABLE\n"
                                " offset type    pointer to\n"
                                " ------ ---- --------------------\n"
                                "   0     dd  Video parameters\n"
                                "   4     dd  Parms save area\n"
                                "   8     dd  Alpha char set\n"
                                "  0Ch    dd  Graphics char set\n"
                                "  10h    dd  2nd save ptr table\n"
                                "  14h    dd  reserved (0:0)\n"
                                "  18h    dd  reserved (0:0)\n"
                                " \n"
                                " 2ND SAVE TABLE (from ptr above)\n"
                                " offset type functions & pointers\n"
                                " ------ ---- --------------------\n"
                                "   0     dw  Bytes in this table\n"
                                "   2     dd  Combination code tbl\n"
                                "   6     dd  2nd alpha char set\n"
                                "  0Ah    dd  user palette tbl\n"
                                "  0Eh    dd  reserved (0:0)\n"
                                "  12h    dd  reserved (0:0)\n"
                                "  16h    dd  reserved (0:0)");
 CW(0x0CE,"days_since1_80",     "Days since 1-Jan-1980 counter");
 make_array(0x4AC,0xCE-0xAC);
}

//-------------------------------------------------------------------------
static main() {
  if ( !add_segm_ex(0x400, 0x4D0, 0x40, 0, 0, 2, ADDSEG_NOSREG) ) {
    warning("Can't create BIOS data segment.");
    return;
  }
  set_segm_name(0x400, "bdata");
  set_segm_class(0x400, "BIOSDATA");
  CmtBdata();
}
