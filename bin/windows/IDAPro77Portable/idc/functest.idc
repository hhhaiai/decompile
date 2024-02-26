//
//      This example shows how to get list of functions.
//

#include <idc.idc>

static main() {
  auto ea,x;

  for ( ea=get_next_func(0); ea != BADADDR; ea=get_next_func(ea) ) {
    msg("Function at %08lX: %s",ea,get_func_name(ea));
    x = get_func_flags(ea);
    if ( x & FUNC_NORET ) msg(" Noret");
    if ( x & FUNC_FAR   ) msg(" Far");
    msg("\n");
  }
  ea = choose_func("Please choose a function");
  msg("The user chose function at %08lX\n",ea);
}
