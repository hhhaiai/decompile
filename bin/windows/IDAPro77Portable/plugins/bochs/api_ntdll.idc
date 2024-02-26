// The format of this file is descriped in api_kernel32.idc

///func=RtlGetLastWin32Error entry=bochsys._BxWin32GetLastError@0
///func=RtlSetLastWin32Error entry=bochsys._BxWin32SetLastError@4
///func=NtSetLdtEntries purge=24
//

// ----------------------------------------------------------------------------
/*
NTSYSAPI NTSTATUS NTAPI NtProtectVirtualMemory(
  IN HANDLE               ProcessHandle,
  IN OUT PVOID            *BaseAddress,
  IN OUT PULONG           NumberOfBytesToProtect,
  IN ULONG                NewAccessProtection,
  OUT PULONG              OldAccessProtection )
*/
///func=NtProtectVirtualMemory entry=nt_NtProtectVirtualMemory purge=20
static nt_NtProtectVirtualMemory()
{
  auto ptr = get_wide_dword(BochsGetParam(2));
  auto sz = get_wide_dword(BochsGetParam(3));
  msg("NtProtectVirtualMemory(ptr=%x, sz=%d)\n", ptr, sz);
  BochsVirtProtect(ptr, sz, 1);
  eax = 0;
  return 0;
}

// ----------------------------------------------------------------------------
/*
NTSYSAPI NTSTATUS NTAPI NtFreeVirtualMemory(
  IN HANDLE               ProcessHandle,
  IN PVOID                *BaseAddress,
  IN OUT PULONG           RegionSize,
  IN ULONG                FreeType );
*/
///func=NtFreeVirtualMemory entry=nt_NtFreeVirtualMemory purge=16
static nt_NtFreeVirtualMemory()
{
  auto ptr = get_wide_dword(BochsGetParam(2));
  BochsVirtFree(ptr, 0);
  eax = 0;
  return 0;
}

// ----------------------------------------------------------------------------
/*
NTSYSAPI NTSTATUS NTAPI NtAllocateVirtualMemory(
  IN HANDLE               ProcessHandle,
  IN OUT PVOID            *BaseAddress,
  IN ULONG                ZeroBits,
  IN OUT PULONG           RegionSize,
  IN ULONG                AllocationType,
  IN ULONG                Protect );
*/
///func=NtAllocateVirtualMemory entry=nt_NtAllocateVirtualMemory purge=24
static nt_NtAllocateVirtualMemory()
{
  auto sz = get_wide_dword(BochsGetParam(4));
  auto mem = BochsVirtAlloc(0, sz, 1);
  auto ptr = BochsGetParam(2);
  //msg("NtAllocateVirtualMemory(sz=%d, mem=%x, ptr=%x)", sz, mem, ptr);
  patch_dword(ptr, mem);
  eax = 0;
  return 0;
}


// ----------------------------------------------------------------------------
///func=RtlAllocateHeap entry=nt_HeapAlloc
static nt_HeapAlloc()
{
  // Redirect HeapAlloc -> VirtualAlloc
  eax = BochsVirtAlloc(0, BochsGetParam(3), 1);
  return 0;
}

// ----------------------------------------------------------------------------
///func=RtlEncodePointer entry=nt_EncodePointer purge=4
static nt_EncodePointer()
{
  eax = BochsGetParam(1) ^ 0x11223344; // return the same parameter scrambled with a constant
  return 0;
}

// ----------------------------------------------------------------------------
///func=RtlDecodePointer entry=nt_DecodePointer purge=4
static nt_DecodePointer()
{
  eax = BochsGetParam(1) ^ 0x11223344; // return the same parameter scrambled with a constant
  return 0;
}
