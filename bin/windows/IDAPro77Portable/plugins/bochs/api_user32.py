#// The format of this file is described in api_kernel32.idc

#///func=MessageBoxA entry=messagebox purge=0x10
def messagebox():
  param2 = BochsGetParam(2)
  msg("[Python] MessageBoxA() has been called: %x %s\n" % (param2, get_strlit_contents(param2, -1, STRTYPE_C)))
  set_reg_value(1,"eax")
  # continue execution
  return 0
