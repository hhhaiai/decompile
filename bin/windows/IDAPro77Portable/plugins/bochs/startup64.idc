// The format of this file is described in startup.idc

// Only lines containing three forward slashes ("/") are processed:

/// stub ntdll.dll
/// stub kernel32.dll
/// stub user32.dll
/// stub shell32.dll
/// stub shlwapi.dll
/// stub urlmon.dll
/// stub advapi32.dll
/// stub mswsock.dll
/// stub wininet.dll
/// stub msvcrt.dll
/// stub gdi32.dll
/// stub ole32.dll
/// stub wsock32.dll

#include <idc.idc>

//--------------------------------------------------------------------------
// New IDC scripts will become available during the debugging session:
// - please refer to startup.idc
//--------------------------------------------------------------------------

// ----------------------------------------------------------------------------
static BochsPatchDbgQword(ea, dv)
{
  auto i;
  for (i=0;i<8;i++)
  {
    patch_dbg_byte(ea, dv & 0xFF);
    ea = ea + 1;
    dv = dv >> 8;
  }
}

// ----------------------------------------------------------------------------
// Utility function that can be used as a conditional breakpoint condition
// in order to skip to the next instruction w/o suspending IDA
static bochs_skipnext()
{
  Eip = next_head(eip, BADADDR);
  return 0;
}

// ----------------------------------------------------------------------------
// Utility function that can be used as a conditional breakpoint condition
// in order to execute the contents of the comments at the bp location
static bochs_execidc_comments()
{
  exec_idc(Comment(eip));
  return 0;
}

// ----------------------------------------------------------------------------
// Utility function used to dump registers. The output can be used as a comment
// with the bochs_execidc_comments() bp condition
static bochs_dump_registers()
{
  msg("rax=0x%x;rbx=0x%x;rcx=0x%x;rdx=0x%x;rsi=0x%x;rdi=0x%x;rbp=0x%x;", rax, rbx, rcx, rdx, rsi, rdi, rbp);
}

// ----------------------------------------------------------------------------
static bochs_startup()
{
  msg("Bochs debugger has been initialized.\n");
  return 0;
}

// ----------------------------------------------------------------------------
static bochs_exit()
{
  msg("Bochs debugger has been terminated.\n");
  return 0;
}

