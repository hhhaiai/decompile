/*
   Rename imports.

   This script renames entries of a dynamically built import table.
   For example, from a table like this:

      dd offset ntdll_NtPowerInformation
      dd offset ntdll_NtInitiatePowerAction
      dd offset ntdll_NtSetThreadExecutionState
      dd offset ntdll_NtRequestWakeupLatency
      dd offset ntdll_NtGetDevicePowerState
      dd offset ntdll_NtIsSystemResumeAutomatic
      dd offset ntdll_NtRequestDeviceWakeup
      dd offset ntdll_NtCancelDeviceWakeupRequest
      dd offset ntdll_RtlQueryRegistryValues


   it will create a table like this:

      NtPowerInformation dd offset ntdll_NtPowerInformation
      NtInitiatePowerAction dd offset ntdll_NtInitiatePowerAction
      NtSetThreadExecutionState dd offset ntdll_NtSetThreadExecutionState
      NtRequestWakeupLatency dd offset ntdll_NtRequestWakeupLatency
      NtGetDevicePowerState dd offset ntdll_NtGetDevicePowerState
      NtIsSystemResumeAutomatic dd offset ntdll_NtIsSystemResumeAutomatic
      NtRequestDeviceWakeup dd offset ntdll_NtRequestDeviceWakeup
      NtCancelDeviceWakeupRequest dd offset ntdll_NtCancelDeviceWakeupRequest
      RtlQueryRegistryValues dd offset ntdll_RtlQueryRegistryValues

   Usage: select the import table and run the script.

   Known problems: if the dll name contains an underscore, the function
   names might be incorrect. Special care is taken for the ws2_32.dll but
   other dlls will have wrong function names.

*/

#include <idc.idc>

static main()
{
  auto ea1, ea2, idx, dllname, name;

  ea1 = read_selection_start();
  ea2 = read_selection_end();
  if ( ea1 == BADADDR )
  {
    warning("Please select the import table before running the renimp script");
    return;
  }

  auto ptrsz, DeRef;
  auto bitness = get_segm_attr(ea1, SEGATTR_BITNESS);
  if ( bitness == 1 )
  {
    ptrsz = 4;
    DeRef = get_wide_dword;
  }
  else if ( bitness == 2 )
  {
    ptrsz = 8;
    DeRef = get_qword;
  }
  else
  {
    warning("Unsupported segment bitness!");
    return;
  }

  while ( ea1 < ea2 )
  {
    name = Name(DeRef(ea1));
    idx = strstr(name, "_");
    dllname = substr(name, 0, idx);

    // Most likely the dll name is ws2_32
    if ( dllname == "ws2" )
      idx = idx + 3;

    // Extract the function name
    name = substr(name, idx+1, -1);
    if ( !set_name(ea1, name, SN_CHECK|SN_NOWARN) )
    {
      // failed to give a name - it could be that the name has already been
      // used in the program. add a suffix
      for ( idx=0; idx < 99; idx++ )
      {
        if ( set_name(ea1, name + "_" + ltoa(idx, 10), SN_CHECK|SN_NOWARN) )
          break;
      }
    }
    ea1 = ea1 + ptrsz;
  }
}
