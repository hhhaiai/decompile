//
//      This example shows how to get fixup information about the file.
//

#include <idc.idc>

static main() {
  auto ea;
  for ( ea = get_next_fixup_ea(get_inf_attr(INF_MIN_EA));
        ea != BADADDR;
        ea = get_next_fixup_ea(ea) ) {
    auto type,sel,off,dis,x;
    type = get_fixup_target_type(ea);
    sel  = get_fixup_target_sel(ea);
    off  = get_fixup_target_off(ea);
    dis  = get_fixup_target_dis(ea);
    msg("%08lX: ",ea);
    x = type & FIXUP_MASK;
         if ( x == FIXUP_BYTE  ) msg("BYTE ");
    else if ( x == FIXUP_OFF16 ) msg("OFF16");
    else if ( x == FIXUP_SEG16 ) msg("SEG16");
    else if ( x == FIXUP_PTR32 ) msg("PTR32");
    else if ( x == FIXUP_OFF32 ) msg("OFF32");
    else if ( x == FIXUP_PTR48 ) msg("PTR48");
    else if ( x == FIXUP_HI8   ) msg("HI8  ");
    else                         msg("?????");
    msg((type & FIXUP_EXTDEF) ? " EXTDEF" : " SEGDEF");
    msg(" [%s,%X]",get_segm_name(get_segm_by_sel(sel)),off);
    if ( type & FIXUP_EXTDEF  ) msg(" (%s)",Name([sel2para(sel),off]));
    if ( type & FIXUP_SELFREL ) msg(" SELF-REL");
    if ( type & FIXUP_UNUSED  ) msg(" UNUSED");
    msg("\n");
  }
}
