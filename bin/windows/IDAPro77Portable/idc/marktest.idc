//
//      This example shows how to get list of marked positions.
//

#include <idc.idc>

static main() {
  auto x;

  put_bookmark(get_screen_ea(),10,5,5,6,"Test of Mark Functions");
  for ( x=0; x<10; x++ )
    msg("%d: %a %s\n",x,get_bookmark(x),get_bookmark_desc(x));
}
