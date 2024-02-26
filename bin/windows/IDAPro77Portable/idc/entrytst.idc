//
//      This example shows how to get list of entry points.
//

#include <idc.idc>

static main() {
  auto i;
  auto ord,ea;

  msg("Number of entry points: %ld\n",get_entry_qty());
  for ( i=0; ; i++ ) {
    ord = get_entry_ordinal(i);
    if ( ord == 0 ) break;
    ea = get_entry(ord);
    msg("Entry point %08lX at %08lX (%s)\n",ord,ea,Name(ea));
  }
}
