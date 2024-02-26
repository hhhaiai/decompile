//
// Sample IDC program to automate IDA.
//
// IDA can be run from the command line in the batch (non-interactive) mode.
//
// If IDA is started with
//
//         ida -A -Sanalysis.idc file
//
// then this IDC file will be executed. It performs the following:
//
//   - analyzes the input file
//   - creates the output file
//   - exits to the operating system
//
// Feel free to modify this file as you wish
// (or write your own script/plugin to automate IDA)
//
// Since the script calls the qexit() function at the end,
// it can be used in the batch files (use text mode idat)
//
// NB: "ida -B file" is a shortcut for the command line above
//

#include <idc.idc>

static main()
{
  // turn on coagulation of data in the final pass of analysis
  set_inf_attr(INF_AF, get_inf_attr(INF_AF) | AF_DODATA | AF_FINAL);
  // .. and plan the entire address space for the final pass
  auto_mark_range(0, BADADDR, AU_FINAL);

  msg("Waiting for the end of the auto analysis...\n");
  auto_wait();

  msg("\n\n------ Creating the output file.... --------\n");
  auto file = get_idb_path()[0:-4] + ".asm";

  auto fhandle = fopen(file, "w");
  gen_file(OFILE_ASM, fhandle, 0, BADADDR, 0); // create the assembler file
  msg("All done, exiting...\n");
  qexit(0); // exit to OS, error code 0 - success
}
