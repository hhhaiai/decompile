#// The format of this file is descriped in api_kernel32.idc

#///func=RtlGetLastWin32Error entry=bochsys._BxWin32GetLastError@0
#///func=RtlSetLastWin32Error entry=bochsys._BxWin32SetLastError@4
#///func=NtSetLdtEntries purge=24

#///func=RtlAllocateHeap entry=nt_HeapAlloc
def nt_HeapAlloc():
  # Redirect HeapAlloc -> VirtualAlloc
  cpu.eax = BochsVirtAlloc(0, BochsGetParam(3), 1)
  return 0

#///func=RtlEncodePointer entry=nt_EncodePointer purge=4
def nt_EncodePointer():
  cpu.eax = BochsGetParam(1) ^ 0x11223344 # return the same parameter scrambled with a constant
  return 0

#///func=RtlDecodePointer entry=nt_DecodePointer purge=4
def nt_DecodePointer():
  cpu.eax = BochsGetParam(1) ^ 0x11223344; # return the same parameter scrambled with a constant
  return 0
