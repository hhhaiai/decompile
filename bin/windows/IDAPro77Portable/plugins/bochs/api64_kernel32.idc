#include <idc.idc>

// The format of this file is described in api_kernel32.idc

//--------------------------------------------------------------------------
// These are system definitions.
// !! Do not change them unless you know what you are doing !!
///func=ExitProcess entry=bochsys64.BxExitProcess
///func=GetModuleHandleA entry=bochsys64.BxGetModuleHandleA
///func=GetModuleHandleW entry=bochsys64.BxGetModuleHandleW
///func=LoadLibraryA entry=bochsys64.BxLoadLibraryA
///func=LoadLibraryW entry=bochsys64.BxLoadLibraryW
///func=GetTickCount entry=bochsys64.BxGetTickCount
///func=GetModuleFileNameA entry=bochsys64.BxGetModuleFileNameA
///func=GetModuleFileNameW entry=bochsys64.BxGetModuleFileNameW
///func=GetProcAddress entry=bochsys64.BxGetProcAddress
///func=VirtualAlloc entry=bochsys64.BxVirtualAlloc
///func=VirtualFree entry=bochsys64.BxVirtualFree
///func=VirtualProtect entry=bochsys64.BxVirtualProtect

//--------------------------------------------------------------------------
// HMODULE WINAPI LoadLibraryExA(LPCSTR lpFileName, HANDLE hFile, DWORD dwFlags);
///func=LoadLibraryExA entry=k32_LoadLibraryExA
static k32_LoadLibraryExA()
{
  auto hFile = BochsGetParam(2);
  if (hFile != 0)
  {
    rax = 0;
    return 0;
  }
  auto lpFileName = get_strlit_contents(BochsGetParam(1), -1, STRTYPE_C);
  auto dwFlags    = BochsGetParam(3);

  // Since Bochs plugin does not support dynamic DLL loading, we simply return the module handle.
  // (the DLL must be declared in startup.idc so it is pre-loaded)
  eax        = BochsGetModuleHandle(lpFileName);
  return 0; // continue execution
}

//--------------------------------------------------------------------------
///func=Beep entry=beep
static beep()
{
  auto param1 = BochsGetParam(1);
  auto param2 = BochsGetParam(2);

  msg("I am Beep(%d, %d)\n", param1, param2);

  // The emulated function returns 1:
  rax = 1;

  // Our return value controls execution of the debugged application:
  //   1 = suspend execution (inside IDACALL)
  //   0 = continue transparently
  return 0;
}

//--------------------------------------------------------------------------
// HGLOBAL WINAPI GlobalAlloc(UINT uFlags, SIZE_T dwBytes);
///func=GlobalAlloc entry=k32_GlobalAlloc
static k32_GlobalAlloc()
{
  // Redirect GlobalAlloc -> VirtualAlloc
  rax = BochsVirtAlloc(0, BochsGetParam(2), 1);
  return 0;
}

//--------------------------------------------------------------------------
//HGLOBAL WINAPI GlobalFree(HGLOBAL hMem);
///func=GlobalFree entry=k32_GlobalFree
static k32_GlobalFree()
{
  // Redirect GlobalFree -> VirtualFree
  rax = BochsVirtFree(BochsGetParam(1), 0);
  return 0;
}

//--------------------------------------------------------------------------
///func=GetCurrentThread entry=k32_GetCurrentThread purge=0
static k32_GetCurrentThread()
{
  eax = -2;
  return 0;
}
