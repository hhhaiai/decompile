//
//      This example shows how to use array manipulation functions.
//

#include <idc.idc>

#define MAXIDX  100

static main() {
  auto id,idx,code;

  id = create_array("my array");
  if ( id == -1 ) {
    warning("Can't create array!");
  } else {

    msg("Filling array of longs...\n");
    for ( idx=0; idx < MAXIDX; idx=idx+10 )
      set_array_long(id,idx,2*idx);

    msg("Displaying array of longs...\n");
    for ( idx=get_first_index(AR_LONG,id);
          idx != -1;
          idx=get_next_index(AR_LONG,id,idx) )
      msg("%d: %d\n",idx,get_array_element(AR_LONG,id,idx));

    msg("Filling array of strings...\n");
    for ( idx=0; idx < MAXIDX; idx=idx+10 )
      set_array_string(id, idx, sprintf("This is %d-th element of array", idx));

    msg("Displaying array of strings...\n");
    for ( idx=0; idx < MAXIDX; idx=idx+10 )
      msg("%d: %s\n",idx,get_array_element(AR_STR,id,idx));

  }

}
