//
//      This example shows how to use structure manipulation functions.
//

#include <idc.idc>

#define MAXSTRUCT       200

// Create MAXSTRUT structures.
// Each structure will have 3 fields:
//      - a byte array field
//      - a word field
//      - a structure field

static main()
{
  auto i, idx, name, id2;

  for ( i=0; i < MAXSTRUCT; i++ )
  {
    name = sprintf("str_%03d", i);
    idx = add_struc(-1, name, 0);               // create a structure
    if ( idx == -1 )                            // if not ok
    {
      warning("Can't create structure %s, giving up",name);
      break;
    }
    else
    {
      add_struc_member(idx,
                     "bytemem",
                     get_struc_size(idx),
                     FF_DATA|FF_BYTE,
                     -1,
                     5*1);                      // char[5]
      add_struc_member(idx,
                     "wordmem",
                     get_struc_size(idx),
                     FF_DATA|FF_WORD,
                     -1,
                     1*2);                      // short
      id2 = get_struc_id(sprintf("str_%03d",i-1));
      if ( i != 0 ) add_struc_member(idx,
                     "inner",
                     get_struc_size(idx),
                     FF_DATA|FF_STRUCT,
                     id2,
                     get_struc_size(id2));        // sizeof(str_...)
      msg("Structure %s is successfully created, idx=%08lX, prev=%08lX\n",
                                                        name, idx, id2);
    }
  }
  msg("Done, total number of structures: %d\n",get_struc_qty());
}
