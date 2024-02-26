//
//
//      This example shows how to use cross-reference related functions.
//      It displays xrefs to the current location.
//

#include <idc.idc>

static main() {
  auto ea,flag,x,y;
  flag = 1;
  ea = get_screen_ea();

//  add_dref(ea,ea1,dr_R);         // set data reference (read)
//  add_cref(ea,ea1,fl_CN);          // set 'call near' reference
//  del_cref(ea,ea1,1);

//
//      Now show all reference relations between ea & ea1.
//
  msg("\n*** Code references from " + atoa(ea) + "\n");
  for ( x=get_first_cref_from(ea); x != BADADDR; x=get_next_cref_from(ea,x) )
    msg(atoa(ea) + " refers to " + atoa(x) + xrefchar() + "\n");

  msg("\n*** Code references to " + atoa(ea) + "\n");
  x = ea;
  for ( y=get_first_cref_to(x); y != BADADDR; y=get_next_cref_to(x,y) )
    msg(atoa(x) + " is referred from " + atoa(y) + xrefchar() + "\n");

  msg("\n*** Code references from " + atoa(ea) + " (only non-trivial refs)\n");
  for ( x=get_first_fcref_from(ea); x != BADADDR; x=get_next_fcref_from(ea,x) )
    msg(atoa(ea) + " refers to " + atoa(x) + xrefchar() + "\n");

  msg("\n*** Code references to " + atoa(ea) + " (only non-trivial refs)\n");
  x = ea;
  for ( y=get_first_fcref_to(x); y != BADADDR; y=get_next_fcref_to(x,y) )
    msg(atoa(x) + " is referred from " + atoa(y) + xrefchar() + "\n");

  msg("\n*** Data references from " + atoa(ea) + "\n");
  for ( x=get_first_dref_from(ea); x != BADADDR; x=get_next_dref_from(ea,x) )
    msg(atoa(ea) + " accesses " + atoa(x) + xrefchar() + "\n");

  msg("\n*** Data references to " + atoa(ea) + "\n");
  x = ea;
  for ( y=get_first_dref_to(x); y != BADADDR; y=get_next_dref_to(x,y) )
    msg(atoa(x) + " is accessed from " + atoa(y) + xrefchar() + "\n");

}

static xrefchar()
{
  auto x, is_user;
  x = get_xref_type();

  is_user = (x & XREF_USER) ? ", user defined)" : ")";

  if ( x == fl_F )  return " (ordinary flow" + is_user;
  if ( x == fl_CF ) return " (call far"      + is_user;
  if ( x == fl_CN ) return " (call near"     + is_user;
  if ( x == fl_JF ) return " (jump far"      + is_user;
  if ( x == fl_JN ) return " (jump near"     + is_user;
  if ( x == dr_O  ) return " (offset"        + is_user;
  if ( x == dr_W  ) return " (write)"        + is_user;
  if ( x == dr_R  ) return " (read"          + is_user;
  if ( x == dr_T  ) return " (textual"       + is_user;
  return "(?)";
}
