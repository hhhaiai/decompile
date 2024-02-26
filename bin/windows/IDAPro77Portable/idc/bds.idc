//
// This file is executed when IDA detects Delphi6-7 or BDS2005-BDS2006
// invoked from pe_bds.pat
//
// Feel free to modify this file as you wish.
//

#include <idc.idc>

static main()
{
  // Set Delphi-Style string
  //set_inf_attr(INF_STRTYPE,STRTYPE_LEN4);

  // Set demangled names to display
  //set_inf_attr(INF_DEMNAMES,DEMNAM_NAME);

  // Set compiler to Borland
  set_inf_attr(INF_COMPILER, COMP_BC);
}


// Add old borland signatures
static bor32(ea)
{
  AddPlannedSig("bh32rw32");
  AddPlannedSig("b32vcl");
  SetOptionalSigs("bdsext/bh32cls/bh32owl/bh32ocf/b5132mfc/bh32dbe/b532cgw");
  return ea;
}

// Add latest version of Borland Cbuilder (Embarcadero)
static emb(ea)
{
  AddPlannedSig("bds8rw32");
  AddPlannedSig("bds8vcl");
  SetOptionalSigs("bdsboost/bds8ext");
  return ea;
}

// Detect the latest version of Borland Cbuilder (Embarcadero)
static detect(ea)
{
  // Use version string to detect which signatures to use. Both bds08
  // and bds10 (up to xe10) have two null bytes after the string we are
  // testing for, which comes immediately before the argument ea.
  //
  // bds06: Borland C++ - Copyright 2005 Borland Corporation
  // bds08: CodeGear C++ - Copyright 2008 Embarcadero Technologies
  // bds10: Embarcadero RAD Studio - Copyright 2009 Embarcadero Technologies, Inc.

  if ( (get_wide_byte(ea - 0x1A    ) == 'E'
     && get_wide_byte(ea - 0x1A + 1) == 'm'
     && get_wide_byte(ea - 0x1A + 2) == 'b')
    || (get_wide_byte(ea - 0x20    ) == 'E'
     && get_wide_byte(ea - 0x20 + 1) == 'm'
     && get_wide_byte(ea - 0x20 + 2) == 'b') )
  {
    ResetPlannedSigs();
    emb(ea);
  }
  return ea;
}

