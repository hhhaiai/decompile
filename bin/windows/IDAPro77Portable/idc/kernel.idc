//
//      This file show how to insert you own comments for the imported DLLs.
//      This file inserts a comment for the kernel function #23 'LOCKSEGMENT'.
//      You may add your own comments for other functions and DLLs.
//      To execute this file your should choose 'Execute IDC file' command
//      from the IDA menu. Usually the  hotkey is F2.
//

#include <idc.idc>

static main(void)
{
  auto faddr;
  auto fname;

  msg("Loading comments...\n");
  fname = sprintf("KERNEL_%ld", 23);        // build the function name
  faddr = get_name_ea_simple(fname);             // get function address
  if ( faddr != -1 ) {                  // if the function exists
    update_extra_cmt(faddr,E_PREV + 0,";컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴컴");
    update_extra_cmt(faddr,E_PREV + 1,"; LockSegment (2.x)");
    update_extra_cmt(faddr,E_PREV + 2,"; ");
    update_extra_cmt(faddr,E_PREV + 3,"; In: AX - segment to lock");
    update_extra_cmt(faddr,E_PREV + 4,";     LockSegment function locks the specified discardable");
    update_extra_cmt(faddr,E_PREV + 5,"; segment. The segment is locked into memory at the given");
    update_extra_cmt(faddr,E_PREV + 6,"; address and its lock count is incremented (increased by one).");
    update_extra_cmt(faddr,E_PREV + 7,"; Returns");
    update_extra_cmt(faddr,E_PREV + 8,"; The return value specifies the data segment if the function is");
    update_extra_cmt(faddr,E_PREV + 9,"; successful. It is NULL if the segment has been discarded or an");
    update_extra_cmt(faddr,E_PREV + 10,"; error occurs.");
  }
  msg("Comment(s) are loaded.\n");
}
