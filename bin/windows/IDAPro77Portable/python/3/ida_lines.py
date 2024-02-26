"""
High level functions that deal with the generation of the disassembled text
lines.

This file also contains definitions for the syntax highlighting.

Finally there are functions that deal with anterior/posterior user-defined
lines."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_lines
else:
    import _ida_lines

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

SWIG_PYTHON_LEGACY_BOOL = _ida_lines.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

COLOR_ON = _ida_lines.COLOR_ON
r"""
Escape character (ON). Followed by a color code (color_t).
"""

COLOR_OFF = _ida_lines.COLOR_OFF
r"""
Escape character (OFF). Followed by a color code (color_t).
"""

COLOR_ESC = _ida_lines.COLOR_ESC
r"""
Escape character (Quote next character). This is needed to output '\1' and '\2'
characters.
"""

COLOR_INV = _ida_lines.COLOR_INV
r"""
Escape character (Inverse foreground and background colors). This escape
character has no corresponding COLOR_OFF. Its action continues until the next
COLOR_INV or end of line.
"""

SCOLOR_ON = _ida_lines.SCOLOR_ON
r"""
Escape character (ON)
"""

SCOLOR_OFF = _ida_lines.SCOLOR_OFF
r"""
Escape character (OFF)
"""

SCOLOR_ESC = _ida_lines.SCOLOR_ESC
r"""
Escape character (Quote next character)
"""

SCOLOR_INV = _ida_lines.SCOLOR_INV
r"""
Escape character (Inverse colors)
"""

SCOLOR_DEFAULT = _ida_lines.SCOLOR_DEFAULT
r"""
Default.
"""

SCOLOR_REGCMT = _ida_lines.SCOLOR_REGCMT
r"""
Regular comment.
"""

SCOLOR_RPTCMT = _ida_lines.SCOLOR_RPTCMT
r"""
Repeatable comment (defined not here)
"""

SCOLOR_AUTOCMT = _ida_lines.SCOLOR_AUTOCMT
r"""
Automatic comment.
"""

SCOLOR_INSN = _ida_lines.SCOLOR_INSN
r"""
Instruction.
"""

SCOLOR_DATNAME = _ida_lines.SCOLOR_DATNAME
r"""
Dummy Data Name.
"""

SCOLOR_DNAME = _ida_lines.SCOLOR_DNAME
r"""
Regular Data Name.
"""

SCOLOR_DEMNAME = _ida_lines.SCOLOR_DEMNAME
r"""
Demangled Name.
"""

SCOLOR_SYMBOL = _ida_lines.SCOLOR_SYMBOL
r"""
Punctuation.
"""

SCOLOR_CHAR = _ida_lines.SCOLOR_CHAR
r"""
Char constant in instruction.
"""

SCOLOR_STRING = _ida_lines.SCOLOR_STRING
r"""
String constant in instruction.
"""

SCOLOR_NUMBER = _ida_lines.SCOLOR_NUMBER
r"""
Numeric constant in instruction.
"""

SCOLOR_VOIDOP = _ida_lines.SCOLOR_VOIDOP
r"""
Void operand.
"""

SCOLOR_CREF = _ida_lines.SCOLOR_CREF
r"""
Code reference.
"""

SCOLOR_DREF = _ida_lines.SCOLOR_DREF
r"""
Data reference.
"""

SCOLOR_CREFTAIL = _ida_lines.SCOLOR_CREFTAIL
r"""
Code reference to tail byte.
"""

SCOLOR_DREFTAIL = _ida_lines.SCOLOR_DREFTAIL
r"""
Data reference to tail byte.
"""

SCOLOR_ERROR = _ida_lines.SCOLOR_ERROR
r"""
Error or problem.
"""

SCOLOR_PREFIX = _ida_lines.SCOLOR_PREFIX
r"""
Line prefix.
"""

SCOLOR_BINPREF = _ida_lines.SCOLOR_BINPREF
r"""
Binary line prefix bytes.
"""

SCOLOR_EXTRA = _ida_lines.SCOLOR_EXTRA
r"""
Extra line.
"""

SCOLOR_ALTOP = _ida_lines.SCOLOR_ALTOP
r"""
Alternative operand.
"""

SCOLOR_HIDNAME = _ida_lines.SCOLOR_HIDNAME
r"""
Hidden name.
"""

SCOLOR_LIBNAME = _ida_lines.SCOLOR_LIBNAME
r"""
Library function name.
"""

SCOLOR_LOCNAME = _ida_lines.SCOLOR_LOCNAME
r"""
Local variable name.
"""

SCOLOR_CODNAME = _ida_lines.SCOLOR_CODNAME
r"""
Dummy code name.
"""

SCOLOR_ASMDIR = _ida_lines.SCOLOR_ASMDIR
r"""
Assembler directive.
"""

SCOLOR_MACRO = _ida_lines.SCOLOR_MACRO
r"""
Macro.
"""

SCOLOR_DSTR = _ida_lines.SCOLOR_DSTR
r"""
String constant in data directive.
"""

SCOLOR_DCHAR = _ida_lines.SCOLOR_DCHAR
r"""
Char constant in data directive.
"""

SCOLOR_DNUM = _ida_lines.SCOLOR_DNUM
r"""
Numeric constant in data directive.
"""

SCOLOR_KEYWORD = _ida_lines.SCOLOR_KEYWORD
r"""
Keywords.
"""

SCOLOR_REG = _ida_lines.SCOLOR_REG
r"""
Register name.
"""

SCOLOR_IMPNAME = _ida_lines.SCOLOR_IMPNAME
r"""
Imported name.
"""

SCOLOR_SEGNAME = _ida_lines.SCOLOR_SEGNAME
r"""
Segment name.
"""

SCOLOR_UNKNAME = _ida_lines.SCOLOR_UNKNAME
r"""
Dummy unknown name.
"""

SCOLOR_CNAME = _ida_lines.SCOLOR_CNAME
r"""
Regular code name.
"""

SCOLOR_UNAME = _ida_lines.SCOLOR_UNAME
r"""
Regular unknown name.
"""

SCOLOR_COLLAPSED = _ida_lines.SCOLOR_COLLAPSED
r"""
Collapsed line.
"""

SCOLOR_ADDR = _ida_lines.SCOLOR_ADDR
r"""
Hidden address mark.
"""

COLOR_SELECTED = _ida_lines.COLOR_SELECTED
r"""
Selected.
"""

COLOR_LIBFUNC = _ida_lines.COLOR_LIBFUNC
r"""
Library function.
"""

COLOR_REGFUNC = _ida_lines.COLOR_REGFUNC
r"""
Regular function.
"""

COLOR_CODE = _ida_lines.COLOR_CODE
r"""
Single instruction.
"""

COLOR_DATA = _ida_lines.COLOR_DATA
r"""
Data bytes.
"""

COLOR_UNKNOWN = _ida_lines.COLOR_UNKNOWN
r"""
Unexplored byte.
"""

COLOR_EXTERN = _ida_lines.COLOR_EXTERN
r"""
External name definition segment.
"""

COLOR_CURITEM = _ida_lines.COLOR_CURITEM
r"""
Current item.
"""

COLOR_CURLINE = _ida_lines.COLOR_CURLINE
r"""
Current line.
"""

COLOR_HIDLINE = _ida_lines.COLOR_HIDLINE
r"""
Hidden line.
"""

COLOR_LUMFUNC = _ida_lines.COLOR_LUMFUNC
r"""
Lumina function.
"""

COLOR_BG_MAX = _ida_lines.COLOR_BG_MAX
r"""
Max color number.
"""


def tag_strlen(*args) -> "ssize_t":
    r"""
    tag_strlen(line) -> ssize_t
    Calculate length of a colored string This function computes the length in
    unicode codepoints of a line

    @param line: (C++: const char *) char const *
    @return: the number of codepoints in the line, or -1 on error
    """
    return _ida_lines.tag_strlen(*args)

def calc_prefix_color(*args) -> "color_t":
    r"""
    calc_prefix_color(ea) -> color_t
    Get prefix color for line at 'ea'

    @param ea: (C++: ea_t)
    @return: Line prefix colors
    """
    return _ida_lines.calc_prefix_color(*args)

def calc_bg_color(*args) -> "bgcolor_t":
    r"""
    calc_bg_color(ea) -> bgcolor_t
    Get background color for line at 'ea'

    @param ea: (C++: ea_t)
    @return: RGB color
    """
    return _ida_lines.calc_bg_color(*args)

def add_sourcefile(*args) -> "bool":
    r"""
    add_sourcefile(ea1, ea2, filename) -> bool
    Mark a range of address as belonging to a source file. An address range may
    belong only to one source file. A source file may be represented by several
    address ranges.

    @param ea1: (C++: ea_t) linear address of start of the address range
    @param ea2: (C++: ea_t) linear address of end of the address range (excluded)
    @param filename: (C++: const char *) name of source file.
    @return: success
    """
    return _ida_lines.add_sourcefile(*args)

def get_sourcefile(*args) -> "char const *":
    r"""
    get_sourcefile(ea, bounds=None) -> char const *
    Get name of source file occupying the given address.

    @param ea: (C++: ea_t) linear address
    @param bounds: (C++: range_t *) pointer to the output buffer with the address range for the
                   current file. May be nullptr.
    @return: nullptr if source file information is not found, otherwise returns
             pointer to file name
    """
    return _ida_lines.get_sourcefile(*args)

def del_sourcefile(*args) -> "bool":
    r"""
    del_sourcefile(ea) -> bool
    Delete information about the source file.

    @param ea: (C++: ea_t) linear address
    @return: success
    """
    return _ida_lines.del_sourcefile(*args)

def install_user_defined_prefix(*args) -> "bool":
    r"""
    install_user_defined_prefix(prefix_len, udp, owner) -> bool
    User-defined line-prefixes are displayed just after the autogenerated line
    prefixes in the disassembly listing. There is no need to call this function
    explicitly. Use the user_defined_prefix_t class.

    @param prefix_len: (C++: size_t) prefixed length. if 0, then uninstall UDP
    @param udp: (C++: struct user_defined_prefix_t *) object to generate user-defined prefix
    @param owner: (C++: const void *) pointer to the plugin_t that owns UDP if non-nullptr, then the
                  object will be uninstalled and destroyed when the plugin gets
                  unloaded
    """
    return _ida_lines.install_user_defined_prefix(*args)
class user_defined_prefix_t(object):
    r"""
    Proxy of C++ user_defined_prefix_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, prefix_len, owner) -> user_defined_prefix_t

        @param prefix_len: size_t
        @param owner: void const *
        """
        if self.__class__ == user_defined_prefix_t:
            _self = None
        else:
            _self = self
        _ida_lines.user_defined_prefix_t_swiginit(self, _ida_lines.new_user_defined_prefix_t(_self, *args))
    __swig_destroy__ = _ida_lines.delete_user_defined_prefix_t

    def get_user_defined_prefix(self, *args) -> "void":
        r"""
        get_user_defined_prefix(self, ea, insn, lnnum, indent, line)
        This callback must be overridden by the derived class.

        @param ea: (C++: ea_t) the current address
        @param insn: (C++: const class insn_t &) the current instruction. if the current item is not an instruction,
                     then insn.itype is zero.
        @param insn: (C++: const class insn_t &) the current instruction. if the current item is not an instruction,
                     then insn.itype is zero.
        @param indent: (C++: int) see explanations for gen_printf()
        @param line: (C++: const char *) the line to be generated. the line usually contains color tags.
                     this argument can be examined to decide whether to generate the
                     prefix.
        """
        return _ida_lines.user_defined_prefix_t_get_user_defined_prefix(self, *args)
    def __disown__(self):
        self.this.disown()
        _ida_lines.disown_user_defined_prefix_t(self)
        return weakref.proxy(self)

# Register user_defined_prefix_t in _ida_lines:
_ida_lines.user_defined_prefix_t_swigregister(user_defined_prefix_t)
cvar = _ida_lines.cvar
COLOR_DEFAULT = cvar.COLOR_DEFAULT
r"""
Default.
"""
COLOR_REGCMT = cvar.COLOR_REGCMT
r"""
Regular comment.
"""
COLOR_RPTCMT = cvar.COLOR_RPTCMT
r"""
Repeatable comment (comment defined somewhere else)
"""
COLOR_AUTOCMT = cvar.COLOR_AUTOCMT
r"""
Automatic comment.
"""
COLOR_INSN = cvar.COLOR_INSN
r"""
Instruction.
"""
COLOR_DATNAME = cvar.COLOR_DATNAME
r"""
Dummy Data Name.
"""
COLOR_DNAME = cvar.COLOR_DNAME
r"""
Regular Data Name.
"""
COLOR_DEMNAME = cvar.COLOR_DEMNAME
r"""
Demangled Name.
"""
COLOR_SYMBOL = cvar.COLOR_SYMBOL
r"""
Punctuation.
"""
COLOR_CHAR = cvar.COLOR_CHAR
r"""
Char constant in instruction.
"""
COLOR_STRING = cvar.COLOR_STRING
r"""
String constant in instruction.
"""
COLOR_NUMBER = cvar.COLOR_NUMBER
r"""
Numeric constant in instruction.
"""
COLOR_VOIDOP = cvar.COLOR_VOIDOP
r"""
Void operand.
"""
COLOR_CREF = cvar.COLOR_CREF
r"""
Code reference.
"""
COLOR_DREF = cvar.COLOR_DREF
r"""
Data reference.
"""
COLOR_CREFTAIL = cvar.COLOR_CREFTAIL
r"""
Code reference to tail byte.
"""
COLOR_DREFTAIL = cvar.COLOR_DREFTAIL
r"""
Data reference to tail byte.
"""
COLOR_ERROR = cvar.COLOR_ERROR
r"""
Error or problem.
"""
COLOR_PREFIX = cvar.COLOR_PREFIX
r"""
Line prefix.
"""
COLOR_BINPREF = cvar.COLOR_BINPREF
r"""
Binary line prefix bytes.
"""
COLOR_EXTRA = cvar.COLOR_EXTRA
r"""
Extra line.
"""
COLOR_ALTOP = cvar.COLOR_ALTOP
r"""
Alternative operand.
"""
COLOR_HIDNAME = cvar.COLOR_HIDNAME
r"""
Hidden name.
"""
COLOR_LIBNAME = cvar.COLOR_LIBNAME
r"""
Library function name.
"""
COLOR_LOCNAME = cvar.COLOR_LOCNAME
r"""
Local variable name.
"""
COLOR_CODNAME = cvar.COLOR_CODNAME
r"""
Dummy code name.
"""
COLOR_ASMDIR = cvar.COLOR_ASMDIR
r"""
Assembler directive.
"""
COLOR_MACRO = cvar.COLOR_MACRO
r"""
Macro.
"""
COLOR_DSTR = cvar.COLOR_DSTR
r"""
String constant in data directive.
"""
COLOR_DCHAR = cvar.COLOR_DCHAR
r"""
Char constant in data directive.
"""
COLOR_DNUM = cvar.COLOR_DNUM
r"""
Numeric constant in data directive.
"""
COLOR_KEYWORD = cvar.COLOR_KEYWORD
r"""
Keywords.
"""
COLOR_REG = cvar.COLOR_REG
r"""
Register name.
"""
COLOR_IMPNAME = cvar.COLOR_IMPNAME
r"""
Imported name.
"""
COLOR_SEGNAME = cvar.COLOR_SEGNAME
r"""
Segment name.
"""
COLOR_UNKNAME = cvar.COLOR_UNKNAME
r"""
Dummy unknown name.
"""
COLOR_CNAME = cvar.COLOR_CNAME
r"""
Regular code name.
"""
COLOR_UNAME = cvar.COLOR_UNAME
r"""
Regular unknown name.
"""
COLOR_COLLAPSED = cvar.COLOR_COLLAPSED
r"""
Collapsed line.
"""
COLOR_FG_MAX = cvar.COLOR_FG_MAX
r"""
Max color number.
"""
COLOR_ADDR = cvar.COLOR_ADDR
r"""
hidden address marks. the address is represented as 8digit hex number: 01234567.
it doesn't have COLOR_OFF pair. NB: for 64-bit IDA, the address is 16digit.
"""
COLOR_OPND1 = cvar.COLOR_OPND1
r"""
Instruction operand 1.
"""
COLOR_OPND2 = cvar.COLOR_OPND2
r"""
Instruction operand 2.
"""
COLOR_OPND3 = cvar.COLOR_OPND3
r"""
Instruction operand 3.
"""
COLOR_OPND4 = cvar.COLOR_OPND4
r"""
Instruction operand 4.
"""
COLOR_OPND5 = cvar.COLOR_OPND5
r"""
Instruction operand 5.
"""
COLOR_OPND6 = cvar.COLOR_OPND6
r"""
Instruction operand 6.
"""
COLOR_OPND7 = cvar.COLOR_OPND7
r"""
Instruction operand 7.
"""
COLOR_OPND8 = cvar.COLOR_OPND8
r"""
Instruction operand 8.
"""
COLOR_RESERVED1 = cvar.COLOR_RESERVED1
r"""
This tag is reserved for internal IDA use.
"""
COLOR_LUMINA = cvar.COLOR_LUMINA
r"""
Lumina-related, only for the navigation band.
"""

VEL_POST = _ida_lines.VEL_POST

VEL_CMT = _ida_lines.VEL_CMT


def add_extra_line(*args) -> "bool":
    r"""
    add_extra_line(ea, isprev, format) -> bool
    Add anterior/posterior non-comment line(s).

    @param ea: (C++: ea_t) linear address
    @param isprev: (C++: bool) do we add anterior lines? (0-no, posterior)
    @param format: (C++: const char *) printf() style format string. may contain \n to denote new lines.
    @return: true if success
    """
    return _ida_lines.add_extra_line(*args)

def add_extra_cmt(*args) -> "bool":
    r"""
    add_extra_cmt(ea, isprev, format) -> bool
    Add anterior/posterior comment line(s).

    @param ea: (C++: ea_t) linear address
    @param isprev: (C++: bool) do we add anterior lines? (0-no, posterior)
    @param format: (C++: const char *) printf() style format string. may contain \n to denote new lines.
                   The resulting string should not contain comment characters (;),
                   the kernel will add them automatically.
    @return: true if success
    """
    return _ida_lines.add_extra_cmt(*args)

def add_pgm_cmt(*args) -> "bool":
    r"""
    add_pgm_cmt(format) -> bool
    Add anterior comment line(s) at the start of program.

    @param format: (C++: const char *) printf() style format string. may contain \n to denote new lines.
                   The resulting string should not contain comment characters (;),
                   the kernel will add them automatically.
    @return: true if success
    """
    return _ida_lines.add_pgm_cmt(*args)

def generate_disasm_line(*args) -> "qstring *":
    r"""
    generate_disasm_line(ea, flags=0) -> str

    @param ea: ea_t
    @param flags: int
    """
    return _ida_lines.generate_disasm_line(*args)
GENDSM_FORCE_CODE = _ida_lines.GENDSM_FORCE_CODE

GENDSM_MULTI_LINE = _ida_lines.GENDSM_MULTI_LINE

GENDSM_REMOVE_TAGS = _ida_lines.GENDSM_REMOVE_TAGS


def get_first_free_extra_cmtidx(*args) -> "int":
    r"""
    get_first_free_extra_cmtidx(ea, start) -> int

    @param ea: ea_t
    @param start: int
    """
    return _ida_lines.get_first_free_extra_cmtidx(*args)

def update_extra_cmt(*args) -> "void":
    r"""
    update_extra_cmt(ea, what, str)

    @param ea: ea_t
    @param what: int
    @param str: char const *
    """
    return _ida_lines.update_extra_cmt(*args)

def del_extra_cmt(*args) -> "void":
    r"""
    del_extra_cmt(ea, what)

    @param ea: ea_t
    @param what: int
    """
    return _ida_lines.del_extra_cmt(*args)

def get_extra_cmt(*args) -> "int":
    r"""
    get_extra_cmt(ea, what) -> ssize_t

    @param ea: ea_t
    @param what: int
    """
    return _ida_lines.get_extra_cmt(*args)

def delete_extra_cmts(*args) -> "void":
    r"""
    delete_extra_cmts(ea, what)

    @param ea: ea_t
    @param what: int
    """
    return _ida_lines.delete_extra_cmts(*args)

def create_encoding_helper(*args) -> "encoder_t *":
    r"""
    create_encoding_helper(encidx=-1, nr=nr_once) -> encoder_t *

    @param encidx: int
    @param nr: enum encoder_t::notify_recerr_t
    """
    return _ida_lines.create_encoding_helper(*args)

def tag_remove(*args) -> "PyObject *":
    r"""
    tag_remove(nonnul_instr) -> str

    @param nonnul_instr: char const *
    """
    return _ida_lines.tag_remove(*args)

def set_user_defined_prefix(*args) -> "PyObject *":
    r"""
    set_user_defined_prefix(width, pycb) -> bool
    Deprecated. Please use install_user_defined_prefix() instead

    @param width: size_t
    @param pycb: PyObject *
    """
    return _ida_lines.set_user_defined_prefix(*args)

def tag_addr(*args) -> "PyObject *":
    r"""
    tag_addr(ea) -> PyObject *
    Insert an address mark into a string.

    @param ea: (C++: ea_t) address to include
    """
    return _ida_lines.tag_addr(*args)

def tag_skipcode(*args) -> "int":
    r"""
    tag_skipcode(line) -> int
    Skip one color code. This function should be used if you are interested in color
    codes and want to analyze all of them. Otherwise tag_skipcodes() function is
    better since it will skip all colors at once. This function will skip the
    current color code if there is one. If the current symbol is not a color code,
    it will return the input.

    @param line: (C++: const char *) char const *
    @return: moved pointer
    """
    return _ida_lines.tag_skipcode(*args)

def tag_skipcodes(*args) -> "int":
    r"""
    tag_skipcodes(line) -> int
    Move the pointer past all color codes.

    @param line: (C++: const char *) can't be nullptr
    @return: moved pointer, can't be nullptr
    """
    return _ida_lines.tag_skipcodes(*args)

def tag_advance(*args) -> "int":
    r"""
    tag_advance(line, cnt) -> int
    Move pointer to a 'line' to 'cnt' positions right. Take into account escape
    sequences.

    @param line: (C++: const char *) pointer to string
    @param cnt: (C++: int) number of positions to move right
    @return: moved pointer
    """
    return _ida_lines.tag_advance(*args)

def generate_disassembly(*args) -> "PyObject *":
    r"""
    generate_disassembly(ea, max_lines, as_stack, notags) -> (int, [str, ...])
    Generate disassembly lines (many lines) and put them into a buffer

    @param ea: address to generate disassembly for
    @param max_lines: how many lines max to generate
    @param as_stack: Display undefined items as 2/4/8 bytes
    @param notags: bool
    @return:     - None on failure
        - tuple(most_important_line_number, list(lines)) : Returns a tuple containing
          the most important line number and a list of generated lines
    """
    return _ida_lines.generate_disassembly(*args)

#<pycode(py_lines)>
import _ida_idaapi
import _ida_lines

# ---------------- Color escape sequence defitions -------------------------
COLOR_ADDR_SIZE = 16 if _ida_idaapi.BADADDR == 0xFFFFFFFFFFFFFFFF else 8
r"""
Size of a tagged address (see COLOR_ADDR)
"""
SCOLOR_FG_MAX   = '\x28'             #  Max color number
cvar = _ida_lines.cvar
SCOLOR_OPND1    = chr(cvar.COLOR_ADDR+1)  #  Instruction operand 1
SCOLOR_OPND2    = chr(cvar.COLOR_ADDR+2)  #  Instruction operand 2
SCOLOR_OPND3    = chr(cvar.COLOR_ADDR+3)  #  Instruction operand 3
SCOLOR_OPND4    = chr(cvar.COLOR_ADDR+4)  #  Instruction operand 4
SCOLOR_OPND5    = chr(cvar.COLOR_ADDR+5)  #  Instruction operand 5
SCOLOR_OPND6    = chr(cvar.COLOR_ADDR+6)  #  Instruction operand 6
SCOLOR_UTF8     = chr(cvar.COLOR_ADDR+10) #  Following text is UTF-8 encoded

# ---------------- Line prefix colors --------------------------------------
PALETTE_SIZE   =  (cvar.COLOR_FG_MAX+_ida_lines.COLOR_BG_MAX)

def requires_color_esc(c):
    r"""
    Checks if the given character requires escaping
    Is the given char a color escape character?
    """
    t = ord(c[0])
    return c >= COLOR_ON and c <= COLOR_INV

def COLSTR(str, tag):
    r"""
    Utility function to create a colored line
    @param str: The string
    @param tag: Color tag constant. One of SCOLOR_XXXX
    """
    return SCOLOR_ON + tag + str + SCOLOR_OFF + tag

#</pycode(py_lines)>


E_PREV = cvar.E_PREV
E_NEXT = cvar.E_NEXT


