//
//      This IDC file is called after a new file is loaded into IDA
//      database.
//      IDA calls "OnLoad" function from this file.
//
//      You may use this function to read extra information (such as
//      debug information) from the input file, or for anything else.
//

#include <idc.idc>

//      If you want to add your own processing of newly created databases,
//      you may create a file named "userload.idc":
//
//      #define USERLOAD_IDC
//      static userload(input_file,real_file,filetype) {
//              ... your processing here ...
//      }
//

#softinclude <userload.idc>

// Input parameteres:
//      input_file - name of loaded file
//      real_file  - name of actual file that contains the input file.
//                   usually this parameter is equal to input_file,
//                   but is different if the input file is extracted from
//                   an archive.
//      filetype   - type of loaded file. See FT_.. definitions in idc.idc

static OnLoad(input_file, real_file, filetype)
{
#ifdef USERLOAD_IDC             // if user-defined IDC file userload.idc
                                // exists...
  if ( userload(input_file, real_file, filetype) )
    return;
#endif
  if ( filetype == FT_DRV )
    DriverLoaded();
//  msg("File %s is loaded into the database.\n",input_file);
}


//--------------------------------------------------------------------------
//      This function is executed when a new device driver is loaded.
//              Device drivers have extensions DRV or SYS.
//
// History:
//
// 08/12/95 20:16 by Alexey Kulentsov:
// + Check for Device Request Block
// + Kludge with Drv/Com supported
// 04/01/96 04:21 by ig:
// + 0000:0000 means end of devices chain too.
// 16/05/96 16:01 by ig:
// + modified to work with the new version of IDA (separate operand types)

static DriverLoaded(void)
{
  auto x,i,base;
  auto intr,strt;
  auto attr,cmt;
  auto nextbase;
  auto DevReq;

  i = 0;
  x = get_inf_attr(INF_MIN_EA);
  base = (x >> 4);   // The segment base

  while ( 1 )
  {
    msg("Device driver block at %04X\n",x);

    set_name(x, sprintf("NextDevice_%ld",i));
    create_word(x);
    op_num(x,0);
    if ( get_wide_word(x) == 0xFFFF ) {
      set_cmt(x, "The last device", 0);
    } else {
      nextbase = base + get_wide_word(x+2);
      op_plain_offset(x,0,nextbase<<4);
      set_cmt(x, "Offset to the next device", 0);
    }

    create_word(x+2);
    op_num(x+2,0);

    set_name(x+4, sprintf("DevAttr_%ld",i));
    create_word(x+4);
    op_num(x+4,0);
    attr = get_wide_word(x+4);
    cmt = "";
    if ( attr & (1<< 0) ) cmt = cmt + "stdin device\n";
    if ( attr & (1<< 1) ) cmt = cmt + ((attr & (1<<15)) ? "stdout device\n" : ">32M\n");
    if ( attr & (1<< 2) ) cmt = cmt + "stdnull device\n";
    if ( attr & (1<< 3) ) cmt = cmt + "clock device\n";
    if ( attr & (1<< 6) ) cmt = cmt + "supports logical devices\n";
    if ( attr & (1<<11) ) cmt = cmt + "supports open/close/RM\n";
    if ( attr & (1<<13) ) cmt = cmt + "non-IBM block device\n";
    if ( attr & (1<<14) ) cmt = cmt + "supports IOCTL\n";
    cmt = cmt + ((attr & (1<<15)) ? "character device" : "block device");
    set_cmt(x+4, cmt, 0);

    set_name(x+6, sprintf("Strategy_%ld",i));
    create_word(x+6);
    op_plain_offset(x+6,0,get_inf_attr(INF_MIN_EA));

    set_name(x+8, sprintf("Interrupt_%ld",i));
    create_word(x+8);
    op_plain_offset(x+8, -1, get_inf_attr(INF_MIN_EA));

    set_name(x+0xA, sprintf("DeviceName_%ld",i));
    create_strlit (x+0xA,8);
    set_cmt(x+0xA, "May be device number", 0);

    strt = (base << 4) + get_wide_word(x+6);
    intr = (base << 4) + get_wide_word(x+8);
    create_insn( strt );
    create_insn( intr );
    auto_mark_range(strt, strt+1, AU_PROC);
    auto_mark_range(intr, intr+1, AU_PROC );
    set_name( strt, sprintf("Strategy_Routine_%ld",i));
    set_name( intr, sprintf("Interrupt_Routine_%ld",i));
    set_cmt( strt, "ES:BX -> Device Request Block", 0);
    set_cmt( intr, "Device Request Block:\n"
             "0 db length\n"
             "1 db unit number\n"
             "2 db command code\n"
             "5 d? reserved\n"
             "0D d? command specific data", 0);

    if( get_wide_byte( strt )==0x2E && get_wide_word(strt+1)==0x1E89
     && get_wide_byte(strt+5)==0x2E && get_wide_word(strt+6)==0x068C
     && get_wide_word(strt+3)==get_wide_word(strt+8)-2)
    {
     DevReq=get_wide_word(strt+3);
     msg("DevReq at %x\n",DevReq);
     del_items(x+DevReq);
     del_items(x+DevReq+2);
     create_dword(x+DevReq);
     set_name(x+DevReq, sprintf("DevRequest_%ld",i));
    }

    if ( get_wide_word(x) == 0xFFFF ||
       ((get_wide_byte(x)==0xE9 || get_wide_byte(x)==0xEB) && i==0) ) break;
    if ( get_wide_dword(x) == 0 ) break; // 04.01.96
    x = (nextbase << 4) + get_wide_word(x);
    i = i + 1;
  }
}
