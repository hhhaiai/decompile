#include <idc.idc>

static main()
{
}

// Android Bionic libc
//
// These functions are called while loading startup signatures from
// elf.sig to obtain the address of main.

static get_main_ea(ea, got_ldr, got_off, main_off)
{
  auto got_ea = 0;

  if ( got_off != 0 )
  {
    create_insn(ea + got_ldr);
    got_ea = get_first_dref_from(ea + got_ldr);
    if ( got_ea == BADADDR )
      return BADADDR;
    got_ea = get_wide_dword(got_ea);
    if ( got_ea == BADADDR )
      return BADADDR;
    got_ea = got_ea + ea + got_off + 8;

    ea = ea + main_off;
    create_insn(ea);
    ea = get_first_dref_from(ea);
    if ( ea == BADADDR )
      return BADADDR;

    ea = get_wide_dword(ea);
    if ( ea == BADADDR )
      return BADADDR;
  }

  ea = got_ea + ea;

  ea = get_wide_dword(ea);
  if ( ea == BADADDR )
    return BADADDR;

  // Check that segment is executable
  if ( (get_segm_attr(ea, SEGATTR_PERM) & SEGPERM_EXEC) == 0 )
    return BADADDR;

  return ea;
}

static get_main_ea_pic(ea, got_ldr, got_off, main_off)
{
  return get_main_ea(ea, long(got_ldr), long(got_off), long(main_off));
}

static get_main_ea_abs(ea)
{
  return get_main_ea(ea, 0, 0, 0);
}
