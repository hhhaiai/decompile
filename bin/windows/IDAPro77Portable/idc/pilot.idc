//
//	This file is executed when a PalmPilot program is loaded.
//	You may customize it as you wish.
//
//	TODO:
//		- decompilation of various resource types
//		  (we don't have any information on the formats)
//

#include <idc.idc>

//-----------------------------------------------------------------------
//
// Process each resource and make some routine tasks
//
static process_segments()
{
  auto ea,segname,prefix;

  for ( ea=get_first_seg(); ea != BADADDR; ea=get_next_seg(ea) )
  {
    segname = get_segm_name(ea);
    prefix = substr(segname,0,4);
    if ( segname == "data0000" )
    {
      if ( get_wide_dword(ea) == 0xFFFFFFFF )
      {
        create_dword(ea);
        set_cmt(ea,"Loader stores SysAppInfoPtr here", 0);
      }
      continue;
    }
    if ( prefix == "TRAP" )
    {
      create_word(ea);
      op_hex(ea,0);
      set_cmt(ea,"System trap function code", 0);
      continue;
    }
    if ( prefix == "tSTR" )
    {
      create_strlit(ea,get_segm_end(ea));
      set_cmt(ea,"String resource", 0);
      continue;
    }
    if ( prefix == "tver" )
    {
      create_strlit(ea,get_segm_end(ea));
      set_cmt(ea,"Version number string", 0);
      continue;
    }
    if ( prefix == "tAIN" )
    {
      create_strlit(ea,get_segm_end(ea));
      set_cmt(ea,"Application icon name", 0);
      continue;
    }
    if ( prefix == "pref" )
    {
      auto flags,cmt;
      flags = get_wide_word(ea);
      create_word(ea); op_hex(ea,0); set_name(ea,"flags");
#define sysAppLaunchFlagNewThread  0x0001
#define sysAppLaunchFlagNewStack   0x0002
#define sysAppLaunchFlagNewGlobals 0x0004
#define sysAppLaunchFlagUIApp      0x0008
#define sysAppLaunchFlagSubCall    0x0010
      cmt = "";
      if ( flags & sysAppLaunchFlagNewThread ) cmt = cmt + "sysAppLaunchFlagNewThread\n";
      if ( flags & sysAppLaunchFlagNewStack  ) cmt = cmt + "sysAppLaunchFlagNewStack\n";
      if ( flags & sysAppLaunchFlagNewGlobals) cmt = cmt + "sysAppLaunchFlagNewGlobals\n";
      if ( flags & sysAppLaunchFlagUIApp     ) cmt = cmt + "sysAppLaunchFlagUIApp\n";
      if ( flags & sysAppLaunchFlagSubCall   ) cmt = cmt + "sysAppLaunchFlagSubCall";
      set_cmt(ea,cmt, 0);
      ea = ea + 2;
      create_dword(ea); op_hex(ea,0); set_name(ea,"stack_size");
      ea = ea + 4;
      create_dword(ea); op_hex(ea,0); set_name(ea,"heap_size");
    }
  }
}

//-----------------------------------------------------------------------
//
//	Create a enumeration with system action codes
//
static make_actions()
{
  auto id;
  id = add_enum(-1,"SysAppLaunchCmd",FF_0NUMD);
  if ( id != -1 )
  {
    set_enum_cmt(id,"Action codes",0);
    add_enum_member(id, "sysAppLaunchCmdNormalLaunch",         0, -1);
    add_enum_member(id, "sysAppLaunchCmdFind",                 1, -1);
    add_enum_member(id, "sysAppLaunchCmdGoTo",                 2, -1);
    add_enum_member(id, "sysAppLaunchCmdSyncNotify",           3, -1);
    add_enum_member(id, "sysAppLaunchCmdTimeChange",           4, -1);
    add_enum_member(id, "sysAppLaunchCmdSystemReset",          5, -1);
    add_enum_member(id, "sysAppLaunchCmdAlarmTriggered",       6, -1);
    add_enum_member(id, "sysAppLaunchCmdDisplayAlarm",         7, -1);
    add_enum_member(id, "sysAppLaunchCmdCountryChange",        8, -1);
    add_enum_member(id, "sysAppLaunchCmdSyncRequest",          9, -1);
    add_enum_member(id, "sysAppLaunchCmdSaveData",            10, -1);
    add_enum_member(id, "sysAppLaunchCmdInitDatabase",        11, -1);
    add_enum_member(id, "sysAppLaunchCmdSyncCallApplication", 12, -1);
    set_enum_member_cmt(get_enum_member(id, 0, 0, -1), "Normal Launch", 1);
    set_enum_member_cmt(get_enum_member(id, 1, 0, -1), "Find string", 1);
    set_enum_member_cmt(get_enum_member(id, 2, 0, -1), "Launch and go to a particular record", 1);
    set_enum_member_cmt(get_enum_member(id, 3, 0, -1),
                        "Sent to apps whose databases changed\n"
                        "during HotSync after the sync has\n"
                        "been completed", 1);
    set_enum_member_cmt(get_enum_member(id, 4, 0, -1), "The system time has changed", 1);
    set_enum_member_cmt(get_enum_member(id, 5, 0, -1), "Sent after System hard resets", 1);
    set_enum_member_cmt(get_enum_member(id, 6, 0, -1), "Schedule next alarm", 1);
    set_enum_member_cmt(get_enum_member(id, 7, 0, -1), "Display given alarm dialog", 1);
    set_enum_member_cmt(get_enum_member(id, 8, 0, -1), "The country has changed", 1);
    set_enum_member_cmt(get_enum_member(id, 9, 0, -1), "The \"HotSync\" button was pressed", 1);
    set_enum_member_cmt(get_enum_member(id, 10, 0, -1),
                        "Sent to running app before\n"
                        "sysAppLaunchCmdFind or other\n"
                        "action codes that will cause data\n"
                        "searches or manipulation", 1);
    set_enum_member_cmt(get_enum_member(id, 11, 0, -1),
                        "Initialize a database; sent by\n"
                        "DesktopLink server to the app whose\n"
                        "creator ID matches that of the database\n"
                        "created in response to the \"create db\" request", 1);
    set_enum_member_cmt(get_enum_member(id, 12, 0, -1),
                        "Used by DesktopLink Server command\n"
                        "\"call application\"", 1);
  }
}

//-----------------------------------------------------------------------
//
//	Create a enumeration with event codes
//
static make_events()
{
  auto id;
  id = add_enum(-1,"events",FF_0NUMD);
  if ( id != -1 )
  {
    set_enum_cmt(id,"Event codes",0);
    add_enum_member(id, "nilEvent",              0, -1);
    add_enum_member(id,"penDownEvent",           1, -1);
    add_enum_member(id,"penUpEvent",             2, -1);
    add_enum_member(id,"penMoveEvent",           3, -1);
    add_enum_member(id,"keyDownEvent",           4, -1);
    add_enum_member(id,"winEnterEvent",          5, -1);
    add_enum_member(id,"winExitEvent",           6, -1);
    add_enum_member(id,"ctlEnterEvent",          7, -1);
    add_enum_member(id,"ctlExitEvent",           8, -1);
    add_enum_member(id,"ctlSelectEvent",         9, -1);
    add_enum_member(id,"ctlRepeatEvent",        10, -1);
    add_enum_member(id,"lstEnterEvent",         11, -1);
    add_enum_member(id,"lstSelectEvent",        12, -1);
    add_enum_member(id,"lstExitEvent",          13, -1);
    add_enum_member(id,"popSelectEvent",        14, -1);
    add_enum_member(id,"fldEnterEvent",         15, -1);
    add_enum_member(id,"fldHeightChangedEvent", 16, -1);
    add_enum_member(id,"fldChangedEvent",       17, -1);
    add_enum_member(id,"tblEnterEvent",         18, -1);
    add_enum_member(id,"tblSelectEvent",        19, -1);
    add_enum_member(id,"daySelectEvent",        20, -1);
    add_enum_member(id,"menuEvent",             21, -1);
    add_enum_member(id,"appStopEvent",          22, -1);
    add_enum_member(id,"frmLoadEvent",          23, -1);
    add_enum_member(id,"frmOpenEvent",          24, -1);
    add_enum_member(id,"frmGotoEvent",          25, -1);
    add_enum_member(id,"frmUpdateEvent",        26, -1);
    add_enum_member(id,"frmSaveEvent",          27, -1);
    add_enum_member(id,"frmCloseEvent",         28, -1);
    add_enum_member(id,"tblExitEvent",          29, -1);
  }
}

//-----------------------------------------------------------------------
static main()
{
  process_segments();
  make_actions();
  make_events();
}

//-----------------------------------------------------------------------
#ifdef __undefined_symbol__
	// WE DO NOT USE IDC HOTKEYS, JUST SIMPLE KEYBOARD MACROS
	// (see IDA.CFG, macro Alt-5 for mc68k)
//-----------------------------------------------------------------------
//
//	Register Ctrl-R as a hotkey for "make offset from A5" command
//	(not used, simple keyboard macro is used instead, see IDA.CFG)
//
//	There is another (manual) way to convert an operand to an offset:
//	  - press Ctrl-R
//	  - enter "A5BASE"
//	  - press Enter
//
static setup_pilot()
{
  auto h0,h1;
  h0 = "Alt-1";
  h1 = "Alt-2";
  add_idc_hotkey(h0,"a5offset0");
  add_idc_hotkey(h1,"a5offset1");
  msg("Use %s to convert the first operand to an offset from A5\n",h0);
  msg("Use %s to convert the second operand to an offset from A5\n",h1);
}

static a5offset0(void) { op_plain_offset(get_screen_ea(),0,get_name_ea_simple("A5BASE")); }
static a5offset1(void) { op_plain_offset(get_screen_ea(),1,get_name_ea_simple("A5BASE")); }

#endif // 0
