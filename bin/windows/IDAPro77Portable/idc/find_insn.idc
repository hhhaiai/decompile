#include <idc.idc>

// This script is to be used with the 'grep' ida plugin
// It looks for the specified instruction mnemonics and saves all matches

static find_insn(mnem)
{
  auto ea;
  for ( ea=get_inf_attr(INF_MIN_EA); ea != BADADDR; ea=next_head(ea, BADADDR) )
  {
    if ( print_insn_mnem(ea) == mnem )
      save_match(ea, "");
  }
}
