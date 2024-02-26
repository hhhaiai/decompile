//
//      This file demonstrates how to copy blocks of memory
//      using IDC. To use it, press F2 and select this file.
//      Once loaded and compiled all IDC functions stay in memory
//      so afterwards you can copy blocks simply pressing Shift-F2
//      and entering something like:
//
//              memcpy(0x30000, 0x20000, 0x100);
//
//      This construction copies 0x100 bytes from 0x20000 to 0x30000.
//
//      Also, you can delete main() function below.
//      When you try to execute this file, you'll get an error:
//      can find function 'main', don't pay attention.
//      You will get memcpy() function in the memory.
//      In this case you should create a segment youself (if nesessary).
//

#include <idc.idc>

//------------------------------------------------------------------------
static memcpy(to, from, size)
{
  auto i;
  for ( i=0; i < size; i=i+1 )
  {
    auto b = get_wide_byte(from);
    patch_byte(to, b);
    from = from + 1;
    to = to + 1;
  }
}

//------------------------------------------------------------------------
static main(void)
{
  auto from = ask_addr(here, "Please enter the source address");
  if ( from == BADADDR )
    return;
  auto to = ask_addr(BADADDR, "Please enter the target address");
  if ( to == BADADDR )
    return;
  auto size = ask_long(0, "Please enter the number of bytes to copy");
  if ( size == 0 )
    return;

  memcpy(to, from, size);
}
