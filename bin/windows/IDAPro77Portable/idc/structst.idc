//
//      This example shows how to use structure manipulation functions.
//

#include <idc.idc>

static main() {
  auto idx,code;

  idx = add_struc(-1, "str1_t", 0);     // create a structure
  if ( idx != -1 ) {                    // if ok
    auto id2;
        // add member: offset from struct start 0, type - byte, 5 elements
    add_struc_member(idx,"bytemem",0,FF_DATA|FF_BYTE,-1,5*1);
    add_struc_member(idx,"wordmem",5,FF_DATA|FF_WORD,-1,1*2);
    set_member_cmt(idx,0,"This is 5 element byte array",0);
    set_member_cmt(idx,5,"This is 1 word",0);
    id2 = add_struc(-1, "str2_t", 0); // create another structure
    add_struc_member(id2,"first", 0,FF_DATA|FF_BYTE,-1,1*1);
    add_struc_member(id2,"strmem",1,FF_DATA|FF_STRUCT,idx,get_struc_size(idx));
    set_member_cmt(id2,1,"This is structure member",0);
  }

  for ( idx=get_first_struc_idx(); idx != -1; idx=get_next_struc_idx(idx) ) {
    auto id,m;
    id = get_struc_by_idx(idx);
    if ( id == -1 ) error("Internal IDA error, get_struc_by_idx returned -1!");
    msg("Structure %s:\n",get_struc_name(id));
    msg("  Regular    comment: %s\n",get_struc_cmt(id,0));
    msg("  Repeatable comment: %s\n",get_struc_cmt(id,1));
    msg("  Size              : %d\n",get_struc_size(id));
    msg("  Number of members : %d\n",get_member_qty(id));
    for ( m = 0;
          m != get_struc_size(id);
          m = get_next_offset(id,m) ) {
      auto mname;
      mname = get_member_name(id,m);
      if ( mname == "" ) {
        msg("  Hole (%d bytes)\n",get_next_offset(id,m)-m);
      } else {
        auto type;
        msg("  Member name   : %s\n",get_member_name(id,m));
        msg("    Regular cmt : %s\n",get_member_cmt(id,m,0));
        msg("    Rept.   cmt : %s\n",get_member_cmt(id,m,1));
        msg("    Member size : %d\n",get_member_size(id,m));
        type = get_member_flag(id,m) & DT_TYPE;
             if ( type == FF_BYTE     ) type = "Byte";
        else if ( type == FF_WORD     ) type = "Word";
        else if ( type == FF_DWORD    ) type = "Double word";
        else if ( type == FF_QWORD    ) type = "Quadro word";
        else if ( type == FF_TBYTE    ) type = "Ten bytes";
        else if ( type == FF_STRLIT   ) type = "ASCII string";
        else if ( type == FF_STRUCT   ) type = sprintf("Structure '%s'",get_struc_name(get_member_strid(id,m)));
        else if ( type == FF_XTRN     ) type = "Unknown external?!"; // should not happen
        else if ( type == FF_FLOAT    ) type = "Float";
        else if ( type == FF_DOUBLE   ) type = "Double";
        else if ( type == FF_PACKREAL ) type = "Packed Real";
        else                            type = sprintf("Unknown type %08X",type);
        msg("    Member type : %s",type);
        type = get_member_flag(id,m);
             if ( is_off0(type)  ) msg(" Offset");
        else if ( is_char0(type) ) msg(" Character");
        else if ( is_seg0(type)  ) msg(" Segment");
        else if ( is_dec0(type)  ) msg(" Decimal");
        else if ( is_hex0(type)  ) msg(" Hex");
        else if ( is_oct0(type)  ) msg(" Octal");
        else if ( is_bin0(type)  ) msg(" Binary");
        msg("\n");
      }
    }
  }
  msg("Total number of structures: %d\n",get_struc_qty());
}
