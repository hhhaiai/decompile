//
// This file is executed when IDA detects Turbo Pascal DLL
//

#include <idc.idc>

static main()
{
  // Set pascal type strings. Just in case
  set_inf_attr(INF_STRTYPE, STRTYPE_PASCAL);

  // System unit used protected commands so
  // set protected mode processor
  set_processor_type("80386p", SETPROC_USER);

  auto start = get_inf_attr(INF_START_EA);

  // Give pascal style name to the entry point
  // and delete the bogus one-instruction function
  // which was created by the startup signature
  set_name(start, "LIBRARY");
  del_func(start);

  // Plan to create a good PROGRAM function instead of
  // the deleted one
  auto_mark_range(start, start+1, AU_PROC);

  // Get address of the initialization subrountine
  auto init = get_first_fcref_from(start+5);
  set_name(init, "@__SystemInit$qv");

  // Delete the bogus function which was created by the secondary
  // startup signature.
  del_func(init);

  // Create a good initialization function
  add_func(init);
  set_func_flags(init, FUNC_LIB|get_func_flags(init));

  // Check for presence of LibExit() function
  auto exit = get_name_ea_simple("@__LibExit$qv");

  // If we have found function then define it
  // with FUNC_NORET attribute
  if ( exit != BADADDR )
  {
    add_func(exit);
    set_func_flags(exit, FUNC_NORET|FUNC_LIB|get_func_flags(exit));
  }
}
