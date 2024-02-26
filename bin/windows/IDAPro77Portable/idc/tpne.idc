//
// This file is executed when IDA detects Turbo Pascal Windows
// or DPMI application.
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
  set_name(start, "PROGRAM");
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

  // find sequence of
  //      xor     cx, cx
  //      xor     bx, bx
  // usually Halt() starts with these instructions

  auto halt = find_binary(init, 1, "33 c9 33 db");

  // If we have found the sequence then define Halt() function
  // with FUNC_NORET attribute
  if ( halt != BADADDR )
  {
    set_name(halt, "@Halt$q4Word");
    add_func(halt);
    set_func_flags(halt, FUNC_NORET|FUNC_LIB|get_func_flags(halt));
  }

  // Create a good initialization function
  add_func(init);
  set_func_flags(init, FUNC_LIB|get_func_flags(init));
}
