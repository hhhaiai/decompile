// PVOID __stdcall ExAllocatePoolWithTag(POOL_TYPE PoolType, SIZE_T NumberOfBytes, ULONG Tag)
///func=ExAllocatePoolWithTag entry=ntos_ExAllocatePoolWithTag purge=12
static ntos_ExAllocatePoolWithTag()
{
  // Redirect GlobalAlloc -> VirtualAlloc
  eax = BochsVirtAlloc(0, BochsGetParam(2), 1);
  return 0;
}

// void __stdcall ExFreePoolWithTag(PVOID P, ULONG Tag)
///func=ExFreePoolWithTag entry=ntos_ExFreePoolWithTag purge=8
static ntos_ExFreePoolWithTag()
{
  // Redirect GlobalAlloc -> VirtualAlloc
  eax = BochsVirtFree(BochsGetParam(1), 0);
  return 0;
}

