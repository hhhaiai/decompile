/*
 *      This file contains IDA built-in function declarations
 *      and internal bit definitions.
 *      Each byte of the program has 32-bit flags
 *      (low 8 bits keep the byte value).
 *      These 32 bits are used in get_full_flags/get_flags functions.
 *
 *      This file is subject to change without any notice.
 *      Future versions of IDA may use other definitions.
 */

#ifndef _IDC_IDC
#define _IDC_IDC

// ----------------------------------------------------------------------------
#define BADADDR         -1                 // Not allowed address value
#define BADSEL          -1                 // Not allowed selector value/number

#define MAXADDR         get_inf_attr(INF_PRIVRANGE_START_EA)

//
//      Flag bit definitions (for get_full_flags())
//

#define MS_VAL  0x000000FF             // Mask for byte value
#define FF_IVL  0x00000100             // Byte has value ?


/// Do flags contain byte value? (i.e. has the byte a value?)
/// if not, the byte is uninitialized.

#define has_value(F)   ((F & FF_IVL) != 0)     // any defined value?


/// Get byte value from flags
/// Get value of byte provided that the byte is initialized.
/// This macro works ok only for 8-bit byte machines.

#define byte_value(F)  (F & MS_VAL)    // quick replacement for get_wide_byte()


/// Is the byte initialized?

#define is_loaded(ea)    has_value(get_full_flags(ea))  // any defined value?


/// \id is_code

#define MS_CLS  0x00000600             // Mask for typing
#define FF_CODE 0x00000600             // Code ?
#define FF_DATA 0x00000400             // Data ?
#define FF_TAIL 0x00000200             // Tail ?
#define FF_UNK  0x00000000             // Unknown ?

#define is_code(F)       ((F & MS_CLS) == FF_CODE) // is code byte?
#define is_data(F)       ((F & MS_CLS) == FF_DATA) // is data byte?
#define is_tail(F)       ((F & MS_CLS) == FF_TAIL) // is tail byte?
#define is_unknown(F)    ((F & MS_CLS) == FF_UNK)  // is unexplored byte?
#define is_head(F)       ((F & FF_DATA) != 0)      // is start of code/data?


/// \id CommonBits
//
//      Common bits
//

#define MS_COMM 0x000FF800             // Mask of common bits
#define FF_COMM 0x00000800             // Has comment?
#define FF_REF  0x00001000             // has references?
#define FF_LINE 0x00002000             // Has next or prev cmt lines ?
#define FF_NAME 0x00004000             // Has user-defined name ?
#define FF_LABL 0x00008000             // Has dummy name?
#define FF_FLOW 0x00010000             // Exec flow from prev instruction?
#define FF_SIGN 0x00020000             // Inverted sign of operands
#define FF_BNOT 0x00040000             // Bitwise negation of operands
#define FF_ANYNAME      (FF_LABL|FF_NAME)

#define is_flow(F)       ((F & FF_FLOW) != 0)
#define is_extra_cmts(F) ((F & FF_LINE) != 0)
#define has_xref(F)      ((F & FF_REF)  != 0)
#define has_name(F)      ((F & FF_NAME) != 0)
#define has_user_name(F) ((F & FF_ANYNAME) == FF_NAME)


/// \id OpTypes

#define MS_0TYPE 0x00F00000            // Mask for 1st arg typing
#define FF_0VOID 0x00000000            // Void (unknown)?
#define FF_0NUMH 0x00100000            // Hexadecimal number?
#define FF_0NUMD 0x00200000            // Decimal number?
#define FF_0CHAR 0x00300000            // Char ('x')?
#define FF_0SEG  0x00400000            // Segment?
#define FF_0OFF  0x00500000            // Offset?
#define FF_0NUMB 0x00600000            // Binary number?
#define FF_0NUMO 0x00700000            // Octal number?
#define FF_0ENUM 0x00800000            // Enumeration?
#define FF_0FOP  0x00900000            // Forced operand?
#define FF_0STRO 0x00A00000            // Struct offset?
#define FF_0STK  0x00B00000            // Stack variable?
#define FF_0FLT  0x00C00000            // Floating point number?
#define FF_0CUST 0x00D00000            // Custom format type?

#define MS_1TYPE 0x0F000000            // Mask for 2nd arg typing
#define FF_1VOID 0x00000000            // Void (unknown)?
#define FF_1NUMH 0x01000000            // Hexadecimal number?
#define FF_1NUMD 0x02000000            // Decimal number?
#define FF_1CHAR 0x03000000            // Char ('x')?
#define FF_1SEG  0x04000000            // Segment?
#define FF_1OFF  0x05000000            // Offset?
#define FF_1NUMB 0x06000000            // Binary number?
#define FF_1NUMO 0x07000000            // Octal number?
#define FF_1ENUM 0x08000000            // Enumeration?
#define FF_1FOP  0x09000000            // Forced operand?
#define FF_1STRO 0x0A000000            // Struct offset?
#define FF_1STK  0x0B000000            // Stack variable?
#define FF_1FLT  0x0C000000            // Floating point number?
#define FF_1CUST 0x0D000000            // Custom format type?

// The following macros answer questions like
//   'is the 1st (or 2nd) operand of instruction or data of the given type'?
// Please note that data items use only the 1st operand type (is...0)

#define is_defarg0(F)    ((F & MS_0TYPE) != FF_0VOID)
#define is_defarg1(F)    ((F & MS_1TYPE) != FF_1VOID)
#define is_dec0(F)       ((F & MS_0TYPE) == FF_0NUMD)
#define is_dec1(F)       ((F & MS_1TYPE) == FF_1NUMD)
#define is_hex0(F)       ((F & MS_0TYPE) == FF_0NUMH)
#define is_hex1(F)       ((F & MS_1TYPE) == FF_1NUMH)
#define is_oct0(F)       ((F & MS_0TYPE) == FF_0NUMO)
#define is_oct1(F)       ((F & MS_1TYPE) == FF_1NUMO)
#define is_bin0(F)       ((F & MS_0TYPE) == FF_0NUMB)
#define is_bin1(F)       ((F & MS_1TYPE) == FF_1NUMB)
#define is_off0(F)       ((F & MS_0TYPE) == FF_0OFF)
#define is_off1(F)       ((F & MS_1TYPE) == FF_1OFF)
#define is_char0(F)      ((F & MS_0TYPE) == FF_0CHAR)
#define is_char1(F)      ((F & MS_1TYPE) == FF_1CHAR)
#define is_seg0(F)       ((F & MS_0TYPE) == FF_0SEG)
#define is_seg1(F)       ((F & MS_1TYPE) == FF_1SEG)
#define is_enum0(F)      ((F & MS_0TYPE) == FF_0ENUM)
#define is_enum1(F)      ((F & MS_1TYPE) == FF_1ENUM)
#define is_manual0(F)    ((F & MS_0TYPE) == FF_0FOP)
#define is_manual1(F)    ((F & MS_1TYPE) == FF_1FOP)
#define is_stroff0(F)    ((F & MS_0TYPE) == FF_0STRO)
#define is_stroff1(F)    ((F & MS_1TYPE) == FF_1STRO)
#define is_stkvar0(F)    ((F & MS_0TYPE) == FF_0STK)
#define is_stkvar1(F)    ((F & MS_1TYPE) == FF_1STK)
#define is_float0(F)     ((F & MS_0TYPE) == FF_0FLT)
#define is_float1(F)     ((F & MS_1TYPE) == FF_1FLT)
#define is_custfmt0(F)   ((F & MS_0TYPE) == FF_0CUST)
#define is_custfmt1(F)   ((F & MS_1TYPE) == FF_1CUST)

//
//      Bits for DATA bytes
//
#define DT_TYPE       0xF0000000       // Mask for DATA typing

#define FF_BYTE       0x00000000       // byte
#define FF_WORD       0x10000000       // word
#define FF_DWORD      0x20000000       // dword
#define FF_QWORD      0x30000000       // qword
#define FF_TBYTE      0x40000000       // tbyte
#define FF_STRLIT     0x50000000       // ASCII    ?
#define FF_STRUCT     0x60000000       // Struct   ?
#define FF_OWORD      0x70000000       // octaword (16 bytes/128 bits)
#define FF_FLOAT      0x80000000       // float
#define FF_DOUBLE     0x90000000       // double
#define FF_PACKREAL   0xA0000000       // packed decimal real
#define FF_ALIGN      0xB0000000       // alignment directive
#define FF_CUSTOM     0xD0000000       // custom data type
#define FF_YWORD      0xE0000000       // ymm word (32 bytes/256 bits)
#define FF_ZWORD      0xF0000000       // zmm word (64 bytes/512 bits)

#define is_byte(F)      (is_data(F) && (F & DT_TYPE) == FF_BYTE)
#define is_word(F)      (is_data(F) && (F & DT_TYPE) == FF_WORD)
#define is_dword(F)     (is_data(F) && (F & DT_TYPE) == FF_DWORD)
#define is_qword(F)     (is_data(F) && (F & DT_TYPE) == FF_QWORD)
#define is_oword(F)     (is_data(F) && (F & DT_TYPE) == FF_OWORD)
#define is_yword(F)     (is_data(F) && (F & DT_TYPE) == FF_YWORD)
#define is_tbyte(F)     (is_data(F) && (F & DT_TYPE) == FF_TBYTE)
#define is_float(F)     (is_data(F) && (F & DT_TYPE) == FF_FLOAT)
#define is_double(F)    (is_data(F) && (F & DT_TYPE) == FF_DOUBLE)
#define is_pack_real(F) (is_data(F) && (F & DT_TYPE) == FF_PACKREAL)
#define is_strlit(F)    (is_data(F) && (F & DT_TYPE) == FF_STRLIT)
#define is_struct(F)    (is_data(F) && (F & DT_TYPE) == FF_STRUCT)
#define is_align(F)     (is_data(F) && (F & DT_TYPE) == FF_ALIGN)
#define is_custom(F)    (is_data(F) && (F & DT_TYPE) == FF_CUSTOM)

//
//      Bits for CODE bytes
//

#define MS_CODE 0xF0000000
#define FF_FUNC 0x10000000             // function start?
#define FF_IMMD 0x40000000             // Has Immediate value ?
#define FF_JUMP 0x80000000             // Has jump table

//
//      Loader flags
//

#define NEF_SEGS   0x0001               // Create segments
#define NEF_RSCS   0x0002               // Load resources
#define NEF_NAME   0x0004               // Rename entries
#define NEF_MAN    0x0008               // Manual load
#define NEF_FILL   0x0010               // Fill segment gaps
#define NEF_IMPS   0x0020               // Create imports section
#define NEF_FIRST  0x0080               // This is the first file loaded
#define NEF_CODE   0x0100               // for load_binary_file:
#define NEF_RELOAD 0x0200               // reload the file at the same place:
#define NEF_FLAT   0x0400               // Autocreated FLAT group (PE)


#undef _notdefinedsymbol
#ifdef _notdefinedsymbol // There aren't declarations in IDC, so comment them

//         List of built-in functions
//         --------------------------
//
// The following conventions are used in this list:
//   'ea' is a linear address
//   'success' is 0 if a function failed, 1 otherwise
//   'void' means that function returns no meaningful value (always 0)
//   'string' means that function returns a string on success or an empty string on failure (unless specified otherwise)
//
//  All function parameter conversions are made automatically.
//
// ----------------------------------------------------------------------------
//                       M I S C E L L A N E O U S
// ----------------------------------------------------------------------------

/// \header is_value...() functions
/// Check the variable type
/// Returns true if the variable type is the expected one
/// Thread-safe functions.

success value_is_string(var);
success value_is_long(var);
success value_is_float(var);
success value_is_object(var);
success value_is_func(var);
success value_is_pvoid(var);
success value_is_int64(var);


/// Return value of expression: ((seg<<4) + off)

long to_ea(long seg, long off);


/// Return a formatted string.
///      format - printf-style format string.
///               %a - means address expression.
///               floating point values are output only in one format
///                regardless of the character specified (f, e, g, E, G)
///               %p is not supported.
/// Thread-safe function.

string sprintf(string format, ...);


/// Return substring of a string
///      str - input string
///      x1  - starting index (0..n)
///      x2  - ending index. If x2 == -1, then return substring
///            from x1 to the end of string.
/// Thread-safe function.

string substr(string str, long x1, long x2);


/// Search a substring in a string
///      str    - input string
///      substr - substring to search
///      icase  - is case-insenstive search?
/// returns: 0..n - index in the 'str' where the substring starts
///          -1   - if the substring is not found
/// Thread-safe function.

long strstr(string str, string substr, bool icase=false);
#endif
#define stristr(str, substr) strstr((str), (substr), 1)
#ifdef _notdefinedsymbol


/// Convert string to lowercase
///      str    - input string
/// returns: lowercase string
/// Thread-safe function.

string tolower(string str);


/// Convert string to uppercase
///      str    - input string
/// returns: uppercase string
/// Thread-safe function.

string toupper(string str);


/// Return length of a string in bytes
///      str - input string
/// Returns: length (0..n)
/// Thread-safe function.

long strlen(string str);


/// Return string filled with the specified character
///      chr - character to fill with
///      len - number of characters
/// Returns: filled string
/// Thread-safe function.

string strfill(long chr, long len);


/// Remove trailing zero bytes from a string
///      str - input string
/// Returns: trimmed string
/// Thread-safe function.

string trim(string str);


/// Convert ascii string to a binary number.
/// (this function is the same as hexadecimal 'strtoul' from C library,
///  use long() for atol)
/// Thread-safe function.

long xtol(string str);


/// Convert address value to a string
/// Returns address in the form 'seg000:1234'
/// (the same as in line prefixes)

string atoa(long ea);


/// Convert a number to a string.
///      n - number
///      radix - number base (2, 8, 10, 16)
/// Thread-safe function.

string ltoa(long n, long radix);


/// Convert ascii string to a number
///      str - a decimal representation of a number
/// returns: a binary number
/// See also \ref ord() function
/// Thread-safe function.

long atol(string str);


/// Get code of an ascii character
///      str - string with one character
/// returns: a binary number, character code
/// See also \ref atol() function
/// Thread-safe function.

long ord(string str);


/// rotate a value to the left (or right)
///    arguments:
///         x      - value to rotate
///         count  - number of times to rotate. negative counter means
///                  rotate to the right
///         nbits  - number of bits to rotate
///         offset - offset of the first bit to rotate
/// returns: the value with the specified field rotated
///          all other bits are not modified
/// Thread-safe function.

long rotate_left(long value, long count, long nbits, long offset);

#endif
#define rotate_dword(x, count) rotate_left(x, count, 32, 0)
#define rotate_word(x, count)  rotate_left(x, count, 16, 0)
#define rotate_byte(x, count)  rotate_left(x, count,  8, 0)
#ifdef _notdefinedsymbol


/// Add hotkey for IDC function
///      hotkey  - hotkey name ('a', "Alt-A", etc)
///      idcfunc - IDC function name
/// returns:
#endif
#define IDCHK_OK        0       // ok
#define IDCHK_ARG       -1      // bad argument(s)
#define IDCHK_KEY       -2      // bad hotkey name
#define IDCHK_MAX       -3      // too many IDC hotkeys
#ifdef _notdefinedsymbol

long add_idc_hotkey(string hotkey, string idcfunc);


/// Delete IDC function hotkey

success del_idc_hotkey(string hotkey);


/// Move cursor to the specifed linear address
///      ea - linear address
/// Screen is refreshed at the end of IDC execution

success jumpto(long ea);


/// Wait for the end of autoanalysis
/// This function will suspend execution of IDC program
/// till the autoanalysis queue is empty.

void auto_wait();


/// Compile an IDC script file.
/// The input should not contain functions that are
/// currently executing - otherwise the behaviour of the replaced
/// functions is undefined.
///      path - path to compile
/// returns: 0 - ok, otherwise it returns an error message.
/// Thread-safe function.

string compile_idc_file(string path);


/// Compile IDC script text.
/// The input should not contain functions that are
/// currently executing - otherwise the behaviour of the replaced
/// functions is undefined.
///      idc_text - text to compile
/// returns: 0 - ok, otherwise it returns an error message.
/// Thread-safe function.

string compile_idc_text(string idc_text);


/// Compile and execute IDC statement(s)
///      input  - IDC statement(s)
/// returns: 1 - ok, otherwise throws an exception
/// Thread-safe function.

long exec_idc(string input);


/// Evaluate an expression, in the current scripting language.
///      expr - an expression
/// returns: the expression value.
/// If there are problems, the returned value will be "IDC_FAILURE: xxx"
/// where xxx is the error description
/// Thread-safe function.

string or long eval(string expr);

#endif
// Macro to check for evaluation failures:
#define EVAL_FAILURE(code) (value_is_string(code) && substr(code, 0, 13) == "IDC_FAILURE: ")
#ifdef _notdefinedsymbol


/// Evaluate a python expression.
///      expr - an expression
/// returns: the expression value.
/// This function will throw an exception if the expression can not be evaluated.
/// Thread-safe function.

any eval_python(string expr);


/// Execute a python statement.
///      stmt - a statement
/// returns: number 0 if executed the statement, otherwise an error string
/// Thread-safe function.

string or long exec_python(string stmt);


/// Save current database to the specified idb file
///      idbname - name of the idb file. if empty, the current idb
///                file will be used.
///      flags   - DBFL_BAK or 0

success save_database(string idbname, long flags);

#endif
#define DBFL_BAK        0x04            // create backup file
#ifdef _notdefinedsymbol


/// Delete information about the user who created the database

void del_user_info();


/// check consistency of IDB name records, return number of bad ones
///      do_repair: (bool) try to repair netnode header it TRUE

long validate_idb_names(long do_repair = 0);


/// Stop execution of IDC program, close the database and exit to OS
///      code - code to exit with.

void qexit(long code);


/// Execute an OS command.
/// IDA will wait for the started program to finish.
/// In order to start the command in parallel, use OS methods.
/// For example, you may start another program in parallel using "start" command.
///      command - command line to execute
/// returns: error code from OS
/// Thread-safe function.

long call_system(string command);


/// Sleep the specified number of milliseconds
/// This function suspends IDA for the specified amount of time
/// Thread-safe function.

void qsleep(long milliseconds);


/// Load and run a plugin
/// The plugin name is a short plugin name without an extension
/// returns: 0 if could not load the plugin, 1 if ok

success load_and_run_plugin(string name, long arg);


/// Load (plan to apply) a FLIRT signature file
///      name - signature name without path and extension
/// returns: 0 if could not load the signature file, !=0 otherwise

success plan_to_apply_idasgn(string name);


/// Get the directory part of the given path

string qdirname(string path);


/// Get the file name part of the given path

string qbasename(string path);


/// Construct filename from base name and extension

string qmakefile(string base, string ext);


/// Is the file name absolute (not relative to the current dir?)

long qisabspath(string file);


/// Convert relative path to absolute path

string qmake_full_path(string path);


/// Search for a file in the PATH environment variable or the current directory

string search_path(string file, long search_cwd);


/// Get the extension of file name

string get_file_ext(string filename);


/// Sanitize the file name.
/// Remove the directory path, and replace wildcards ? * and chars<' ' with underscore.

string sanitize_file_name(string filename);


// ----------------------------------------------------------------------------
//  O B J E C T S
// ----------------------------------------------------------------------------
// NB: Thread-safe functions should not be called on the same variable
//     concurrently.

/// Does an object attribute exist?
///      self  - object
///      attr  - attribute name
/// Thread-safe function.

success hasattr(object self, string attr);


/// Get object attribute
///      self  - object
///      attr  - attribute name
/// This function gets the attribute value without calling __getattr__()
/// Thread-safe function.

any getattr(object self, string attr);


/// Set object attribute
///      self  - object
///      attr  - attribute name
///      value - value
/// This function sets the attribute value without calling __setattr__()
/// Returns false: self is not an object
/// Thread-safe function.

success setattr(object self, string attr, any value);


/// Del object attribute
///      self  - object
///      attr  - attribute name
/// Thread-safe function.

success delattr(object self, string attr);


/// Get the first object attribute
///      self  - object
/// If there are no attributes, returns 0
/// Thread-safe function.

string firstattr(object self);


/// Get the last object attribute
///      self  - object
/// If there are no attributes, returns 0
/// Thread-safe function.

string lastattr(object self);


/// Get the next object attribute
///      self  - object
///      attr  - current attribute name
/// If there are no more attributes, returns 0
/// Thread-safe function.

string nextattr(object self, string attr);


/// Get the previois object attribute
///      self  - object
///      attr  - current attribute name
/// If there are no more attributes, returns 0
/// Thread-safe function.

string prevattr(object self, string attr);


/// Convert the object into a C structure and store it into the idb or a buffer
///  typeinfo - description of the C structure. Can be specified
///             as a declaration string or result of \ref get_tinfo() or
///             similar functions
///  dest     - address (ea) to store the C structure
///             OR a reference to a destination string
///  flags    - combination of PIO_.. bits

void object.store(typeinfo, dest, flags);

#endif
#define PIO_NOATTR_FAIL 0x0004 // missing attributes are not ok
#define PIO_IGNORE_PTRS 0x0008 // do not follow pointers

#define PDF_INCL_DEPS 0x1      // Include dependencies
#define PDF_DEF_FWD   0x2      // Allow forward declarations
#define PDF_DEF_BASE  0x4      // Include base '__intX' types
#ifdef _notdefinedsymbol


/// Retrieve a C structure from the idb or a buffer and convert it into an object
///  typeinfo - description of the C structure. Can be specified
///             as a declaration string or result of \ref get_tinfo() or
///             similar functions
///  src      - address (ea) to retrieve the C structure from
///             OR a string buffer previously packed with the store method
///  flags    - combination of \ref object_store[PIO_...] bits

void object.retrieve(typeinfo, src, flags);


/// Print typeinfo in a human readable form
///   flags - optional parameter, combination of PRTYPE_... bits
/// The typeinfo object must have the "typid" attribute
/// If the "name" attribute is present, it will be used in the output too
/// If failed, returns 0

string typeinfo.print(flags);

#endif
#define PRTYPE_1LINE   0x0000 // print to one line
#define PRTYPE_MULTI   0x0001 // print to many lines
#define PRTYPE_TYPE    0x0002 // print type declaration (not variable declaration)
#define PRTYPE_PRAGMA  0x0004 // print pragmas for alignment
#define PRTYPE_SEMI    0x0008 // append ; to the end
#define PRTYPE_CPP     0x0010 // use c++ name (only for print_type2)
#define PRTYPE_DEF     0x0020 // tinfo_t: print definition, if available
#define PRTYPE_NOARGS  0x0040 // tinfo_t: do not print function argument names
#define PRTYPE_NOARRS  0x0080 // tinfo_t: print arguments with #FAI_ARRAY as pointers
#define PRTYPE_NORES   0x0100 // tinfo_t: never resolve types (meaningful with PRTYPE_DEF)
#define PRTYPE_RESTORE 0x0200 // tinfo_t: print restored types for #FAI_ARRAY and #FAI_STRUCT
#define PRTYPE_NOREGEX 0x0400 // do not apply regular expressions to beautify name
#define PRTYPE_COLORED 0x0800 // add color tag COLOR_SYMBOL for any parentheses, commas and colons
#define PRTYPE_METHODS 0x1000 // tinfo_t: print udt methods
#ifdef _notdefinedsymbol


/// Return the type size in bytes
/// 0xFFFFFFFF is the size cannot be calculated

long typeinfo.size();


// ----------------------------------------------------------------------------
//  L O A D E R  I N P U T  C L A S S
// ----------------------------------------------------------------------------

/// Open an input file for reading
///      filename - name of the file to open
///      is_remote- !=0 means to open a file on the remote computer
///                 (possible only during remote debugging)
/// Returns loader_input_t object or 0
/// \header loader_input_t

loader_input_t open_loader_input(string filename, long is_remote);


class loader_input_t
{
/// Read from the input file
///      buf - reference to the variable that will hold the read bytes
///            in form of a string
///      size - number of bytes to read
/// Returns: number of read bytes

long loader_input_t.read(vref buf, long size);

/*
// For example:

        auto li, buf;
        li = open_loader_input("myfile", 0);
        li.read(&buf, 100);
*/


/// Get size of the input file

long loader_input_t.size();


/// Seek in the input file
///      pos - position to seek to
///      whence - where from?
/// Returns: the new file position

long loader_input_t.seek(long pos, long whence);

#endif
#define SEEK_SET   0 // from the file start
#define SEEK_CUR   1 // from the current position
#define SEEK_END   2 // from the file end
#ifdef _notdefinedsymbol


/// Get the current file position

long loader_input_t.tell();


/// Read one line of text from the input file
///      maxsize - maximal size of the line
/// Returns: one line of text or 0
/// If the input file contains zeroes, the line will be truncated at them

string loader_input_t.gets(long maxsize);


/// Read a zero terminated string from the input file
///      pos     - file position to read from
///      maxsize - maximal size of the string
/// Returns: a string or 0

string loader_input_t.getz(long pos, long maxsize);


/// Read one byte from the input file
/// Returns -1 if no more bytes

long loader_input_t.getc();


/// Read a multibyte value from the input file
///      result - reference to the variable that will hold the result
///      size   - size of the value. Usually is: 1, 2, 4, 8
///      be     - treat bytes as big-endian?
/// Returns: 0:ok, -1:failure

long loader_input_t.readbytes(vref result, long size, long be);


/// Close the input file

void loader_input_t.close();


};

#endif
// Definitions for loaders that are implemented in IDC

// The bit that can be used in the 'options' attribute of the object
// that is returned by loader.accept_file()
#define ACCEPT_ARCHIVE  0x2000            // Specify that a file format is served by
                                          // archive loader
#define ACCEPT_CONTINUE 0x4000            // Specify that the function must be called
                                          // another time
#define ACCEPT_FIRST    0x8000            // Put the loader at the top of the list
                                          // on the 'load file' dialog

// Flags for the loader.load_file() function
#define NEF_SEGS        0x0001            // Create segments
#define NEF_RSCS        0x0002            // Load resources
#define NEF_NAME        0x0004            // Rename entries
#define NEF_MAN         0x0008            // Manual load
#define NEF_FILL        0x0010            // Fill segment gaps
#define NEF_IMPS        0x0020            // Create import segment
#define NEF_FIRST       0x0080            // This is the first file loaded
                                          // into the database.
#define NEF_CODE        0x0100            // for load_binary_file:
                                          //   load as a code segment
#define NEF_RELOAD      0x0200            // reload the file at the same place:
                                          //   don't create segments
                                          //   don't create fixup info
                                          //   don't import segments
                                          //   etc
                                          // load only the bytes into the base.
                                          // a loader should have LDRF_RELOAD
                                          // bit set
#define NEF_FLAT        0x0400            // Autocreate FLAT group (PE)
#define NEF_MINI        0x0800            // Create mini database (do not copy
                                          // segment bytes from the input file;
                                          // use only the file header metadata)
#define NEF_LOPT        0x1000            // Display additional loader options dialog
#define NEF_LALL        0x2000            // Load all segments without questions
#ifdef _notdefinedsymbol

// ----------------------------------------------------------------------------
// C H A N G E   P R O G R A M   R E P R E S E N T A T I O N
// ----------------------------------------------------------------------------

/// Delete all segments, instructions, comments, i.e. everything
/// except values of bytes.

void delete_all_segments();


/// Create an instruction at the specified address
///      ea - linear address
/// returns: 0 - can't create an instruction (no such opcode, the instruction would
///              overlap with existing items, etc)
///          otherwise returns length of the instruction in bytes

long create_insn(long ea);


/// Perform full analysis of the range
///      sEA        - starting linear address
///      eEA        - ending linear address (excluded)
///      final_pass - make the final pass over the specified range
/// returns: 1-ok, 0-Ctrl-Break was pressed.

long plan_and_wait(long sEA, long eEA, long final_pass=1);


/// Rename an address
///      ea - linear address
///      name - new name of address. If name == "", then delete old name
///      flags - combination of SN_... constants
/// returns: 1-ok, 0-failure

success set_name(long ea, string name, long flags=SN_CHECK);

#endif
#define SN_CHECK        0x01    // Fail if the name contains invalid characters
                                // If this bit is clear, all invalid chars
                                // (those !is_ident_char()) will be replaced
                                // by SUBSTCHAR
                                // List of valid characters is defined in ida.cfg
#define SN_NOCHECK      0x00    // Replace invalid chars with SUBSTCHAR
#define SN_PUBLIC       0x02    // if set, make name public
#define SN_NON_PUBLIC   0x04    // if set, make name non-public
#define SN_WEAK         0x08    // if set, make name weak
#define SN_NON_WEAK     0x10    // if set, make name non-weak
#define SN_AUTO         0x20    // if set, make name autogenerated
#define SN_NON_AUTO     0x40    // if set, make name non-autogenerated
#define SN_NOLIST       0x80    // if set, exclude name from the list
                                // if not set, then include the name into
                                // the list (however, if other bits are set,
                                // the name might be immediately excluded
                                // from the list)
#define SN_NOWARN       0x100   // don't display a warning if failed
#define SN_LOCAL        0x200   // create local name. a function should exist.
                                // local names can't be public or weak.
                                // also they are not included into the list of names
                                // they can't have dummy prefixes
#define SN_IDBENC       0x400   // the name is given in the IDB encoding;
                                // non-ASCII bytes will be decoded accordingly.
                                // Specifying SN_IDBENC also implies SN_NODUMMY
#define SN_FORCE        0x800   // if the specified name is already present
                                // in the database, try variations with a
                                // numerical suffix like "_123"
#define SN_NODUMMY      0x1000  // automatically prepend the name with '_' if it
                                // begins with a dummy suffix such as 'sub_'.
                                // See also SN_IDBENC
#define SN_DELTAIL      0x2000  // if name cannot be set because of a tail byte,
                                // delete the hindering item
#ifdef _notdefinedsymbol


/// Set an indented comment.
///      ea      - linear address
///      comment - comment string
///      rptble  - is repeatable?

success set_cmt(long ea, string comment, long rptble);


/// Create an array.
///      ea      - linear address
///      nitems  - size of array in items
/// This function will create an array of the items with the same type as the
/// type of the item at 'ea'. If the byte at 'ea' is undefined, then this
/// function will create an array of bytes.

success make_array(long ea, long nitems);


/// Create a string.
/// This function creates a string (the string type is determined by the value
/// of get_inf_attr(INF_STRTYPE))
///   ea      - linear address
///   len     - length of the string in bytes
/// returns: 1-ok, 0-failure
/// note: the type of an existing string is returned by get_str_type()

success create_strlit(long ea, long len=0);


/// Create a data item at the specified address
///      ea - linear address
///      flags - FF_BYTE..FF_PACKREAL
///      size - size of item in bytes
///      tid - for FF_STRUCT the structure id
/// returns: 1-ok, 0-failure

success create_data(long ea, long flags, long size, long tid);


/// Convert the current item to a byte
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_byte(ea)     create_data(ea, FF_BYTE, 1, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a word (2 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_word(ea)     create_data(ea, FF_WORD, 2, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a double word (4 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_dword(ea)    create_data(ea, FF_DWORD, 4, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a quadro word (8 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_qword(ea)    create_data(ea, FF_QWORD, 8, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a octa word (16 bytes/128 bits)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_oword(ea)    create_data(ea, FF_OWORD, 16, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a ymm word (32 bytes/256 bits)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_yword(ea)    create_data(ea, FF_YWORD, 32, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a floating point (4 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_float(ea)    create_data(ea, FF_FLOAT, 4, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a double floating point (8 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_double(ea)   create_data(ea, FF_DOUBLE, 8, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a packed real (10 or 12 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_pack_real(ea) create_data(ea, FF_PACKREAL, 10, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a tbyte (10 or 12 bytes)
///      ea - linear address
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_tbyte(ea)    create_data(ea, FF_TBYTE, 10, BADADDR)
#ifdef _notdefinedsymbol


/// Convert the current item to a custom data type
///      ea   - linear address
///      size - size of the item
///      dtid - custom data type id (see @hlpIdcfind_custom_data_type[find_custom_data_type])
///      fid  - custom data format id (see @hlpIdcfind_custom_data_format[find_custom_data_format])
/// returns: 1-ok, 0-failure
/// This is a convenience macro, see also \ref create_data() function

#endif
#define create_custom_data(ea, size, dtid, fid) create_data(ea, FF_CUSTOM, size, dtid|((fid)<<16))
#ifdef _notdefinedsymbol


/// Create a structure data item at the specified address
///      ea      - linear address
///      size    - structure size in bytes. -1 means that the size
///                will be calculated automatically
///      strname - name of a structure type
/// returns: 1-ok, 0-failure

success create_struct(long ea, long size, string strname);


/// Convert the current item to an alignment directive
///      ea      - linear address
///      count   - number of bytes to convert
///      align   - 0 or 1..32
///                if it is 0, the correct alignment will be calculated
///                by the kernel
/// returns: 1-ok, 0-failure

success create_align(long ea, long count, long align);


/// Create a local variable
///      start, end - range of addresses for the local variable.
///                   For the stack variables the end address is ignored.
///                   If there is no function at 'start' then this function.
///                   will fail.
///      location  -  the variable location in the "[bp+xx]" form where xx is
///                   a number. The location can also be specified
///                   as a register name.
///      name      -  name of the local variable
/// returns: 1-ok, 0-failure

success define_local_var(long start, long end, string location, string name);


/// Convert item (instruction/data) to unexplored bytes.
/// The whole item (including the head and tail bytes) will be destroyed.
/// It is allowed to pass any address in the item to this function
///      ea     - any address within the item to delete
///      flags  - combination of DELIT_... constants
///      nbytes - number of bytes in the range to be undefined
/// returns: 1-ok, 0-failure

success del_items(ea_t ea, long flags=0, long nbytes=1);

#endif
#define DELIT_SIMPLE    0x0000  // simply undefine the specified item
#define DELIT_EXPAND    0x0001  // propogate undefined items, for example
                                // if removing an instruction removes all
                                // references to the next instruction, then
                                // plan to convert to unexplored the next
                                // instruction too.
#define DELIT_DELNAMES  0x0002  // delete any names at the specified
                                // address range (except for the starting
                                // address). this bit is valid if nbytes > 1
#define DELIT_NOTRUNC   0x0004  // don't truncate the current function
#ifdef _notdefinedsymbol


/// Set array representation format
///      ea      - linear address
///      flags   - combination of AP_... constants or 0
///      litems  - number of items per line. 0 means auto
///      align   - element alignment:
///                  -1: do not align
///                  0:  automatic alignment
///                  other values: element width
/// Returns: 1-ok, 0-failure

success set_array_params(long ea, long flags, long litems, long align);

#endif
#define AP_ALLOWDUPS    0x00000001L     // use 'dup' construct
#define AP_SIGNED       0x00000002L     // treats numbers as signed
#define AP_INDEX        0x00000004L     // display array element indexes as comments
#define AP_ARRAY        0x00000008L     // reserved (this flag is not stored in database)
#define AP_IDXBASEMASK  0x000000F0L     // mask for number base of the indexes
#define   AP_IDXDEC     0x00000000L     // display indexes in decimal
#define   AP_IDXHEX     0x00000010L     // display indexes in hex
#define   AP_IDXOCT     0x00000020L     // display indexes in octal
#define   AP_IDXBIN     0x00000030L     // display indexes in binary
#ifdef _notdefinedsymbol


/// Convert an operand of the item (instruction or data) to a binary number
///      ea  - linear address
///       n  - number of operand
///              0 - the first operand
///              1 - the second, third and all other operands
///              -1 - all operands
/// Note: the data items use only the type of the first operand
/// Returns: 1-ok, 0-failure

success op_bin(long ea, int n);

// Convert an operand of the item (instruction or data) to an octal number

success op_oct(long ea, int n);

// Convert operand to decimal, hex, char

success op_dec(long ea, int n);
success op_hex(long ea, int n);
success op_chr(long ea, int n);


/// Convert operand to an offset
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())
///      base - base of the offset as a linear address
///             If base == BADADDR then the current operand becomes non-offset
/// Example:
///  seg000:2000 dw      1234h
/// and there is a segment at paragraph 0x1000 and there is a data item
/// within the segment at 0x1234:
///  seg000:1234 MyString        db 'Hello, world!', 0
/// Then you need to specify a linear address of the segment base to
/// create a proper offset:
///      op_plain_offset(to_ea("seg000", 0x2000), 0, 0x10000);
/// and you will have:
///  seg000:2000 dw      offset MyString
/// Motorola 680x0 processor have a concept of "outer offsets".
/// If you want to create an outer offset, you need to combine number
/// of the operand with the following bit:

#endif
#define OPND_OUTER      0x80                    // outer offset base
#ifdef _notdefinedsymbol
// Please note that the outer offsets are meaningful only for
// Motorola 680x0.

success op_plain_offset(long ea, int n, long base);


/// Convert operand to a complex offset expression
/// This is a more powerful version of \ref op_plain_offset() function.
/// It allows to explicitly specify the reference type (off8, off16, etc)
/// and the expression target with a possible target delta.
/// The complex expressions are represented by IDA in the following form:
///
///         target + tdelta - base
///
/// If the target is not present, then it will be calculated using
///         target = operand_value - tdelta + base
/// The target must be present for LOW.. and HIGH.. reference types
///      ea      - linear address of the instruction/data
///      n       - number of operand to convert (the same as in op_plain_offset)
///      reftype - one of REF_... constants
///      target  - an explicitly specified expression target. if you don't
///                want to specify it, use -1. Please note that LOW... and
///                HIGH... reference type requre the target.
///      base    - the offset base (a linear address)
///      tdelta  - a displacement from the target which will be displayed
///                in the expression.

success op_offset(long ea, int n, long reftype, long target, long base, long tdelta);

#endif
#define REF_OFF8    0              // 8bit full offset
#define REF_OFF16   1              // 16bit full offset
#define REF_OFF32   2              // 32bit full offset
#define REF_LOW8    3              // low 8bits of 16bit offset
#define REF_LOW16   4              // low 16bits of 32bit offset
#define REF_HIGH8   5              // high 8bits of 16bit offset
#define REF_HIGH16  6              // high 16bits of 32bit offset
#define V695_REF_VHIGH   7         // obsolete
#define V695_REF_VLOW    8         // obsolete
#define REF_OFF64   9              // 64bit full offset
                                   // note: processor modules or plugins may register additional
                                   // custom reference types (for example, REF_HIGHA16 is
                                   // used by MIPS, SPARC, PPC, ALPHA, TRICORE, etc.)
#define REFINFO_RVA         0x10   // based reference (rva)
#define REFINFO_PASTEND     0x20   // reference past an item
                                   // it may point to an nonexistitng address
                                   // do not destroy alignment dirs
#define REFINFO_NOBASE      0x80   // offset base is a number
                                   // implies that base have be any value
                                   // nb: base xrefs are created only if base
                                   // points to the middle of a segment
#define REFINFO_SUBTRACT  0x0100   // the reference value is subtracted from
                                   // the base value instead of (as usual)
                                   // being added to it
#define REFINFO_SIGNEDOP  0x0200   // the operand value is sign-extended (only
                                   // supported for REF_OFF8/16/32/64)
#define REFINFO_NO_ZEROS  0x0400  ///< an opval of 0 will be considered invalid
#define REFINFO_NO_ONES   0x0800  ///< an opval of ~0 will be considered invalid
#ifdef _notdefinedsymbol


/// Convert operand to a segment expression
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success op_seg(long ea, int n);


/// Convert operand to a number (with default number base, radix)
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success op_num(long ea, int n);


/// Convert operand to a floating-point number
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success op_flt(long ea, int n);


/// Specify operand represenation manually.
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())
///      str - a string represenation of the operand
/// IDA will not check the specified operand, it will simply display
/// it instead of the orginal representation of the operand.

success op_man(long ea, long n, string str);// manually enter n-th operand


/// Change sign of the operand.
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success toggle_sign(long ea, int n);


/// Toggle the bitwise not operator for the operand
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success toggle_bnot(long ea, int n);


/// Convert operand to a symbolic constant
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())
///      enumid - id of enumeration type
///      serial - serial number of the constant in the enumeration
///               The serial numbers are used if there are more than
///               one symbolic constant with the same value in the
///               enumeration. In this case the first defined constant
///               get the serial number 0, then second 1, etc.
///               There could be 256 symbolic constants with the same
///               value in the enumeration.

success op_enum(long ea, int n, long enumid, long serial);


/// Convert operand to an offset in a structure
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())
///      strid - id of a structure type
///      delta - struct offset delta. usually 0. denotes the difference
///              between the structure base and the pointer into the structure.

success op_stroff(long ea, int n, long strid, long delta);


/// Convert operand to a stack variable
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())

success op_stkvar(long ea, int n);


/// Convert operand to a high offset
/// High offset is the upper 16bits of an offset.
/// This type is used by PPC, MIPS, and other RISC processors.
/// (for the explanations of 'ea' and 'n' please see \ref op_bin())
///      target - the full value (all 32bits) of the offset

success op_offset_high16(long ea, int n, long target);


/// Get id of a custom data type
///      name - name of the custom data type
/// Returns: id or -1

long find_custom_data_type(string name);


/// Get id of a custom data format
///      name - name of the custom data format
/// Returns: id or -1

long find_custom_data_format(string name);


#endif
// Every anterior/posterior line has its number.
// Anterior  lines have numbers from E_PREV
// Posterior lines have numbers from E_NEXT

#define E_PREV 1000
#define E_NEXT 2000
#ifdef _notdefinedsymbol


/// Get extra comment line
///      ea - linear address
///      n  - number of line (0..MAX_ITEM_LINES)
///           MAX_ITEM_LINES is defined in IDA.CFG
/// To get anterior  line #n use (E_PREV + n)
/// To get posterior line #n use (E_NEXT + n)
/// Returns number 0 if the comment line does not exit

string get_extra_cmt(long ea, long n);


/// Set or update extra comment line
///      ea   - linear address
///      n    - number of additional line (0..MAX_ITEM_LINES)
///      line - the line to display
/// IDA displays additional lines from number 0 up to the first unexisting
/// additional line. So, if you specify additional line #150 and there is no
/// additional line #149, your line will not be displayed.
/// MAX_ITEM_LINES is defined in IDA.CFG
/// To set anterior  line #n use (E_PREV + n)
/// To set posterior line #n use (E_NEXT + n)

void update_extra_cmt(long ea, long n, string line);


/// Delete an extra comment line
///      ea   - linear address
///      n    - number of additional line (0..MAX_ITEM_LINES)
/// To delete anterior  line #n use (E_PREV + n)
/// To delete posterior line #n use (E_NEXT + n)

void del_extra_cmt(long ea, long n);


/// Specify instruction represenation manually.
///      ea   - linear address
///      insn - a string represenation of the operand
/// IDA will not check the specified instruction, it will simply display
/// it instead of the orginal representation.

void set_manual_insn(long ea, string insn);


/// Get manual representation of instruction
///      ea   - linear address
/// This function returns value set by set_manual_insn earlier.

string get_manual_insn(long ea);


/// Change a byte in the debugged process memory only
///      ea    - linear address
///      value - new value of the byte
/// Returns: 1 if successful, 0 if not
/// Thread-safe function (may be called only from the main thread and debthread)

success patch_dbg_byte(long ea, long value);


/// Change value of a program byte
/// If debugger was active then the debugged process memory will be patched too
///      ea    - linear address
///      value - new value of the byte
/// Returns: 1 if the database has been modified,
///          0 if either the debugger is running and the process' memory
///            has value 'value' at address 'ea',
///            or the debugger is not running, and the IDB
///            has value 'value' at address 'ea already.

success patch_byte(long ea, long value);


/// Change value of a program word (2 bytes)
///      ea    - linear address
///      value - new value of the word
/// Returns: 1 if the database has been modified,
///          0 if either the debugger is running and the process' memory
///            has value 'value' at address 'ea',
///            or the debugger is not running, and the IDB
///            has value 'value' at address 'ea already.

success patch_word(long ea, long value);


/// Change value of a double word
///      ea    - linear address
///      value - new value of the double word
/// Returns: 1 if the database has been modified,
///          0 if either the debugger is running and the process' memory
///            has value 'value' at address 'ea',
///            or the debugger is not running, and the IDB
///            has value 'value' at address 'ea already.

success patch_dword(long ea, long value);


/// Change value of a quad word
///      ea    - linear address
///      value - new value of the quad word
/// Returns: 1 if the database has been modified,
///          0 if either the debugger is running and the process' memory
///            has value 'value' at address 'ea',
///            or the debugger is not running, and the IDB
///            has value 'value' at address 'ea' already.

success patch_qword(long ea, long value);


/// Set value of a segment register.
///      ea - linear address
///      reg - name of a register, like "cs", "ds", "es", etc.
///      value - new value of the segment register.
///      tag   - one of SR_... constants
/// IDA keeps tracks of all the points where segment registers change their
/// values. This function allows you to specify the correct value of a segment
/// register if IDA is not able to find the corrent value.

success split_sreg_range(long ea, string reg, long value, long tag=SR_user);

#endif
#define SR_inherit      1               // the value is inherited from the previous range
#define SR_user         2               // the value is specified by the user
#define SR_auto         3               // the value is determined by IDA
#define SR_autostart    4               // used as SR_auto for segment starting address
#ifdef _notdefinedsymbol


/// Plan to perform an action in the future.
/// This function will put your request to a special autoanalysis queue.
/// Later IDA will retrieve the request from the queue and process
/// it. There are several autoanalysis queue types. IDA will process all
/// queries from the first queue and then switch to the second queue, etc.

// plan/unplan range of addresses
void auto_mark_range(long start, long end, long queuetype);
void auto_unmark(long start, long end, long queuetype);

#endif
// plan to analyze an address
#define auto_mark(ea, qtype)      auto_mark_range(ea, (ea)+1, qtype)

#define AU_UNK  10      // make unknown
#define AU_CODE 20      // convert to instruction
#define AU_PROC 30      // make function
#define AU_USED 40      // reanalyze
#define AU_LIBF 60      // apply a flirt signature (the current signature!)
#define AU_FINAL 200    // coagulate unexplored items
#ifdef _notdefinedsymbol


// ----------------------------------------------------------------------------
//             P R O D U C E   O U T P U T   F I L E S
// ----------------------------------------------------------------------------


/// Generate an output file
///      type  - type of output file. One of OFILE_... symbols. See below.
///      fp    - the output file handle
///      ea1   - start address. For some file types this argument is ignored
///      ea2   - end address. For some file types this argument is ignored
///      flags - bit combination of GENFLG_...
/// returns: number of the generated lines.
///          -1 if an error occurred
///          OFILE_EXE: 0-can't generate exe file, 1-ok

int gen_file(long type, long file_handle, long ea1, long ea2, long flags);

#endif
// output file types:

#define OFILE_MAP  0
#define OFILE_EXE  1
#define OFILE_IDC  2
#define OFILE_LST  3
#define OFILE_ASM  4
#define OFILE_DIF  5

// output control flags:

#define GENFLG_MAPSEGS 0x0001          // map: generate map of segments
#define GENFLG_MAPNAME 0x0002          // map: include dummy names
#define GENFLG_MAPDMNG 0x0004          // map: demangle names
#define GENFLG_MAPLOC  0x0008          // map: include local names
#define GENFLG_IDCTYPE 0x0008          // idc: gen only information about types
#define GENFLG_ASMTYPE 0x0010          // asm&lst: gen information about types too
#define GENFLG_GENHTML 0x0020          // asm&lst: generate html (gui version only)
#define GENFLG_ASMINC  0x0040          // asm&lst: gen information only about types
#ifdef _notdefinedsymbol


/// Generate a flow chart GDL file
///      outfile - output file name. GDL extension will be used
///      title   - graph title
///      ea1     - beginning of the range to flow chart
///      ea2     - end of the range to flow chart. if ea2 == BADADDR
///                then ea1 is treated as an address within a function.
///                That function will be flow charted.
///      flags   - combination of CHART_... constants

success gen_flow_graph(string outfile, string title, long ea1, long ea2, long flags);

#endif
#define CHART_PRINT_NAMES 0x1000 // print labels for each block?
#define CHART_GEN_GDL     0x4000 // generate .gdl file (file extension is forced to .gdl)
#define CHART_WINGRAPH    0x8000 // call wingraph32 to display the graph
#define CHART_NOLIBFUNCS  0x0400 // don't include library functions in the graph
#ifdef _notdefinedsymbol


/// Generate a function call graph GDL file
///      outfile - output file name. GDL extension will be used
///      title   - graph title
///      ea1     - beginning of the range to flow chart
///      ea2     - end of the range to flow chart. if ea2 == BADADDR
///                then ea1 is treated as an address within a function.
///                That function will be flow charted.
///      flags   - combination of CHART_GEN_GDL, CHART_WINGRAPH, CHART_NOLIBFUNCS

success gen_simple_call_chart(string outfile, string title, long flags);


// ----------------------------------------------------------------------------
//               C O M M O N   I N F O R M A T I O N
// ----------------------------------------------------------------------------

/// Get IDA directory
/// This function returns the directory where IDA.EXE resides

string idadir();


/// Get input file name
/// This function returns name of the file being disassembled

string get_root_filename();             // only the file name
string get_input_file_path();           // full path


/// Set input file name
/// This function updates the file name that is stored in the database
/// It is used by the debugger and other parts of IDA
/// Use it when the database is moved to another location or when you
/// use remote debugging.

void set_root_filename(string path);


/// Get IDB full path
/// This function returns full path of the current IDB database

string get_idb_path();


/// Get MD5 hash of the input file.
/// This function returns the MD5 hash string of the input file (32 chars)

string retrieve_input_file_md5();


/// Get base address of the input file

long get_imagebase();


/// Get full internal flags
///      ea - linear address
/// This function returns all bits, including MS_VAL and FF_IVL.
/// These bits may be expensive to retrieve when the debugger is active.
/// returns: 32-bit value of internal flags. See start of this file
/// for explanations.

long get_full_flags(long ea);


/// Get internal flags without MS_VAL and FF_IVL.
///      ea - linear address
/// MS_VAL and FF_IVL may be expensive to retrieve when the debugger is active.
/// returns: 32-bit value of internal flags. See start of this file
/// for explanations.

long get_flags(long ea);


/// Get one byte (8-bit) of the program at 'ea' from the database
/// even if the debugger is active.
///      ea - linear address
/// returns: byte value. If the byte has no value then 0xFF is returned.
/// If the current byte size is different from 8 bits, then the returned value
/// may have more 1's.
/// To check if a byte has a value, use \ref is_loaded(ea)

long get_db_byte(long ea);              // get a byte at ea


/// Return the specified number of bytes of the program
///       ea - linear address
///       size - size of buffer in normal 8-bit bytes
///       use_dbg - use debugger memory or just the database
/// returns: 0-failure
///          or a string containing the read bytes

string get_bytes(long ea, long size, long use_dbg);


/// Get one wide byte of the program at 'ea'.
///      ea - linear address
/// returns: value of byte. If byte has no value then returns 0xFF
/// Some processors may access more than 8bit quantity at an address.
/// These processors have 32-bit byte organization from the IDA's point of view.
/// To check if a byte has a value, use \ref is_loaded(ea).

long get_wide_byte(long ea);
#endif
#define byte(ea) get_wide_byte(ea)
#ifdef _notdefinedsymbol


/// Get value of program byte using the debugger memory
///      ea - linear address
/// returns: value of byte. Throws an exception on failure.
/// Thread-safe function (may be called only from the main thread and debthread)

long read_dbg_byte(long ea);


/// Get original value of program byte
///      ea - linear address
/// returns: the original value of byte before any patch applied to it

long get_original_byte(long ea);


/// Get one wide word (2 'byte') of the program at 'ea'.
///      ea - linear address
/// returns: the value of the word. If word has no value then returns 0xFFFF
/// Some processors may access more than 8bit quantity at an address.
/// These processors have 32-bit byte organization from the IDA's point of view.
/// This function takes into account order of bytes specified in inf.is_be()

long get_wide_word(long ea);
#endif
#define word(ea) get_wide_word(ea)
#ifdef _notdefinedsymbol


/// Get value of program word (2 bytes) using the debugger memory
///      ea - linear address
/// returns: the value of the word. Throws an exception on failure.
/// Thread-safe function (may be called only from the main thread and debthread)

long read_dbg_word(long ea);


/// Get value of program double word (4 bytes)
///      ea - linear address
/// returns: the value of the double word. Throws an exception on failure.

long get_wide_dword(long ea);
#endif
#define dword(ea) get_wide_dword(ea)
#ifdef _notdefinedsymbol


/// Get value of program double word (4 bytes) using the debugger memory
///      ea - linear address
/// returns: the value of the quadro word. Throws an exception on failure.
/// Thread-safe function (may be called only from the main thread and debthread)

long read_dbg_dword(long ea);


/// Get value of program quadro word (8 bytes)
///      ea - linear address
/// returns: the value of the quadro word. If failed, throws an exception
/// Note: this function is available only in the 64-bit version of IDA Pro

long get_qword(long ea);
#endif
#define qword(ea) get_qword(ea)
#ifdef _notdefinedsymbol


/// Get value of program quadro word (8 bytes) using the debugger memory
///      ea - linear address
/// returns: the value of the quadro word. If failed, throws an exception
/// Note: this function is available only in the 64-bit version of IDA Pro
/// Thread-safe function (may be called only from the main thread and debthread)

long read_dbg_qword(long ea);


/// Read from debugger memory
///      ea - linear address
///      size - size of data to read
/// returns: data as a string. If failed, If failed, throws an exception
/// Thread-safe function (may be called only from the main thread and debthread)

string read_dbg_memory(long ea, long size);


/// Write to debugger memory
///      ea - linear address
///      data - string to write
/// returns: number of written bytes (-1 - network/debugger error)
/// Thread-safe function (may be called only from the main thread and debthread)

long write_dbg_memory(long ea, string data);


/// Get value of a floating point number (4/8 bytes)
///      ea - linear address or string that contains float number byte rep
/// Returns: a floating point number at the specified address.
/// If the bytes at the specified address cannot be represented as a floating
/// point number, then return integer value -1.
/// If the first argument has not long or string type, throw an exception

float get_fpnum(long ea, long size);

// Convenience macros:
#endif
#define get_float(ea)     get_fpnum(ea, 4)
#define get_double(ea)    get_fpnum(ea, 8)
#ifdef _notdefinedsymbol


/// Get linear address of a name
///      from - the referring address.
///             Allows to retrieve local label addresses in functions.
///             If a local name is not found, then address of a global name is returned.
///      name - name of program byte
/// returns: address of the name
///          BADADDR - no such name
/// Dummy names (like byte_xxxx where xxxx are hex digits) are parsed by this
/// function to obtain the address. The database is not consulted for them.

long get_name_ea(long from, string name);
#endif
#define get_name_ea_simple(name)  get_name_ea(BADADDR, name)
#ifdef _notdefinedsymbol


/// Get segment by segment base
///      base - segment base paragraph or selector
/// returns: linear address of the start of the segment
///          BADADDR - no such segment

long get_segm_by_sel(long base);


/// Get linear address of cursor

long get_screen_ea();

#endif
#define here  get_screen_ea()
#ifdef _notdefinedsymbol


/// Get address of Global Offset Table
/// returns: address of the GOT table
///          BADADDR - no GOT address detected

long get_gotea();


/// Invokes an IDA UI action by name
///      name    - Name of the command
///      flags   - Reserved. Must be zero.
/// returns: 1-ok, 0-failed

long process_ui_action(string name, long flags);


/// Get the disassembly line at the cursor

string get_curline();


/// Get start address of the selected range
/// returns BADADDR - no selection

long read_selection_start();


/// Get end address of the selected area
/// returns BADADDR - no selection

long read_selection_end();


/// Clear selection

void clear_selection();


/// Get value of segment register at the specified address
///      ea - linear address
///      reg - name of segment register
/// returns: the value of the segment register. The segment registers in
/// 32bit program usually contain selectors, so to get paragraph pointed by
/// the segment register you need to call sel2para() function.

long get_sreg(long ea, string reg);


/// Get next address in the program
///      ea - linear address
/// returns: BADADDR - the specified address in the last used address

long next_addr(long ea);


/// Get previous address in the program
///      ea - linear address
/// returns: BADADDR - the specified address in the first address

long prev_addr(long ea);


/// Is the specified address 'ea' present in the program?

success is_mapped(long ea);


/// Get next defined item (instruction or data) in the program
///      ea    - linear address to start search from
///      maxea - the search will stop at the address
///              maxea is not included in the search range
/// returns: BADADDR - no (more) defined items

long next_head(long ea, long maxea);


/// Get previous defined item (instruction or data) in the program
///      ea    - linear address to start search from
///      minea - the search will stop at the address
///              minea is included in the search range
/// returns: BADADDR - no (more) defined items

long prev_head(long ea, long minea);


/// Get next not-tail address in the program
/// This function searches for the next displayable address in the program.
/// The tail bytes of instructions and data are not displayable.
///      ea - linear address
/// returns: BADADDR - no (more) not-tail addresses

long next_not_tail(long ea);


/// Get previous not-tail address in the program
/// This function searches for the previous displayable address in the program.
/// The tail bytes of instructions and data are not displayable.
///      ea - linear address
/// returns: BADADDR - no (more) not-tail addresses

long prev_not_tail(long ea);


/// Get starting address of the item
///      ea - linear address
/// returns: the starting address of the item
///          if the current address is unexplored, returns 'ea'

long get_item_head(long ea);


/// Get address of the end of the item (instruction or data)
///      ea - linear address
/// returns: address past end of the item at 'ea'

long get_item_end(long ea);


/// Get size of instruction or data item in bytes
///      ea - linear address
/// returns: 1..n

long get_item_size(long ea);


/// Does the given function contain the given address?
///      func_ea - any address belonging to the function
///      ea - linear address

success func_contains(long func_ea, long ea);


/// Get name at the specified address.
///      ea        - linear address
///      gtn_flags - how exactly the name should be retrieved.
///                  combination of GN_ bits
/// returns: name

string get_name(long ea, long gtn_flags=0);

// GN_ bits for \ref get_name() function.
// There is a convenience function calc_gtn_flags() to calculate the GN_LOCAL flag
#endif
#define GN_VISIBLE   0x0001     // replace forbidden characters by SUBSTCHAR
#define GN_COLORED   0x0002     // return colored name
#define GN_DEMANGLED 0x0004     // return demangled name
#define GN_STRICT    0x0008     // fail if cannot demangle
#define GN_SHORT     0x0010     // use short form of demangled name
#define GN_LONG      0x0020     // use long form of demangled name
#define GN_LOCAL     0x0040     // try to get local name first; if failed, get global
#define GN_ISRET     0x0080     // for dummy names: use retloc
#define GN_NOT_ISRET 0x0100     // for dummy names: do not use retloc

// Calculate flags for get_name() function
static calc_gtn_flags(from, ea)
{
  return func_contains(from, ea) ? GN_LOCAL : 0;
}
#ifdef _notdefinedsymbol


/// Get the name assigned to the ea by the debugger module
///      ea  - linear address
///      how - one of the DEBNAME_ constants

string get_debug_name(long ea, long how);

#endif
#define DEBNAME_EXACT 0 // find a name at exactly the specified address
#define DEBNAME_LOWER 1 // find a name with the address >= the specified address
#define DEBNAME_UPPER 2 // find a name with the address >  the specified address
#define DEBNAME_NICE  3 // find a name with the address <= the specified address
#ifdef _notdefinedsymbol


/// Get the address of a symbol created by the debugger module

long get_debug_name_ea(string name);


/// Demangle a name
///      name - name to demangle
///      disable_mask - a mask that tells how to demangle the name
///                     it is a good idea to get this mask using
///                     get_inf_attr(INF_SHORT_DN) or get_inf_attr(INF_LONG_DN)
/// Returns: a demangled name
/// If the input name cannot be demangled, returns 0

string demangle_name(string name, long disable_mask);


/// Get disassembly line
///      ea - linear address of instruction
///      flags - combination of the GENDSM_ flags, or 0
/// returns: "" - could not decode instruction at the specified location
/// note: this function may return not exactly the same mnemonics
/// as you see on the screen.

string generate_disasm_line(long ea, long flags);  // get disassembly line
#endif

// flags for generate_disasm_line
#define GENDSM_FORCE_CODE 1     // generate a disassembly line as if
                                // there is an instruction at 'ea'
#define GENDSM_MULTI_LINE 2     // if the instruction consists of several lines,
                                // produce all of them(useful for parallel instructions)
#ifdef _notdefinedsymbol


/// Get instruction mnemonics
///      ea - linear address of instruction
/// returns: 0 - no instruction at the specified location
/// note: this function may not return exactly the same mnemonics
/// as you see on the screen.

string print_insn_mnem(long ea);              // get instruction name


/// Get text representation of an operand
///      ea - linear address of instruction (or data)
///      n  - number of operand:
///              0 - the first operand
///              1 - the second operand
/// returns: the current text representation of operand

string print_operand(long ea, long n);


/// Get type of instruction operand
///      ea - linear address of instruction
///      n  - number of operand:
///              0 - the first operand
///              1 - the second operand
/// returns:
///      -1      bad operand number passed

long get_operand_type(long ea, long n);

#endif
#define o_void        0  // No Operand                           ----------
#define o_reg         1  // General Register (al, ax, es, ds...) reg
#define o_mem         2  // Direct Memory Reference  (DATA)      addr
#define o_phrase      3  // Memory Ref [Base Reg + Index Reg]    phrase
#define o_displ       4  // Memory Reg [Base Reg + Index Reg + Displacement] phrase+addr
#define o_imm         5  // Immediate Value                      value
#define o_far         6  // Immediate Far Address  (CODE)        addr
#define o_near        7  // Immediate Near Address (CODE)        addr
#define o_idpspec0    8  // IDP specific type
#define o_idpspec1    9  // IDP specific type
#define o_idpspec2   10  // IDP specific type
#define o_idpspec3   11  // IDP specific type
#define o_idpspec4   12  // IDP specific type
#define o_idpspec5   13  // IDP specific type

// x86
#define o_trreg         o_idpspec0      // trace register
#define o_dbreg         o_idpspec1      // debug register
#define o_crreg         o_idpspec2      // control register
#define o_fpreg         o_idpspec3      // floating point register
#define o_mmxreg        o_idpspec4      // mmx register
#define o_xmmreg        o_idpspec5      // xmm register

// arm
#define o_reglist       o_idpspec1      // Register list (for LDM/STM)
#define o_creglist      o_idpspec2      // Coprocessor register list (for CDP)
#define o_creg          o_idpspec3      // Coprocessor register (for LDC/STC)
#define o_fpreglist     o_idpspec4      // Floating point register list
#define o_text          o_idpspec5      // Arbitrary text stored in the operand
#define o_cond          (o_idpspec5+1)  // ARM condition as an operand

// ppc
#define o_spr           o_idpspec0      // Special purpose register
#define o_twofpr        o_idpspec1      // Two FPRs
#define o_shmbme        o_idpspec2      // SH & MB & ME
#define o_crf           o_idpspec3      // crfield      x.reg
#define o_crb           o_idpspec4      // crbit        x.reg
#define o_dcr           o_idpspec5      // Device control register
#ifdef _notdefinedsymbol


/// Get number used in the operand
/// This function returns an immediate number used in the operand
///      ea - linear address of instruction
///      n  - the operand number
/// The return values are:
///      operand is an immediate value  => immediate value
///      operand has a displacement     => displacement
///      operand is a direct memory ref => memory address
///      operand is a register          => register number
///      operand is a register phrase   => phrase number
///      otherwise                      => -1

long get_operand_value(long ea, long n);


/// Decode an instruction and returns an insn_t object (check ua.hpp)
///      ea - linear address of the instruction to decode
/// The return values are:
///      0 => if the function fails
///    or:
///      insn_t object:
///        cs, ip, ea, itype, size, auxpref, insnpref, segpref, flags
///        n: number of operands
///        is_canonical: Boolean. True if its a canonical instruction.
///        feature, mnem: canonical feature and mnemonic string (if is_canonical is True)
///        Op0..Op7: instances of op_t (check ua.hpp)
///                  n, type, offb, offo, flags, dtyp, reg, value, addr, specval,
///                  specflag1, specflag2, specflag3, specflag4

object decode_insn(long ea);


/// Get indented comment
///      ea - linear address
///      repeatable: 0-regular, !=0-repeatable comment

string get_cmt(long ea, long repeatable);


/// Get manually entered operand string
///      ea - linear address
///      n  - number of operand:
///              0 - the first operand
///              1 - the second operand

string get_forced_operand(long ea, long n);


/// Get string contents
///      ea   - linear address
///      len  - string length. -1 means to calculate the max string length
///      type - the string type (one of \ref get_str_type[STRTYPE_...] constants)
/// Returns: string contents or empty string

string get_strlit_contents(long ea, long len, long type);


/// Get string type
///      ea - linear address
/// Returns one of STRTYPE_... constants

long get_str_type(long ea);

#endif
// Character-terminated string. The termination characters are kept in
// the next bytes of string type.
#define STRTYPE_TERMCHR   (STRWIDTH_1B|STRLYT_TERMCHR<<STRLYT_SHIFT)
// C-style string.
#define STRTYPE_C         STRTYPE_TERMCHR
// Zero-terminated 16bit chars
#define STRTYPE_C_16      (STRWIDTH_2B|STRLYT_TERMCHR<<STRLYT_SHIFT)
// Zero-terminated 32bit chars
#define STRTYPE_C_32      (STRWIDTH_4B|STRLYT_TERMCHR<<STRLYT_SHIFT)
// Pascal-style, one-byte length prefix
#define STRTYPE_PASCAL    (STRWIDTH_1B|STRLYT_PASCAL1<<STRLYT_SHIFT)
// Pascal-style, 16bit chars, one-byte length prefix
#define STRTYPE_PASCAL_16 (STRWIDTH_2B|STRLYT_PASCAL1<<STRLYT_SHIFT)
// Pascal-style, two-byte length prefix
#define STRTYPE_LEN2      (STRWIDTH_1B|STRLYT_PASCAL2<<STRLYT_SHIFT)
// Pascal-style, 16bit chars, two-byte length prefix
#define STRTYPE_LEN2_16   (STRWIDTH_2B|STRLYT_PASCAL2<<STRLYT_SHIFT)
// Pascal-style, two-byte length prefix
#define STRTYPE_LEN4      (STRWIDTH_1B|STRLYT_PASCAL4<<STRLYT_SHIFT)
// Pascal-style, 16bit chars, two-byte length prefix
#define STRTYPE_LEN4_16   (STRWIDTH_2B|STRLYT_PASCAL4<<STRLYT_SHIFT)

#define         STRTERM1(strtype)       ((strtype>>8)&0xFF)
                                        // 3d byte:
#define         STRTERM2(strtype)       ((strtype>>16)&0xFF)
                                        // The termination characters are kept in
                                        // the 2nd and 3d bytes of string type
                                        // if the second termination character is
                                        // '\0', then it is ignored.
#ifdef _notdefinedsymbol


/// The following functions search for the specified byte
///      ea - address to start from
///      flag is combination of the following bits:
/// Returns BADADDR - not found
/// \id Find

#endif
#define SEARCH_UP       0x00            // search backward
#define SEARCH_DOWN     0x01            // search forward
#define SEARCH_NEXT     0x02            // start the search at the next/prev item
                                        // useful only for find_text() and find_binary()
                                        // for other Find.. functions it is implicitly set
#define SEARCH_CASE     0x04            // search case-sensitive
                                        // (only for bin&txt search)
#define SEARCH_REGEX    0x08            // enable regular expressions (only for txt)
#define SEARCH_NOBRK    0x10            // don't test ctrl-break
#define SEARCH_NOSHOW   0x20            // don't display the search progress
#ifdef _notdefinedsymbol

long find_suspop(long ea, long flag);
long find_code(long ea, long flag);
long find_data(long ea, long flag);
long find_unknown(long ea, long flag);
long find_defined(long ea, long flag);
long find_imm(long ea, long flag, long value);
long find_text(long ea, long flag, long y, long x, string str);
                // y - number of text line at ea to start from (0..MAX_ITEM_LINES)
                // x - x coordinate in this line
long find_binary(long ea, long flag, string str);
                // str - a string as a user enters it for Search Text in Core
                //      example:  "41 42" - find 2 bytes 41h, 42h
                // The default radix depends on the current IDP module
                // (radix for ibm pc is 16)


// ----------------------------------------------------------------------------
//     G L O B A L   S E T T I N G S
// ----------------------------------------------------------------------------

/// Parse one or more ida.cfg config directives
///      line - directives to process, for example: PACK_DATABASE=2
/// If the directives are erroneous, a fatal error will be generated.
/// The changes are permanent: effective for the current session and the next ones

void process_config_directive(string directive);


/// The following functions allow you to set/get common parameters.
/// Please note that not all parameters can be set directly.
/// \id inf_attr

long    get_inf_attr(long attr);
success set_inf_attr(long attr, long value);

// Set or clear bits in parameter
//      attr   - same as for get_inf_attr()/set_inf_attr() functions
//      bits   - bit mask
//      on     - boolean value, set or clear bits
// Convenience function
void set_flag(long attr, long bits, long on);

#endif
// 'attr' may be one of the following:

#define INF_VERSION      0              // ushort;  Version of database
#define INF_PROCNAME     1              // char[16];Name of current processor
#define INF_GENFLAGS     2              // ushort;  General flags:
#define         INFFL_AUTO       0x01   //              Autoanalysis is enabled?
#define         INFFL_ALLASM     0x02   //              May use constructs not supported by
                                        //              the target assembler
#define         INFFL_LOADIDC    0x04   //              Loading an idc file that contains database info
#define         INFFL_NOUSER     0x08   //              do not store user info in the database
#define         INFFL_READONLY   0x10   //              (internal) temporary interdiction to modify the database
#define         INFFL_CHKOPS     0x20   //              check manual operands? (unused)
#define         INFFL_NMOPS      0x40   //              allow non-matched operands? (unused)
#define         INFFL_GRAPH_VIEW 0x80   //              currently using graph options (\dto{graph})
#define INF_LFLAGS       3              // uint32   IDP-dependent flags
#define     LFLG_PC_FPP     0x00000001  //              decode floating point
                                        //              processor instructions?
#define     LFLG_PC_FLAT    0x00000002  //              Flat model?
#define     LFLG_64BIT      0x00000004  //              64-bit program?
#define     LFLG_IS_DLL     0x00000008  //              is dynamic library?
#define     LFLG_FLAT_OFF32 0x00000010  //              treat REF_OFF32 as 32-bit offset for 16bit segments (otherwise try SEG16:OFF16)
#define     LFLG_MSF        0x00000020  //              byte order: is MSB first?
#define     LFLG_WIDE_HBF   0x00000040  //              bit order of wide bytes: high byte first?
#define     LFLG_DBG_NOPATH 0x00000080  //              do not store input full path
#define     LFLG_SNAPSHOT   0x00000100  //              is memory snapshot?
#define     LFLG_PACK       0x00000200  //              pack the database?
#define     LFLG_COMPRESS   0x00000400  //              compress the database?
#define     LFLG_KERNMODE   0x00000800  //              is kernel mode binary?

#define INF_DATABASE_CHANGE_COUNT 4     // uint32; database change counter; keeps track of byte and segment modifications

#define INF_FILETYPE     5              // ushort;  type of input file (see ida.hpp)
#define         FT_EXE_OLD      0       //              MS DOS EXE File (obsolete)
#define         FT_COM_OLD      1       //              MS DOS COM File (obsolete)
#define         FT_BIN          2       //              Binary File
#define         FT_DRV          3       //              MS DOS Driver
#define         FT_WIN          4       //              New Executable (NE)
#define         FT_HEX          5       //              Intel Hex Object File
#define         FT_MEX          6       //              MOS Technology Hex Object File
#define         FT_LX           7       //              Linear Executable (LX)
#define         FT_LE           8       //              Linear Executable (LE)
#define         FT_NLM          9       //              Netware Loadable Module (NLM)
#define         FT_COFF         10      //              Common Object File Format (COFF)
#define         FT_PE           11      //              Portable Executable (PE)
#define         FT_OMF          12      //              Object Module Format
#define         FT_SREC         13      //              R-records
#define         FT_ZIP          14      //              ZIP file (this file is never loaded to IDA database)
#define         FT_OMFLIB       15      //              Library of OMF Modules
#define         FT_AR           16      //              ar library
#define         FT_LOADER       17      //              file is loaded using LOADER DLL
#define         FT_ELF          18      //              Executable and Linkable Format (ELF)
#define         FT_W32RUN       19      //              Watcom DOS32 Extender (W32RUN)
#define         FT_AOUT         20      //              Linux a.out (AOUT)
#define         FT_PRC          21      //              PalmPilot program file
#define         FT_EXE          22      //              MS DOS EXE File
#define         FT_COM          23      //              MS DOS COM File
#define         FT_AIXAR        24      //              AIX ar library
#define         FT_MACHO        25      //              Mac OS X Mach-O file
#define INF_OSTYPE       6              // ushort;  FLIRT: OS type the program is for
#define         OSTYPE_MSDOS 0x0001
#define         OSTYPE_WIN   0x0002
#define         OSTYPE_OS2   0x0004
#define         OSTYPE_NETW  0x0008
#define INF_APPTYPE      7              // ushort;  FLIRT: Application type
#define         APPT_CONSOLE 0x0001     //              console
#define         APPT_GRAPHIC 0x0002     //              graphics
#define         APPT_PROGRAM 0x0004     //              EXE
#define         APPT_LIBRARY 0x0008     //              DLL
#define         APPT_DRIVER  0x0010     //              DRIVER
#define         APPT_1THREAD 0x0020     //              Singlethread
#define         APPT_MTHREAD 0x0040     //              Multithread
#define         APPT_16BIT   0x0080     //              16 bit application
#define         APPT_32BIT   0x0100     //              32 bit application
#define INF_ASMTYPE      8              // uchar;   target assembler number (0..n)
#define INF_SPECSEGS     9              // uchar;   What format do special segments use? 0-unspecified, 4-entries are 4 bytes, 8- entries are 8 bytes
                                        //          program execution

#define INF_AF          10              // uint32;  Analysis flags:
#define AF_CODE         0x00000001      //              Trace execution flow
#define AF_MARKCODE     0x00000002      //              Mark typical code sequences as code
#define AF_JUMPTBL      0x00000004      //              Locate and create jump tables
#define AF_PURDAT       0x00000008      //              Control flow to data segment is ignored
#define AF_USED         0x00000010      //              Analyze and create all xrefs
#define AF_UNK          0x00000020      //              Delete instructions with no xrefs

#define AF_PROCPTR      0x00000040      //              Create function if data xref data->code32 exists
#define AF_PROC         0x00000080      //              Create functions if call is present
#define AF_FTAIL        0x00000100      //              Create function tails
#define AF_LVAR         0x00000200      //              Create stack variables
#define AF_STKARG       0x00000400      //              Propagate stack argument information
#define AF_REGARG       0x00000800      //              Propagate register argument information
#define AF_TRACE        0x00001000      //              Trace stack pointer
#define AF_VERSP        0x00002000      //              Perform full SP-analysis. (\ph{verify_sp})
#define AF_ANORET       0x00004000      //              Perform 'no-return' analysis
#define AF_MEMFUNC      0x00008000      //              Try to guess member function types
#define AF_TRFUNC       0x00010000      //              Truncate functions upon code deletion

#define AF_STRLIT       0x00020000      //              Create string literal if data xref exists
#define AF_CHKUNI       0x00040000      //              Check for unicode strings
#define AF_FIXUP        0x00080000      //              Create offsets and segments using fixup info
#define AF_DREFOFF      0x00100000      //              Create offset if data xref to seg32 exists
#define AF_IMMOFF       0x00200000      //              Convert 32bit instruction operand to offset
#define AF_DATOFF       0x00400000      //              Automatically convert data to offsets

#define AF_FLIRT        0x00800000      //              Use flirt signatures
#define AF_SIGCMT       0x01000000      //              Append a signature name comment for recognized anonymous library functions
#define AF_SIGMLT       0x02000000      //              Allow recognition of several copies of the same function
#define AF_HFLIRT       0x04000000      //              Automatically hide library functions

#define AF_JFUNC        0x08000000      //              Rename jump functions as j_...
#define AF_NULLSUB      0x10000000      //              Rename empty functions as nullsub_...

#define AF_DODATA       0x20000000      //              Coagulate data segs at the final pass
#define AF_DOCODE       0x40000000      //              Coagulate code segs at the final pass
#define AF_FINAL        0x80000000      //              Final pass of analysis

#define INF_AF2         11              // uint32;  Analysis flags 2

#define AF2_DOEH        0x00000001      //              Handle EH information
#define AF2_DORTTI      0x00000002      //              Handle RTTI information
#define AF2_MACRO       0x00000004      //              Try to combine several instructions into a macro instruction

#define INF_BASEADDR    12              // uval_t;  base paragraph of the program
#define INF_START_SS    13              // sel_t;   value of SS at the start
#define INF_START_CS    14              // sel_t;   value of CS at the start
#define INF_START_IP    15              // ea_t;    IP register value at the start of
#define INF_START_EA    16              // ea_t;    Linear address of program entry point
#define INF_START_SP    17              // ea_t;    SP register value at the start of
#define INF_MAIN        18              // ea_t;    address of main()
#define INF_MIN_EA      19              // ea_t;    The lowest address used
                                        //          in the program
#define INF_MAX_EA      20              // ea_t;    The highest address used
                                        //          in the program - 1
#define INF_OMIN_EA     21              // ea_t;
#define INF_OMAX_EA     22              // ea_t;
#define INF_LOWOFF      23              // ea_t;    low limit of voids
#define INF_HIGHOFF     24              // ea_t;    high limit of voids
#define INF_MAXREF      25              // uval_t;  max xref depth
#define INF_PRIVRANGE_START_EA 27       // ea_t;    Range of addresses reserved for internal use.
#define INF_PRIVRANGE_END_EA 28         // ea_t;    Initially specified by cfgvar PRIVRANGE

#define INF_NETDELTA    29              // sval_t; Delta value to be added to all adresses for mapping to netnodes.
                                        // Initially 0.
// CROSS REFERENCES
#define INF_XREFNUM     30              // uchar;   Number of references to generate
                                        //          0 - xrefs won't be generated at all
#define INF_TYPE_XREFNUM 31             // uchar;   Number of references to generate
                                        //          in the struct & enum windows
                                        //          0 - xrefs won't be generated at all
#define INF_REFCMTNUM   32              // uchar; number of comment lines to
                                        //        generate for refs to ASCII
                                        //        string or demangled name
                                        //        0 - such comments won't be
                                        //        generated at all
#define INF_XREFFLAG    33              // uchar;   xrefs representation:
#define         SW_SEGXRF       0x01    //              show segments in xrefs?
#define         SW_XRFMRK       0x02    //              show xref type marks?
#define         SW_XRFFNC       0x04    //              show function offsets?
#define         SW_XRFVAL       0x08    //              show xref values? (otherwise-"...")

// NAMES
#define INF_MAX_AUTONAME_LEN 34         // ushort;  max autogenerated name length (without zero byte)
#define INF_NAMETYPE    34              // char;    dummy names represenation type
#define         NM_REL_OFF      0
#define         NM_PTR_OFF      1
#define         NM_NAM_OFF      2
#define         NM_REL_EA       3
#define         NM_PTR_EA       4
#define         NM_NAM_EA       5
#define         NM_EA           6
#define         NM_EA4          7
#define         NM_EA8          8
#define         NM_SHORT        9
#define         NM_SERIAL      10
#define INF_SHORT_DEMNAMES 36           // uint32;  short form of demangled names
#define INF_LONG_DEMNAMES 37            // uint32;  long form of demangled names
                                        //          see demangle.h for definitions
#define INF_DEMNAMES    38              // uchar;   display demangled names as:
#define         DEMNAM_CMNT  0          //              comments
#define         DEMNAM_NAME  1          //              regular names
#define         DEMNAM_NONE  2          //              don't display
#define         DEMNAM_GCC3  4          //          assume gcc3 names (valid for gnu compiler)
#define         DEMNAM_FIRST 8          //          override type info
#define INF_LISTNAMES   39              // uchar;   What names should be included in the list?
#define         LN_NORMAL       0x01    //              normal names
#define         LN_PUBLIC       0x02    //              public names
#define         LN_AUTO         0x04    //              autogenerated names
#define         LN_WEAK         0x08    //              weak names

// DISASSEMBLY LISTING DETAILS
#define INF_INDENT      40              // uchar;   Indention for instructions
#define INF_CMT_INDENT  41              // uchar;   Indention for comments
#define INF_MARGIN      42              // ushort;  max length of data lines
#define INF_LENXREF     43              // ushort;  max length of line with xrefs
#define INF_OUTFLAGS    44              // uint32;  output flags
#define         OFLG_SHOW_VOID  0x0002  //              Display void marks?
#define         OFLG_SHOW_AUTO  0x0004  //              Display autoanalysis indicator?
#define         OFLG_GEN_NULL   0x0010  //              Generate empty lines?
#define         OFLG_SHOW_PREF  0x0020  //              Show line prefixes?
#define         OFLG_PREF_SEG   0x0040  //              line prefixes with segment name?
#define         OFLG_LZERO      0x0080  //              generate leading zeroes in numbers
#define         OFLG_GEN_ORG    0x0100  //              Generate 'org' directives?
#define         OFLG_GEN_ASSUME 0x0200  //              Generate 'assume' directives?
#define         OFLG_GEN_TRYBLKS 0x0400 //              Generate try/catch directives?
#define INF_CMTFLG      45              // uchar;   comments:
#define         SCF_RPTCMT       0x01   //              show repeatable comments?
#define         SCF_ALLCMT       0x02   //              comment all lines?
#define         SCF_NOCMT        0x04   //              no comments at all
#define         SCF_LINNUM       0x08   //              show source line numbers
#define         SCF_TESTMODE     0x10   //              testida.idc is running
#define         SCF_SHHID_ITEM   0x20   //              show hidden instructions
#define         SCF_SHHID_FUNC   0x40   //              show hidden functions
#define         SCF_SHHID_SEGM   0x80   //              show hidden segments
#define INF_LIMITER     46              // uchar;   Generate borders?
#define INF_BIN_PREFIX_SIZE 47          // short;   # of instruction bytes to show
                                        //          in line prefix
#define INF_PREFFLAG    48              // uchar;   line prefix type:
#define         PREF_SEGADR     0x01    //              show segment addresses?
#define         PREF_FNCOFF     0x02    //              show function offsets?
#define         PREF_STACK      0x04    //              show stack pointer?
#define         PREF_PFXTRUNC   0x08    //              truncate instruction bytes if they would need more than 1 line

// STRING LITERALS
#define INF_STRLIT_FLAGS 49             // uchar;   string literal flags
#define         STRF_GEN        0x01    //              generate names?
#define         STRF_AUTO       0x02    //              names have 'autogenerated' bit?
#define         STRF_SERIAL     0x04    //              generate serial names?
#define         STRF_COMMENT    0x10    //              generate auto comment for string references?
#define         STRF_SAVECASE   0x20    //              preserve case of strings for identifiers
#define INF_STRLIT_BREAK 50             // uchar;   string literal line break symbol
#define INF_STRLIT_ZEROES 51            // char;    leading zeroes
#define INF_STRTYPE     52              // int32;   current ascii string type
                                        //          is considered as several bytes:
                                        //      low byte:
// Number of bytes per "units" in a string.
#define STRWIDTH_1B 0
#define STRWIDTH_2B 1
#define STRWIDTH_4B 2
#define STRWIDTH_MASK 0x03
// The string layout; how the string is laid out in data.
#define STRLYT_TERMCHR 0
#define STRLYT_PASCAL1 1
#define STRLYT_PASCAL2 2
#define STRLYT_PASCAL4 3
#define STRLYT_MASK 0xFC
#define STRLYT_SHIFT 2

#define INF_STRLIT_PREF 53              // char[16];ASCII names prefix
#define INF_STRLIT_SERNUM 54            // uval_t;  serial number

// DATA ITEMS
#define INF_DATATYPES   55              // uval_t;  data types allowed in data carousel

// COMPILER
#define INF_CC_ID       57              // uchar;   compiler
#define      COMP_MASK        0x0F      //              mask to apply to get the pure compiler id
#define         COMP_UNK      0x00      // Unknown
#define         COMP_MS       0x01      // Visual C++
#define         COMP_BC       0x02      // Borland C++
#define         COMP_WATCOM   0x03      // Watcom C++
#define         COMP_GNU      0x06      // GNU C++
#define         COMP_VISAGE   0x07      // Visual Age C++
#define         COMP_BP       0x08      // Delphi
#define         COMP_UNSURE   0x80      // uncertain compiler id
#define INF_CC_CM       58              // cm_t;  memory model & calling convention. see below
#define INF_CC_SIZE_I   59              // uchar;  sizeof(int)
#define INF_CC_SIZE_B   60              // uchar;  sizeof(bool)
#define INF_CC_SIZE_E   61              // uchar;  sizeof(enum)
#define INF_CC_DEFALIGN 62              // uchar;  default alignment
#define INF_CC_SIZE_S   63              // uchar;
#define INF_CC_SIZE_L   64              // uchar;
#define INF_CC_SIZE_LL  65              // uchar;
#define INF_CC_SIZE_LDBL 66             // uchar;  sizeof(long double)
#define INF_ABIBITS     67              // uint32; ABI features
#define   ABI_8ALIGN4       0x00000001  //   4 byte alignment for 8byte scalars (__int64/double) inside structures?
#define   ABI_PACK_STKARGS  0x00000002  //   do not align stack arguments to stack slots
#define   ABI_BIGARG_ALIGN  0x00000004  //   use natural type alignment for argument if the alignment exceeds native word size (e.g. __int64 argument should be 8byte aligned on some 32bit platforms)
#define   ABI_STACK_LDBL    0x00000008  //   long double areuments are passed on stack
#define   ABI_STACK_VARARGS 0x00000010  //   varargs are always passed on stack (even when there are free registers)
#define   ABI_HARD_FLOAT    0x00000020  //   use the floating-point register set
#define   ABI_SET_BY_USER   0x00000040  //   compiler/abi were set by user flag and require SETCOMP_BY_USER flag to be changed
#define   ABI_GCC_LAYOUT    0x00000080  //   use gcc layout for udts (used for mingw)
#define   ABI_MAP_STKARGS   0x00000100  //   register arguments are mapped to stack area (and consume stack slots)
#define   ABI_HUGEARG_ALIGN 0x00000200  //   use natural type alignment for an argument
                                        //   even if its alignment exceeds double native word size
                                        //   (the default is to use double word max).
                                        //   e.g. if this bit is set, __int128 has 16-byte alignment
#define INF_APPCALL_OPTIONS 68          // uint32; appcall options

// Pointer size, memory model, and calling convention are encoded using:
#define  CM_MASK   0x03         // Default pointer size:
#define   CM_UNKNOWN     0x00   //   unknown
#define   CM_N8_F16      0x01   //   if sizeof(int)<=2: near 1 byte, far 2 bytes
#define   CM_N64         0x01   //   if sizeof(int)>2: near 8 bytes, far 8 bytes
#define   CM_N16_F32     0x02   //   near 2 bytes, far 4 bytes
#define   CM_N32_F48     0x03   //   near 4 bytes, far 6 bytes
#define  CM_M_MASK   0x0C       // Memory model:
#define   CM_M_NN        0x00   //   small:   code=near, data=near (or unknown if CM_UNKNOWN)
#define   CM_M_FF        0x04   //   large:   code=far, data=far
#define   CM_M_NF        0x08   //   compact: code=near, data=far
#define   CM_M_FN        0x0C   //   medium:  code=far, data=near

#define is_code_far(cm) (((cm) & 4) != 0) // Does the given model specify far code?
#define is_data_far(cm) (((cm) &= CM_M_MASK) && (cm) != CM_M_FN) // Does the given model specify far data?

/// \defgroup CM_CC_
//@{
#define  CM_CC_MASK   0xF0      // Calling convention
#define   CM_CC_INVALID    0x00 // this value is invalid
#define   CM_CC_UNKNOWN    0x10 // unknown calling convention
#define   CM_CC_VOIDARG    0x20 // function without arguments
                                // if has other cc and argnum == 0,
                                // represent as f() - unknown list
#define   CM_CC_CDECL      0x30 // stack
#define   CM_CC_ELLIPSIS   0x40 // cdecl + ellipsis
#define   CM_CC_STDCALL    0x50 // stack, purged
#define   CM_CC_PASCAL     0x60 // stack, purged, reverse order of args
#define   CM_CC_FASTCALL   0x70 // stack, purged (x86), first args are in regs (compiler-dependent)
#define   CM_CC_THISCALL   0x80 // stack, purged (x86), first arg is in reg (compiler-dependent)
#define   CM_CC_GOLANG     0xB0 // GO: arguments and return value in stack
#define   CM_CC_SPECIALE   0xD0 // ::CM_CC_SPECIAL with ellipsis
#define   CM_CC_SPECIALP   0xE0 // Equal to ::CM_CC_SPECIAL, but with purged stack.
#define   CM_CC_SPECIAL    0xF0 // usercall: locations of all arguments
                                // and the return value are explicitly specified

// Convenience function to set a flag bit
static set_flag(off, bit, value)
{
  auto v = get_inf_attr(off);
  v = value ? (bit | v) : (~bit & v);
  return set_inf_attr(off, v);
}
// Set application bitness
#define inf_set_64bit() set_flag(INF_LFLAGS, LFLG_64BIT, 1)
#define inf_set_32bit() set_flag(INF_LFLAGS, LFLG_PC_FLAT, 1)

#ifdef _notdefinedsymbol


//--------------------------------------------------------------------------

/// Set target processor type.
/// Once a processor module is loaded, it cannot be replaced until we close the idb.
///      processor - name of processor in short form.
///      level     - the request level:
///  SETPROC_IDB         set processor type for old idb
///  SETPROC_LOADER      set processor type for new idb;
///                      if the user has specified a compatible processor,
///                      return success without changing it.
///                      if failure, call loader_failure()
///  SETPROC_LOADER_NON_FATAL the same as SETPROC_LOADER but non-fatal failures.
///  SETPROC_USER        set user-specified processor
///                      used for -p and manual processor change at later time

success set_processor_type(string processor, long level);

#endif
#define SETPROC_IDB              0
#define SETPROC_LOADER           1
#define SETPROC_LOADER_NON_FATAL 2
#define SETPROC_USER             3
#ifdef _notdefinedsymbol


/// Get name of the current processor
/// returns: processor name

string get_processor_name(void);


/// Set target assembler
///      asmidx - index of the target assembler in the array of assemblers
///               for the current processor.
/// Returns: 1 - success, 0 - failure.

long set_target_assembler(long asmidx);


/// Enable/disable batch mode of operation
///      batch:  0 - ida will display dialog boxes and wait for the user input
///              1 - ida will not display dialog boxes, warnings, etc.
/// returns: old balue of batch flag

long batch(long batch);


// ----------------------------------------------------------------------------
//        I N T E R A C T I O N   W I T H   T H E   U S E R
// ----------------------------------------------------------------------------

/// \id Asks
// Ask the user to enter a string
//      defval - the default string value. This value
//               will appear in the dialog box.
//      hist   - history id. One of HIST_... constants
//      prompt - the prompt to display in the dialog box
// Returns: the entered string.

string ask_str(string defval, long hist, string prompt);

#endif
#define HIST_SEG    1           ///< segment names
#define HIST_CMT    2           ///< comments
#define HIST_SRCH   3           ///< search substrings
#define HIST_IDENT  4           ///< names
#define HIST_FILE   5           ///< file names
#define HIST_TYPE   6           ///< type declarations
#define HIST_CMD    7           ///< commands
#define HIST_DIR    8           ///< directory names (text version only)
#ifdef _notdefinedsymbol

// Ask the user to choose a file
//      for_saving- 0: "Open" dialog box, 1: "Save" dialog box
//      mask   - the input file mask as "*.*" or the default file name.
//      prompt - the prompt to display in the dialog box
// Returns: the selected file.

string ask_file(bool for_saving, string mask, string prompt);

// Ask the user to enter an address
//      defval - the default address value. This value
//               will appear in the dialog box.
//      prompt - the prompt to display in the dialog box
// Returns: the entered address or BADADDR.

long ask_addr(long defval, string prompt);

// Ask the user to enter a number
//      defval - the default value. This value
//               will appear in the dialog box.
//      prompt - the prompt to display in the dialog box
// Returns: the entered number or -1.

long ask_long(long defval, string prompt);

// Ask the user to enter a segment value
//      defval - the default value. This value
//               will appear in the dialog box.
//      prompt - the prompt to display in the dialog box
// Returns: the entered segment selector or BADSEL.

long ask_seg(long defval, string prompt);

// Ask the user a question and let him answer Yes/No/Cancel
//      defval - the default answer. This answer will be selected if the user
//               presses Enter.
//      prompt - the prompt to display in the dialog box
// Returns: -1:cancel, 0-no, 1-ok

long ask_yn(long defval, string prompt);


/// Display an UTF-8 encoded message in the message window
///      format - printf() style format string
///      ...    - additional parameters if any
/// This function can be used to debug IDC scripts
/// The result of the stringification of the arguments
/// will be treated as an UTF-8 string.
/// Thread-safe function.

void msg(string format, ...);

// Print variables in the message window
// This function print text representation of all its arguments to the output window.
// This function can be used to debug IDC scripts

void print(...);

// Display a message in a message box
//      format - printf() style format string
//      ...    - additional parameters if any
// This function can be used to debug IDC scripts
// The user will be able to hide messages if they appear twice in a row on the screen

void warning(string format, ...);

// Display a fatal message in a message box and quit IDA
//      format - printf() style format string
//      ...    - additional parameters if any

void error(string format, ...);


/// Change IDA indicator.
/// Returns the previous status.

long set_ida_state(long status);

#endif
#define IDA_STATUS_READY    0 // READY     IDA is idle
#define IDA_STATUS_THINKING 1 // THINKING  Analyzing but the user may press keys
#define IDA_STATUS_WAITING  2 // WAITING   Waiting for the user input
#define IDA_STATUS_WORK     3 // BUSY      IDA is busy
#ifdef _notdefinedsymbol


/// \header Refresh Screen
/// \id Refresh
// Refresh all disassembly views

void refresh_idaview_anyway(void);

// Refresh all choosers (names, functions, etc)

void refresh_choosers(void);


// ----------------------------------------------------------------------------
//                        S E G M E N T A T I O N
// ----------------------------------------------------------------------------

/// Get mapping of a selector.
///         arguments:      sel - the selector number
///         returns:        selector value if found
///                         otherwise the input value (sel)
///         note:           selector values are always in paragraphs

long sel2para(long sel);


/// Find a selector that has mapping to the specified paragraph.
///         arguments:      val - value to search for
///         returns:        the selector number if found
///                         otherwise the input value (val & 0xFFFF)
///         note:           selector values are always in paragraphs

long find_selector(long val);


/// set a selector value
///         arguments:      sel - the selector number
///                         val - value of selector
///         returns:        nothing
///         note:           ida supports up to 4096 selectors.
///                         if 'sel' == 'val' then the
///                         selector is destroyed because
///                         it has no significance

void set_selector(long sel, long value);


/// delete a selector
///         arguments:      sel - the selector number to delete
///         returns:        nothing
///         note:           if the selector is found, it will
///                         be deleted

void del_selector(long sel);


// ***********************************************
// ** SEGMENT FUNCTIONS

/// Get first segment
/// returns: linear address of the start of the first segment
/// BADADDR - no segments are defined

long get_first_seg();


/// Get next segment
///      ea - linear address
/// returns: start of the next segment
///          BADADDR - no next segment

long get_next_seg(long ea);


/// Get start address of a segment
///      ea - any address in the segment
/// returns: start of segment
///          BADADDR - the specified address doesn't belong to any segment
/// Note: it is a macro

#endif
#define get_segm_start(ea)  get_segm_attr(ea, SEGATTR_START)
#ifdef _notdefinedsymbol


/// Get end address of a segment
///      ea - any address in the segment
/// returns: end of segment (an address past end of the segment)
///          BADADDR - the specified address doesn't belong to any segment
/// Note: it is a macro

#endif
#define get_segm_end(ea)    get_segm_attr(ea, SEGATTR_END)
#ifdef _notdefinedsymbol


/// Get name of a segment
///      ea - any address in the segment
///   flags - 0-name as is;1-substitute invalid chars with _
/// returns: segment name, 0 - no segment at the specified address

string get_segm_name(long ea, long flags=0);


/// Create a new segment
///      startea  - linear address of the start of the segment
///      endea    - linear address of the end of the segment
///                 this address will not belong to the segment
///                 'endea' should be higher than 'startea'
///      base     - base paragraph or selector of the segment.
///                 a paragraph is 16byte memory chunk.
///                 If a selector value is specified, the selector should be
///                 already defined.
///      use32    - 0: 16bit segment, 1: 32bit segment, 2: 64bit segment
///      align    - segment alignment. see below for alignment values
///      comb     - segment combination. see below for combination values.
///      flags    - combination of ADDSEG_... bits
/// returns: 0-failed, 1-ok

success add_segm_ex(long startea, long endea, long sel, long use32, long align, long comb, long flags);

#endif
#define ADDSEG_NOSREG   0x0001  // set all default segment register values
                                // to BADSELs
                                // (undefine all default segment registers)
#define ADDSEG_OR_DIE   0x0002  // qexit() if can't add a segment
#define ADDSEG_NOTRUNC  0x0004  // don't truncate the new segment at the beginning
                                // of the next segment if they overlap.
                                // destroy/truncate old segments instead.
#define ADDSEG_QUIET    0x0008  // silent mode, no "Adding segment..." in the messages window
#define ADDSEG_FILLGAP  0x0010  // If there is a gap between the new segment
                                // and the previous one, and this gap is less
                                // than 64K, then fill the gap by extending the
                                // previous segment and adding .align directive
                                // to it. This way we avoid gaps between segments.
                                // Too many gaps lead to a virtual array failure.
                                // It cannot hold more than ~1000 gaps.
#define ADDSEG_SPARSE   0x0020  // Use sparse storage method for the new segment
#ifdef _notdefinedsymbol


/// Delete a segment
///   ea      - any address in the segment
///   flags   - combination of SEGMOD_... flags

success del_segm(long ea, long flags);

#endif
#define SEGMOD_KILL    0x0001 // disable addresses if segment gets shrinked or deleted
#define SEGMOD_KEEP    0x0002 // keep information (code & data, etc)
#define SEGMOD_SILENT  0x0004 // be silent
#define SEGMOD_KEEP0   0x0008 // flag for internal use, don't set
#define SEGMOD_KEEPSEL 0x0010 // do not try to delete unused selector
#define SEGMOD_NOMOVE  0x0020 // don't move info from the start of segment to the new start address
                              // (for set_segm_start())
#define SEGMOD_SPARSE  0x0040 // use sparse storage if extending the segment
                              // (for set_segm_start(), set_segm_end())
#ifdef _notdefinedsymbol


/// Change segment boundaries
///   ea      - any address in the segment
///   startea - new start address of the segment
///   endea   - new end address of the segment
///   flags   - combination of SEGMOD_... flags

success set_segment_bounds(long ea, long startea, long endea, long flags);


/// Change name of the segment
///   ea      - any address in the segment
///   name    - new name of the segment

success set_segm_name(long ea, string name);


/// Change class of the segment
///   ea      - any address in the segment
///   class   - new class of the segment

success set_segm_class(long ea, string klass);


/// Change alignment of the segment
///   ea      - any address in the segment
///   align   - new alignment of the segment, one of sa... constants
/// Note: it is a macro

#endif
#define set_segm_alignment(ea, alignment) set_segm_attr(ea, SEGATTR_ALIGN, alignment)
        #define saAbs         0  // Absolute segment.
        #define saRelByte     1  // Relocatable, byte aligned.
        #define saRelWord     2  // Relocatable, word (2-byte, 16-bit) aligned.
        #define saRelPara     3  // Relocatable, paragraph (16-byte) aligned.
        #define saRelPage     4  // Relocatable, aligned on 256-byte boundary (a "page"
                                 // in the original Intel specification).
        #define saRelDble     5  // Relocatable, aligned on a double word (4-byte)
                                 // boundary. This value is used by the PharLap OMF for
                                 // the same alignment.
        #define saRel4K       6  // This value is used by the PharLap OMF for page (4K)
                                 // alignment. It is not supported by LINK.
        #define saGroup       7  // Segment group
        #define saRel32Bytes  8  // 32 bytes
        #define saRel64Bytes  9  // 64 bytes
        #define saRelQword   10  // 8 bytes
#ifdef _notdefinedsymbol


/// Change combination of the segment
///   ea      - any address in the segment
///   comb    - new combination of the segment, one of sc... constants
/// Note: it is a macro

#endif
#define set_segm_combination(ea, comb) set_segm_attr(ea, SEGATTR_COMB, comb)
        #define scPriv     0    // Private. Do not combine with any other program
                                // segment.
        #define scPub      2    // Public. Combine by appending at an offset that meets
                                // the alignment requirement.
        #define scPub2     4    // As defined by Microsoft, same as C=2 (public).
        #define scStack    5    // Stack. Combine as for C=2. This combine type forces
                                // byte alignment.
        #define scCommon   6    // Common. Combine by overlay using maximum size.
        #define scPub3     7    // As defined by Microsoft, same as C=2 (public).
#ifdef _notdefinedsymbol


/// Change segment addressing
///   ea      - any address in the segment
///   bitness - 0: 16bit, 1: 32bit, 2: 64bit

success set_segm_addressing(long ea, long bitness);


/// Get segment selector by name
///      segname - name of segment
/// returns: segment selector or BADADDR

long selector_by_name(string segname);


/// Set default segment register value for a segment
///   ea      - any address in the segment
///             if no segment is present at the specified address
///             then all segments will be affected
///   reg     - name of segment register
///   value   - default value of the segment register. -1-undefined.

success set_default_sreg_value(long ea, string reg, long value);


/// set segment type
///         arguments:      segea - any address within segment
///                         type  - new segment type:
///         returns:        !=0 - ok
/// note: this function is a macro, see its definition at the end of idc.idc
/// Note: it is a macro

#endif
#define set_segm_type(ea, type)  set_segm_attr(ea, SEGATTR_TYPE, type)

#define SEG_NORM        0
#define SEG_XTRN        1       // * segment with 'extern' definitions
                                //   no instructions are allowed
#define SEG_CODE        2       // pure code segment
#define SEG_DATA        3       // pure data segment
#define SEG_IMP         4       // implementation segment
#define SEG_GRP         6       // * group of segments
                                //   no instructions are allowed
#define SEG_NULL        7       // zero-length segment
#define SEG_UNDF        8       // undefined segment type
#define SEG_BSS         9       // uninitialized segment
#define SEG_ABSSYM     10       // * segment with definitions of absolute symbols
                                //   no instructions are allowed
#define SEG_COMM       11       // * segment with communal definitions
                                //   no instructions are allowed
#define SEG_IMEM       12       // internal processor memory & sfr (8051)
#ifdef _notdefinedsymbol


/// get segment attribute
///       arguments:      segea - any address within segment
///                       attr  - one of SEGATTR_... (see \ref set_segm_attr()) constants

long get_segm_attr(long segea, long attr);


/// set segment attribute
///      arguments:      segea - any address within segment
///                      attr  - one of SEGATTR_... constants
/// Please note that not all segment attributes are modifiable.
/// Also some of them should be modified using special functions
/// like set_segm_addressing, etc.

success set_segm_attr(long segea, long attr, long value);

#endif
#ifndef __EA64__
#define SEGATTR_START    0      // starting address
#define SEGATTR_END      4      // ending address
#define SEGATTR_ORGBASE 16
#define SEGATTR_ALIGN   20      // alignment
#define SEGATTR_COMB    21      // combination
#define SEGATTR_PERM    22      // permissions
#define SEGATTR_BITNESS 23      // bitness (0: 16, 1: 32, 2: 64 bit segment)
                                // Note: modifying the attrbite directly does
                                // not lead to the reanalysis of the segment.
                                // Using set_segm_addressing() is more correct.
#define SEGATTR_FLAGS   24      // segment flags
#define SEGATTR_SEL     28      // segment selector
#define SEGATTR_ES      32      // default ES value
#define SEGATTR_CS      36      // default CS value
#define SEGATTR_SS      40      // default SS value
#define SEGATTR_DS      44      // default DS value
#define SEGATTR_FS      48      // default FS value
#define SEGATTR_GS      52      // default GS value
#define SEGATTR_TYPE    96      // segment type
#define SEGATTR_COLOR   100     // segment color
#else
#define SEGATTR_START    0
#define SEGATTR_END      8
#define SEGATTR_ORGBASE 32
#define SEGATTR_ALIGN   40
#define SEGATTR_COMB    41
#define SEGATTR_PERM    42
#define SEGATTR_BITNESS 43
#define SEGATTR_FLAGS   44
#define SEGATTR_SEL     48
#define SEGATTR_ES      56
#define SEGATTR_CS      64
#define SEGATTR_SS      72
#define SEGATTR_DS      80
#define SEGATTR_FS      88
#define SEGATTR_GS      96
#define SEGATTR_TYPE    184
#define SEGATTR_COLOR   188
#endif

// Segment permissions
#define SEGPERM_EXEC  1         // Execute
#define SEGPERM_WRITE 2         // Write
#define SEGPERM_READ  4         // Read
#define SEGPERM_MAXVAL (SEGPERM_EXEC + SEGPERM_WRITE + SEGPERM_READ)

// Valid segment flags
#define SFL_COMORG   0x01       // IDP dependent field (IBM PC: if set, ORG directive is not commented out)
#define SFL_OBOK     0x02       // orgbase is present? (IDP dependent field)
#define SFL_HIDDEN   0x04       // is the segment hidden?
#define SFL_DEBUG    0x08       // is the segment created for the debugger?
#define SFL_LOADER   0x10       // is the segment created by the loader?
#define SFL_HIDETYPE 0x20       // hide segment type (do not print it in the listing)
#ifdef _notdefinedsymbol


/// Move a segment to a new address
/// This function moves all information to the new address
/// It fixes up address sensitive information in the kernel
/// The total effect is equal to reloading the segment to the target address
///      ea    - any address within the segment to move
///      to    - new segment start address
///      flags - combination MFS_... constants
/// returns: MOVE_SEGM_... error code

long move_segm(long ea, long to, long flags);

#endif
#define MSF_SILENT    0x0001    // don't display a "please wait" box on the screen
#define MSF_NOFIX     0x0002    // don't call the loader to fix relocations
#define MSF_LDKEEP    0x0004    // keep the loader in the memory (optimization)
#define MSF_FIXONCE   0x0008    // valid for \ref rebase_program(): call loader only once
#define MSF_NETDELTA  0x0010    // change inf.netdelta if possible
#define MSF_PRIORITY  0x0020    // loader segments will overwrite any existing debugger segments when moved.
#define MSF_NETNODES  0x0080    // move netnodes instead of changing inf.netdelta (this is slower)

#define MOVE_SEGM_OK      0     // all ok
#define MOVE_SEGM_PARAM  -1     // The specified segment does not exist
#define MOVE_SEGM_ROOM   -2     // Not enough free room at the target address
#define MOVE_SEGM_IDP    -3     // IDP module forbids moving the segment
#define MOVE_SEGM_CHUNK  -4     // Too many chunks are defined, can't move
#define MOVE_SEGM_LOADER -5     // The segment has been moved but the loader complained
#define MOVE_SEGM_ODD    -6     // Can't move segments by an odd number of bytes
#define MOVE_SEGM_ORPHAN -7     // Orphan bytes hinder segment movement
#ifdef _notdefinedsymbol


/// Rebase the whole program by 'delta' bytes
///      delta - number of bytes to move the program
///      flags - combination of \ref move_segm[MFS_...] constants
///              it is recommended to use MSF_FIXONCE so that the loader takes
///              care of global variables it stored in the database
/// returns: error code \ref move_segm[MOVE_SEGM_...]

long rebase_program(long delta, long flags);


/// Set storage type
///      start_ea - starting address
///      end_ea   - ending address
///      stt     - new storage type, one of STT_VA and STT_MM
/// returns: 0 - ok, otherwise internal error code

long set_storage_type(long start_ea, long end_ea, long stt);

#endif
#define STT_VA 0  // regular storage: virtual arrays, an explicit flag for each byte
#define STT_MM 1  // memory map: sparse storage. useful for huge objects
#ifdef _notdefinedsymbol


// ----------------------------------------------------------------------------
//                    C R O S S   R E F E R E N C E S
// ----------------------------------------------------------------------------

/// \id Xrefs
//      See sample file xrefs.idc to learn to use these functions.

//      Flow types (combine with XREF_USER!):
#endif
#define fl_CF   16              // Call Far
#define fl_CN   17              // Call Near
#define fl_JF   18              // jumpto Far
#define fl_JN   19              // jumpto Near
#define fl_F    21              // Ordinary flow

#define XREF_USER 32            // All user-specified xref types
                                // must be combined with this bit
#ifdef _notdefinedsymbol

// Mark exec flow 'from' 'to'
success add_cref(long from, long to, long flowtype);

// Unmark exec flow 'from' 'to'
// undef - make 'to' undefined if no
//        more references to it
// returns 1 - planned to be made undefined
long del_cref(long from, long to, int undef);

// The following functions include the ordinary flows:
// (the ordinary flow references are returned first)

// Get first code xref from 'from'
long get_first_cref_from(long From);

// Get next code xref from
long get_next_cref_from(long from, long current);

// Get first code xref to 'to'
long get_first_cref_to(long to);

// Get next code xref to 'to'
long get_next_cref_to(long to, long current);

// The following functions don't take into account the ordinary flows:
long get_first_fcref_from(long from);
long get_next_fcref_from(long from, long current);
long get_first_fcref_to(long to);
long get_next_fcref_to(long to, long current);

// Data reference types (combine with XREF_USER!):
#endif
#define dr_O    1                       // Offset
#define dr_W    2                       // Write
#define dr_R    3                       // Read
#define dr_T    4                       // Text (names in manual operands)
#define dr_I    5                       // Informational
#ifdef _notdefinedsymbol

// Create Data Ref
success add_dref(long From, long to, long dreftype);

// Unmark Data Ref
void del_dref(long from, long to);

// Get first data xref from 'from'
long get_first_dref_from(long from);
long get_next_dref_from(long From, long current);

// Get first data xref to 'to'
long get_first_dref_to(long to);
long get_next_dref_to(long to, long current);

// returns type of the last xref
// obtained by get_first_.../get_next_...
// functions. Return values
// are fl_... or dr_...
long get_xref_type(void);


// ----------------------------------------------------------------------------
//                            F I L E   I / O
// ----------------------------------------------------------------------------

/// open a file
/// arguments: similiar to C fopen()
/// returns: 0 - error
///          otherwise a file handle
/// Thread-safe function.

long fopen(string file, string mode);


/// close a file
///      handle - file handle
/// returns: nothing
/// Thread-safe function.

void fclose(long handle);


/// get file length
///      handle - file handle
/// returns: -1 - error
///          otherwise file length in bytes
/// Thread-safe function.

long filelength(long handle);


/// set cursor position in the file
///      handle - file handle
///      offset - offset from origin
///      origin - 0 = from the start of file
///               1 = from the current cursor position
///               2 = from the end of file
/// returns: 0 - ok
///          otherwise error
/// Thread-safe function.

long fseek(long handle, long offset, long origin);


/// get cursor position in the file
///      handle - file handle
/// returns: -1 - error
///          otherwise current cursor position
/// Thread-safe function.

long ftell(long handle);


/// load file into IDA database
///      handle - file handle or loader_input_t object
///      pos    - position in the file
///      ea     - linear address to load
///      size   - number of bytes to load
/// returns: 0 - error
///          1 - ok

success loadfile(long handle, long pos, long ea, long size);


/// save from IDA database to file
///      handle  - file handle
///      pos     - position in the file
///      ea      - linear address to save from
///      size    - number of bytes to save
/// returns: 0 - error
///          1 - ok

success savefile(long handle, long pos, long ea, long size);


/// read one byte from file
///      handle  - file handle
/// returns: -1 - error
///          otherwise a byte read.
/// Thread-safe function.

long fgetc(long handle);


/// write one byte to file
///      handle  - file handle
///      byte    - byte to write
/// returns: 0 - ok
///          -1 - error
/// Thread-safe function.

long fputc(long byte, long handle);


/// fprintf
///      handle  - file handle
///      format  - format string
/// returns: 0 - ok
///          -1 - error
/// Thread-safe function.

long fprintf(long handle, string format, ...);


/// read 2 bytes from file
///      handle    - file hanlde
///      mostfirst - 0 least significant byte is first (intel)
///                  1 most  significant byte is first
/// returns: -1 - error
///          otherwise: a 16-bit value
/// Thread-safe function.

long readshort(long handle, long mostfirst);


/// read 4 bytes from file
///      handle  - file hanlde
///      mostfirst  - 0 least significant byte is first (intel)
///                   1 most  significant byte is first
/// returns: a 32-bit value
/// Thread-safe function.

long readlong(long handle, long mostfirst);


/// write 2 bytes to file
///      handle    - file hanlde
///      word      - a 16-bit value to write
///      mostfirst - 0 least significant byte is first (intel)
///                  1  most  significant byte is first
/// returns: 0 - ok
/// Thread-safe function.

long writeshort(long handle, long word, long mostfirst);


/// write 4 bytes to file
///      handle    - file hanlde
///      dword     - a 32-bit value to write
///      mostfirst - 0 least significant byte is first (intel)
///                  1 most  significant byte is first
/// returns: 0 - ok
/// Thread-safe function.

long writelong(long handle, long dword, long mostfirst);


/// read a string from file
///      handle  - file hanlde
/// returns: a string
/// Check for EOF like this: !value_is_string(retvalue)
/// Thread-safe function.

string readstr(long handle);


/// write a string to file
///      handle  - file hanlde
///      str     - string to write
/// returns: 0 - ok
/// Thread-safe function.

long writestr(long handle, string str);


/// rename a file
///      oldname - existing file name
///      newname - new file name
/// returns: error code from the system
/// Thread-safe function.

long rename(string oldname, string newname);


/// delete a file
///      filename - existing file/dir name
/// returns: error code from the system
/// Thread-safe function.

long unlink(string filename);


/// create a directory
///      dirname - directory name
///      mode    - file permissions (for unix)
/// returns: error code from the system
/// Thread-safe function.

long mkdir(string dirname, long mode);


// ----------------------------------------------------------------------------
//                           F U N C T I O N S
// ----------------------------------------------------------------------------

/// create a function
///      start, end - function bounds
///                   If the function end address is BADADDR, then
///                   IDA will try to determine the function bounds
///                   automatically. IDA will define all necessary
///                   instructions to determine the function bounds.
/// returns: !=0 - ok
/// note: an instruction should be present at the start address

success add_func(long start, long end=BADADDR);


/// delete a function
///      ea - any address belonging to the function
/// returns: !=0 - ok

success del_func(long ea);


/// change function start address
///      ea  - any address belonging to the function
///      end - new function start address
/// returns: !=0 - ok

success set_func_start(long ea, long start);


/// change function end address
///      ea  - any address belonging to the function
///      end - new function end address
/// returns: !=0 - ok

success set_func_end(long ea, long end);


/// find next function
///      ea - any address belonging to the function
/// returns: -1 - no more functions
///          otherwise returns the next function start address

long get_next_func(long ea);


/// find previous function
///      ea - any address belonging to the function
/// returns: -1 - no more functions
///          otherwise returns the previous function start address

long get_prev_func(long ea);


/// get a function attribute
///      ea   - any address belonging to the function
///      attr - one of FUNCATTR_... constants
/// returns: -1 - error
///          otherwise returns the attribute value

long get_func_attr(long ea, long attr);

#endif
#ifndef __EA64__
#define FUNCATTR_START    0     // readonly: function start address
#define FUNCATTR_END      4     // readonly: function end address
#define FUNCATTR_FLAGS    8     // function flags
#define FUNCATTR_FRAME   16     // readonly: function frame id
#define FUNCATTR_FRSIZE  20     // readonly: size of local variables
#define FUNCATTR_FRREGS  24     // readonly: size of saved registers area
#define FUNCATTR_ARGSIZE 28     // readonly: number of bytes purged from the stack
#define FUNCATTR_FPD     32     // frame pointer delta
#define FUNCATTR_COLOR   36     // function color code
#define FUNCATTR_OWNER   16     // readonly: chunk owner (valid only for tail chunks)
#define FUNCATTR_REFQTY  20     // readonly: number of chunk parents (valid only for tail chunks)
#else // EA64
#define FUNCATTR_START    0
#define FUNCATTR_END      8
#define FUNCATTR_FLAGS   16
#define FUNCATTR_FRAME   24
#define FUNCATTR_FRSIZE  32
#define FUNCATTR_FRREGS  40
#define FUNCATTR_ARGSIZE 48
#define FUNCATTR_FPD     56
#define FUNCATTR_COLOR   64
#define FUNCATTR_OWNER   24
#define FUNCATTR_REFQTY  32
#endif

#ifdef _notdefinedsymbol


/// set a function attribute
///      ea    - any address belonging to the function
///      attr  - one of \ref get_func_attr[FUNCATTR_...] constants.
///      value - new value of the attribute
/// returns: 1 - ok
///          0 - failed

success set_func_attr(long ea, long attr, long value);


/// retrieve function flags
///      ea - any address belonging to the function
/// returns: -1 - function doesn't exist
///          otherwise returns the flags FUNC_...

#endif
#define get_func_flags(ea)        get_func_attr(ea, FUNCATTR_FLAGS)

#define FUNC_NORET         0x00000001     // function doesn't return
#define FUNC_FAR           0x00000002     // far function
#define FUNC_LIB           0x00000004     // library function
#define FUNC_STATIC        0x00000008     // static function
#define FUNC_FRAME         0x00000010     // function uses frame pointer (BP)
#define FUNC_USERFAR       0x00000020     // user has specified far-ness
                                          // of the function
#define FUNC_HIDDEN        0x00000040     // a hidden function
#define FUNC_THUNK         0x00000080     // thunk (jump) function
#define FUNC_BOTTOMBP      0x00000100     // BP points to the bottom of the stack frame
#define FUNC_NORET_PENDING 0x00000200     // Function 'non-return' analysis
                                          // must be performed. This flag is
                                          // verified upon func_does_return()
#define FUNC_SP_READY      0x00000400     // SP-analysis has been performed
                                          // If this flag is on, the stack
                                          // change points should not be not
                                          // modified anymore. Currently this
                                          // analysis is performed only for PC
#define FUNC_FUZZY_SP      0x00000800     // Function changes SP in untraceable way,
                                          // for example: and esp, 0FFFFFFF0h
#define FUNC_PROLOG_OK     0x00001000     // Prolog analysis has be performed
                                          // by last SP-analysis
#define FUNC_PURGED_OK     0x00004000     // 'argsize' field has been validated.
                                          // If this bit is clear and 'argsize'
                                          // is 0, then we do not known the real
                                          // number of bytes removed from
                                          // the stack. This bit is handled
                                          // by the processor module.
#define FUNC_TAIL          0x00008000     // This is a function tail.
                                          // Other bits must be clear
                                          // (except FUNC_HIDDEN)
#define FUNC_LUMINA        0x00010000     // Function info is provided by Lumina
#ifdef _notdefinedsymbol


/// change function flags
///      ea    - any address belonging to the function
///      flags - see \ref get_func_flags() for explanations
/// returns: !=0 - ok

#endif
#define set_func_flags(ea, flags) set_func_attr(ea, FUNCATTR_FLAGS, flags)
#ifdef _notdefinedsymbol


/// retrieve function name
///      ea - any address belonging to the function
/// returns: 0 - function doesn't exist
///          otherwise returns function name

string get_func_name(long ea);


/// retrieve function comment
///      ea - any address belonging to the function
///      repeatable - 1: get repeatable comment
///                   0: get regular comment
/// returns: function comment string

string get_func_cmt(long ea, long repeatable);


/// set function comment
///      ea         - any address belonging to the function
///      cmt        - a function comment line
///      repeatable - 1: get repeatable comment
///                   0: get regular comment

void set_func_cmt(long ea, string cmt, long repeatable);


/// ask the user to select a function
///      title - title of the dialog box
/// returns: -1 - user refused to select a function
///          otherwise returns the selected function start address

long choose_func(string title);


/// convert address to 'funcname+offset' string
///      ea - address to convert
/// returns: if the address belongs to a function then
///            return a string formed as 'name+offset'
///            where 'name'   is a function name
///                  'offset' is offset within the function
///          else
///            return 0

string get_func_off_str(long ea);


/// Determine a new function boundaries
///      ea  - starting address of a new function
/// returns: if a function already exists,
///          then return its end address.
///          if a function end cannot be determined,
///          then return BADADDR
///          otherwise return the end address of the new function

long find_func_end(long ea);


/// Get ID of function frame structure
///      ea - any address belonging to the function
/// returns: ID of function frame.
///          In order to access stack variables you need to use
///          structure member manipulation functions with the
///          obtained ID.
///          -1 if function or function frame does not exist.

#endif
#define get_frame_id(ea)  get_func_attr(ea, FUNCATTR_FRAME)
#ifdef _notdefinedsymbol


/// Get size of local variables in function frame
///      ea - any address belonging to the function
/// returns: Size of local variables in bytes.
///          If the function doesn't have a frame, return 0
///          If the function does't exist, return -1

#endif
#define get_frame_lvar_size(ea)  get_func_attr(ea, FUNCATTR_FRSIZE)
#ifdef _notdefinedsymbol


/// Get size of saved registers in function frame
///      ea - any address belonging to the function
/// returns: Size of saved registers in bytes.
///          If the function doesn't have a frame, return 0
///          This value is used as offset for BP
///          (if FUNC_FRAME is set)
///          If the function does't exist, return -1

#endif
#define get_frame_regs_size(ea)  get_func_attr(ea, FUNCATTR_FRREGS)
#ifdef _notdefinedsymbol


/// Get size of arguments in function frame which are purged upon return
///      ea - any address belonging to the function
/// returns: Size of function arguments in bytes.
///          If the function doesn't have a frame, return 0
///          If the function does't exist, return -1

#endif
#define get_frame_args_size(ea)  get_func_attr(ea, FUNCATTR_ARGSIZE)
#ifdef _notdefinedsymbol


/// Get full size of function frame
///      ea - any address belonging to the function
/// returns: Size of function frame in bytes.
///          This function takes into account size of local
///          variables + size of saved registers + size of
///          return address + number of purged bytes.
///          The purged bytes correspond to the arguments of
///          __stdcall functions.
///          If the function doesn't have a frame, return size of
///          function return address in the stack.
///          If the function does't exist, return 0

long get_frame_size(long ea);


/// Make function frame
///      ea      - any address belonging to the function
///      lvsize  - size of function local variables
///      frregs  - size of saved registers
///      argsize - size of function arguments that will be purged
///                from the stack upon return
/// returns: ID of function frame or -1
///          If the function did not have a frame, the frame
///          will be created. Otherwise the frame will be modified

long set_frame_size(long ea, long lvsize, long frregs, long argsize);


/// Get current delta for the stack pointer
///      ea      - end address of the instruction
///                i.e. the last address of the instruction+1
/// returns: The difference between the original SP upon
///          entering the function and SP for the specified address

long get_spd(long ea);


/// Get modification of SP made by the instruction
///      ea      - end address of the instruction
///                i.e. the last address of the instruction+1
/// returns: Get modification of SP made at the specified location
///          If the specified location doesn't contain a SP
///          change point, return 0
///          Otherwise return delta of SP modification

long get_sp_delta(long ea);


/// Add automatical SP register change point
///      func_ea  - function start
///      ea       - linear address where SP changes
///                 usually this is the end of the instruction which
///                 modifies the stack pointer (cmd.ea+cmd.size)
///      delta    - difference between old and new values of SP
/// returns: 1-ok, 0-failed

success add_auto_stkpnt(func_ea, ea, sval_t delta);


/// Add user-defined SP register change point
///      ea    - linear address where SP changes
///      delta - difference between old and new values of SP
/// returns: 1-ok, 0-failed

success add_user_stkpnt(ea, sval_t delta);


/// Delete SP register change point
///      func_ea - function start
///      ea      - linear address
/// returns: 1-ok, 0-failed

success del_stkpnt(func_ea, ea_t ea);


/// Return the address with the minimal spd (stack pointer delta)
/// If there are no SP change points, then return BADADDR.
///      func_ea - function start
/// returns: BADDADDR - no such function

long get_min_spd_ea(func_ea);


/// Recalculate SP delta for an instruction that stops execution.
///      cur_ea  - linear address of the current instruction
/// returns: 1 - new stkpnt is added, 0 - nothing is changed

success recalc_spd(cur_ea);


// Below are the function chunk (or function tail) related functions

/// \header Function chunk related functions
/// \id Fchunks

// Get a function chunk attribute
//       ea     - any address in the chunk
//       attr   - one of: FUNCATTR_START, FUNCATTR_END
//                        FUNCATTR_OWNER, FUNCATTR_REFQTY
// returns: desired attribute or -1

long get_fchunk_attr(long ea, long attr);

// Set a function chunk attribute
//       ea     - any address in the chunk
//       attr   - nothing defined yet
//       value  - desired bg color (RGB)
// returns: 0 if failed, 1 if success

success set_fchunk_attr(long ea, long attr, long value);

// Get a function chunk referer
//       ea     - any address in the chunk
//       idx    - referer index (0..get_fchunk_attr(FUNCATTR_REFQTY))
// returns: referer address or BADADDR

long get_fchunk_referer(long ea, long idx);

// Get next function chunk
//       ea     - any address
// returns: the starting address of the next
//          function chunk or BADADDR
// This function enumerates all chunks of all functions in the database

long get_next_fchunk(long ea);

// Get previous function chunk
//       ea     - any address
// returns: the starting address of the previous
//          function chunk or BADADDR
// This function enumerates all chunks of all functions in the database

long get_prev_fchunk(long ea);

// Append a function chunk to the function
//       funcea   - any address in the function
//       ea1, ea2 - boundaries of a function tail to add.
//                  If a chunk exists at the specified addresses,
//                  it must have exactly the specified boundaries
// returns: 0 if failed, 1 if success

success append_func_tail(long funcea, long ea1, long ea2);

// Remove a function chunk from the function
//       funcea - any address in the function
//       ea1    - any address in the function chunk to remove
// returns: 0 if failed, 1 if success

success remove_fchunk(long funcea, long tailea);

// Change the function chunk owner
//       tailea - any address in the function chunk
//       funcea - the starting address of the new owner
// returns: 0 if failed, 1 if success
// The new owner must already have the chunk appended before the call

success set_tail_owner(long tailea, long funcea);

// Get the first function chunk of the specified function
//       funcea - any address in the function
// returns: the function entry point or BADADDR
// This function returns the first (main) chunk of the specified function

long first_func_chunk(long funcea);

// Get the next function chunk of the specified function
//         arguments:      funcea - any address in the function
//                         tailea - any address in the current chunk
//         returns:        the starting address of the next
//                         function chunk or BADADDR
// This function returns the next chunk of the specified function

long next_func_chunk(long funcea, long tailea);


// ----------------------------------------------------------------------------
//                        E N T R Y   P O I N T S
// ----------------------------------------------------------------------------

/// retrieve number of entry points
/// returns: number of entry points

long get_entry_qty(void);


/// add entry point
///      ordinal  - entry point number
///                 if entry point doesn't have an ordinal
///                 number, 'ordinal' should be equal to 'ea'
///      ea       - address of the entry point
///      name     - name of the entry point. If null string,
///                 the entry point won't be renamed.
///      makecode - if 1 then this entry point is a start
///                 of a function. Otherwise it denotes data bytes.
/// returns: 0 - entry point with the specifed ordinal already exists
///          1 - ok

success add_entry(long ordinal, long ea, string name, long makecode);


/// retrieve entry point ordinal number
///      index - 0..get_entry_qty()-1
/// returns: 0 if entry point doesn't exist
///          otherwise entry point ordinal

long get_entry_ordinal(long index);


/// retrieve entry point address
///      ordinal - entry point number
///                it is returned by get_entry_ordinal()
/// returns: -1 if entry point doesn't exist
///          otherwise entry point address.
///          If entry point address is equal to its ordinal
///          number, then the entry point has no ordinal.

long get_entry(long ordinal);


/// retrieve entry point name
///      ordinal - entry point number
///                it is returned by get_entry_ordinal()
/// returns: entry point name or ""

string get_entry_name(long ordinal);


/// rename entry point
///      ordinal - entry point number
///      name    - new name
/// returns: !=0 - ok

success rename_entry(long ordinal, string name);


// ----------------------------------------------------------------------------
//                              F I X U P S
// ----------------------------------------------------------------------------

/// find next address with fixup information
///      ea - current address
/// returns: -1 - no more fixups
///          otherwise returns the next address with fixup information

long get_next_fixup_ea(long ea);


/// find previous address with fixup information
///      ea - current address
/// returns: -1 - no more fixups
///          otherwise returns the previous address with fixup information

long get_prev_fixup_ea(long ea);


/// get fixup target type
///      ea - address to get information about
/// returns: -1 - no fixup at the specified address
///          otherwise returns fixup target type FIXUP_...

long get_fixup_target_type(long ea);

#endif
#define FIXUP_MASK      0xF
#define FIXUP_BYTE      FIXUP_OFF8 // 8-bit offset.
#define FIXUP_OFF8      0       // 8-bit offset.
#define FIXUP_OFF16     1       // 16-bit offset.
#define FIXUP_SEG16     2       // 16-bit base--logical segment base (selector).
#define FIXUP_PTR32     3       // 32-bit long pointer (16-bit base:16-bit
                                // offset).
#define FIXUP_OFF32     4       // 32-bit offset.
#define FIXUP_PTR48     5       // 48-bit pointer (16-bit base:32-bit offset).
#define FIXUP_HI8       6       // high  8 bits of 16bit offset
#define FIXUP_HI16      7       // high 16 bits of 32bit offset
#define FIXUP_LOW8      8       // low   8 bits of 16bit offset
#define FIXUP_LOW16     9       // low  16 bits of 32bit offset
#define FIXUP_REL       0x10    // fixup is relative to the linear address
                                // specified in the 3d parameter to set_fixup()
#define FIXUP_SELFREL   0x0     // self-relative?
                                //   - disallows the kernel to convert operands
                                //      in the first pass
                                //   - this fixup is used during output
                                // This type of fixups is not used anymore.
                                // Anyway you can use it for commenting purposes
                                // in the loader modules
#define FIXUP_EXTDEF    0x20    // target is a location (otherwise - segment)
#define FIXUP_UNUSED    0x40    // fixup is ignored by IDA
                                //   - disallows the kernel to convert operands
                                //   - this fixup is not used during output
#define FIXUP_CREATED   0x80    // fixup was not present in the input file
#ifdef _notdefinedsymbol


/// get fixup target flags
///      ea - address to get information about
/// returns: 0 - no fixup at the specified address
///          otherwise returns fixup flags:

long get_fixup_target_flags(long ea);

#endif
#define FIXUPF_REL      0x1  // fixup is relative to the linear address
#define FIXUPF_EXTDEF   0x2  // target is a location (otherwise - segment)
#define FIXUPF_UNUSED   0x4  // fixup is ignored by IDA
#define FIXUPF_CREATED  0x8  // fixup was not present in the input file
#ifdef _notdefinedsymbol


/// get fixup target selector
///      ea - address to get information about
/// returns: -1 - no fixup at the specified address
///          otherwise returns fixup target selector

long get_fixup_target_sel(long ea);


/// get fixup target offset
///      ea - address to get information about
/// returns: -1 - no fixup at the specified address
///          otherwise returns fixup target offset

long get_fixup_target_off(long ea);


/// get fixup target displacement
///      ea - address to get information about
/// returns: -1 - no fixup at the specified address
///          otherwise returns fixup target displacement

long get_fixup_target_dis(long ea);


/// set fixup information
///      ea        - address to set fixup information about
///      type      - fixup type. see get_fixup_target_type()
///                  for possible fixup types.
///      fixupf    - FIXUPF_... bits
///      targetsel - target selector
///      targetoff - target offset
///      displ     - displacement
/// returns: none

void set_fixup(long ea, long type, long fixupf, long targetsel, long targetoff, long displ);

#endif
/// The fixupf argument may have the following bits:
/// fixup is relative to the linear address `base'. Otherwise fixup is
/// relative to the start of the segment with `sel' selector.
#define FIXUPF_REL         0x0001

/// target is a location (otherwise - segment).
/// Use this bit if the target is a symbol rather than an offset from the
/// beginning of a segment.
#define FIXUPF_EXTDEF      0x0002

/// fixup is ignored by IDA
///   - disallows the kernel to convert operands
///   - this fixup is not used during output
#define FIXUPF_UNUSED      0x0004

/// fixup was not present in the input file
#define FIXUPF_CREATED     0x0008
#ifdef _notdefinedsymbol


/// delete fixup information
///      ea - address to delete fixup information about
/// returns: none

void del_fixup(long ea);


// ----------------------------------------------------------------------------
//                    M A R K E D   P O S I T I O N S
// ----------------------------------------------------------------------------

/// mark position
///      ea      - address to mark
///      lnnum   - number of generated line for the 'ea'
///      x       - x coordinate of cursor
///      y       - y coordinate of cursor
///      slot    - slot number: 0..1023
///                if the specifed value is not within the range,
///                IDA will ask the user to select slot.
///      comment - description of the mark.
///                Should be not empty.
/// returns: none

void put_bookmark(long ea, long lnnum, long x, long y, long slot, string comment);


/// get marked position
///      slot    - slot number: 0..1023
///                if the specifed value is <= 0,
///                IDA will ask the user to select slot.
/// returns: -1 - the slot doesn't contain a marked address
///          otherwise returns the marked address

long get_bookmark(long slot);


/// get marked position comment
///      slot    - slot number: 0..1023
/// returns: 0 if the slot doesn't contain a marked address
///          otherwise returns the marked address comment

string get_bookmark_desc(long slot);


// ----------------------------------------------------------------------------
//                          S T R U C T U R E S
// ----------------------------------------------------------------------------

/// Begin type updating. Use this function if you
/// plan to call AddEnumConst or similar type modification functions
/// many times or from inside a loop
///
///      utp - (one of UTP_... consts)
/// returns: none

success begin_type_updating(long utp);


/// End type updating. Refreshes the type system
/// at the end of type modification operations
///
///      utp  - (one of UTP_... consts)
/// returns: none

success end_type_updating(long utp);


/// get number of defined structure types
/// returns: number of structure types

long get_struc_qty(void);


/// get index of first structure type
/// returns: -1 if no structure type is defined
///          index of first structure type.
///          Each structure type has an index and ID.
///          INDEX determines position of structure definition
///           in the list of structure definitions. Index 1
///           is listed first, after index 2 and so on.
///           The index of a structure type can be changed any
///           time, leading to movement of the structure definition
///           in the list of structure definitions.
///          ID uniquely denotes a structure type. A structure
///           gets a unique ID at the creation time and this ID
///           can't be changed. Even when the structure type gets
///           deleted, its ID won't be resued in the future.

long get_first_struc_idx(void);


/// get index of last structure type
///      none
/// returns: -1 if no structure type is defined
///          index of last structure type.
///          See \ref get_first_struc_idx() for the explanation of
///          structure indices and IDs.

long get_last_struc_idx(void);


/// get index of next structure type
///      current structure index
/// returns: -1 if no (more) structure type is defined
///          index of the next structure type.
///          See \ref get_first_struc_idx() for the explanation of
///          structure indices and IDs.

long get_next_struc_idx(long index);


/// get index of previous structure type
///      current structure index
/// returns: -1 if no (more) structure type is defined
///          index of the presiouvs structure type.
///          See \ref get_first_struc_idx() for the explanation of
///          structure indices and IDs.

long get_prev_struc_idx(long index);


/// get structure index by structure ID
///      structure ID
/// returns: -1 if bad structure ID is passed
///          otherwise returns structure index.
///          See \ref get_first_struc_idx() for the explanation of
///          structure indices and IDs.

long get_struc_idx(long id);


/// get structure ID by structure index
///      structure index
/// returns: -1 if bad structure index is passed
///          otherwise returns structure ID.
///          See \ref get_first_struc_idx() for the explanation of
///          structure indices and IDs.

long get_struc_by_idx(long index);


/// get structure ID by structure name
///      structure type name
/// returns: -1 if bad structure type name is passed
///          otherwise returns structure ID.

long get_struc_id(string name);


/// get structure type name
///      structure type ID
/// returns: -1 if bad structure type ID is passed
///          otherwise returns structure type name.

string get_struc_name(long id);


/// get structure type comment
///      id         - structure type ID
///      repeatable - 1: get repeatable comment
///                   0: get regular comment
/// returns: 0 if bad structure type ID is passed
///          otherwise returns comment.

string get_struc_cmt(long id, long repeatable);


/// get size of a structure
///      id         - structure type ID
/// returns: 0 if bad structure type ID is passed
///          otherwise returns size of structure in bytes.

long get_struc_size(long id);


/// get number of members of a structure
///      id         - structure type ID
/// returns: -1 if bad structure type ID is passed
///          otherwise returns number of members.

long get_member_qty(long id);


/// get member id
///      id         - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
/// returns: -1 if bad structure type ID is passed or there is
///          no member at the specified offset.
///          otherwise returns the member id.

long get_member_id(long id, long member_offset);


/// get previous offset in a structure
///      id     - structure type ID
///      offset - current offset
/// returns: -1 if bad structure type ID is passed
///          or no (more) offsets in the structure
///          otherwise returns previous offset in a structure.
///          NOTE: IDA allows 'holes' between members of a
///                structure. It treats these 'holes'
///                as unnamed arrays of bytes.
///          This function returns a member offset or a hole offset.
///          It will return size of the structure if input
///          'offset' is bigger than the structure size.
///          NOTE: Union members are, in IDA's internals, located
///                at subsequent byte offsets: member 0 -> offset 0x0,
///                member 1 -> offset 0x1, etc...

long get_prev_offset(long id, long offset);


/// get next offset in a structure
///      id     - structure type ID
///      offset - current offset
/// returns: -1 if bad structure type ID is passed
///          or no (more) offsets in the structure
///          otherwise returns next offset in a structure.
///          NOTE: IDA allows 'holes' between members of a
///                structure. It treats these 'holes'
///                as unnamed arrays of bytes.
///          This function returns a member offset or a hole offset.
///          It will return size of the structure if input
///          'offset' belongs to the last member of the structure.
///          NOTE: Union members are, in IDA's internals, located
///                at subsequent byte offsets: member 0 -> offset 0x0,
///                member 1 -> offset 0x1, etc...

long get_next_offset(long id, long offset);


/// get offset of the first member of a structure
///      id            - structure type ID
/// returns: -1 if bad structure type ID is passed
///          or structure has no members
///          otherwise returns offset of the first member.
///          NOTE: IDA allows 'holes' between members of a
///                structure. It treats these 'holes'
///                as unnamed arrays of bytes.
///          NOTE: Union members are, in IDA's internals, located
///                at subsequent byte offsets: member 0 -> offset 0x0,
///                member 1 -> offset 0x1, etc...

long get_first_member(long id);


/// get offset of the last member of a structure
///      id            - structure type ID
/// returns: -1 if bad structure type ID is passed
///          or structure has no members
///          otherwise returns offset of the last member.
///          NOTE: IDA allows 'holes' between members of a
///                structure. It treats these 'holes'
///                as unnamed arrays of bytes.
///          NOTE: Union members are, in IDA's internals, located
///                at subsequent byte offsets: member 0 -> offset 0x0,
///                member 1 -> offset 0x1, etc...

long get_last_member(long id);


/// get offset of a member of a structure by the member name
///      id            - structure type ID
///      member_name   - name of structure member
/// returns: -1 if bad structure type ID is passed
///          or no such member in the structure
///          otherwise returns offset of the specified member.
///          NOTE: Union members are, in IDA's internals, located
///                at subsequent byte offsets: member 0 -> offset 0x0,
///                member 1 -> offset 0x1, etc...

long get_member_offset(long id, string member_name);


/// get name of a member of a structure
///      id            - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
/// returns: 0 if bad structure type ID is passed
///            or no such member in the structure
///          otherwise returns name of the specified member.

string get_member_name(long id, long member_offset);


/// get comment of a member
///      id            - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
///      repeatable   - 1: get repeatable comment
///                     0: get regular comment
/// returns: 0 if bad structure type ID is passed
///            or no such member in the structure
///          otherwise returns comment of the specified member.

string get_member_cmt(long id, long member_offset, long repeatable);


/// get size of a member
///      id            - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
/// returns: -1 if bad structure type ID is passed
///             or no such member in the structure
///          otherwise returns size of the specified member in bytes.

long get_member_size(long id, long member_offset);


/// get type of a member
///      id            - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
/// returns: -1 if bad structure type ID is passed
///             or no such member in the structure
///          otherwise returns type of the member, see bit
///          definitions above. If the member type is a structure
///          then function \ref get_member_strid() should be used to
///          get the structure type id.

long get_member_flag(long id, long member_offset);


/// get structure id of a member
///      id            - structure type ID
///      member_offset - member offset. The offset can be
///                      any offset in the member. For example,
///                      is a member is 4 bytes long and starts
///                      at offset 2, then 2, 3, 4, 5 denote
///                      the same structure member.
/// returns: -1 if bad structure type ID is passed
///             or no such member in the structure
///          otherwise returns structure id of the member.
///          If the current member is not a structure, returns -1.

long get_member_strid(long id, long member_offset);


/// is a structure a union?
///      id            - structure type ID
/// returns: 1: yes, this is a union id
///          0: no
///
/// Unions are a special kind of structures

long is_union(long id);


/// define a new structure type
///      index    - index of new structure type
///                 If another structure has the specified index,
///                 then index of that structure and all other
///                 structures will be increentedfreeing the specifed
///                 index. If index is == -1, then the biggest index
///                 number will be used.
///                 See \ref get_first_struc_idx() for the explanation of
///                 structure indices and IDs.
///
///      name     - name of the new structure type.
///
///      is_union - 0: structure
///                 1: union
///
/// returns: -1 if can't define structure type because of bad structure name:
///             the name is ill-formed or is already used in the program.
///          otherwise returns ID of the new structure type

long add_struc(long index, string name, long is_union);


/// delete a structure type
///      id - structure type ID
/// returns: 0 if bad structure type ID is passed
///          1 otherwise the structure type is deleted. All data
///            and other structure types referencing to the
///            deleted structure type will be displayed as array of bytes.

success del_struc(long id);


/// change structure index
///      id      - structure type ID
///      index   - new index of the structure
///                See \ref get_first_struc_idx() for the explanation of
///                structure indices and IDs.
/// returns: !=0 - ok

long set_struc_idx(long id, long index);


/// change structure name
///      id      - structure type ID
///      name    - new name of the structure
/// returns: !=0 - ok

long set_struc_name(long id, string name);


/// change structure comment
///      id      - structure type ID
///      comment - new comment of the structure
///      repeatable - 1: change repeatable comment
///                   0: change regular comment
/// returns: !=0 - ok

long set_struc_cmt(long id, string comment, long repeatable);


/// Add structure member.
///
/// This function can be used in two forms.
/// First form:
/// long add_struc_member(long id, string name, long offset, long flag,
///                     long typeid, long nbytes);
/// Second form:
/// long add_struc_member(long id, string name, long offset, long flag,
///                     long typeid, long nbytes,
///                     long target, long tdelta, long reftype);
///
/// arguments:
///   id      - structure type ID
///   name    - name of the new member
///   offset  - offset of the new member
///             -1 means to add at the end of the structure
///   flag    - type of the new member. Should be one of
///             FF_BYTE..FF_PACKREAL (see above)
///             combined with FF_DATA
///   typeid  - if is_struct(flag) then typeid specifies
///             the structure id for the member
///             if is_off0(flag) then typeid specifies
///             the offset base.
///             if is_strlit(flag) then typeid specifies
///             the string type (\ref get_str_type[STRTYPE_...]).
///             if is_stroff(flag) then typeid specifies
///             the structure id
///             if is_enum(flag) then typeid specifies
///             the enum id
///             Otherwise typeid should be -1
///   nbytes  - number of bytes in the new member
/// the remaining arguments are allowed only if isOff0(flag) and you want
/// to specify a complex offset expression
///   target  - target address of the offset expr. You may specify it as
///             -1, ida will calculate it itself
///   tdelta  - offset target delta. usually 0
///   reftype - see REF_... definitions
/// returns: 0 - ok, otherwise error code STRUC_ERROR_...

long add_struc_member(long id, string name, long offset, long flag, long typeid, long nbytes,
                      long target, long tdelta, long reftype);

#endif
// Constants used with begin_type_updating() and end_type_updating()
#define UTP_ENUM      0
#define UTP_STRUCT    1

#define STRUC_ERROR_MEMBER_NAME    (-1) // already has member with this name (bad name)
#define STRUC_ERROR_MEMBER_OFFSET  (-2) // already has member at this offset
#define STRUC_ERROR_MEMBER_SIZE    (-3) // bad number of bytes or bad sizeof(type)
#define STRUC_ERROR_MEMBER_TINFO   (-4) // bad typeid parameter
#define STRUC_ERROR_MEMBER_STRUCT  (-5) // bad struct id (the 1st argument)
#define STRUC_ERROR_MEMBER_UNIVAR  (-6) // unions can't have variable sized members
#define STRUC_ERROR_MEMBER_VARLAST (-7) // variable sized member should be the last member in the structure
#define STRUC_ERROR_MEMBER_NESTED  (-8) // recursive structure nesting is forbidden

#ifdef _notdefinedsymbol


/// delete structure member
///      id            - structure type ID
///      member_offset - offset of the member
/// returns: !=0 - ok.
/// NOTE: IDA allows 'holes' between members of a structure.
///       It treats these 'holes' as unnamed arrays of bytes.

long del_struc_member(long id, long member_offset);


/// change structure member name
///      id            - structure type ID
///      member_offset - offset of the member
///      name          - new name of the member
/// returns: !=0 - ok.

long set_member_name(long id, long member_offset, string name);


/// Change structure member type.
///
/// This function can be used in two forms.
/// First form:
/// long set_member_type(long id, long member_offset, long flag, long typeid, long nitems);
///
/// Second form:
/// long set_member_type(long id, long member_offset, long flag, long typeid, long nitems,
///                      long target, long tdelta, long reftype);
///
/// arguments:
///   id            - structure type ID
///   member_offset - offset of the member
///   flag    - new type of the member. Should be one of
///             FF_BYTE..FF_PACKREAL (see above)
///             combined with FF_DATA
///   typeid  - if is_struct(flag) then typeid specifies
///             the structure id for the member
///             if is_off0(flag) then typeid specifies
///             the offset base.
///             if is_strlit(flag) then typeid specifies
///             the string type (\ref get_str_type[STRTYPE_...]).
///             if is_stroff(flag) then typeid specifies
///             the structure id
///             if is_enum(flag) then typeid specifies
///             the enum id
///             Otherwise typeid should be -1
///   nitems  - number of items in the member
/// the remaining arguments are allowed only if \ref OpTypes[is_off0(flag)] and you want
/// to specify a complex offset expression:
///   target  - target address of the offset expr. You may specify it as
///             -1, ida will calculate it itself
///   tdelta  - offset target delta. usually 0
///   reftype - see REF_... definitions
/// returns:        !=0 - ok.

long set_member_type(long id, long member_offset, long flag, long typeid, long nitems,
                     long target, long tdelta, long reftype);


/// change structure member comment
///      id            - structure type ID
///      member_offset - offset of the member
///      comment       - new comment of the structure member
///      repeatable    - 1: change repeatable comment
///                      0: change regular comment
/// returns: !=0 - ok

long set_member_cmt(long id, long member_offset, string comment, long repeatable);


/// expand or shrink a structure type
///      id     - structure type ID
///      offset - offset in the structure
///      delta  - how many bytes to add or remove
///      recalc - recalculate the locations where
///               the structure type is used
/// returns: !=0 - ok

success expand_struc(long id, long offset, long delta, long recalc);


// ----------------------------------------------------------------------------
//                          E N U M S
// ----------------------------------------------------------------------------

/// get number of enum types
/// returns: number of enumerations

long get_enum_qty(void);


/// get ID of the specified enum by its serial number
///      idx - number of enum (0..get_enum_qty()-1)
/// returns: ID of enum or -1 if error

long getn_enum(long idx);


/// get serial number of enum by its ID
///      enum_id - ID of enum
/// returns: (0..get_enum_qty()-1) or -1 if error

long get_enum_idx(long enum_id);


/// get enum ID by the name of enum
///      name - name of enum
/// returns: ID of enum or -1 if no such enum exists

long get_enum(string name);


/// get name of enum
///      enum_id - ID of enum
/// returns: name of enum or empty string

string get_enum_name(long enum_id);


/// get comment of enum
///      enum_id - ID of enum
///      repeatable - 0:get regular comment
///                   1:get repeatable comment
/// returns: comment of enum

string get_enum_cmt(long enum_id, long repeatable);


/// get size of enum
///      enum_id - ID of enum
/// returns: number of constants in the enum
///          Returns 0 if enum_id is bad.

long get_enum_size(long enum_id);


/// get width of enum elements
///      enum_id - ID of enum
/// returns: size of enum elements in bytes
///          (0 if enum_id is bad or the width is unknown).

long get_enum_width(long enum_id);


/// get flag of enum
///      enum_id - ID of enum
/// returns: flags of enum. These flags determine representation
///          of numeric constants (binary, octal, decimal, hex)
///          in the enum definition. See start of this file for
///          more information about flags.
///          Returns 0 if enum_id is bad.

long get_enum_flag(long enum_id);


/// get member of enum - a symbolic constant ID
///      name - name of symbolic constant
/// returns: ID of constant or -1

long get_enum_member_by_name(string name);


/// get value of symbolic constant
///      const_id - id of symbolic constant
/// returns: value of constant or 0

long get_enum_member_value(long const_id);


/// get bit mask of symbolic constant
///      const_id - id of symbolic constant
/// returns: bitmask of constant or 0
///                         ordinary enums have bitmask = -1

long get_enum_member_bmask(long const_id);


/// get id of enum by id of constant
///      const_id - id of symbolic constant
/// returns: id of enum the constant belongs to.
///                         -1 if const_id is bad.

long get_enum_member_enum(long const_id);


/// get id of constant
///      enum_id - id of enum
///      value   - value of constant
///      serial  - serial number of the constant in the enumeration.
///                See \ref op_enum() for for details.
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
/// returns: id of constant or -1 if error

long get_enum_member(long enum_id, long value, long serial, long bmask);


/// get first bitmask in the enum (bitfield)
///      enum_id - id of enum (bitfield)
/// returns: the smallest bitmask of constant or -1
///          no bitmasks are defined yet
///          All bitmasks are sorted by their values as unsigned longs.

long get_first_bmask(long enum_id);


/// get last bitmask in the enum (bitfield)
///      enum_id - id of enum
/// returns: the biggest bitmask or -1 no bitmasks are defined yet
///          All bitmasks are sorted by their values as unsigned longs.

long get_last_bmask(long enum_id);


/// get next bitmask in the enum (bitfield)
///      enum_id - id of enum
///      bmask   - value of the current bitmask
/// returns: value of a bitmask with value higher than the specified
///          value. -1 if no such bitmasks exist.
///          All bitmasks are sorted by their values as unsigned longs.

long get_next_bmask(long enum_id, long value);


/// get prev bitmask in the enum (bitfield)
///      enum_id - id of enum
///      value   - value of the current bitmask
/// returns: value of a bitmask with value lower than the specified
///          value. -1 no such bitmasks exist.
///          All bitmasks are sorted by their values as unsigned longs.

long get_prev_bmask(long enum_id, long value);


/// get bitmask name (only for bitfields)
///      enum_id - id of enum
///      bmask   - bitmask of the constant
/// returns: name of bitmask if it exists. otherwise returns 0.

long get_bmask_name(long enum_id, long bmask);


/// get bitmask comment (only for bitfields)
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///      repeatable - type of comment, 0-regular, 1-repeatable
/// returns: comment attached to bitmask if it exists.
///          otherwise returns 0.

long get_bmask_cmt(long enum_id, long bmask, long repeatable);


/// set bitmask name (only for bitfields)
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///      name    - name of bitmask
/// returns: 1-ok, 0-failed

success set_bmask_name(long enum_id, long bmask, string name);


/// set bitmask comment (only for bitfields)
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///      cmt     - comment
///      repeatable - type of comment, 0-regular, 1-repeatable
/// returns: 1-ok, 0-failed

long set_bmask_cmt(long enum_id, long bmask, string cmt, long repeatable);


/// get first constant in the enum
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
/// returns: value of constant or -1 no constants are defined
///          All constants are sorted by their values as unsigned longs.

long get_first_enum_member(long enum_id, long bmask);


/// get last constant in the enum
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
/// returns: value of constant or -1 no constants are defined
///          All constants are sorted by their values as unsigned longs.

long get_last_enum_member(long enum_id, long bmask);


/// get next constant in the enum
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
///      value   - value of the current constant
/// returns: value of a constant with value higher than the specified
///          value. -1 no such constants exist.
///          All constants are sorted by their values as unsigned longs.

long get_next_enum_member(long enum_id, long value, long bmask);


/// get prev constant in the enum
///      enum_id - id of enum
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
///      value   - value of the current constant
/// returns: value of a constant with value lower than the specified
///          value. -1 no such constants exist.
///          All constants are sorted by their values as unsigned longs.

long get_prev_enum_member(long enum_id, long value, long bmask);


/// get name of a constant
/// arguments: const_id - id of const
/// returns: name of constant

string get_enum_member_name(long const_id);


/// get comment of a constant
///      const_id   - id of const
///      repeatable - 0:get regular comment
///                   1:get repeatable comment
/// returns: comment string

string get_enum_member_cmt(long const_id, long repeatable);


/// add a new enum type
///      idx - serial number of the new enum.
///            If another enum with the same serial number
///            exists, then all enums with serial
///            numbers >= the specified idx get their
///            serial numbers incremented (in other words,
///            the new enum is put in the middle of the list
///            of enums).
///            If idx >= get_enum_qty() or idx == -1
///            then the new enum is created at the end of
///            the list of enums.
///      name - name of the enum.
///      flag - flags for representation of numeric constants
///             in the definition of enum.
/// returns: id of new enum or -1.

long add_enum(long idx, string name, long flag);


/// delete enum type
///      enum_id - id of enum

void del_enum(long enum_id);


/// specify another serial number for a enum
///      enum_id - id of enum
///      idx     - new serial number.
///                If another enum with the same serial number
///                exists, then all enums with serial
///                numbers >= the specified idx get their
///                serial numbers incremented (in other words,
///                the new enum is put in the middle of the list
///                of enums).
///                If idx >= get_enum_qty() then the enum is
///                moved to the end of the list of enums.
/// returns: comment string

success set_enum_idx(long enum_id, long idx);


/// rename enum
///      enum_id - id of enum
///      name    - new name of enum
/// returns: 1-ok, 0-failed

success set_enum_name(long enum_id, string name);


/// set comment of enum
///      enum_id    - id of enum
///      cmt        - new comment for the enum
///      repeatable - 0:set regular comment
///                   1:set repeatable comment
/// returns: 1-ok, 0-failed

success set_enum_cmt(long enum_id, string cmt, long repeatable);


/// set flag of enum
///      enum_id - id of enum
///      flag    - flags for representation of numeric constants
///                in the definition of enum.
/// returns: 1-ok, 0-failed

success set_enum_flag(long enum_id, long flag);


/// set bitfield property of enum
///      enum_id - id of enum
///      flag    - 1: convert to bitfield
///                0: convert to ordinary enum
/// returns: 1-ok, 0-failed

success set_enum_bf(long enum_id, long flag);


/// set width of enum elements
///      enum_id - id of enum
///      width   - element width in bytes (0-unknown)
/// returns: 1-ok, 0-failed

success set_enum_width(long enum_id, long width);


/// is enum a bitfield?
///      enum_id - id of enum
/// returns: 1-yes, 0-no, ordinary enum

success is_bf(long enum_id);


/// add a member of enum - a symbolic constant
///      enum_id - id of enum
///      name    - name of symbolic constant. Must be unique
///                in the program.
///      value   - value of symbolic constant.
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
///                all bits set in value should be set in bmask too
/// returns: 0-ok, otherwise error code CONST_ERROR_...

long add_enum_member(long enum_id, string name, long value, long bmask);

#endif
#define CONST_ERROR_NAME  1     // already have member with this name (bad name)
#define CONST_ERROR_VALUE 2     // already have member with this value
#define CONST_ERROR_ENUM  3     // bad enum id
#define CONST_ERROR_MASK  4     // bad bmask
#define CONST_ERROR_ILLV  5     // bad bmask and value combination (~bmask & value != 0)
#ifdef _notdefinedsymbol


/// delete a member of enum - a symbolic constant
///      enum_id - id of enum
///      value   - value of symbolic constant.
///      serial  - serial number of the constant in the enumeration.
///                See \ref op_enum() for for details.
///      bmask   - bitmask of the constant
///                ordinary enums accept only -1 as a bitmask
/// returns: 1-ok, 0-failed

success del_enum_member(long enum_id, long value, long serial, long bmask);


/// rename a member of enum - a symbolic constant
///      const_id - id of const
///      name     - new name of constant
/// returns: 1-ok, 0-failed

success set_enum_member_name(long const_id, string name);


/// set a comment of a symbolic constant
///      const_id - id of const
///      cmt     - new comment for the constant
///      repeatable - 0:set regular comment
///                   1:set repeatable comment
/// returns: 1-ok, 0-failed

success set_enum_member_cmt(long const_id, string cmt, long repeatable);


/// Get address of the specified field using the type information
///      ea         - address of the strcture
///      field_name - name of the structure field
/// If the database contains a structurue at the specified ea and the
/// type information is present, this function will return the address of the
/// structure field.

long get_field_ea(long ea, string field_name);

/*
For example:

  .data:00413060 errtable        dd 1   ; oscode
  .data:00413060                 dd 16h ; errnocode


        msg("address is: %x\n", _errtable.errnocode);

prints 413064.
The "_errtable.errnocode" expression is essentially a shortcut for:

get_field_ea(get_name_ea_simple("_errtable"), "errnocode")
*/


// ----------------------------------------------------------------------------
//                          A R R A Y S  I N  I D C
// ----------------------------------------------------------------------------

// The following functions allow you to manipulate arrays in IDC.
// They have nothing to do with arrays in the disassembled program.
// The IDC arrays are persistent and are kept in the database.
// They remain until you explicitly delete them using delete_array().
//
// The arrays are virtual. IDA allocates space for and keeps only the specified
// elements of an array. The array index is 32-bit long. Actually, each array
// may keep a set of strings and a set of long(32bit or 64bit) values.

/// create array
///      name - name of array. There are no restrictions
///             on the name (its length should be less than
///             120 characters, though)
/// returns: -1 - can't create array (it already exists)
///          otherwise returns id of the array

long create_array(string name);


/// get array id by its name
///      name - name of existing array.
/// returns: -1 - no such array
///          otherwise returns id of the array

long get_array_id(string name);


/// rename array
///      id      - array id returned by create_array() or get_array_id()
///      newname - new name of array. There are no
///                restrictions on the name (its length should
///                be less than 120 characters, though)
/// returns: 1-ok, 0-failed

success rename_array(long id, string newname);


/// delete array
/// This function deletes all elements of the array.
///      id      - array id

void delete_array(long id);


/// set long value of array element.
///      id      - array id
///      idx     - index of an element
///      value   - 32bit or 64bit value to store in the array
/// returns: 1-ok, 0-failed

success set_array_long(long id, long idx, long value);


/// set string value of array element
///      id      - array id
///      idx     - index of an element
///      str     - string to store in array element
/// returns: 1-ok, 0-failed

success set_array_string(long id, long idx, string str);


/// get value of array element
///      tag     - tag of array, specifies one of two
///                array types AR_...
///      id      - array id
///      idx     - index of an element
/// returns: value of the specified array element.
///          note that this function may return char or long
///          result. Unexistent array elements give zero as
///          a result.

string or long get_array_element(long tag, long id, long idx);

#endif
#define AR_LONG 'A'     // array of longs
#define AR_STR  'S'     // array of strings
#ifdef _notdefinedsymbol


/// delete an array element
///      tag     - tag of array (AR_LONG or AR_STR)
///      id      - array id
///      idx     - index of an element
/// returns: 1-ok, 0-failed

success del_array_element(long tag, long id, long idx);


/// get index of the first existing array element
///      tag     - tag of array (AR_LONG or AR_STR)
///      id      - array id
/// returns: -1 - array is empty
///          otherwise returns index of the first array element

long get_first_index(long tag, long id);


/// get index of the last existing array element
///      tag     - tag of array (AR_LONG or AR_STR)
///      id      - array id
/// returns: -1 - array is empty
///          otherwise returns index of the last array element

long get_last_index(long tag, long id);


/// get index of the next existing array element
///      tag     - tag of array (AR_LONG or AR_STR)
///      id      - array id
///      idx     - index of the current element
/// returns: -1 - no more array elements
///          otherwise returns index of the next array element

long get_next_index(long tag, long id, long idx);


/// get index of the previous existing array element
///      tag     - tag of array (AR_LONG or AR_STR)
///      id      - array id
///      idx     - index of the current element
/// returns: -1 - no more array elements
///          otherwise returns index of the previous array element

long get_prev_index(long tag, long id, long idx);


/// associative arrays (the same as hashes in Perl)
/// to create a hash, use \ref create_array() function
/// you can use the following function with hashes:
///      \ref get_array_id(), \ref rename_array(), \ref delete_array()
/// The following additional functions are defined:
/// \id Hashes

success set_hash_long(long id, string idx, long value);
success set_hash_string(long id, string idx, string value);
long    get_hash_long(long id, string idx);
string  get_hash_string(long id, string idx);
success del_hash_string(long id, string idx);
string  get_first_hash_key(long id);
string  get_next_hash_key(long id, string idx);
string  get_last_hash_key(long id);
string  get_prev_hash_key(long id, string idx);


// ----------------------------------------------------------------------------
//                 S O U R C E   F I L E / L I N E   N U M B E R S
// ----------------------------------------------------------------------------
//
//   IDA can keep information about source files used to create the program.
//   Each source file is represented by a range of addresses.
//   A source file may contains several address ranges.

/// Mark a range of address as belonging to a source file
///    An address range may belong only to one source file.
///    A source file may be represented by several address ranges.
///         ea1     - linear address of start of the address range
///         ea2     - linear address of end of the address range
///         filename- name of source file.
///    returns: 1-ok, 0-failed.

success add_sourcefile(long ea1, ulong ea2, string filename);


/// Get name of source file occupying the given address
///      ea - linear address
/// returns: NULL - source file information is not found
///          otherwise returns pointer to file name

string get_sourcefile(long ea);


/// Delete information about the source file
///      ea - linear address belonging to the source file
/// returns: NULL - source file information is not found
///          otherwise returns pointer to file name

success del_sourcefile(long ea);


/// set source line number
///      ea      - linear address
///      lnnum   - number of line in the source file
/// returns: nothing

void set_source_linnum(long ea, long lnnum);


/// get source line number
///      ea      - linear address
/// returns: number of line in the source file or -1

long get_source_linnum(long ea);


/// delete information about source line number
/// arguments: ea      - linear address
///      nothing

void del_source_linnum(long ea);


// ----------------------------------------------------------------------------
//                 T Y P E  L I B R A R I E S
// ----------------------------------------------------------------------------

/// Load a type library
///      name - name of type library.
/// returns: 1-ok, 0-failed.

success add_default_til(string name);


/// Copy information from type library to database
///    Copy structure, union, or enum definition from the type library
///    to the IDA database.
///         idx       - the position of the new type in the list of
///                     types (structures or enums)
///                     -1 means at the end of the list
///         type_name - name of type to copy
///    returns: BADNODE-failed, otherwise the type id
///                 (structure id or enum id)

long import_type(long idx, string type_name);


/// Get type of function/variable
///      ea - the address of the object
/// returns: type string, 0 - failed

string get_type(long ea);


/// Get type information of function/variable as 'typeinfo' object
///      ea - the address of the object
///      type_name - name of a named type
/// returns: typeinfo object, 0 - failed
/// The typeinfo object has one mandatory attribute: typid

typeinfo get_tinfo(long ea);
typeinfo get_tinfo(string type_name);


/// Guess type of function/variable
///      ea - the address of the object.
///           can be the structure member id too
/// returns: type string, 0 - failed

string guess_type(long ea);


/// Apply the specified type to the address
///      ea    - the address of the object
///      type  - typeinfo object or a C declaration string with ';'
///              if specified as zero or an empty string, then the type
///              assciated with 'ea' will be deleted
///      flags - combination of TINFO_... constants or 0
/// returns: 1-ok, 0-failed.
/// Note: this function accepts member ids and change struct member types too

success apply_type(long ea, typeinfo type, long flags = TINFO_DEFINITE);

#endif
#define TINFO_GUESSED    0x0000 // this is a guessed type
#define TINFO_DEFINITE   0x0001 // this is a definite type
#define TINFO_DELAYFUNC  0x0002 // if type is a function and no function exists at ea,
                                // schedule its creation and argument renaming to auto-analysis
                                // otherwise try to create it immediately
#ifdef _notdefinedsymbol


/// Parse many type declarations
///      input -  file name or C declarations (depending on the flags)
///      flags -  combination of PT_... constants or 0
/// returns: number of errors

long parse_decls(string input, long flags);

/// Parse one type declaration
///      input -  a C declaration
///      flags -  combination of PT_... constants or 0
///               PT_FILE should not be specified in flags (it is ignored)
/// returns: typeinfo object or num 0

typeinfo parse_decl(string input, long flags);


/// Print types in a format suitable for use in a header file
///      ordinals - comma-separated list of type ordinals
///      flags    - combination of PDF_... constants or 0
/// returns: string containing the type definitions

string print_decls(string ordinals, long flags);

#endif
#define PT_FILE   0x0001  // input if a file name (otherwise contains type declarations)
#define PT_SILENT 0x0002  // silent mode
#define PT_PAKDEF 0x0000  // default pack value
#define PT_PAK1   0x0010  // #pragma pack(1)
#define PT_PAK2   0x0020  // #pragma pack(2)
#define PT_PAK4   0x0030  // #pragma pack(4)
#define PT_PAK8   0x0040  // #pragma pack(8)
#define PT_PAK16  0x0050  // #pragma pack(16)
#define PT_HIGH   0x0080  // assume high level prototypes
                          // (with hidden args, etc)
#define PT_LOWER  0x0100  // lower the function prototypes
#define PT_REPLACE 0x0200 // replace the old type
#define PT_RAWARGS 0x0400 // leave argument names unchanged
                          // (do not remove underscores)

#define PDF_INCL_DEPS  0x1 // include dependencies
#define PDF_DEF_FWD    0x2 // allow forward declarations
#define PDF_DEF_BASE   0x4 // include base types: __int8, __int16, etc..
#define PDF_HEADER_CMT 0x8 // prepend output with a descriptive comment
#ifdef _notdefinedsymbol


/// Calculate the size of a type
///      type - type to calculate the size of
///             can be specified as a typeinfo object (e.g. the result of get_tinfo())
///             or a string with C declaration (e.g. "int")
/// returns: size of the type or -1 if error

long sizeof(typeinfo type);


/// Get number of local types + 1
/// returns: value >= 1. 1 means that there are no local types.

long get_ordinal_qty(void);


/// Parse one type declaration and store it in the specified slot
///      ordinal -  slot number (1...NumberOfLocalTypes)
///                 -1 means allocate new slot or reuse the slot
///                 of the existing named type
///      input -  C declaration. Empty input empties the slot
///      flags -  combination of PT_... constants or 0
/// returns: slot number or 0 if error

success set_local_type(long ordinal, string input, long flags);


/// Retrieve a local type
///      ordinal -  slot number (1...NumberOfLocalTypes)
/// returns: typeinfo object or 0

typeinfo get_local_tinfo(long ordinal);


/// Retrieve a local type name
///      ordinal -  slot number (1...NumberOfLocalTypes)
/// returns: local type name or ""

string get_numbered_type_name(long ordinal);


/// Format value(s) as a C/C++ data initializers
///      outvec - reference to the output object
///               after the call will contain array of strings
///      value  - value to format
///      type   - type of the data to format
///      options- optional object, which may have the attributes PTV_...
///                      'ptvf' - combination of PTV_... constants:
///                      'flags'      number representation (e.g. hex_flag(), dec_flags(), etc)
///                      'max_length' max length of the formatted text (0 means no limit)
///                      'arrbase'    for arrays: the first element of array to print
///                      'arrnelems'  for arrays: number of elements to print
///                      'margin'     length of one line (0 means to print everything on one line)
///                      'indent'     how many spaces to use to indent nested structures/arrays
///      info   - object to store additional information about the generated lines
///               after the call will contain array of objects, each of which has:
///                      'ea' - address of the line
///                      'type' - typeinfo of the line (may include label for the line as 'name')
///               may be specified as 0 if this info is not required
/// Returns: error code

long format_cdata(object &outvec, anyvalue value, typeinfo type, object options, object &info);

#endif
#define PTV_DEREF  0x0001  // take value to print from the database.
                           // its address is specifed by value.num (default)
#define PTV_QUEST  0x0002  // print '?' for uninited data
#define PTV_EMPTY  0x0004  // return empty string for uninited data (default)
#define PTV_CSTR   0x0008  // print constant strings inline (default)
#define PTV_EXPAND 0x0010  // print only top level on separate lines
                           // max_length applies to separate lines
                           // margin is ignored
#define PTV_LZHEX  0x0020  // print hex numbers with leading zeroes
#define PTV_STPFLT 0x0040  // fail on bad floating point numbers
                           // (if not set, just print ?flt for them)
#define PTV_SPACE  0x0080  // add spaces after commas and around braces (default)
#define PTV_DEBUG  0x0100  // format output for debugger
#ifdef _notdefinedsymbol


/// \header Hidden ranges
/// \id HiddenRange
// ----------------------------------------------------------------------------
//                           H I D D E N  A R E A S
// ----------------------------------------------------------------------------

// Hidden ranges - address ranges which can be replaced by their descriptions

// hide a range
//       start, end  - range boundaries
//       description - description to display if the range is collapsed
//       header      - header lines to display if the range is expanded
//       footer      - footer lines to display if the range is expanded
//       visible     - the range state
//       color       - RGB color code (-1 means default color)
//  returns: !=0 - ok

success add_hidden_range(long start, long end, string description, string header, string footer, long color);

// set hidden range state
//       ea      - any address belonging to the hidden range
//       visible - new state of the range
//  returns: !=0 - ok

success update_hidden_range(long ea, long visible);

// delete a hidden range
//       ea - any address belonging to the hidden range
//  returns: !=0 - ok

success del_hidden_range(long ea);


// ----------------------------------------------------------------------------
//                           D E B U G G E R  I N T E R F A C E
// ----------------------------------------------------------------------------

/// Load the debugger
///      dbgname - debugger module name
///                Examples: win32, linux, mac.
///      use_remote - 0/1: use remote debugger or not
/// This function is needed only when running idc scripts from the command line.
/// In other cases IDA loads the debugger module automatically.

success load_debugger(string dbgname, long use_remote);


/// Launch the debugger
///      path - path to the executable file.
///      args - command line arguments
///      sdir - initial directory for the process
/// for all args: if empty, the default value from the database will be used
/// returns: -1-failed, 0-cancelled by the user, 1-ok
/// See the important note to the step_into() function

long start_process(string path, string args, string sdir);


/// Stop the debugger
/// Kills the currently debugger process and returns to the disassembly mode
///    arguments: none
/// returns: success

success exit_process(void);


/// Suspend the running process
/// Tries to suspend the process. If successful, the PROCESS_SUSPENDED
/// debug event will arrive (see wait_for_next_event)
///    arguments: none
/// returns: success
/// To resume a suspended process use the \ref DebEvents[wait_for_next_event] function.
/// See the important note to the step_into() function

success suspend_process(void);


/// Take a snapshot of running processes and return their description.
/// returns: the object with the attributes:
/// "size" - number of processes
/// "0", "1", "2", ... up to the number of processes - 1
///        - contains object which describes the process with the attributes:
///          "pid"  - PID
///          "name" - process name, usually executable name prefixed
///                   with the process bitness

object get_processes(void);

/*
For example, to get the name of the 5th process:

  extern fifth_name;
  fifth_name = get_processes()[4].name
*/


/// Attach the debugger to a running process
///      pid - PID of the process to attach to. If NO_PROCESS, a dialog box
///            will interactively ask the user for the process to attach to.
///      event_id - reserved, must be -1
/// returns:
///         -2 - impossible to find a compatible process
///         -1 - impossible to attach to the given process (process died, privilege
///              needed, not supported by the debugger plugin, ...)
///          0 - the user cancelled the attaching to the process
///          1 - the debugger properly attached to the process
/// See the important note to the step_into() function

long attach_process(long pid, long event_id);


/// Detach the debugger from the debugged process.

success detach_process(void);


/// Get number of threads.

long get_thread_qty(void);


/// Get the ID of a thread
///      idx - number of thread, is in range 0..get_thread_qty()-1
/// returns: -1 if failure

long getn_thread(long idx);


/// Get current thread ID
/// returns: -1 if failure

long get_current_thread(void);


/// Get the NAME of a thread
///      idx - number of thread, is in range 0..get_thread_qty()-1
///            or -1 for the current thread
/// returns: required info

string getn_thread_name(long idx);


/// Select the given thread as the current debugged thread.
///      tid - ID of the thread to select
/// The process must be suspended to select a new thread.
/// returns: success

success select_thread(long tid);


/// Suspend thread
/// Suspending a thread may deadlock the whole application if the suspended
/// was owning some synchronization objects.
///      tid - thread id
/// Return: -1:network error, 0-failed, 1-ok

long suspend_thread(long tid);


/// Resume thread
///      tid - thread id
/// Return: -1:network error, 0-failed, 1-ok

long resume_thread(long tid);


/// Unwind the stack for the given thread
///      tid - thread id
/// returns: a call stack object with the attributes:
/// "size" - number of frames
/// array subscript "[0]", "[1]", ... up to the number of frames - 1
/// each frame object has the attributes:
///   "callea" - the address of the call instruction.
///              for the 0th frame this is usually just the current value of EIP.
///   "funcea" - the address of the called function
///   "fp"     - the value of the frame pointer of the called function
///   "funcok" - is there a function created in the database for the current frame?

object collect_stack_trace(long tid);


/// Get a description of the module that contains the given ea
/// returned objct has attributes:
///   "name"      - the full path of the module
///   "base"      - module's base address
///   "size"      - module size
///   "rebase_to" - address the module was rebased to
///                 BADADDR if module was not rebased at all

object get_module_info(long ea);


/// \header Debugger: modules
/// \id DebModules
// Enumerate process modules
// These function return the module base address

long get_first_module(void);
long get_next_module(long base);

// Get process module name
//      base - the base address of the module
// returns: required info

string get_module_name(long base);

// Get process module size
//      base - the base address of the module
// returns: required info or -1

long get_module_size(long base);


/// \header Debugger: control
/// \id DebControl
// Execute one instruction in the current thread.
// Other threads are kept suspended.
//
// NOTE
//   You must call wait_for_next_event() after this call
//   in order to find out what happened. Normally you will
//   get the STEP event but other events are possible (for example,
//   an exception might occur or the process might exit).
//   This remark applies to all execution control functions.
//   The event codes depend on the issued command.
// returns: success

success step_into(void);

// Execute one instruction in the current thread,
// but without entering into functions
// Others threads keep suspended.
// See the important note to the step_into() function

success step_over(void);

// Execute the process until the given address is reached.
// If no process is active, a new process is started.
// See the important note to the step_into() function

success run_to(long ea, long pid=NO_PROCESS, long tid=NO_THREAD);

// Execute instructions in the current thread until
// a function return instruction is executed (aka "step out").
// Other threads are kept suspended.
// See the important note to the step_into() function

success step_until_ret(void);


/// \header Debugger: events
/// \id DebEvents
/// Wait for the next event
/// This function (optionally) resumes the process
/// execution and wait for a debugger event until timeout
///      wfne - combination of WFNE_... constants
///      timeout - number of seconds to wait, -1-infinity
/// returns: debugger event codes, see below

long wait_for_next_event(long wfne, long timeout);

#endif
// convenience function
#define resume_process() wait_for_next_event(WFNE_CONT|WFNE_NOWAIT, 0)
// wfne flag is combination of the following:
#define WFNE_ANY    0x0001 // return the first event (even if it doesn't suspend the process)
                           // if the process is still running, the database
                           // does not reflect the memory state. you might want
                           // to call refresh_debugger_memory() in this case
#define WFNE_SUSP   0x0002 // wait until the process gets suspended
#define WFNE_SILENT 0x0004 // 1: be slient, 0:display modal boxes if necessary
#define WFNE_CONT   0x0008 // continue from the suspended state
#define WFNE_NOWAIT 0x0010 // do not wait for any event, immediately return DEC_TIMEOUT
                           // (to be used with WFNE_CONT)
#define WFNE_USEC   0x0020 // timeout is specified in microseconds
                           // (minimum non-zero timeout is 40000us)

// debugger event codes
#define NOTASK         -2            // process does not exist
#define DBG_ERROR      -1            // error (e.g. network problems)
#define DBG_TIMEOUT     0            // timeout
#define PROCESS_STARTED   0x00000001 // New process started
#define PROCESS_EXITED    0x00000002 // Process stopped
#define THREAD_STARTED    0x00000004 // New thread started
#define THREAD_EXITED     0x00000008 // Thread stopped
#define BREAKPOINT        0x00000010 // Breakpoint reached
#define STEP              0x00000020 // One instruction executed
#define EXCEPTION         0x00000040 // Exception
#define LIB_LOADED        0x00000080 // New library loaded
#define LIB_UNLOADED      0x00000100 // Library unloaded
#define INFORMATION       0x00000200 // User-defined information
#define PROCESS_ATTACHED  0x00000400 // Attached to running process
#define PROCESS_DETACHED  0x00000800 // Detached from process
#define PROCESS_SUSPENDED 0x00001000 // Process has been suspended
#ifdef _notdefinedsymbol

// refresh_idaview_anyway debugger memory
// Upon this call IDA will forget all cached information
// about the debugged process. This includes the segmentation
// information and memory contents (register cache is managed
// automatically). Also, this function refreshes exported name
// from loaded DLLs.
// You must call this function before using the segmentation
// information, memory contents, or names of a non-suspended process.
// This is an expensive call.

void refresh_debugger_memory(void);

// Get debugged process state
// returns: one of the DSTATE_... constants (see below)

long get_process_state(void);

#endif
#define DSTATE_SUSP             -1 // process is suspended
#define DSTATE_NOTASK            0 // no process is currently debugged
#define DSTATE_RUN               1 // process is running
#ifdef _notdefinedsymbol

// ***********************************************
// Get various information about the current debug event
// These function are valid only when the current event exists
// (the process is in the suspended state)

// For all events:
long get_event_id(void);
long get_event_pid(void);
long get_event_tid(void);
long get_event_ea(void);
long is_event_handled(void);

// For PROCESS_STARTED, PROCESS_ATTACHED, LIB_LOADED events:
string get_event_module_name(void);
long get_event_module_base(void);
long get_event_module_size(void);

// For PROCESS_EXITED, THREAD_EXITED events
long get_event_exit_code(void);

// For THREAD_STARTED (thread name)
// For LIB_UNLOADED (unloaded library name)
// For INFORMATION (message to display)
string get_event_info(void);

// For BREAKPOINT event
long get_event_bpt_hea(void);

// For EXCEPTION event
long get_event_exc_code(void);
long get_event_exc_ea(void);
long can_exc_continue(void);
string get_event_exc_info(void);


/// \header Debugger: options
/// \id DebOptions
/// Get/set debugger options
///      opt - combination of DOPT_... constants
/// returns: old options

long set_debugger_options(long opt);

#endif
#define DOPT_SEGM_MSGS    0x00000001 // print messages on debugger segments modifications
#define DOPT_START_BPT    0x00000002 // break on process start
#define DOPT_THREAD_MSGS  0x00000004 // print messages on thread start/exit
#define DOPT_THREAD_BPT   0x00000008 // break on thread start/exit
#define DOPT_BPT_MSGS     0x00000010 // print message on breakpoint
#define DOPT_LIB_MSGS     0x00000040 // print message on library load/unlad
#define DOPT_LIB_BPT      0x00000080 // break on library load/unlad
#define DOPT_INFO_MSGS    0x00000100 // print message on debugging information
#define DOPT_INFO_BPT     0x00000200 // break on debugging information
#define DOPT_REAL_MEMORY  0x00000400 // don't hide breakpoint instructions
#define DOPT_REDO_STACK   0x00000800 // reconstruct the stack
#define DOPT_ENTRY_BPT    0x00001000 // break on program entry point
#define DOPT_EXCDLG       0x00006000 // exception dialogs:
#  define EXCDLG_NEVER    0x00000000 // never display exception dialogs
#  define EXCDLG_UNKNOWN  0x00002000 // display for unknown exceptions
#  define EXCDLG_ALWAYS   0x00006000 // always display
#define DOPT_LOAD_DINFO   0x00008000 // automatically load debug files (pdb)
#ifdef _notdefinedsymbol

// ***********************************************
// Set remote debugging options
//       hostname - remote host name or address
//                  if empty, revert to local debugger
//       password - password for the debugger server
//       portnum  - port number to connect (-1: don't change)
// returns: nothing

void set_remote_debugger(string hostname, string password, long portnum);


/// Take memory snapshot of the debugged process
///      only_loader_segs: 0-copy all segments to idb
///                        1-copy only SFL_LOADER segments

success take_memory_snapshot(long only_loader_segs);


/// Return the debugger event condition
///
/// returns: event condition

string get_debugger_event_cond();


/// Set a new debugger event condition

string set_debugger_event_cond(string condition);


/// Get number of defined exception codes

long get_exception_qty(void);


/// Get exception code
///      idx - number of exception in the vector (0..get_exception_qty()-1)
/// returns: exception code (0 - error)

long get_exception_code(long idx);


/// Get exception information
///      code - exception code
/// see also \ref define_exception (definition of exception flags)

string get_exception_name(long code); // returns "" on error
long get_exception_flags(long code);  // returns -1 on error


/// Add exception handling information
///      code - exception code
///      name - exception name
///      desc - exception description
///      flags - exception flags (combination of EXC_...)
/// returns: failure description or ""

string define_exception(long code, string name, string desc, long flags);

#endif
#define EXC_BREAK  0x0001 // break on the exception
#define EXC_HANDLE 0x0002 // should be handled by the debugger?
#define EXC_MSG    0x0004 // instead of warn, log the exception to the output window
#define EXC_SILENT 0x0008 // do not warn or log to the output window
#ifdef _notdefinedsymbol


/// Set exception flags
///      code - exception code
///      flags - exception flags (combination of EXC_...)

success set_exception_flags(long code, long flags);


/// Delete exception handling information
///      code - exception code

success forget_exception(long code);


/// get register value
///      name - the register name
/// the debugger should be running. otherwise the function fails
/// the register name should be valid.
/// It is not necessary to use this function to get register values
/// because a register name in the script will do too.
/// returns: register value (integer or floating point)
/// Thread-safe function (may be called only from the main thread and debthread)

number get_reg_value(string name);


/// set register value
///      name - the register name
///      value - new register value
/// the debugger should be running
/// It is not necessary to use this function to set register values.
/// A register name in the left side of an assignment will do too.
/// Thread-safe function (may be called only from the main thread and debthread)

success set_reg_value(number value, string name);


/// get value of the IP (program counter) register for the current thread

long get_ip_val();


// ----------------------------------------------------------------------------
/// \header Breakpoint handling functions
/// \id Bpts
// Get number of breakpoints.
// Returns: number of breakpoints

long get_bpt_qty();

// Get breakpoint address
//      n - number of breakpoint, is in range 0..get_bpt_qty()-1
// returns: address of the breakpoint or BADADDR

long get_bpt_ea(long n);

// Get the characteristics of a breakpoint
//      address - any address in the breakpoint range
//      bptattr - the desired attribute code, one of BPTATTR_... constants
// Returns: the desired attribute value or -1

long get_bpt_attr(long ea, number bptattr);

#endif
#define NO_PROCESS    -1  // invalid process
#define NO_THREAD      0  // invalid thread
#define BPTATTR_EA     1  // starting address of the breakpoint
#define BPTATTR_SIZE   2  // size of the breakpoint (undefined for software breakpoint)
#define BPTATTR_TYPE   3                     // type of the breakpoint
                                             // Breakpoint types:
#define  BPT_WRITE   1                       // Hardware: Write access
#define  BPT_READ    2                       // Hardware: Read access
#define  BPT_RDWR    3                       // Hardware: Read/write access
#define  BPT_SOFT    4                       // Software breakpoint
#define  BPT_EXEC    8                       // Hardware: Execute instruction
#define  BPT_DEFAULT (BPT_SOFT|BPT_EXEC)     // Choose bpt type automaticaly

#define BPTATTR_COUNT  4  // number of times the breakpoint is hit before stopping

#define BPTATTR_FLAGS  5  // Breakpoint attributes:
#define BPT_BRK        0x001 // the debugger stops on this breakpoint
#define BPT_TRACE      0x002 // the debugger adds trace information when
                             // this breakpoint is reached
#define BPT_UPDMEM     0x004 // refresh the memory layout and contents before evaluating bpt condition
#define BPT_ENABLED    0x008 // enabled?
#define BPT_LOWCND     0x010 // condition is calculated at low level (on the server side)
#define BPT_TRACEON    0x020 // enable tracing when the breakpoint is reached
#define BPT_TRACE_INSN 0x040 //   instruction tracing
#define BPT_TRACE_FUNC 0x080 //   function tracing
#define BPT_TRACE_BBLK 0x100 //   basic block tracing

#define BPTATTR_COND   6  // Breakpoint condition
                          // NOTE: the return value is a string in this case
#define BPTATTR_PID    7  // Breakpoint process id
#define BPTATTR_TID    8  // Breakpoint thread id

// Breakpoint location type:
#define BPLT_ABS     0    // Absolute address. Attributes:
                          // - locinfo: absolute address

#define BPLT_REL     1    // Module relative address. Attributes:
                          // - locpath: the module path
                          // - locinfo: offset from the module base address

#define BPLT_SYM     2    // Symbolic name. The name will be resolved on DLL load/unload
                          // events and on naming an address. Attributes:
                          // - locpath: symbol name
                          // - locinfo: offset from the symbol base address

// Breakpoint properties:
#define BKPT_BADBPT   0x01 // failed to write the bpt to the process memory (at least one location)
#define BKPT_LISTBPT  0x02 // include in bpt list (user-defined bpt)
#define BKPT_TRACE    0x04 // trace bpt; should not be deleted when the process gets suspended
#define BKPT_ACTIVE   0x08 // active?
#define BKPT_PARTIAL  0x10 // partially active? (some locations were not written yet)
#define BKPT_CNDREADY 0x20 // condition has been compiled
#ifdef _notdefinedsymbol

// ***********************************************
class Breakpoint
{
  // Breakpoint type. One of BPT_... constants
  attribute type;

  // Breakpoint size (for hardware breakpoint)
  attribute size;

  // Breakpoint condition (string)
  attribute condition;

  // Scripting language of the condition string
  // "IDC" for IDC, "Python" for Python etc. ('name' field of extlang_t)
  // if empty, default extlang is assumed
  attribute elang;

  // Breakpoint flags. Refer to BPTATTR_FLAGS
  attribute flags;

  // Breakpoint properties. Refer to BKPT_... constants
  attribute props;

  // Breakpoint pass count
  attribute pass_count;

  // Attribute location type. Refer to BPLT_... constants.
  // Readonly attribute.
  attribute loctype;

  // Breakpoint path (depending on the loctype)
  // Readonly attribute.
  attribute locpath;

  // Breakpoint address info (depending on the loctype)
  // Readonly attribute.
  attribute locinfo;

  // Set absolute breakpoint
  success set_abs_bpt(address);

  // Set symbolic breakpoint
  success set_sym_bpt(symbol_name, offset);

  // Set relative breakpoint
  success set_rel_bpt(path, offset);
};

// Set modifiable characteristics of a breakpoint
//       address - any address in the breakpoint range
//       bptattr - the attribute code, one of BPTATTR_... constants.
//                 BPTATTR_COND is not allowed, see \ref Bpts
//       value   - the attibute value
// Returns: success

success set_bpt_attr(long ea, number bptattr, long value);

// Set breakpoint condition
//       address  - any address in the breakpoint range
//       cnd      - breakpoint condition
//       is_lowcnd- 0:regular condition, 1:low level condition
// Returns: success

success set_bpt_cond(long ea, string cnd, long is_lowcnd=0);

// Add a new breakpoint
//       ea   - any address in the process memory space:
//       size - size of the breakpoint (irrelevant for software breakpoints):
//       type - type of the breakpoint (one of BPT_... constants)
// Only one breakpoint can exist at a given address.
// Returns: success

success add_bpt(long ea, long size=0, long bpttype=BPT_DEFAULT);

// Delete breakpoint
//       ea   - any address in the process memory space:
// Returns: success

success del_bpt(long ea);

// Enable/disable breakpoint
//       ea   - any address in the process memory space
// Disabled breakpoints are not written to the process memory
// To check the state of a breakpoint, use check_bpt()
// Returns: success

success enable_bpt(long ea, long enable);

// Check a breakpoint
//       ea   - any address in the process memory space
// Returns: one of BPTCK_... constants

long check_bpt(long ea);

#endif
#define BPTCK_NONE -1  // breakpoint does not exist
#define BPTCK_NO    0  // breakpoint is disabled
#define BPTCK_YES   1  // breakpoint is enabled
#define BPTCK_ACT   2  // breakpoint is active (written to the process)
#ifdef _notdefinedsymbol


// ----------------------------------------------------------------------------

/// Enable step tracing
///      trace_level - what kind of trace to modify
///      enable      - 0: turn off, 1: turn on
/// Returns: success

success enable_tracing(long trace_level, long enable);

#endif
#define TRACE_STEP 0x0  // lowest level trace. trace buffers are not maintained
#define TRACE_INSN 0x1  // instruction level trace
#define TRACE_FUNC 0x2  // function level trace (calls & rets)
#define TRACE_BBLK 0x4  // basic block level trace
#ifdef _notdefinedsymbol


/// \header Step Tracing Options
/// \id StepTracingOptions
// Get step current tracing options
// Returns combination of ST_... constants

long get_step_trace_options();

// Set step current tracing options.
//      options - combination of ST_... constants

void set_step_trace_options(long options);

#endif
#define ST_OVER_DEBUG_SEG 0x01 // step tracing will be disabled when IP is in a debugger segment
#define ST_OVER_LIB_FUNC  0x02 // step tracing will be disabled when IP is in a library function
#define ST_ALREADY_LOGGED 0x04 // step tracing will be disabled when IP is already logged
#define ST_SKIP_LOOPS     0x08 // step tracing will try to skip loops already recorded
#define ST_DIFFERENTIAL   0x10 // tracing: log only new instructions
#ifdef _notdefinedsymbol


// ----------------------------------------------------------------------------
/// \header Trace file functions
/// \id TraceFileFunctions
// Load a previously recorded binary trace file
//       filename - trace file
success load_trace_file(string filename);

// Save current trace to a binary trace file
//       filename - trace file
//       description - trace description
success save_trace_file(string filename, string description);

// Check the given binary trace file
//       filename - trace file
success is_valid_trace_file(string filename);

// Diff current trace buffer against given trace
//       filename - trace file
success diff_trace_file(string filename);

// Clear the current trace buffer
void clear_trace();

// Update the trace description of the given binary trace file
//       filename - trace file
//       description - trace description
success set_trace_file_desc(string filename, string description);

// Get the trace description of the given binary trace file
//       filename - trace file
string get_trace_file_desc(string filename);


// ----------------------------------------------------------------------------
/// \header Trace events functions
/// \id TraceEventFunctions
// Return the total number of recorded events
long get_tev_qty();

// Return the address of the specified event
//       tev - event number
long get_tev_ea(long tev);

// Return the type of the specified event (TEV_... constants)
//       tev - event number
long get_tev_type(long tev);

#endif
#define TEV_NONE  0 // no event
#define TEV_INSN  1 // an instruction trace
#define TEV_CALL  2 // a function call trace
#define TEV_RET   3 // a function return trace
#define TEV_BPT   4 // write, read/write, execution trace
#define TEV_MEM   5 // memory layout changed
#define TEV_EVENT 6 // debug event
#ifdef _notdefinedsymbol

// Return the thread id of the specified event
//       tev - event number
long get_tev_tid(long tev);

// Return the register value for the specified event
//       tev - event number
//       reg - register name (like EAX, RBX, ...)
long get_tev_reg(long tev, string reg);

// Return the number of memory addresses recorded for the specified event
//       tev - event number
long get_tev_mem_qty(long tev);

// Return the memory pointed by 'index' for the specified event
//       tev - event number
//       idx - memory address index
string get_tev_mem(long tev, long idx);

// Return the address pointed by 'index' for the specified event
//       tev - event number
//       idx - memory address index
string get_tev_mem_ea(long tev, long idx);

// Return the address of the callee for the specified event
//       tev - event number
long get_call_tev_callee(long tev);

// Return the return address for the specified event
//       tev - event number
long get_ret_tev_return(long tev);

// Return the address of the specified TEV_BPT event
//       tev - event number
long get_bpt_tev_ea(long tev);


// ----------------------------------------------------------------------------
/// Call application function
///      ea - address to call
///      type - type of the function to call. can be specified as:
///              - declaration string. example: "int func(void);"
///              - typeinfo object. example: get_tinfo(ea)
///              - zero: the type will be retrieved from the idb
///      ... - arguments of the function to call
/// Returns: the result of the function call
/// If the call fails because of an access violation or other exception,
/// a runtime error will be generated (it can be caught with try/catch)
/// In fact there is rarely any need to call this function explicitly.
/// IDC tries to resolve any unknown function name using the application labels
/// and in the case of success, will call the function. For example:
///      _printf("hello\n")
/// will call the application function _printf provided that there is
/// no IDC function with the same name.

anyvalue dbg_appcall(ea, type, ...);

// Set/get appcall options
#endif
#define set_appcall_options(x) set_inf_attr(INF_APPCALL_OPTIONS, x)
#define get_appcall_options()  get_inf_attr(INF_APPCALL_OPTIONS)

#define APPCALL_MANUAL 0x0001   // Only set up the appcall, do not run it.
                                // you should call \ref cleanup_appcall() when finished
#define APPCALL_DEBEV  0x0002   // Return debug event information
                                // If this bit is set, exceptions during appcall
                                // will generate idc exceptions with full
                                // information about the exception
#define APPCALL_TIMEOUT 0x0004  // dbg_appcall with timeout
                                // The timeout value in milliseconds is specified
                                // in the high 2 bytes of the 'options' argument:
                                // If timed out, exception message will contain "timeout".
#define SET_APPCALL_TIMEOUT(x) ((x<<16)|0x0004) // dbg_appcall with timeout
#ifdef _notdefinedsymbol

/*
With dbg_appcall, it is possible to call an arbitrary function from the
debugged application without any special measures like dll injection or
modifying the process memory. The call can be simplified to func(args), if the
function name is a valid identifier. For example, given this:

        verinfo = object();
        verinfo.dwOSVersionInfoSize = sizeof(OSVERSIONINFOA);

the following dbg_appcall:

        GetVersionExA(&verinfo);

will call create an instance of OSVERSIONINFOA in the application memory
and call GetVersionExA with a pointer to it. After the call, it will convert the
OSVERSIONINFO instance into an IDC object. The verinfo variable will contain:

object
  __at__:        18FEB0h
  dwBuildNumber:        7600.
  dwMajorVersion:          6.
  dwMinorVersion:          1.
  dwOSVersionInfoSize:
  dwPlatformId:            2.
  szCSDVersion: "\x00\x00\x00\x00..."


The __at__ attribute tells us the address of the structure. If this particular
case it is not very useful since the object was temporary, but in other cases
it could be useful.

dbg_appcall converts IDC objects to C objects and vice versa. The conversion is
controlled by the type information. The following rules control the conversion:

 PLAIN SCALARS:

  - if the target type a plain scalar type (not a pointer),
    a simple conversion is done, with sign extension or truncation.
    For example, an IDC value of -1 is converted into an __int32(0xFFFFFFFF).
    For example, an IDC value of 0x555 is converted into an __int8(0x55).

 POINTERS:

  - if the target type a pointer and the corresponding idc value is a string,
    the string is accepted as the pointed object. It is simply copied to the
    process memory without any modifications. There will be a terminating zero
    after the string.

    If the corresponding idc value a number, its value is used as the pointer
    value. To create pointers to numbers, use the & operator.

    If the corresponding idc value is not a string, it is converted to C
    and a pointer to the converted object will be used to initialize the pointer.

 STRUCTURES:

  - if the target type is a structure, ida tries to initialize its fields one by
    one, by accessing the corresponding attributes. For example, in the above
    sample only the dwOSVersionInfoSize attribute exists, and its corresponding
    field will be initialized with its value. If a field does not exist,
    the corresponding field will be initialized with zeroes.

 ARRAYS:

  - each array element is initialized individually, expect if the corresponding
    idc value is a string. In this case, the string value is used as the value
    of the whole array. It is the user's responsibility to prepare a valid
    string that will represent an array in this case.

Some more examples. Calling printf is very easy:

  auto n = 5;
  auto s = "short";
  _printf("Hello world, number is %d, string is %s\n", n, s);

Calling sscanf will require using the & operator:

  auto x;
  auto nsuccess = _sscanf(s, "%d", &x);

Structures can be passed by ref without & because they are always
passed by reference:

  verinfo = object();
  GetVersionExA(verinfo);


All calling conventions, including @hlpHelpSetType[__usercall], are supported.

For calls that generate exceptions, single stepping is possible using
the APPCALL_MANUAL bit.
*/


/// Cleanup the current appcall
/// This function can be used to terminate the current \ref dbg_appcall that was
/// started with APPCALL_MANUAL

success cleanup_appcall();


// ----------------------------------------------------------------------------
//                           C O L O R S
// ----------------------------------------------------------------------------

/// get item color
///      ea - address of the item
///      what - type of the item (one of COLWHAT... constants)
/// returns: color code in RGB (hex 0xBBGGRR)

long get_color(long ea, long what);

#endif
// color item codes:
#define CIC_ITEM 1          // one instruction or data
#define CIC_FUNC 2          // function
#define CIC_SEGM 3          // segment

#define DEFCOLOR 0xFFFFFFFF     // Default color
#ifdef _notdefinedsymbol


/// set item color
///      ea - address of the item
///      what - type of the item (one of COLWHAT... constants)
///      color - new color code in RGB (hex 0xBBGGRR)
/// returns: 1-ok, 0-failure

success set_color(long ea, long what, long color);


// ----------------------------------------------------------------------------
//                     T I M E   A N D   D A T E
// ----------------------------------------------------------------------------

/// get the current timestamp, in nanoseconds.
///    Retrieves the high-resolution current timestamp, in nanoseconds.
/// returns: the timestamp, a 64-bit number.

long get_nsec_stamp();


// ----------------------------------------------------------------------------
//                       A R M   S P E C I F I C
// ----------------------------------------------------------------------------

/// \header ARM specific
/// \id ARMSpecific
/// Some ARM compilers in Thumb mode use BL (branch-and-link)
/// instead of B (branch) for long jumps, since BL has more range.
/// By default, IDA tries to determine if BL is a jump or a call.
/// You can override IDA's decision using commands in Edit/Other menu
/// (Force BL call/Force BL jump) or the following two functions.

//  Force BL instruction to be a jump
//       ea - address of the BL instruction
//  returns: 1-ok, 0-failed

success force_bl_jump(long ea);

//  Force BL instruction to be a call
//       ea - address of the BL instruction
//  returns: 1-ok, 0-failed

success force_bl_call(long ea);


// ----------------------------------------------------------------------------

/// Send arbitrary command to the debugger engine.
/// Returns: the command output.
///
/// Note: this function is available for the following debuggers:
/// windbg, gdb, bochs

string send_dbg_command(string cmd);


// ----------------------------------------------------------------------------
//                   D A L V I K   S P E C I F I C
// ----------------------------------------------------------------------------

/// \header Dalvik debugger extension functions
/// \id DalvikDebuggerFunctions
// Get local variable or function argument value
//       name - variable name ("v0", "v1", ... or user defined name)
auto dalvik_get_local(string name);

// Get typed local variable value
//       name - variable name ("v0", "v1", ... or user defined name)
//       wanted_type - Java VM's representation of type signature
auto dalvik_get_local_typed(string name, string wanted_type);

// Get object instance field value
//       oid - object id
//       name - object field name
auto dalvik_get_instance_fld(int64 oid, string name);

// Get number or array elements
//       oid - array object id
long dalvik_get_array_size(int64 oid);

// Get array element by index
//       oid - object id
//       idx - element index
auto dalvik_get_array_elem(int64 oid, long idx);


// ----------------------------------------------------------------------------
//      R E P L A Y E R   D E B U G G E R   S P E C I F I C
// ----------------------------------------------------------------------------

/// \header Functions provided by the replayer debugger
/// \id ReplayerDebuggerFunctions
// Step back in the currently replayed trace
// Returns: error code (0 if none happened).

success step_back(void);

// Set the current event number, changing the PC register.
// Input  : the event to move to
// Events are numbered in reverse order, i.e. 0 is the last available event.
// Returns: error code.

success set_current_tev(long event);

// Get the current event number.
// Returns: the current event number.

long get_current_tev(void);


// ----------------------------------------------------------------------------
//      W I N D B G   D E B U G G E R   S P E C I F I C
// ----------------------------------------------------------------------------

/// \header Functions provided by the WinDbg debugger
/// \id WinDbgDebuggerFunctions
// Send arbitrary command to the WinDbg engine
// Returns: the command output

string \ref send_dbg_command(string cmd);

// Read a model specific register
// Returns: the register value. if this function fails,
//          an exception with the error code is raised
// Note: this function works only in the kernel mode

int64 read_msr(long reg_id);

// Write a model specific register
// Returns: windows error code (0-ok)
// Note: this function works only in the kernel mode

success write_msr(long reg_id, int64 value);



// -------------------------------------------------------------------------
#endif // _notdefinedsymbol


// ----------------------------------------------------------------------------
//               P R O C E S S O R  M O D U L E   C O N S T A N T S
// ----------------------------------------------------------------------------
// asm_t.flag
#define AS_OFFST      0x00000001L       // offsets are 'offset xxx' ?
#define AS_COLON      0x00000002L       // create colons after data names ?
#define AS_UDATA      0x00000004L       // can use '?' in data directives

#define AS_2CHRE      0x00000008L       // double char constants are: "xy
#define AS_NCHRE      0x00000010L       // char constants are: 'x
#define AS_N2CHR      0x00000020L       // can't have 2 byte char consts

//----------------------------------------------------------------------
// asm_t.flag2
                                        // ASCII directives:
#define AS_1TEXT      0x00000040L       //   1 text per line, no bytes
#define AS_NHIAS      0x00000080L       //   no characters with high bit
#define AS_NCMAS      0x00000100L       //   no commas in ascii directives

#define AS_HEXFM      0x00000E00L       // format of hex numbers:
#define ASH_HEXF0     0x00000000L       //   34h
#define ASH_HEXF1     0x00000200L       //   h'34
#define ASH_HEXF2     0x00000400L       //   34
#define ASH_HEXF3     0x00000600L       //   0x34
#define ASH_HEXF4     0x00000800L       //   $34
#define ASH_HEXF5     0x00000A00L       //   <^R   > (radix)
#define AS_DECFM      0x00003000L       // format of dec numbers:
#define ASD_DECF0     0x00000000L       //   34
#define ASD_DECF1     0x00001000L       //   #34
#define ASD_DECF2     0x00002000L       //   34.
#define ASD_DECF3     0x00003000L       //   .34
#define AS_OCTFM      0x0001C000L       // format of octal numbers:
#define ASO_OCTF0     0x00000000L       //   123o
#define ASO_OCTF1     0x00004000L       //   0123
#define ASO_OCTF2     0x00008000L       //   123
#define ASO_OCTF3     0x0000C000L       //   @123
#define ASO_OCTF4     0x00010000L       //   o'123
#define ASO_OCTF5     0x00014000L       //   123q
#define ASO_OCTF6     0x00018000L       //   ~123
#define AS_BINFM      0x000E0000L       // format of binary numbers:
#define ASB_BINF0     0x00000000L       //   010101b
#define ASB_BINF1     0x00020000L       //   ^B010101
#define ASB_BINF2     0x00040000L       //   %010101
#define ASB_BINF3     0x00060000L       //   0b1010101
#define ASB_BINF4     0x00080000L       //   b'1010101
#define ASB_BINF5     0x000A0000L       //   b'1010101'

#define AS_UNEQU      0x00100000L       // replace undefined data items
                                        // with EQU (for ANTA's A80)
#define AS_ONEDUP     0x00200000L       // One array definition per line
#define AS_NOXRF      0x00400000L       // Disable xrefs during the output file generation
#define AS_XTRNTYPE   0x00800000L       // Assembler understands type of extrn
                                        // symbols as ":type" suffix
#define AS_RELSUP     0x01000000L       // Checkarg: 'and', 'or', 'xor' operations
                                        // with addresses are possible
#define AS_LALIGN     0x02000000L       // Labels at "align" keyword
                                        // are supported.
#define AS_NOCODECLN  0x04000000L       // don't create colons after code names
#define AS_NOTAB      0x08000000L       // Disable tabulation symbols during the output file generation
#define AS_NOSPACE    0x10000000L       // No spaces in expressions
#define AS_ALIGN2     0x20000000L       // .align directive expects an exponent rather than a power of 2
                                        // (.align 5 means to align at 32byte boundary)
#define AS_ASCIIC     0x40000000L       // ascii directive accepts C-like
                                        // escape sequences (\n, \x01 and similar)
#define AS_ASCIIZ     0x80000000L       // ascii directive inserts implicit
                                        // zero byte at the end

#define AS2_BRACE     0x00000001        // Use braces for all expressions
#define AS2_STRINV    0x00000002        // For processors with bytes bigger than 8 bits:
                                        //  invert the meaning of inf.wide_high_byte_first
                                        //  for text strings
#define AS2_BYTE1CHAR 0x00000004        // One symbol per processor byte
                                        // Meaningful only for wide byte processors
#define AS2_IDEALDSCR 0x00000008        // Description of struc/union is in
                                        // the 'reverse' form (keyword before name)
                                        // the same as in borland tasm ideal
#define AS2_TERSESTR  0x00000010        // 'terse' structure initialization form
                                        // NAME<fld, fld, ...> is supported
#define AS2_COLONSUF  0x00000020        // addresses may have ":xx" suffix
                                        // this suffix must be ignored when extracting
                                        // the address under the cursor

//----------------------------------------------------------------------
// processor_t.version
#define IDP_INTERFACE_VERSION 76

//----------------------------------------------------------------------
// processor_t.flags
#define PR_SEGS       0x000001  // has segment registers?
#define PR_USE32      0x000002  // supports 32-bit addressing?
#define PR_DEFSEG32   0x000004  // segments are 32-bit by default
#define PR_RNAMESOK   0x000008  // allow to user register names for
                                // location names
#define PR_DB2CSEG    0x0010  // .byte directive in code segments
                              // should define even number of bytes
                              // (used by AVR processor)
#define PR_ADJSEGS    0x000020  // IDA may adjust segments moving
                                // their starting/ending addresses.
#define PR_DEFNUM     0x0000C0  // default number representation:
#define PRN_HEX       0x000000  //      hex
#define PRN_OCT       0x000040  //      octal
#define PRN_DEC       0x000080  //      decimal
#define PRN_BIN       0x0000C0  //      binary
#define PR_WORD_INS   0x000100  // instruction codes are grouped
                                // 2bytes in binrary line prefix
#define PR_NOCHANGE   0x000200  // The user can't change segments
                                // and code/data attributes
                                // (display only)
#define PR_ASSEMBLE   0x000400  // Module has a built-in assembler
                                // and will react to ev_assemble
#define PR_ALIGN      0x000800  // All data items should be aligned
                                // properly
#define PR_TYPEINFO   0x001000  // the processor module supports
                                // type information callbacks
                                // ALL OF THEM SHOULD BE IMPLEMENTED!
#define PR_USE64      0x002000  // supports 64-bit addressing?
#define PR_SGROTHER   0x004000  // the segment registers don't contain
                                // the segment selectors, something else
#define PR_STACK_UP   0x008000  // the stack grows up
#define PR_BINMEM     0x010000  // the processor module provides correct
                                // segmentation for binary files
                                // (i.e. it creates additional segments)
                                // The kernel will not ask the user
                                // to specify the RAM/ROM sizes
#define PR_SEGTRANS   0x020000  // the processor module supports
                                // the segment translation feature
                                // (it means it calculates the code
                                // addresses using the map_code_ea() function)
#define PR_CHK_XREF   0x040000  // don't allow near xrefs between segments
                                // with different bases
#define PR_NO_SEGMOVE 0x080000  // the processor module doesn't support move_segm()
                                // (i.e. the user can't move segments)
#define PR_FULL_HIFXP 0x100000  // REF_VHIGH operand value contains full operand
                                // not only the high bits. Meaningful if ph.high_fixup_bits
#define PR_USE_ARG_TYPES 0x200000 // use ph.use_arg_types callback
#define PR_SCALE_STKVARS 0x400000 // use ph.get_stkvar_scale callback
#define PR_DELAYED    0x800000 // has delayed jumps and calls
#define PR_ALIGN_INSN 0x1000000 // allow ida to create alignment instructions
                                // arbirtrarily. Since these instructions
                                // might lead to other wrong instructions
                                // and spoil the listing, IDA does not create
                                // them by default anymore
#define PR_PURGING    0x2000000 // there are calling conventions which may
                                // purge bytes from the stack
#define PR_CNDINSNS   0x4000000 // has conditional instructions
#define PR_USE_TBYTE  0x8000000 // BTMT_SPECFLT means _TBYTE type
#define PR_DEFSEG64  0x10000000 // segments are 64-bit by default

//----------------------------------------------------------------------
// insn_t.flags
#define INSN_MACRO  0x01        // macro instruction
#define INSN_MODMAC 0x02        // macros: may modify the database
                                // to make room for the macro insn


//----------------------------------------------------------------------
// processor_t.set_idp_options
#define IDPOPT_STR 1                    // string constant (char *)
#define IDPOPT_NUM 2                    // number (uval_t *)
#define IDPOPT_BIT 3                    // bit, yes/no (int *)
#define IDPOPT_I64 5                    // 64bit number (int64 *)
// returns:
#define IDPOPT_OK       0               // ok
#define IDPOPT_BADKEY   1               // illegal keyword
#define IDPOPT_BADTYPE  2               // illegal type of value
#define IDPOPT_BADVALUE 3               // illegal value (bad range, for example)

//----------------------------------------------------------------------
// processor_t.is_sp_based return code
#define OP_FP_BASED  0x00000000 // operand is FP based
#define OP_SP_BASED  0x00000001 // operand is SP based
#define OP_SP_ADD    0x00000000 // operand value is added to the pointer
#define OP_SP_SUB    0x00000002 // operand value is substracted from the pointer

//----------------------------------------------------------------------
//
//      Floating point -> IEEE conversion function
// error codes returned by the processor_t.realcvt function (load/store):
#define REAL_ERROR_FORMAT  -1 // not supported format for current .idp
#define REAL_ERROR_RANGE   -2 // number too big (small) for store (mem NOT modifyed)
#define REAL_ERROR_BADDATA -3 // illegal real data for load (IEEE data not filled)

//-----------------------------------------------------------------------
// instruc_t.feature
#define CF_STOP 0x00001  // Instruction doesn't pass execution to the
                         // next instruction
#define CF_CALL 0x00002  // CALL instruction (should make a procedure here)
#define CF_CHG1 0x00004  // The instruction modifies the first operand
#define CF_CHG2 0x00008  // The instruction modifies the second operand
#define CF_CHG3 0x00010  // The instruction modifies the third operand
#define CF_CHG4 0x00020  // The instruction modifies 4 operand
#define CF_CHG5 0x00040  // The instruction modifies 5 operand
#define CF_CHG6 0x00080  // The instruction modifies 6 operand
#define CF_USE1 0x00100  // The instruction uses value of the first operand
#define CF_USE2 0x00200  // The instruction uses value of the second operand
#define CF_USE3 0x00400  // The instruction uses value of the third operand
#define CF_USE4 0x00800  // The instruction uses value of the 4 operand
#define CF_USE5 0x01000  // The instruction uses value of the 5 operand
#define CF_USE6 0x02000  // The instruction uses value of the 6 operand
#define CF_JUMP 0x04000  // The instruction passes execution using indirect
                         // jump or call (thus needs additional analysis)
#define CF_SHFT 0x08000  // Bit-shift instruction (shl, shr...)
#define CF_HLL  0x10000  // Instruction may be present in a high level
                         // language function.

//-----------------------------------------------------------------------
// op_t.dtyp
#define dt_byte         0       // 8 bit integer
#define dt_word         1       // 16 bit integer
#define dt_dword        2       // 32 bit integer
#define dt_float        3       // 4 byte floating point
#define dt_double       4       // 8 byte floating point
#define dt_tbyte        5       // variable size (\ph{tbyte_size}) floating point
#define dt_packreal     6       // packed real format for mc68040
#define dt_qword        7       // 64 bit integer
#define dt_byte16       8       // 128 bit integer
#define dt_code         9       // ptr to code (not used?)
#define dt_void         10      // none
#define dt_fword        11      // 48 bit
#define dt_bitfild      12      // bit field (mc680x0)
#define dt_string       13      // pointer to asciiz string
#define dt_unicode      14      // pointer to unicode string
#define dt_ldbl         15      // long double (which may be different from tbyte)
#define dt_byte32       16      // 256 bit integer
#define dt_byte64       17      // 512 bit integer
#define dt_half         18      // 2-byte floating point

//-----------------------------------------------------------------------
// op_t.flags
#define OF_NO_BASE_DISP 0x80    // o_displ: base displacement doesn't exist
                                // meaningful only for o_displ type
                                // if set, base displacement (x.addr)
                                // doesn't exist.
#define OF_OUTER_DISP   0x40    // o_displ: outer displacement exists
                                // meaningful only for o_displ type
                                // if set, outer displacement (x.value) exists.
#define PACK_FORM_DEF   0x20    // !o_reg + dt_packreal: packed factor defined
#define OF_NUMBER       0x10    // can be output as number only
                                // if set, the operand can be converted to a
                                // number only
#define OF_SHOW         0x08    // should the operand be displayed?
                                // if clear, the operand is hidden and should
                                // not be displayed

// ----------------------------------------------------------------------------
//               P L U G I N S  C O N S T A N T S
// ----------------------------------------------------------------------------

#define PLUGIN_MOD   0x0001     // Plugin changes the database.
                                // IDA won't call the plugin if
                                // the processor prohibited any changes
                                // by setting PR_NOCHANGES in processor_t.
#define PLUGIN_DRAW  0x0002     // IDA should redraw everything after calling
                                // the plugin
#define PLUGIN_SEG   0x0004     // Plugin may be applied only if the
                                // current address belongs to a segment
#define PLUGIN_UNL   0x0008     // Unload the plugin immediately after
                                // calling 'run'.
                                // This flag may be set anytime.
                                // The kernel checks it after each call to 'run'
                                // The main purpose of this flag is to ease
                                // the debugging of new plugins.
#define PLUGIN_HIDE  0x0010     // Plugin should not appear in the Edit, Plugins menu
                                // This flag is checked at the start
#define PLUGIN_DBG   0x0020     // A debugger plugin. init() should put
                                // the address of debugger_t to dbg
                                // See idd.hpp for details
#define PLUGIN_PROC  0x0040     // Load plugin when a processor module is loaded and keep it
                                // until the processor module is unloaded
#define PLUGIN_FIX   0x0080     // Load plugin when IDA starts and keep it in the
                                // memory until IDA stops
#define PLUGIN_MULTI 0x0100     // The plugin can work with multiple idbs in parallel.

#define PLUGIN_SKIP  0          // Plugin doesn't want to be loaded
#define PLUGIN_OK    1          // Plugin agrees to work with the current database
                                // It will be loaded as soon as the user presses the hotkey

#define PLUGIN_KEEP  2          // Plugin agrees to work with the current database
                                // and wants to stay in the memory

// ----------------------------------------------------------------------------
//               C O M P A T I B I L I T Y    M A C R O S
// ----------------------------------------------------------------------------
#define Compile(file)           CompileEx(file, 1)
#define OpOffset(ea, base)      op_plain_offset(ea, -1, base)
#define OpNum(ea)               op_num(ea, -1)
#define OpChar(ea)              op_chr(ea, -1)
#define OpSegment(ea)           op_seg(ea, -1)
#define OpDec(ea)               op_dec(ea, -1)
#define OpAlt1(ea, str)         op_man(ea, 0, str)
#define OpAlt2(ea, str)         op_man(ea, 1, str)

// Convenience functions
#define StringStp(x)            set_inf_attr(INF_STRLIT_BREAK, x)
#define LowVoids(x)             set_inf_attr(INF_LOW_OFF, x)
#define HighVoids(x)            set_inf_attr(INF_HIGH_OFF, x)
#define TailDepth(x)            set_inf_attr(INF_MAXREF, x)
#define Analysis(x)             set_flag(INF_GENFLAGS, INFFL_AUTO, x)
#define Comments(x)             set_flag(INF_CMTFLG, SCF_ALLCMT, x)
#define Voids(x)                set_flag(INF_OUTFLAGS, OFLG_SHOW_VOID, x)
#define XrefShow(x)             set_inf_attr(INF_XREFNUM, x)
#define Indent(x)               set_inf_attr(INF_INDENT, x)
#define CmtIndent(x)            set_inf_attr(INF_COMMENT, x)
#define AutoShow(x)             set_flag(INF_OUTFLAGS, OFLG_SHOW_AUTO, x)
#define MinEA()                 get_inf_attr(INF_MIN_EA)
#define MaxEA()                 get_inf_attr(INF_MAX_EA)
#define StartEA()               get_inf_attr(INF_START_EA)
#define set_start_cs(x)         set_inf_attr(INF_START_CS, x)
#define set_start_ip(x)         set_inf_attr(INF_START_IP, x)
#define auto_make_code(x)       auto_mark_range(x, (x)+1, AU_CODE);

#define WriteMap(file) \
        gen_file(OFILE_MAP, fopen(file, "w"), 0, BADADDR, \
        GENFLG_MAPSEGS|GENFLG_MAPNAME)
#define WriteTxt(file, ea1, ea2) \
        gen_file(OFILE_ASM, fopen(file, "w"), ea1, ea2, 0)
#define WriteExe(file) \
        gen_file(OFILE_EXE, fopen(file, "wb"), 0, BADADDR, 0)
#define AddConst(enum_id, name, value) add_enum_member(enum_id, name, value, -1)
#define AddStruc(index, name)       add_struc(index, name, 0)
#define AddUnion(index, name)       add_struc(index, name, 1)
#define OpStroff(ea, n, strid)      op_stroff(ea, n, strid, 0)
#define OpEnum(ea, n, enumid)       op_enum(ea, n, enumid, 0)
#define DelConst(id, v, mask)       del_enum_member(id, v, 0, mask)
#define GetConst(id, v, mask)       get_enum_member(id, v, 0, mask)
#define AnalyseRange(sEA, eEA)      plan_and_wait(sEA, eEA)
#define AnalyseArea(sEA, eEA)       plan_and_wait(sEA, eEA)
#define AnalyzeArea(sEA, eEA)       plan_and_wait(sEA, eEA)

#define MakeStruct(ea, name)        create_struct(ea, -1, name)
#define Name(ea)                    get_name(ea, GN_VISIBLE)
#define GetTrueName(ea)             get_name(ea)
#define MakeName(ea, name)          set_name(ea, name, SN_CHECK)

#define GetFrame(ea)                get_func_attr(ea, FUNCATTR_FRAME)
#define GetFrameLvarSize(ea)        get_func_attr(ea, FUNCATTR_FRSIZE)
#define GetFrameRegsSize(ea)        get_func_attr(ea, FUNCATTR_FRREGS)
#define GetFrameArgsSize(ea)        get_func_attr(ea, FUNCATTR_ARGSIZE)
#define GetFunctionFlags(ea)        get_func_attr(ea, FUNCATTR_FLAGS)
#define SetFunctionFlags(ea, flags) set_func_attr(ea, FUNCATTR_FLAGS, flags)

#define AddSeg(a1, a2, sel, use32, align, comb) add_segm_ex(a1, a2, sel, use32, align, comb, ADDSEG_NOSREG)
#define SegCreate(a1, a2, base, use32, align, comb) AddSeg(a1, a2, base, use32, align, comb)
#define SegDelete(ea, flags)        del_segm(ea, flags)
#define SegBounds(ea, startea, endea, flags) set_segment_bounds(ea, startea, endea, flags)
#define SegRename(ea, name)         set_segm_name(ea, name)
#define SegClass(ea, klass)         set_segm_class(ea, klass)
#define SegAddrng(ea, bitness)      set_segm_addressing(ea, bitness)
#define SegDefReg(ea, reg, value)   set_default_sreg_value(ea, reg, value)

#define Comment(ea)                 get_cmt(ea, 0)
#define RptCmt(ea)                  get_cmt(ea, 1)

#define MakeByte(ea)                create_data(ea, FF_BYTE, 1, BADADDR)
#define MakeWord(ea)                create_data(ea, FF_WORD, 2, BADADDR)
#define MakeDword(ea)               create_data(ea, FF_DWORD, 4, BADADDR)
#define MakeQword(ea)               create_data(ea, FF_QWORD, 8, BADADDR)
#define MakeOword(ea)               create_data(ea, FF_OWORD, 16, BADADDR)
#define MakeYword(ea)               create_data(ea, FF_YWORD, 32, BADADDR)
#define MakeFloat(ea)               create_data(ea, FF_FLOAT, 4, BADADDR)
#define MakeDouble(ea)              create_data(ea, FF_DOUBLE, 8, BADADDR)
#define MakePackReal(ea)            create_data(ea, FF_PACKREAL, 10, BADADDR)
#define MakeTbyte(ea)               create_data(ea, FF_TBYTE, 10, BADADDR)
#define MakeCustomData(ea, size, dtid, fid) create_data(ea, FF_CUSTOM, size, dtid|((fid)<<16))

#define SetReg(ea, reg, value)      split_sreg_range(ea, reg, value, SR_user)

#define form sprintf

#define GetLocalType(ordinal, flags) get_local_tinfo(ordinal).print(flags)
#define SetType(ea, type) apply_type(ea, type)
#define GetDisasm(ea) generate_disasm_line((ea), 0)
#define SetPrcsr(processor) set_processor_type(processor, SETPROC_USER)

// ----------------------------------------------------------------------------
#define SegByName(segname)               selector_by_name(segname)
#define MK_FP(seg, off)                  to_ea(seg, off)
#define toEA(seg, off)                   to_ea(seg, off)
#define MakeCode(ea)                     create_insn(ea)
#define MakeNameEx(ea, name, flags)      set_name(ea, name, flags)
#define MakeArray(ea, nitems)            make_array(ea, nitems)
#define MakeData(ea, flags, size, tid)   create_data(ea, flags, size, tid)
#define GetRegValue(name)                get_reg_value(name)
#define SetRegValue(value, name)         set_reg_value(value, name)
#define Byte(ea)                         get_wide_byte(ea)
#define Word(ea)                         get_wide_word(ea)
#define Dword(ea)                        get_wide_dword(ea)
#define Qword(ea)                        get_qword(ea)
#define LocByName(name)                  get_name_ea_simple(name)
#define ScreenEA()                       get_screen_ea()
#define Appcall                          dbg_appcall
#define CleanupAppcall()                 cleanup_appcall()
#define GetTinfo(ea)                     get_tinfo(ea)
#define OpChr(ea, n)                     op_chr(ea, n)
#define OpSeg(ea, n)                     op_seg(ea, n)
#define OpNumber(ea, n)                  op_num(ea, n)
#define OpDecimal(ea, n)                 op_dec(ea, n)
#define OpOctal(ea, n)                   op_oct(ea, n)
#define OpBinary(ea, n)                  op_bin(ea, n)
#define OpHex(ea, n)                     op_hex(ea, n)
#define OpAlt(ea, n, str)                op_man(ea, n, str)
#define OpSign(ea, n)                    toggle_sign(ea, n)
#define OpNot(ea, n)                     toggle_bnot(ea, n)
#define OpEnumEx(ea, n, enumid, serial)  op_enum(ea, n, enumid, serial)
#define OpStroffEx(ea, n, strid, delta)  op_stroff(ea, n, strid, delta)
#define OpStkvar(ea, n)                  op_stkvar(ea, n)
#define OpFloat(ea, n)                   op_flt(ea, n)
#define OpOffEx(ea, n, reftype, target, base, tdelta) \
        op_offset(ea, n, reftype, target, base, tdelta)
#define OpOff(ea, n, base)               op_plain_offset(ea, n, base)
#define MakeStructEx(ea, size, strname)  create_struct(ea, size, strname)
#define MakeStr(ea, endea)               create_strlit(ea, (endea) == BADADDR ? 0 : (endea-ea))
#define Jump(ea)                         jumpto(ea)
#define GenerateFile(type, file_handle, ea1, ea2, flags) \
        gen_file(type, file_handle, ea1, ea2, flags)
#define GenFuncGdl(outfile, title, ea1, ea2, flags) \
        gen_flow_graph(outfile, title, ea1, ea2, flags)
#define GenCallGdl(outfile, title, flags) \
        gen_simple_call_chart(outfile, title, flags)
#define IdbByte(ea)                      get_db_byte(ea)
#define DbgByte(ea)                      read_dbg_byte(ea)
#define DbgWord(ea)                      read_dbg_word(ea)
#define DbgDword(ea)                     read_dbg_dword(ea)
#define DbgQword(ea)                     read_dbg_qword(ea)
#define DbgRead(ea, size)                read_dbg_memory(ea, size)
#define DbgWrite(ea, data)               write_dbg_memory(ea, data)
#define GetManyBytes(ea, size, use_dbg)  get_bytes(ea, size, use_dbg)
#define PatchDbgByte(ea, value)          patch_dbg_byte(ea, value)
#define PatchByte(ea, value)             patch_byte(ea, value)
#define PatchWord(ea, value)             patch_word(ea, value)
#define PatchDword(ea, value)            patch_dword(ea, value)
#define PatchQword(ea, value)            patch_qword(ea, value)
#define SetProcessorType(processor, level) \
        set_processor_type(processor, level)
#define GetProcessorName()               get_processor_name()
#define SetTargetAssembler(asmidx)       set_target_assembler(asmidx)
#define Batch(mode)                      batch(mode)
#define SetSegDefReg(ea, reg, value)     set_default_sreg_value(ea, reg, value)
#define GetReg(ea, reg)                  get_sreg(ea, reg)
#define SetRegEx(ea, reg, value, tag)    split_sreg_range(ea, reg, value, tag)
#define AskStr(defval, prompt)           ask_str(defval, 0, prompt)
#define AskFile(for_saving, mask, prompt) ask_file(for_saving, mask, prompt)
#define AskAddr(defval, prompt)          ask_addr(defval, prompt)
#define AskLong(defval, prompt)          ask_long(defval, prompt)
#define AskSeg(defval, prompt)           ask_seg(defval, prompt)
#define AskIdent(defval, prompt)         ask_str(defval, HIST_IDENT, prompt)
#define AskYN(defval, prompt)            ask_yn(defval, prompt)
#define Warning                          warning
#define Fatal                            error
#define DeleteAll()                      delete_all_segments()
#define AddSegEx(startea, endea, sel, use32, align, comb, flags) \
        add_segm_ex(startea, endea, sel, use32, align, comb, flags)
#define SetSegBounds(ea, startea, endea, flags) \
        set_segment_bounds(ea, startea, endea, flags)
#define RenameSeg(ea, name)              set_segm_name(ea, name)
#define SetSegClass(ea, klass)           set_segm_class(ea, klass)
#define SetSegAddressing(ea, bitness)    set_segm_addressing(ea, bitness)
#define SetSegmentAttr(segea, attr, value) \
        set_segm_attr(segea, attr, value)
#define GetSegmentAttr(segea, attr)      get_segm_attr(segea, attr)
#define SetStorageType(startEA, endEA, stt) \
        set_storage_type(startEA, endEA, stt)
#define MoveSegm(ea, to, flags)          move_segm(ea, to, flags)
#define RebaseProgram(delta, flags)      rebase_program(delta, flags)
#define GetNsecStamp()                   get_nsec_stamp()
#define LocByNameEx(From, name)          get_name_ea(From, name)
#define SegByBase(base)                  get_segm_by_sel(base)
#define GetCurrentLine()                 get_curline()
#define SelStart()                       read_selection_start()
#define SelEnd()                         read_selection_end()
#define FirstSeg()                       get_first_seg()
#define NextSeg(ea)                      get_next_seg(ea)
#define SegName(ea)                      get_segm_name(ea)
#define CommentEx(ea, repeatable)        get_cmt(ea, repeatable)
#define AltOp(ea, n)                     get_forced_operand(ea, n)
#define GetDisasmEx(ea, flags)           generate_disasm_line(ea, flags)
#define GetMnem(ea)                      print_insn_mnem(ea)
#define GetOpType(ea, n)                 get_operand_type(ea, n)
#define GetOperandValue(ea, n)           get_operand_value(ea, n)
#define DecodeInstruction(ea)            decode_insn(ea)
#define NextAddr(ea)                     next_addr(ea)
#define PrevAddr(ea)                     prev_addr(ea)
#define NextHead(ea, maxea)              next_head(ea, maxea)
#define PrevHead(ea, minea)              prev_head(ea, minea)
#define NextNotTail(ea)                  next_not_tail(ea)
#define PrevNotTail(ea)                  prev_not_tail(ea)
#define ItemHead(ea)                     get_item_head(ea)
#define ItemEnd(ea)                      get_item_end(ea)
#define ItemSize(ea)                     get_item_size(ea)
#define AnalyzeRange(sEA, eEA)           plan_and_wait(sEA, eEA)
#define ExecIDC(input)                   exec_idc(input)
#define Eval(expr)                       eval(expr)
#define Exit(code)                       qexit(code)
#define SaveBase(idbname, flags)         save_database(idbname, flags)
#define Checkpoint(num)                  test_checkpoint(num)
#define GetTestId()                      get_test_id()
#define FindVoid(ea, flag)               find_suspop(ea, flag)
#define FindCode(ea, flag)               find_code(ea, flag)
#define FindData(ea, flag)               find_data(ea, flag)
#define FindUnexplored(ea, flag)         find_unknown(ea, flag)
#define FindExplored(ea, flag)           find_defined(ea, flag)
#define FindImmediate(ea, flag, value)   find_imm(ea, flag, value)
#define FindText(ea, flag, y, x, str)    find_text(ea, flag, y, x, str)
#define FindBinary(ea, flag, str)        find_binary(ea, flag, str)
#define AddCodeXref(From, To, flowtype)  add_cref(From, To, flowtype)
#define DelCodeXref(From, To, undef)     del_cref(From, To, undef)
#define Rfirst(From)                     get_first_cref_from(From)
#define RfirstB(To)                      get_first_cref_to(To)
#define Rnext(From, current)             get_next_cref_from(From, current)
#define RnextB(To, current)              get_next_cref_to(To, current)
#define Rfirst0(From)                    get_first_fcref_from(From)
#define RfirstB0(To)                     get_first_fcref_to(To)
#define Rnext0(From, current)            get_next_fcref_from(From, current)
#define RnextB0(To, current)             get_next_fcref_to(To, current)
#define Dfirst(From)                     get_first_dref_from(From)
#define Dnext(From, current)             get_next_dref_from(From, current)
#define DfirstB(To)                      get_first_dref_to(To)
#define DnextB(To, current)              get_next_dref_to(To, current)
#define XrefType()                       get_xref_type()
#define AutoUnmark(start, end, queuetype) \
        auto_unmark(start, end, queuetype)
#define AutoMark2(start, end, queuetype) \
        auto_mark_range(start, end, queuetype)
#define SetSelector(sel, value)          set_selector(sel, value)
#define AskSelector(sel)                 sel2para(sel)
#define ask_selector(sel)                sel2para(sel)
#define FindSelector(val)                find_selector(val)
#define DelSelector(sel)                 del_selector(sel)
#define MakeFunction(start, end)         add_func(start, end)
#define DelFunction(ea)                  del_func(ea)
#define SetFunctionEnd(ea, end)          set_func_end(ea, end)
#define NextFunction(ea)                 get_next_func(ea)
#define PrevFunction(ea)                 get_prev_func(ea)
#define GetFunctionAttr(ea, attr)        get_func_attr(ea, attr)
#define SetFunctionAttr(ea, attr, value) set_func_attr(ea, attr, value)
#define GetFunctionName(ea)              get_func_name(ea)
#define GetFunctionCmt(ea, repeatable)   get_func_cmt(ea, repeatable)
#define SetFunctionCmt(ea, cmt, repeatable) \
        set_func_cmt(ea, cmt, repeatable)
#define ChooseFunction(title)            choose_func(title)
#define GetFuncOffset(ea)                get_func_off_str(ea)
#define MakeLocal(start, end, location, name) \
        define_local_var(start, end, location, name)
#define FindFuncEnd(ea)                  find_func_end(ea)
#define GetFrameSize(ea)                 get_frame_size(ea)
#define MakeFrame(ea, lvsize, frregs, argsize) \
        set_frame_size(ea, lvsize, frregs, argsize)
#define GetSpd(ea)                       get_spd(ea)
#define GetSpDiff(ea)                    get_sp_delta(ea)
#define DelStkPnt(func_ea, ea)           del_stkpnt(func_ea, ea)
#define AddAutoStkPnt2(func_ea, ea, delta) \
        add_auto_stkpnt(func_ea, ea, delta)
#define RecalcSpd(cur_ea)                recalc_spd(cur_ea)
#define GetMinSpd(func_ea)               get_min_spd_ea(func_ea)
#define GetFchunkAttr(ea, attr)          get_fchunk_attr(ea, attr)
#define SetFchunkAttr(ea, attr, value)   set_fchunk_attr(ea, attr, value)
#define GetFchunkReferer(ea, idx)        get_fchunk_referer(ea, idx)
#define NextFchunk(ea)                   get_next_fchunk(ea)
#define PrevFchunk(ea)                   get_prev_fchunk(ea)
#define AppendFchunk(funcea, ea1, ea2)   append_func_tail(funcea, ea1, ea2)
#define RemoveFchunk(funcea, tailea)     remove_fchunk(funcea, tailea)
#define SetFchunkOwner(tailea, funcea)   set_tail_owner(tailea, funcea)
#define FirstFuncFchunk(funcea)          first_func_chunk(funcea)
#define NextFuncFchunk(funcea, tailea)   next_func_chunk(funcea, tailea)
#define GetEntryPointQty()               get_entry_qty()
#define AddEntryPoint(ordinal, ea, name, makecode) \
        add_entry(ordinal, ea, name, makecode)
#define GetEntryName(ordinal)            get_entry_name(ordinal)
#define GetEntryOrdinal(index)           get_entry_ordinal(index)
#define GetEntryPoint(ordinal)           get_entry(ordinal)
#define RenameEntryPoint(ordinal, name)  rename_entry(ordinal, name)
#define GetNextFixupEA(ea)               get_next_fixup_ea(ea)
#define GetPrevFixupEA(ea)               get_prev_fixup_ea(ea)
#define GetFixupTgtType(ea)              get_fixup_target_type(ea)
#define GetFixupTgtFlags(ea)             get_fixup_target_flags(ea)
#define GetFixupTgtSel(ea)               get_fixup_target_sel(ea)
#define GetFixupTgtOff(ea)               get_fixup_target_off(ea)
#define GetFixupTgtDispl(ea)             get_fixup_target_dis(ea)
#define SetFixup(ea, type, targetsel, targetoff, displ) \
        set_fixup(ea, type, targetsel, targetoff, displ)
#define DelFixup(ea)                     del_fixup(ea)
#define MarkPosition(ea, lnnum, x, y, slot, comment) \
        put_bookmark(ea, lnnum, x, y, slot, comment)
#define GetMarkedPos(slot)               get_bookmark(slot)
#define GetMarkComment(slot)             get_bookmark_desc(slot)
#define GetStrucQty()                    get_struc_qty()
#define GetFirstStrucIdx()               get_first_struc_idx()
#define GetLastStrucIdx()                get_last_struc_idx()
#define GetNextStrucIdx(index)           get_next_struc_idx(index)
#define GetPrevStrucIdx(index)           get_prev_struc_idx(index)
#define GetStrucIdx(id)                  get_struc_idx(id)
#define GetStrucId(index)                get_struc_by_idx(index)
#define GetStrucIdByName(name)           get_struc_id(name)
#define GetStrucName(id)                 get_struc_name(id)
#define GetStrucComment(id, repeatable)  get_struc_cmt(id, repeatable)
#define GetStrucSize(id)                 get_struc_size(id)
#define GetMemberQty(id)                 get_member_qty(id)
#define GetStrucPrevOff(id, offset)      get_prev_offset(id, offset)
#define GetStrucNextOff(id, offset)      get_next_offset(id, offset)
#define GetFirstMember(id)               get_first_member(id)
#define GetLastMember(id)                get_last_member(id)
#define GetMemberOffset(id, member_name) get_member_offset(id, member_name)
#define GetMemberName(id, member_offset) get_member_name(id, member_offset)
#define GetMemberComment(id, member_offset, repeatable) \
        get_member_cmt(id, member_offset, repeatable)
#define GetMemberSize(id, member_offset) get_member_size(id, member_offset)
#define GetMemberFlag(id, member_offset) get_member_flag(id, member_offset)
#define GetMemberStrId(id, member_offset) \
        get_member_strid(id, member_offset)
#define GetMemberId(id, member_offset)   get_member_id(id, member_offset)
#define AddStrucEx(index, name, is_union) \
        add_struc(index, name, is_union)
#define IsUnion(id)                      is_union(id)
#define DelStruc(id)                     del_struc(id)
#define SetStrucIdx(id, index)           set_struc_idx(id, index)
#define SetStrucName(id, name)           set_struc_name(id, name)
#define SetStrucComment(id, comment, repeatable) \
        set_struc_cmt(id, comment, repeatable)
#define SetStrucAlign(sid, shift)        set_struc_align(sid, shift)
#define AddStrucMember                   add_struc_member
#define DelStrucMember(id, member_offset) \
        del_struc_member(id, member_offset)
#define SetMemberName(id, member_offset, name) \
        set_member_name(id, member_offset, name)
#define SetMemberType                    set_member_type
#define SetMemberComment(id, member_offset, comment, repeatable) \
        set_member_cmt(id, member_offset, comment, repeatable)
#define ExpandStruc(id, offset, delta, recalc) \
        expand_struc(id, offset, delta, recalc)
#define GetVxdFuncName(vxdnum, fnnum)    get_vxd_func_name(vxdnum, fnnum)
#define SetLineNumber(ea, lnnum)         set_source_linnum(ea, lnnum)
#define GetLineNumber(ea)                get_source_linnum(ea)
#define DelLineNumber(ea)                del_source_linnum(ea)
#define AddSourceFile(ea1, uea2, filename) \
        add_sourcefile(ea1, uea2, filename)
#define GetSourceFile(ea)                get_sourcefile(ea)
#define DelSourceFile(ea)                del_sourcefile(ea)
#define CreateArray(name)                create_array(name)
#define GetArrayId(name)                 get_array_id(name)
#define RenameArray(id, newname)         rename_array(id, newname)
#define DeleteArray(id)                  delete_array(id)
#define SetArrayLong(id, idx, value)     set_array_long(id, idx, value)
#define SetArrayString(id, idx, str)     set_array_string(id, idx, str)
#define GetArrayElement(tag, id, idx)    get_array_element(tag, id, idx)
#define DelArrayElement(tag, id, idx)    del_array_element(tag, id, idx)
#define GetFirstIndex(tag, id)           get_first_index(tag, id)
#define GetNextIndex(tag, id, idx)       get_next_index(tag, id, idx)
#define GetLastIndex(tag, id)            get_last_index(tag, id)
#define GetPrevIndex(tag, id, idx)       get_prev_index(tag, id, idx)
#define SetHashLong(id, idx, value)      set_hash_long(id, idx, value)
#define SetHashString(id, idx, value)    set_hash_string(id, idx, value)
#define GetHashLong(id, idx)             get_hash_long(id, idx)
#define GetHashString(id, idx)           get_hash_string(id, idx)
#define DelHashElement(id, idx)          del_hash_string(id, idx)
#define GetFirstHashKey(id)              get_first_hash_key(id)
#define GetNextHashKey(id, idx)          get_next_hash_key(id, idx)
#define GetLastHashKey(id)               get_last_hash_key(id)
#define GetPrevHashKey(id, idx)          get_prev_hash_key(id, idx)
#define GetEnumQty()                     get_enum_qty()
#define GetnEnum(idx)                    getn_enum(idx)
#define GetEnumIdx(enum_id)              get_enum_idx(enum_id)
#define GetEnum(name)                    get_enum(name)
#define GetEnumName(enum_id)             get_enum_name(enum_id)
#define GetEnumCmt(enum_id, repeatable)  get_enum_cmt(enum_id, repeatable)
#define GetEnumSize(enum_id)             get_enum_size(enum_id)
#define GetEnumWidth(enum_id)            get_enum_width(enum_id)
#define GetEnumFlag(enum_id)             get_enum_flag(enum_id)
#define GetConstByName(name)             get_enum_member_by_name(name)
#define GetConstValue(const_id)          get_enum_member_value(const_id)
#define GetConstBmask(const_id)          get_enum_member_bmask(const_id)
#define GetConstEnum(const_id)           get_enum_member_enum(const_id)
#define GetConstEx(enum_id, value, serial, bmask) \
        get_enum_member(enum_id, value, serial, bmask)
#define GetFirstBmask(enum_id)           get_first_bmask(enum_id)
#define GetLastBmask(enum_id)            get_last_bmask(enum_id)
#define GetNextBmask(enum_id, value)     get_next_bmask(enum_id, value)
#define GetPrevBmask(enum_id, value)     get_prev_bmask(enum_id, value)
#define GetFirstConst(enum_id, bmask)    get_first_enum_member(enum_id, bmask)
#define GetLastConst(enum_id, bmask)     get_last_enum_member(enum_id, bmask)
#define GetNextConst(enum_id, value, bmask) \
        get_next_enum_member(enum_id, value, bmask)
#define GetPrevConst(enum_id, value, bmask) \
        get_prev_enum_member(enum_id, value, bmask)
#define GetConstName(const_id)           get_enum_member_name(const_id)
#define GetConstCmt(const_id, repeatable) \
        get_enum_member_cmt(const_id, repeatable)
#define AddEnum(idx, name, flag)         add_enum(idx, name, flag)
#define DelEnum(enum_id)                 del_enum(enum_id)
#define SetEnumIdx(enum_id, idx)         set_enum_idx(enum_id, idx)
#define SetEnumName(enum_id, name)       set_enum_name(enum_id, name)
#define SetEnumCmt(enum_id, cmt, repeatable) \
        set_enum_cmt(enum_id, cmt, repeatable)
#define SetEnumFlag(enum_id, flag)       set_enum_flag(enum_id, flag)
#define SetEnumWidth(enum_id, width)     set_enum_width(enum_id, width)
#define SetEnumBf(enum_id, flag)         set_enum_bf(enum_id, flag)
#define AddConstEx(enum_id, name, value, bmask) \
        add_enum_member(enum_id, name, value, bmask)
#define DelConstEx(enum_id, value, serial, bmask) \
        del_enum_member(enum_id, value, serial, bmask)
#define SetConstName(const_id, name)     set_enum_member_name(const_id, name)
#define SetConstCmt(const_id, cmt, repeatable) \
        set_enum_member_cmt(const_id, cmt, repeatable)
#define IsBitfield(enum_id)              is_bf(enum_id)
#define SetBmaskName(enum_id, bmask, name) \
        set_bmask_name(enum_id, bmask, name)
#define GetBmaskName(enum_id, bmask)     get_bmask_name(enum_id, bmask)
#define SetBmaskCmt(enum_id, bmask, cmt, repeatable) \
        set_bmask_cmt(enum_id, bmask, cmt, repeatable)
#define GetBmaskCmt(enum_id, bmask, repeatable) \
        get_bmask_cmt(enum_id, bmask, repeatable)
#define GetLongPrm(offset)               get_inf_attr(offset)
#define GetShortPrm(offset)              get_inf_attr(offset)
#define GetCharPrm(offset)               get_inf_attr(offset)
#define SetLongPrm(offset, value)        set_inf_attr(offset, value)
#define SetShortPrm(offset, value)       set_inf_attr(offset, value)
#define SetCharPrm(offset, value)        set_inf_attr(offset, value)
#define ChangeConfig(directive)          process_config_line(directive)
#define AddHotkey(hotkey, idcfunc)       add_idc_hotkey(hotkey, idcfunc)
#define DelHotkey(hotkey)                del_idc_hotkey(hotkey)
#define GetInputFile()                   get_root_filename()
#define GetInputFilePath()               get_input_file_path()
#define SetInputFilePath(path)           set_root_filename(path)
#define GetInputFileSize()               retrieve_input_file_size()
#define Exec(command)                    call_system(command)
#define ProcessUiAction(name, flags)     process_ui_action(name, flags)
#define Sleep(milliseconds)              qsleep(milliseconds)
#define GetIdaDirectory()                idadir()
#define GetIdbPath()                     get_idb_path()
#define GetInputMD5()                    retrieve_input_file_md5()
#define GetInputSHA256()                 retrieve_input_file_sha256()
#define DelUserInfo()                    del_user_info()
#define OpHigh(ea, n, target)            op_offset_high16(ea, n, target)
#define MakeAlign(ea, count, align)      create_align(ea, count, align)
#define Demangle(name, disable_mask)     demangle_name(name, disable_mask)
#define SetManualInsn(ea, insn)          set_manual_insn(ea, insn)
#define GetManualInsn(ea)                get_manual_insn(ea)
#define SetArrayFormat(ea, flags, litems, align) \
        set_array_params(ea, flags, litems, align)
#define LoadTil(name)                    add_default_til(name)
#define Til2Idb(idx, type_name)          import_type(idx, type_name)
#define GetMaxLocalType()                get_ordinal_qty()
#define SetLocalType(ordinal, input, flags) \
        set_local_type(ordinal, input, flags)
#define GetLocalTinfo(ordinal)           get_local_tinfo(ordinal)
#define GetLocalTypeName(ordinal)        get_numbered_type_name(ordinal)
#define PrintLocalTypes(ordinals, flags) print_decls(ordinals, flags)
#define SetStatus(status)                set_ida_state(status)
#define Refresh()                        refresh_idaview_anyway()
#define RefreshLists()                   refresh_choosers()
#define RunPlugin(name, arg)             load_and_run_plugin(name, arg)
#define ApplySig(name)                   plan_to_apply_idasgn(name)
#define GetStringType(ea)                get_str_type(ea)
#define GetString(ea, len, type)         get_strlit_contents(ea, len, type)
#define GetOriginalByte(ea)              get_original_byte(ea)
#define GetFpNum(ea, n)                  get_fpnum(ea, n)
#define HideRange(start, end, description, header, footer, color) \
        add_hidden_range(start, end, description, header, footer, color)
#define SetHiddenRange(ea, visible)      update_hidden_range(ea, visible)
#define DelHiddenRange(ea)               del_hidden_range(ea)
#define GetType(ea)                      get_type(ea)
#define GuessType(ea)                    guess_type(ea)
#define ApplyType(ea, type, flags)       apply_type(ea, type, flags)
#define ParseTypes(input, flags)         parse_decls(input, flags)
#define ParseType(input, flags)          parse_decl(input, flags)
#define GetColor(ea, what)               get_color(ea, what)
#define SetColor(ea, what, color)        set_color(ea, what, color)
#define GetBptQty()                      get_bpt_qty()
#define GetBptEA(n)                      get_bpt_ea(n)
#define GetBptAttr(ea, bptattr)          get_bpt_attr(ea, bptattr)
#define SetBptAttr(ea, bptattr, value)   set_bpt_attr(ea, bptattr, value)
#define SetBptCndEx(ea, cnd, is_lowcnd)  set_bpt_cond(ea, cnd, is_lowcnd)
#define SetBptCnd(ea, cnd)               set_bpt_cond(ea, cnd)
#define AddBptEx(ea, size, bpttype)      add_bpt(ea, size, bpttype)
#define AddBpt(ea)                       add_bpt(ea)
#define DelBpt(ea)                       del_bpt(ea)
#define EnableBpt(ea, enable)            enable_bpt(ea, enable)
#define CheckBpt(ea)                     check_bpt(ea)
#define LoadDebugger(dbgname, use_remote) \
        load_debugger(dbgname, use_remote)
#define StartDebugger(path, args, sdir)  start_process(path, args, sdir)
#define StopDebugger()                   exit_process()
#define PauseProcess()                   suspend_process()
#define GetProcessQty()                  get_processes().size
#define GetProcessPid(idx)               get_processes()[idx].pid
#define GetProcessName(idx)              get_processes()[idx].name
#define AttachProcess(pid, event_id)     attach_process(pid, event_id)
#define DetachProcess()                  detach_process()
#define GetThreadQty()                   get_thread_qty()
#define GetThreadId(idx)                 getn_thread(idx)
#define GetCurrentThreadId()             get_current_thread()
#define SelectThread(tid)                select_thread(tid)
#define SuspendThread(tid)               suspend_thread(tid)
#define ResumeThread(tid)                resume_thread(tid)
#define GetFirstModule()                 get_first_module()
#define GetNextModule(base)              get_next_module(base)
#define GetModuleName(base)              get_module_name(base)
#define GetModuleSize(base)              get_module_size(base)
#define StepInto()                       step_into()
#define StepOver()                       step_over()
#define RunTo(ea)                        run_to(ea)
#define StepUntilRet()                   step_until_ret()
#define GetDebuggerEvent(wfne, timeout)  wait_for_next_event(wfne, timeout)
#define GetProcessState()                get_process_state()
#define SetDebuggerOptions(opt)          set_debugger_options(opt)
#define SetRemoteDebugger(hostname, password, portnum) \
        set_remote_debugger(hostname, password, portnum)
#define GetDebuggerEventCondition()      get_debugger_event_cond()
#define SetDebuggerEventCondition(condition) \
        set_debugger_event_cond(condition)
#define GetEventId()                     get_event_id()
#define GetEventPid()                    get_event_pid()
#define GetEventTid()                    get_event_tid()
#define GetEventEa()                     get_event_ea()
#define IsEventHandled()                 is_event_handled()
#define GetEventModuleName()             get_event_module_name()
#define GetEventModuleBase()             get_event_module_base()
#define GetEventModuleSize()             get_event_module_size()
#define GetEventExitCode()               get_event_exit_code()
#define GetEventInfo()                   get_event_info()
#define GetEventBptHardwareEa()          get_event_bpt_hea()
#define GetEventExceptionCode()          get_event_exc_code()
#define GetEventExceptionEa()            get_event_exc_ea()
#define GetEventExceptionInfo()          get_event_exc_info()
#define CanExceptionContinue()           can_exc_continue()
#define RefreshDebuggerMemory()          refresh_debugger_memory()
#define TakeMemorySnapshot(only_loader_segs) \
        take_memory_snapshot(only_loader_segs)
#define EnableTracing(trace_level, enable) \
        enable_tracing(trace_level, enable)
#define GetStepTraceOptions()            get_step_trace_options()
#define SetStepTraceOptions(options)     set_step_trace_options(options)
#define GetExceptionQty()                get_exception_qty()
#define GetExceptionCode(idx)            get_exception_code(idx)
#define GetExceptionName(code)           get_exception_name(code)
#define GetExceptionFlags(code)          get_exception_flags(code)
#define DefineException(code, name, desc, flags) \
        define_exception(code, name, desc, flags)
#define SetExceptionFlags(code, flags)   set_exception_flags(code, flags)
#define ForgetException(code)            forget_exception(code)
#define IsString(var)                    value_is_string(var)
#define IsLong(var)                      value_is_long(var)
#define IsFloat(var)                     value_is_float(var)
#define IsObject(var)                    value_is_object(var)
#define IsFunc(var)                      value_is_func(var)
#define IsPvoid(var)                     value_is_pvoid(var)
#define IsInt64(var)                     value_is_int64(var)
#define GetCustomDataType(name)          find_custom_data_type(name)
#define GetCustomDataFormat(name)        find_custom_data_format(name)
#define BeginTypeUpdating(utp)           begin_type_updating(utp)
#define EndTypeUpdating(utp)             end_type_updating(utp)
#define FormatCData(outvec, value, type, options, info) \
        format_cdata(outvec, value, type, options, info)
#define ValidateNames()                  validate_idb_names()
#define GetFloat(ea)                     get_fpnum(ea, 4)
#define GetDouble(ea)                    get_fpnum(ea, 8)
#define SegStart(ea)                     get_segm_attr(ea, SEGATTR_START)
#define SegEnd(ea)                       get_segm_attr(ea, SEGATTR_END)
#define SegAlign(ea, alignment)          set_segm_attr(ea, SEGATTR_ALIGN, alignment)
#define SegComb(ea, comb)                set_segm_attr(ea, SEGATTR_COMB, comb)
#define SetSegmentType(ea, type)         set_segm_attr(ea, SEGATTR_TYPE, type)
#define AutoMark(ea, qtype)              auto_mark_range(ea, (ea)+1, qtype)

#define MakeComm(ea, cmt)                set_cmt(ea, cmt, 0)
#define MakeRptCmt(ea, cmt)              set_cmt(ea, cmt, 1)
#define MakeUnkn(ea, flags)              del_items(ea, flags)
#define MakeUnknown(ea, size, flags)     del_items(ea, flags, size)
#define LineA(ea, n)                     get_extra_cmt(ea, E_PREV + (n))
#define LineB(ea, n)                     get_extra_cmt(ea, E_NEXT + (n))
#define ExtLinA(ea, n, line)             update_extra_cmt(ea, E_PREV + (n), line)
#define ExtLinB(ea, n, line)             update_extra_cmt(ea, E_NEXT + (n), line)
#define DelExtLnA(ea, n)                 del_extra_cmt(ea, E_PREV + (n))
#define DelExtLnB(ea, n)                 del_extra_cmt(ea, E_NEXT + (n))
#define CompileEx(inp, isfile)           (isfile ? compile_idc_file(inp) : compile_idc_text(inp))
#define SetSpDiff(ea, delta)             add_user_stkpnt(ea, delta)
#define AddUserStkPnt(ea, delta)         add_user_stkpnt(ea, delta)
#define NameEx(From, ea)                 get_name(ea, GN_VISIBLE | calc_gtn_flags(From, ea))
#define GetTrueNameEx(From, ea)          get_name(ea, calc_gtn_flags(From, ea))
#define Message                          msg
#define UMessage                         msg
#define uprint                           print
#define DelSeg(ea, flags)                del_segm(ea, flags)
#define Wait()                           auto_wait()

#define LoadTraceFile(filename)              load_trace_file(filename)
#define SaveTraceFile(filename, description) save_trace_file(filename, description)
#define CheckTraceFile(filename)             is_valid_trace_file(filename)
#define DiffTraceFile(filename)              diff_trace_file(filename)
#define ClearTraceFile()                     clear_trace()
#define SetTraceDesc(filename, description)  get_trace_file_desc(filename, description)
#define GetTraceDesc(filename)               set_trace_file_desc(filename)
#define GetMaxTev()                          get_tev_qty()
#define GetTevEa(tev)                        get_tev_ea(tev)
#define GetTevType(tev)                      get_tev_type(tev)
#define GetTevTid(tev)                       get_tev_tid(tev)
#define GetTevRegVal(tev, reg)               get_tev_reg(tev, reg)
#define GetTevRegMemQty(tev)                 get_tev_mem_qty(tev)
#define GetTevRegMem(tev, idx)               get_tev_mem(tev, idx)
#define GetTevRegMemEa(tev, idx)             get_tev_mem_ea(tev, idx)
#define GetTevCallee(tev)                    get_call_tev_callee(tev)
#define GetTevReturn(tev)                    get_ret_tev_return(tev)
#define GetBptTevEa(tev)                     get_bpt_tev_ea(tev)

#define ArmForceBLJump(ea)              force_bl_jump(ea)
#define ArmForceBLCall(ea)              force_bl_call(ea)

#define StepBack()                      step_back()
#define SetCurrentTev(event)            set_current_tev(event)
#define GetCurrentTev()                 get_current_tev()

#define BochsCommand(cmd)               send_dbg_command(cmd)
#define SendGDBMonitor(cmd)             send_dbg_command(cmd)
#define WinDbgCommand(cmd)              send_dbg_command(cmd)

#define SetAppcallOptions(x)            set_inf_attr(INF_APPCALL_OPTIONS, x)
#define GetAppcallOptions()             get_inf_attr(INF_APPCALL_OPTIONS)

#define AF2_ANORET AF_ANORET
#define AF2_CHKUNI AF_CHKUNI
#define AF2_DATOFF AF_DATOFF
#define AF2_DOCODE AF_DOCODE
#define AF2_DODATA AF_DODATA
#define AF2_FTAIL AF_FTAIL
#define AF2_HFLIRT AF_HFLIRT
#define AF2_JUMPTBL AF_JUMPTBL
#define AF2_PURDAT AF_PURDAT
#define AF2_REGARG AF_REGARG
#define AF2_SIGCMT AF_SIGCMT
#define AF2_SIGMLT AF_SIGMLT
#define AF2_STKARG AF_STKARG
#define AF2_TRFUNC AF_TRFUNC
#define AF2_VERSP AF_VERSP
#define AF_ASCII AF_STRLIT
#define ASCF_AUTO STRF_AUTO
#define ASCF_COMMENT STRF_COMMENT
#define ASCF_GEN STRF_GEN
#define ASCF_SAVECASE STRF_SAVECASE
#define ASCF_SERIAL STRF_SERIAL

#define ASCSTR_C STRTYPE_C
#define ASCSTR_LEN2 STRTYPE_LEN2
#define ASCSTR_LEN4 STRTYPE_LEN4
#define ASCSTR_PASCAL STRTYPE_PASCAL
#define ASCSTR_TERMCHR STRTYPE_TERMCHR
#define ASCSTR_ULEN2 STRTYPE_LEN2_16
#define ASCSTR_ULEN4 STRTYPE_LEN4_16
#define ASCSTR_UNICODE STRTYPE_C_16

#define BeginEA StartEA
#define DOUNK_SIMPLE DELIT_SIMPLE
#define DOUNK_EXPAND DELIT_EXPAND
#define DOUNK_DELNAMES DELIT_DELNAMES
#define DelHiddenArea DelHiddenRange

#define FF_ASCI FF_STRLIT
#define FF_DWRD FF_DWORD
#define FF_OWRD FF_OWORD
#define FF_QWRD FF_QWORD
#define FF_STRU FF_STRUCT
#define FF_TBYT FF_TBYTE
#define FF_VAR 0x00080000 // do not use!

#define FIXUP_BYTE FIXUP_OFF8
#define FIXUP_CREATED FIXUPF_CREATED
#define FIXUP_EXTDEF FIXUPF_EXTDEF
#define FIXUP_REL FIXUPF_REL
#define FIXUP_SELFREL 0
#define FIXUP_UNUSED FIXUPF_UNUSED

#define GetFlags get_full_flags
#define HideArea HideRange
#define ResumeProcess resume_process

#define isEnabled(ea) is_mapped(ea)

#define hasValue(F) has_value(F)
#define isByte(F) is_byte(F)
#define isWord(F) is_word(F)
#define isDwrd(F) is_dword(F)
#define isQwrd(F) is_qword(F)
#define isOwrd(F) is_oword(F)
#define isTbyt(F) is_tbyte(F)
#define isFloat(F) is_float(F)
#define isDouble(F) is_double(F)
#define is_pack_real(F) is_pack_real(F)
#define isASCII(F) is_strlit(F)
#define isStruct(F) is_struct(F)
#define isAlign(F) is_align(F)

#define isChar0(F) is_char0(F)
#define isChar1(F) is_char1(F)
#define isCode(F) is_code(F)
#define isData(F) is_data(F)
#define isDefArg0(F) is_defarg0(F)
#define isDefArg1(F) is_defarg1(F)
#define isEnum0(F) is_enum0(F)
#define isEnum1(F) is_enum1(F)
#define isFlow(F) is_flow(F)
#define isHead(F) is_head(F)
#define isLoaded(F) is_loaded(F)
#define isOff0(F) is_off0(F)
#define isOff1(F) is_off1(F)
#define isPackReal(F) is_pack_real(F)
#define isSeg0(F) is_seg0(F)
#define isSeg1(F) is_seg1(F)
#define isStkvar0(F) is_stkvar0(F)
#define isStkvar1(F) is_stkvar1(F)
#define isStroff0(F) is_stroff0(F)
#define isStroff1(F) is_stroff1(F)
#define isTail(F) is_tail(F)
#define isUnknown(F) is_unknown(F)

#define SEGDEL_KEEP SEGMOD_KEEP
#define SEGDEL_PERM SEGMOD_KILL
#define SEGDEL_SILENT SEGMOD_SILENT

#define SETPROC_ALL SETPROC_LOADER_NON_FATAL
#define SETPROC_COMPAT SETPROC_IDB
#define SETPROC_FATAL SETPROC_LOADER

#define INF_CHANGE_COUNTER INF_DATABASE_CHANGE_COUNT
#define INF_LOW_OFF INF_LOWOFF
#define INF_HIGH_OFF INF_HIGHOFF
#define INF_START_PRIVRANGE INF_PRIVRANGE_START_EA
#define INF_END_PRIVRANGE INF_PRIVRANGE_END_EA
#define INF_TYPE_XREFS INF_TYPE_XREFNUM
#define INF_REFCMTS INF_REFCMTNUM
#define INF_XREFS INF_XREFFLAG
#define INF_NAMELEN INF_MAX_AUTONAME_LEN
#define INF_SHORT_DN INF_SHORT_DEMNAMES
#define INF_LONG_DN INF_LONG_DEMNAMES
#define INF_CMTFLAG INF_CMTFLG
#define INF_BORDER INF_LIMITER
#define INF_BINPREF INF_BIN_PREFIX_SIZE
#define INF_COMPILER INF_CC_ID
#define INF_MODEL INF_CC_CM
#define INF_SIZEOF_INT INF_CC_SIZE_I
#define INF_SIZEOF_BOOL INF_CC_SIZE_B
#define INF_SIZEOF_ENUM INF_CC_SIZE_E
#define INF_SIZEOF_ALGN INF_CC_DEFALIGN
#define INF_SIZEOF_SHORT INF_CC_SIZE_S
#define INF_SIZEOF_LONG INF_CC_SIZE_L
#define INF_SIZEOF_LLONG INF_CC_SIZE_LL
#define INF_SIZEOF_LDBL INF_CC_SIZE_LDBL
#define INF_COMMENT INF_CMT_INDENT

#define REF_VHIGH V695_REF_VHIGH
#define REF_VLOW  V695_REF_VLOW

#define GetOpnd(ea, n) print_operand(ea, n)
#define patch_long(ea, value) patch_dword(ea, value)
#define process_config_line(directive) process_config_directive(directive)

// convenience macro to turn python on
#define python_on() load_and_run_plugin("idapython", 3)

#define RunPythonStatement(stmt) exec_python(stmt)

#define SW_RPTCMT SCF_RPTCMT
#define SW_ALLCMT SCF_ALLCMT
#define SW_NOCMT  SCF_NOCMT
#define SW_LINNUM SCF_LINNUM

#endif // _IDC_IDC
