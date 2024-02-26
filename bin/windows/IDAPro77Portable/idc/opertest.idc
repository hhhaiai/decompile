//
//      This example shows how to use get_operand_value() function.
//

#include <idc.idc>

static main() {
  auto ea;

  for ( ea = get_inf_attr(INF_MIN_EA); ea != BADADDR; ea=find_code(ea,1) ) {
    auto x;
    x = get_operand_value(ea,0);
    if ( x != -1 ) msg("%08lX: operand 1 = %08lX\n",ea,x);
    x = get_operand_value(ea,1);
    if ( x != -1 ) msg("%08lX: operand 2 = %08lX\n",ea,x);
    x = get_operand_value(ea,2);
    if ( x != -1 ) msg("%08lX: operand 3 = %08lX\n",ea,x);
  }
}
