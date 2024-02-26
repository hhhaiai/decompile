"""
Contains definition of the interface to IDP modules.

The interface consists of two structures:
* definition of target assembler: ::ash
* definition of current processor: ::ph

These structures contain information about target processor and assembler
features.

It also defines two groups of kernel events:
* processor_t::event_t processor related events
* idb_event:event_code_t database related events

The processor related events are used to communicate with the processor module.
The database related events are used to inform any interested parties, like
plugins or processor modules, about the changes in the database."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_idp
else:
    import _ida_idp

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

SWIG_PYTHON_LEGACY_BOOL = _ida_idp.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class reg_access_vec_t(object):
    r"""
    Proxy of C++ qvector< reg_access_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_access_vec_t
        __init__(self, x) -> reg_access_vec_t

        @param x: qvector< reg_access_t > const &
        """
        _ida_idp.reg_access_vec_t_swiginit(self, _ida_idp.new_reg_access_vec_t(*args))
    __swig_destroy__ = _ida_idp.delete_reg_access_vec_t

    def push_back(self, *args) -> "reg_access_t &":
        r"""
        push_back(self, x)

        @param x: reg_access_t const &

        push_back(self) -> reg_access_t
        """
        return _ida_idp.reg_access_vec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_idp.reg_access_vec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_idp.reg_access_vec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_idp.reg_access_vec_t_empty(self, *args)

    def at(self, *args) -> "reg_access_t const &":
        r"""
        at(self, _idx) -> reg_access_t

        @param _idx: size_t
        """
        return _ida_idp.reg_access_vec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_idp.reg_access_vec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_idp.reg_access_vec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: reg_access_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_idp.reg_access_vec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=reg_access_t())

        @param x: reg_access_t const &
        """
        return _ida_idp.reg_access_vec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_idp.reg_access_vec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_idp.reg_access_vec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_idp.reg_access_vec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< reg_access_t > &
        """
        return _ida_idp.reg_access_vec_t_swap(self, *args)

    def extract(self, *args) -> "reg_access_t *":
        r"""
        extract(self) -> reg_access_t
        """
        return _ida_idp.reg_access_vec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: reg_access_t *
        @param len: size_t
        """
        return _ida_idp.reg_access_vec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< reg_access_t > const &
        """
        return _ida_idp.reg_access_vec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< reg_access_t > const &
        """
        return _ida_idp.reg_access_vec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< reg_access_t >::const_iterator":
        r"""
        begin(self) -> reg_access_t
        """
        return _ida_idp.reg_access_vec_t_begin(self, *args)

    def end(self, *args) -> "qvector< reg_access_t >::const_iterator":
        r"""
        end(self) -> reg_access_t
        """
        return _ida_idp.reg_access_vec_t_end(self, *args)

    def insert(self, *args) -> "qvector< reg_access_t >::iterator":
        r"""
        insert(self, it, x) -> reg_access_t

        @param it: qvector< reg_access_t >::iterator
        @param x: reg_access_t const &
        """
        return _ida_idp.reg_access_vec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< reg_access_t >::iterator":
        r"""
        erase(self, it) -> reg_access_t

        @param it: qvector< reg_access_t >::iterator

        erase(self, first, last) -> reg_access_t

        @param first: qvector< reg_access_t >::iterator
        @param last: qvector< reg_access_t >::iterator
        """
        return _ida_idp.reg_access_vec_t_erase(self, *args)

    def find(self, *args) -> "qvector< reg_access_t >::const_iterator":
        r"""
        find(self, x) -> reg_access_t

        @param x: reg_access_t const &

        """
        return _ida_idp.reg_access_vec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: reg_access_t const &
        """
        return _ida_idp.reg_access_vec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: reg_access_t const &
        """
        return _ida_idp.reg_access_vec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: reg_access_t const &

        """
        return _ida_idp.reg_access_vec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_idp.reg_access_vec_t___len__(self, *args)

    def __getitem__(self, *args) -> "reg_access_t const &":
        r"""
        __getitem__(self, i) -> reg_access_t

        @param i: size_t
        """
        return _ida_idp.reg_access_vec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: reg_access_t const &
        """
        return _ida_idp.reg_access_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register reg_access_vec_t in _ida_idp:
_ida_idp.reg_access_vec_t_swigregister(reg_access_vec_t)


def AssembleLine(*args) -> "PyObject *":
    r"""
    AssembleLine(ea, cs, ip, use32, nonnul_line) -> bytes
    Assemble an instruction to a string (display a warning if an error is found)

    @param ea: linear address of instruction
    @param cs: cs of instruction
    @param ip: ip of instruction
    @param use32: is 32bit segment
    @param nonnul_line: char const *
    @return:     - None on failure
        - or a string containing the assembled instruction
    """
    return _ida_idp.AssembleLine(*args)
IDP_INTERFACE_VERSION = _ida_idp.IDP_INTERFACE_VERSION
r"""
The interface version number.
@note: see also IDA_SDK_VERSION from pro.h
"""

CF_STOP = _ida_idp.CF_STOP
r"""
Instruction doesn't pass execution to the next instruction
"""

CF_CALL = _ida_idp.CF_CALL
r"""
CALL instruction (should make a procedure here)
"""

CF_CHG1 = _ida_idp.CF_CHG1
r"""
The instruction modifies the first operand.
"""

CF_CHG2 = _ida_idp.CF_CHG2
r"""
The instruction modifies the second operand.
"""

CF_CHG3 = _ida_idp.CF_CHG3
r"""
The instruction modifies the third operand.
"""

CF_CHG4 = _ida_idp.CF_CHG4
r"""
The instruction modifies 4 operand.
"""

CF_CHG5 = _ida_idp.CF_CHG5
r"""
The instruction modifies 5 operand.
"""

CF_CHG6 = _ida_idp.CF_CHG6
r"""
The instruction modifies 6 operand.
"""

CF_USE1 = _ida_idp.CF_USE1
r"""
The instruction uses value of the first operand.
"""

CF_USE2 = _ida_idp.CF_USE2
r"""
The instruction uses value of the second operand.
"""

CF_USE3 = _ida_idp.CF_USE3
r"""
The instruction uses value of the third operand.
"""

CF_USE4 = _ida_idp.CF_USE4
r"""
The instruction uses value of the 4 operand.
"""

CF_USE5 = _ida_idp.CF_USE5
r"""
The instruction uses value of the 5 operand.
"""

CF_USE6 = _ida_idp.CF_USE6
r"""
The instruction uses value of the 6 operand.
"""

CF_JUMP = _ida_idp.CF_JUMP
r"""
The instruction passes execution using indirect jump or call (thus needs
additional analysis)
"""

CF_SHFT = _ida_idp.CF_SHFT
r"""
Bit-shift instruction (shl,shr...)
"""

CF_HLL = _ida_idp.CF_HLL
r"""
Instruction may be present in a high level language function
"""

CF_CHG7 = _ida_idp.CF_CHG7
r"""
The instruction modifies the 7th operand.
"""

CF_CHG8 = _ida_idp.CF_CHG8
r"""
The instruction modifies the 8th operand.
"""

CF_USE7 = _ida_idp.CF_USE7
r"""
The instruction uses value of the 7th operand.
"""

CF_USE8 = _ida_idp.CF_USE8
r"""
The instruction uses value of the 8th operand.
"""


def has_cf_chg(*args) -> "bool":
    r"""
    has_cf_chg(feature, opnum) -> bool
    Does an instruction with the specified feature modify the i-th operand?

    @param feature: (C++: uint32)
    @param opnum: (C++: uint)
    """
    return _ida_idp.has_cf_chg(*args)

def has_cf_use(*args) -> "bool":
    r"""
    has_cf_use(feature, opnum) -> bool
    Does an instruction with the specified feature use a value of the i-th operand?

    @param feature: (C++: uint32)
    @param opnum: (C++: uint)
    """
    return _ida_idp.has_cf_use(*args)

def has_insn_feature(*args) -> "bool":
    r"""
    has_insn_feature(icode, bit) -> bool
    Does the specified instruction have the specified feature?

    @param icode: (C++: int)
    @param bit: (C++: uint32)
    """
    return _ida_idp.has_insn_feature(*args)

def is_call_insn(*args) -> "bool":
    r"""
    is_call_insn(insn) -> bool
    Is the instruction a "call"?

    @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
    """
    return _ida_idp.is_call_insn(*args)

def is_ret_insn(*args) -> "bool":
    r"""
    is_ret_insn(insn, strict=True) -> bool
    Is the instruction a "return"?

    @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param strict: (C++: bool)
    """
    return _ida_idp.is_ret_insn(*args)

def is_indirect_jump_insn(*args) -> "bool":
    r"""
    is_indirect_jump_insn(insn) -> bool
    Is the instruction an indirect jump?

    @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
    """
    return _ida_idp.is_indirect_jump_insn(*args)

def is_basic_block_end(*args) -> "bool":
    r"""
    is_basic_block_end(insn, call_insn_stops_block) -> bool
    Is the instruction the end of a basic block?

    @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param call_insn_stops_block: (C++: bool)
    """
    return _ida_idp.is_basic_block_end(*args)
class asm_t(object):
    r"""
    Proxy of C++ asm_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    flag = property(_ida_idp.asm_t_flag_get, _ida_idp.asm_t_flag_set, doc=r"""flag""")
    r"""
    Assembler feature bits
    """
    uflag = property(_ida_idp.asm_t_uflag_get, _ida_idp.asm_t_uflag_set, doc=r"""uflag""")
    r"""
    user defined flags (local only for IDP) you may define and use your own bits
    """
    name = property(_ida_idp.asm_t_name_get, _ida_idp.asm_t_name_set, doc=r"""name""")
    r"""
    Assembler name (displayed in menus)
    """
    help = property(_ida_idp.asm_t_help_get, _ida_idp.asm_t_help_set, doc=r"""help""")
    r"""
    Help screen number, 0 - no help.
    """
    header = property(_ida_idp.asm_t_header_get, _ida_idp.asm_t_header_set, doc=r"""header""")
    r"""
    array of automatically generated header lines they appear at the start of
    disassembled text
    """
    origin = property(_ida_idp.asm_t_origin_get, _ida_idp.asm_t_origin_set, doc=r"""origin""")
    r"""
    org directive
    """
    end = property(_ida_idp.asm_t_end_get, _ida_idp.asm_t_end_set, doc=r"""end""")
    r"""
    end directive
    """
    cmnt = property(_ida_idp.asm_t_cmnt_get, _ida_idp.asm_t_cmnt_set, doc=r"""cmnt""")
    r"""
    comment string (see also cmnt2)
    """
    ascsep = property(_ida_idp.asm_t_ascsep_get, _ida_idp.asm_t_ascsep_set, doc=r"""ascsep""")
    r"""
    string literal delimiter
    """
    accsep = property(_ida_idp.asm_t_accsep_get, _ida_idp.asm_t_accsep_set, doc=r"""accsep""")
    r"""
    char constant delimiter
    """
    esccodes = property(_ida_idp.asm_t_esccodes_get, _ida_idp.asm_t_esccodes_set, doc=r"""esccodes""")
    r"""
    special chars that cannot appear as is in string and char literals
    """
    a_ascii = property(_ida_idp.asm_t_a_ascii_get, _ida_idp.asm_t_a_ascii_set, doc=r"""a_ascii""")
    r"""
    string literal directive
    """
    a_byte = property(_ida_idp.asm_t_a_byte_get, _ida_idp.asm_t_a_byte_set, doc=r"""a_byte""")
    r"""
    byte directive
    """
    a_word = property(_ida_idp.asm_t_a_word_get, _ida_idp.asm_t_a_word_set, doc=r"""a_word""")
    r"""
    word directive
    """
    a_dword = property(_ida_idp.asm_t_a_dword_get, _ida_idp.asm_t_a_dword_set, doc=r"""a_dword""")
    r"""
    nullptr if not allowed
    """
    a_qword = property(_ida_idp.asm_t_a_qword_get, _ida_idp.asm_t_a_qword_set, doc=r"""a_qword""")
    r"""
    nullptr if not allowed
    """
    a_oword = property(_ida_idp.asm_t_a_oword_get, _ida_idp.asm_t_a_oword_set, doc=r"""a_oword""")
    r"""
    nullptr if not allowed
    """
    a_float = property(_ida_idp.asm_t_a_float_get, _ida_idp.asm_t_a_float_set, doc=r"""a_float""")
    r"""
    float; 4bytes; nullptr if not allowed
    """
    a_double = property(_ida_idp.asm_t_a_double_get, _ida_idp.asm_t_a_double_set, doc=r"""a_double""")
    r"""
    double; 8bytes; nullptr if not allowed
    """
    a_tbyte = property(_ida_idp.asm_t_a_tbyte_get, _ida_idp.asm_t_a_tbyte_set, doc=r"""a_tbyte""")
    r"""
    long double; nullptr if not allowed
    """
    a_packreal = property(_ida_idp.asm_t_a_packreal_get, _ida_idp.asm_t_a_packreal_set, doc=r"""a_packreal""")
    r"""
    packed decimal real nullptr if not allowed
    """
    a_dups = property(_ida_idp.asm_t_a_dups_get, _ida_idp.asm_t_a_dups_set, doc=r"""a_dups""")
    r"""
    array keyword. the following sequences may appear:
    * #h header
    * #d size
    * #v value
    * #s(b,w,l,q,f,d,o) size specifiers for byte,word, dword,qword,
    float,double,oword
    """
    a_bss = property(_ida_idp.asm_t_a_bss_get, _ida_idp.asm_t_a_bss_set, doc=r"""a_bss""")
    r"""
    uninitialized data directive should include 's' for the size of data
    """
    a_equ = property(_ida_idp.asm_t_a_equ_get, _ida_idp.asm_t_a_equ_set, doc=r"""a_equ""")
    r"""
    'equ' Used if AS_UNEQU is set
    """
    a_seg = property(_ida_idp.asm_t_a_seg_get, _ida_idp.asm_t_a_seg_set, doc=r"""a_seg""")
    r"""
    'seg ' prefix (example: push seg seg001)
    """
    a_curip = property(_ida_idp.asm_t_a_curip_get, _ida_idp.asm_t_a_curip_set, doc=r"""a_curip""")
    r"""
    current IP (instruction pointer) symbol in assembler
    """
    a_public = property(_ida_idp.asm_t_a_public_get, _ida_idp.asm_t_a_public_set, doc=r"""a_public""")
    r"""
    "public" name keyword. nullptr-use default, ""-do not generate
    """
    a_weak = property(_ida_idp.asm_t_a_weak_get, _ida_idp.asm_t_a_weak_set, doc=r"""a_weak""")
    r"""
    "weak" name keyword. nullptr-use default, ""-do not generate
    """
    a_extrn = property(_ida_idp.asm_t_a_extrn_get, _ida_idp.asm_t_a_extrn_set, doc=r"""a_extrn""")
    r"""
    "extern" name keyword
    """
    a_comdef = property(_ida_idp.asm_t_a_comdef_get, _ida_idp.asm_t_a_comdef_set, doc=r"""a_comdef""")
    r"""
    "comm" (communal variable)
    """
    a_align = property(_ida_idp.asm_t_a_align_get, _ida_idp.asm_t_a_align_set, doc=r"""a_align""")
    r"""
    "align" keyword
    """
    lbrace = property(_ida_idp.asm_t_lbrace_get, _ida_idp.asm_t_lbrace_set, doc=r"""lbrace""")
    r"""
    left brace used in complex expressions
    """
    rbrace = property(_ida_idp.asm_t_rbrace_get, _ida_idp.asm_t_rbrace_set, doc=r"""rbrace""")
    r"""
    right brace used in complex expressions
    """
    a_mod = property(_ida_idp.asm_t_a_mod_get, _ida_idp.asm_t_a_mod_set, doc=r"""a_mod""")
    r"""
    % mod assembler time operation
    """
    a_band = property(_ida_idp.asm_t_a_band_get, _ida_idp.asm_t_a_band_set, doc=r"""a_band""")
    r"""
    & bit and assembler time operation
    """
    a_bor = property(_ida_idp.asm_t_a_bor_get, _ida_idp.asm_t_a_bor_set, doc=r"""a_bor""")
    r"""
    | bit or assembler time operation
    """
    a_xor = property(_ida_idp.asm_t_a_xor_get, _ida_idp.asm_t_a_xor_set, doc=r"""a_xor""")
    r"""
    ^ bit xor assembler time operation
    """
    a_bnot = property(_ida_idp.asm_t_a_bnot_get, _ida_idp.asm_t_a_bnot_set, doc=r"""a_bnot""")
    r"""
    ~ bit not assembler time operation
    """
    a_shl = property(_ida_idp.asm_t_a_shl_get, _ida_idp.asm_t_a_shl_set, doc=r"""a_shl""")
    r"""
    << shift left assembler time operation
    """
    a_shr = property(_ida_idp.asm_t_a_shr_get, _ida_idp.asm_t_a_shr_set, doc=r"""a_shr""")
    r"""
    >> shift right assembler time operation
    """
    a_sizeof_fmt = property(_ida_idp.asm_t_a_sizeof_fmt_get, _ida_idp.asm_t_a_sizeof_fmt_set, doc=r"""a_sizeof_fmt""")
    r"""
    size of type (format string)
    """
    flag2 = property(_ida_idp.asm_t_flag2_get, _ida_idp.asm_t_flag2_set, doc=r"""flag2""")
    r"""
    Secondary assembler feature bits
    """
    cmnt2 = property(_ida_idp.asm_t_cmnt2_get, _ida_idp.asm_t_cmnt2_set, doc=r"""cmnt2""")
    r"""
    comment close string (usually nullptr) this is used to denote a string which
    closes comments, for example, if the comments are represented with (* ... *)
    then cmnt = "(*" and cmnt2 = "*)"
    """
    low8 = property(_ida_idp.asm_t_low8_get, _ida_idp.asm_t_low8_set, doc=r"""low8""")
    r"""
    low8 operation, should contain s for the operand
    """
    high8 = property(_ida_idp.asm_t_high8_get, _ida_idp.asm_t_high8_set, doc=r"""high8""")
    r"""
    high8
    """
    low16 = property(_ida_idp.asm_t_low16_get, _ida_idp.asm_t_low16_set, doc=r"""low16""")
    r"""
    low16
    """
    high16 = property(_ida_idp.asm_t_high16_get, _ida_idp.asm_t_high16_set, doc=r"""high16""")
    r"""
    high16
    """
    a_include_fmt = property(_ida_idp.asm_t_a_include_fmt_get, _ida_idp.asm_t_a_include_fmt_set, doc=r"""a_include_fmt""")
    r"""
    the include directive (format string)
    """
    a_vstruc_fmt = property(_ida_idp.asm_t_a_vstruc_fmt_get, _ida_idp.asm_t_a_vstruc_fmt_set, doc=r"""a_vstruc_fmt""")
    r"""
    if a named item is a structure and displayed in the verbose (multiline) form
    then display the name as printf(a_strucname_fmt, typename) (for asms with type
    checking, e.g. tasm ideal)
    """
    a_rva = property(_ida_idp.asm_t_a_rva_get, _ida_idp.asm_t_a_rva_set, doc=r"""a_rva""")
    r"""
    'rva' keyword for image based offsets (see REFINFO_RVAOFF)
    """
    a_yword = property(_ida_idp.asm_t_a_yword_get, _ida_idp.asm_t_a_yword_set, doc=r"""a_yword""")
    r"""
    32-byte (256-bit) data; nullptr if not allowed requires AS2_YWORD
    """
    a_zword = property(_ida_idp.asm_t_a_zword_get, _ida_idp.asm_t_a_zword_set, doc=r"""a_zword""")
    r"""
    64-byte (512-bit) data; nullptr if not allowed requires AS2_ZWORD
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> asm_t
        """
        _ida_idp.asm_t_swiginit(self, _ida_idp.new_asm_t(*args))
    __swig_destroy__ = _ida_idp.delete_asm_t

# Register asm_t in _ida_idp:
_ida_idp.asm_t_swigregister(asm_t)
AS_OFFST = _ida_idp.AS_OFFST
r"""
offsets are 'offset xxx' ?
"""

AS_COLON = _ida_idp.AS_COLON
r"""
create colons after data names ?
"""

AS_UDATA = _ida_idp.AS_UDATA
r"""
can use '?' in data directives
"""

AS_2CHRE = _ida_idp.AS_2CHRE
r"""
double char constants are: "xy
"""

AS_NCHRE = _ida_idp.AS_NCHRE
r"""
char constants are: 'x
"""

AS_N2CHR = _ida_idp.AS_N2CHR
r"""
can't have 2 byte char consts
"""

AS_1TEXT = _ida_idp.AS_1TEXT
r"""
1 text per line, no bytes
"""

AS_NHIAS = _ida_idp.AS_NHIAS
r"""
no characters with high bit
"""

AS_NCMAS = _ida_idp.AS_NCMAS
r"""
no commas in ascii directives
"""

AS_HEXFM = _ida_idp.AS_HEXFM
r"""
mask - hex number format
"""

ASH_HEXF0 = _ida_idp.ASH_HEXF0
r"""
34h
"""

ASH_HEXF1 = _ida_idp.ASH_HEXF1
r"""
h'34
"""

ASH_HEXF2 = _ida_idp.ASH_HEXF2
r"""
34
"""

ASH_HEXF3 = _ida_idp.ASH_HEXF3
r"""
0x34
"""

ASH_HEXF4 = _ida_idp.ASH_HEXF4
r"""
$34
"""

ASH_HEXF5 = _ida_idp.ASH_HEXF5
r"""
<^R > (radix)
"""

AS_DECFM = _ida_idp.AS_DECFM
r"""
mask - decimal number format
"""

ASD_DECF0 = _ida_idp.ASD_DECF0
r"""
34
"""

ASD_DECF1 = _ida_idp.ASD_DECF1
r"""
#34
"""

ASD_DECF2 = _ida_idp.ASD_DECF2
r"""
34.
"""

ASD_DECF3 = _ida_idp.ASD_DECF3
r"""
.34
"""

AS_OCTFM = _ida_idp.AS_OCTFM
r"""
mask - octal number format
"""

ASO_OCTF0 = _ida_idp.ASO_OCTF0
r"""
123o
"""

ASO_OCTF1 = _ida_idp.ASO_OCTF1
r"""
0123
"""

ASO_OCTF2 = _ida_idp.ASO_OCTF2
r"""
123
"""

ASO_OCTF3 = _ida_idp.ASO_OCTF3
r"""
@123
"""

ASO_OCTF4 = _ida_idp.ASO_OCTF4
r"""
o'123
"""

ASO_OCTF5 = _ida_idp.ASO_OCTF5
r"""
123q
"""

ASO_OCTF6 = _ida_idp.ASO_OCTF6
r"""
~123
"""

ASO_OCTF7 = _ida_idp.ASO_OCTF7
r"""
q'123
"""

AS_BINFM = _ida_idp.AS_BINFM
r"""
mask - binary number format
"""

ASB_BINF0 = _ida_idp.ASB_BINF0
r"""
010101b
"""

ASB_BINF1 = _ida_idp.ASB_BINF1
r"""
^B010101
"""

ASB_BINF2 = _ida_idp.ASB_BINF2
r"""
%010101
"""

ASB_BINF3 = _ida_idp.ASB_BINF3
r"""
0b1010101
"""

ASB_BINF4 = _ida_idp.ASB_BINF4
r"""
b'1010101
"""

ASB_BINF5 = _ida_idp.ASB_BINF5
r"""
b'1010101'
"""

AS_UNEQU = _ida_idp.AS_UNEQU
r"""
replace undefined data items with EQU (for ANTA's A80)
"""

AS_ONEDUP = _ida_idp.AS_ONEDUP
r"""
One array definition per line.
"""

AS_NOXRF = _ida_idp.AS_NOXRF
r"""
Disable xrefs during the output file generation.
"""

AS_XTRNTYPE = _ida_idp.AS_XTRNTYPE
r"""
Assembler understands type of extern symbols as ":type" suffix.
"""

AS_RELSUP = _ida_idp.AS_RELSUP
r"""
Checkarg: 'and','or','xor' operations with addresses are possible.
"""

AS_LALIGN = _ida_idp.AS_LALIGN
r"""
Labels at "align" keyword are supported.
"""

AS_NOCODECLN = _ida_idp.AS_NOCODECLN
r"""
don't create colons after code names
"""

AS_NOSPACE = _ida_idp.AS_NOSPACE
r"""
No spaces in expressions.
"""

AS_ALIGN2 = _ida_idp.AS_ALIGN2
r"""
.align directive expects an exponent rather than a power of 2 (.align 5 means to
align at 32byte boundary)
"""

AS_ASCIIC = _ida_idp.AS_ASCIIC
r"""
ascii directive accepts C-like escape sequences (\n,\x01 and similar)
"""

AS_ASCIIZ = _ida_idp.AS_ASCIIZ
r"""
ascii directive inserts implicit zero byte at the end
"""

AS2_BRACE = _ida_idp.AS2_BRACE
r"""
Use braces for all expressions.
"""

AS2_STRINV = _ida_idp.AS2_STRINV
r"""
Invert meaning of idainfo::wide_high_byte_first for text strings (for processors
with bytes bigger than 8 bits)
"""

AS2_BYTE1CHAR = _ida_idp.AS2_BYTE1CHAR
r"""
One symbol per processor byte. Meaningful only for wide byte processors
"""

AS2_IDEALDSCR = _ida_idp.AS2_IDEALDSCR
r"""
Description of struc/union is in the 'reverse' form (keyword before name), the
same as in borland tasm ideal
"""

AS2_TERSESTR = _ida_idp.AS2_TERSESTR
r"""
'terse' structure initialization form; NAME<fld,fld,...> is supported
"""

AS2_COLONSUF = _ida_idp.AS2_COLONSUF
r"""
addresses may have ":xx" suffix; this suffix must be ignored when extracting the
address under the cursor
"""

AS2_YWORD = _ida_idp.AS2_YWORD
r"""
a_yword field is present and valid
"""

AS2_ZWORD = _ida_idp.AS2_ZWORD
r"""
a_zword field is present and valid
"""


HKCB_GLOBAL = _ida_idp.HKCB_GLOBAL
r"""
is global event listener? if true, the listener will survive database closing
and opening. it will stay in the memory until explicitly unhooked. otherwise the
kernel will delete it as soon as the owner is unloaded. should be used only with
PLUGIN_FIX plugins.
"""

PLFM_386 = _ida_idp.PLFM_386
r"""
Intel 80x86.
"""

PLFM_Z80 = _ida_idp.PLFM_Z80
r"""
8085, Z80
"""

PLFM_I860 = _ida_idp.PLFM_I860
r"""
Intel 860.
"""

PLFM_8051 = _ida_idp.PLFM_8051
r"""
8051
"""

PLFM_TMS = _ida_idp.PLFM_TMS
r"""
Texas Instruments TMS320C5x.
"""

PLFM_6502 = _ida_idp.PLFM_6502
r"""
6502
"""

PLFM_PDP = _ida_idp.PLFM_PDP
r"""
PDP11.
"""

PLFM_68K = _ida_idp.PLFM_68K
r"""
Motorola 680x0.
"""

PLFM_JAVA = _ida_idp.PLFM_JAVA
r"""
Java.
"""

PLFM_6800 = _ida_idp.PLFM_6800
r"""
Motorola 68xx.
"""

PLFM_ST7 = _ida_idp.PLFM_ST7
r"""
SGS-Thomson ST7.
"""

PLFM_MC6812 = _ida_idp.PLFM_MC6812
r"""
Motorola 68HC12.
"""

PLFM_MIPS = _ida_idp.PLFM_MIPS
r"""
MIPS.
"""

PLFM_ARM = _ida_idp.PLFM_ARM
r"""
Advanced RISC Machines.
"""

PLFM_TMSC6 = _ida_idp.PLFM_TMSC6
r"""
Texas Instruments TMS320C6x.
"""

PLFM_PPC = _ida_idp.PLFM_PPC
r"""
PowerPC.
"""

PLFM_80196 = _ida_idp.PLFM_80196
r"""
Intel 80196.
"""

PLFM_Z8 = _ida_idp.PLFM_Z8
r"""
Z8.
"""

PLFM_SH = _ida_idp.PLFM_SH
r"""
Renesas (formerly Hitachi) SuperH.
"""

PLFM_NET = _ida_idp.PLFM_NET
r"""
Microsoft Visual Studio.Net.
"""

PLFM_AVR = _ida_idp.PLFM_AVR
r"""
Atmel 8-bit RISC processor(s)
"""

PLFM_H8 = _ida_idp.PLFM_H8
r"""
Hitachi H8/300, H8/2000.
"""

PLFM_PIC = _ida_idp.PLFM_PIC
r"""
Microchip's PIC.
"""

PLFM_SPARC = _ida_idp.PLFM_SPARC
r"""
SPARC.
"""

PLFM_ALPHA = _ida_idp.PLFM_ALPHA
r"""
DEC Alpha.
"""

PLFM_HPPA = _ida_idp.PLFM_HPPA
r"""
Hewlett-Packard PA-RISC.
"""

PLFM_H8500 = _ida_idp.PLFM_H8500
r"""
Hitachi H8/500.
"""

PLFM_TRICORE = _ida_idp.PLFM_TRICORE
r"""
Tasking Tricore.
"""

PLFM_DSP56K = _ida_idp.PLFM_DSP56K
r"""
Motorola DSP5600x.
"""

PLFM_C166 = _ida_idp.PLFM_C166
r"""
Siemens C166 family.
"""

PLFM_ST20 = _ida_idp.PLFM_ST20
r"""
SGS-Thomson ST20.
"""

PLFM_IA64 = _ida_idp.PLFM_IA64
r"""
Intel Itanium IA64.
"""

PLFM_I960 = _ida_idp.PLFM_I960
r"""
Intel 960.
"""

PLFM_F2MC = _ida_idp.PLFM_F2MC
r"""
Fujistu F2MC-16.
"""

PLFM_TMS320C54 = _ida_idp.PLFM_TMS320C54
r"""
Texas Instruments TMS320C54xx.
"""

PLFM_TMS320C55 = _ida_idp.PLFM_TMS320C55
r"""
Texas Instruments TMS320C55xx.
"""

PLFM_TRIMEDIA = _ida_idp.PLFM_TRIMEDIA
r"""
Trimedia.
"""

PLFM_M32R = _ida_idp.PLFM_M32R
r"""
Mitsubishi 32bit RISC.
"""

PLFM_NEC_78K0 = _ida_idp.PLFM_NEC_78K0
r"""
NEC 78K0.
"""

PLFM_NEC_78K0S = _ida_idp.PLFM_NEC_78K0S
r"""
NEC 78K0S.
"""

PLFM_M740 = _ida_idp.PLFM_M740
r"""
Mitsubishi 8bit.
"""

PLFM_M7700 = _ida_idp.PLFM_M7700
r"""
Mitsubishi 16bit.
"""

PLFM_ST9 = _ida_idp.PLFM_ST9
r"""
ST9+.
"""

PLFM_FR = _ida_idp.PLFM_FR
r"""
Fujitsu FR Family.
"""

PLFM_MC6816 = _ida_idp.PLFM_MC6816
r"""
Motorola 68HC16.
"""

PLFM_M7900 = _ida_idp.PLFM_M7900
r"""
Mitsubishi 7900.
"""

PLFM_TMS320C3 = _ida_idp.PLFM_TMS320C3
r"""
Texas Instruments TMS320C3.
"""

PLFM_KR1878 = _ida_idp.PLFM_KR1878
r"""
Angstrem KR1878.
"""

PLFM_AD218X = _ida_idp.PLFM_AD218X
r"""
Analog Devices ADSP 218X.
"""

PLFM_OAKDSP = _ida_idp.PLFM_OAKDSP
r"""
Atmel OAK DSP.
"""

PLFM_TLCS900 = _ida_idp.PLFM_TLCS900
r"""
Toshiba TLCS-900.
"""

PLFM_C39 = _ida_idp.PLFM_C39
r"""
Rockwell C39.
"""

PLFM_CR16 = _ida_idp.PLFM_CR16
r"""
NSC CR16.
"""

PLFM_MN102L00 = _ida_idp.PLFM_MN102L00
r"""
Panasonic MN10200.
"""

PLFM_TMS320C1X = _ida_idp.PLFM_TMS320C1X
r"""
Texas Instruments TMS320C1x.
"""

PLFM_NEC_V850X = _ida_idp.PLFM_NEC_V850X
r"""
NEC V850 and V850ES/E1/E2.
"""

PLFM_SCR_ADPT = _ida_idp.PLFM_SCR_ADPT
r"""
Processor module adapter for processor modules written in scripting languages.
"""

PLFM_EBC = _ida_idp.PLFM_EBC
r"""
EFI Bytecode.
"""

PLFM_MSP430 = _ida_idp.PLFM_MSP430
r"""
Texas Instruments MSP430.
"""

PLFM_SPU = _ida_idp.PLFM_SPU
r"""
Cell Broadband Engine Synergistic Processor Unit.
"""

PLFM_DALVIK = _ida_idp.PLFM_DALVIK
r"""
Android Dalvik Virtual Machine.
"""

PLFM_65C816 = _ida_idp.PLFM_65C816
r"""
65802/65816
"""

PLFM_M16C = _ida_idp.PLFM_M16C
r"""
Renesas M16C.
"""

PLFM_ARC = _ida_idp.PLFM_ARC
r"""
Argonaut RISC Core.
"""

PLFM_UNSP = _ida_idp.PLFM_UNSP
r"""
SunPlus unSP.
"""

PLFM_TMS320C28 = _ida_idp.PLFM_TMS320C28
r"""
Texas Instruments TMS320C28x.
"""

PLFM_DSP96K = _ida_idp.PLFM_DSP96K
r"""
Motorola DSP96000.
"""

PLFM_SPC700 = _ida_idp.PLFM_SPC700
r"""
Sony SPC700.
"""

PLFM_AD2106X = _ida_idp.PLFM_AD2106X
r"""
Analog Devices ADSP 2106X.
"""

PLFM_PIC16 = _ida_idp.PLFM_PIC16
r"""
Microchip's 16-bit PIC.
"""

PLFM_S390 = _ida_idp.PLFM_S390
r"""
IBM's S390.
"""

PLFM_XTENSA = _ida_idp.PLFM_XTENSA
r"""
Tensilica Xtensa.
"""

PLFM_RISCV = _ida_idp.PLFM_RISCV
r"""
RISC-V.
"""

PLFM_RL78 = _ida_idp.PLFM_RL78
r"""
Renesas RL78.
"""

PLFM_RX = _ida_idp.PLFM_RX
r"""
Renesas RX.
"""

PR_SEGS = _ida_idp.PR_SEGS
r"""
has segment registers?
"""

PR_USE32 = _ida_idp.PR_USE32
r"""
supports 32-bit addressing?
"""

PR_DEFSEG32 = _ida_idp.PR_DEFSEG32
r"""
segments are 32-bit by default
"""

PR_RNAMESOK = _ida_idp.PR_RNAMESOK
r"""
allow user register names for location names
"""

PR_ADJSEGS = _ida_idp.PR_ADJSEGS
r"""
IDA may adjust segments' starting/ending addresses.
"""

PR_DEFNUM = _ida_idp.PR_DEFNUM
r"""
mask - default number representation
"""

PRN_HEX = _ida_idp.PRN_HEX
r"""
hex
"""

PRN_OCT = _ida_idp.PRN_OCT
r"""
octal
"""

PRN_DEC = _ida_idp.PRN_DEC
r"""
decimal
"""

PRN_BIN = _ida_idp.PRN_BIN
r"""
binary
"""

PR_WORD_INS = _ida_idp.PR_WORD_INS
r"""
instruction codes are grouped 2bytes in binary line prefix
"""

PR_NOCHANGE = _ida_idp.PR_NOCHANGE
r"""
The user can't change segments and code/data attributes (display only)
"""

PR_ASSEMBLE = _ida_idp.PR_ASSEMBLE
r"""
Module has a built-in assembler and will react to ev_assemble.
"""

PR_ALIGN = _ida_idp.PR_ALIGN
r"""
All data items should be aligned properly.
"""

PR_TYPEINFO = _ida_idp.PR_TYPEINFO
r"""
the processor module fully supports type information callbacks; without full
support, function argument locations and other things will probably be wrong.
"""

PR_USE64 = _ida_idp.PR_USE64
r"""
supports 64-bit addressing?
"""

PR_SGROTHER = _ida_idp.PR_SGROTHER
r"""
the segment registers don't contain the segment selectors.
"""

PR_STACK_UP = _ida_idp.PR_STACK_UP
r"""
the stack grows up
"""

PR_BINMEM = _ida_idp.PR_BINMEM
r"""
the processor module provides correct segmentation for binary files (i.e. it
creates additional segments). The kernel will not ask the user to specify the
RAM/ROM sizes
"""

PR_SEGTRANS = _ida_idp.PR_SEGTRANS
r"""
the processor module supports the segment translation feature (meaning it
calculates the code addresses using the map_code_ea() function)
"""

PR_CHK_XREF = _ida_idp.PR_CHK_XREF
r"""
don't allow near xrefs between segments with different bases
"""

PR_NO_SEGMOVE = _ida_idp.PR_NO_SEGMOVE
r"""
the processor module doesn't support move_segm() (i.e. the user can't move
segments)
"""

PR_USE_ARG_TYPES = _ida_idp.PR_USE_ARG_TYPES
r"""
use processor_t::use_arg_types callback
"""

PR_SCALE_STKVARS = _ida_idp.PR_SCALE_STKVARS
r"""
use processor_t::get_stkvar_scale callback
"""

PR_DELAYED = _ida_idp.PR_DELAYED
r"""
has delayed jumps and calls. If this flag is set,
processor_t::is_basic_block_end, processor_t::delay_slot_insn should be
implemented
"""

PR_ALIGN_INSN = _ida_idp.PR_ALIGN_INSN
r"""
allow ida to create alignment instructions arbitrarily. Since these instructions
might lead to other wrong instructions and spoil the listing, IDA does not
create them by default anymore
"""

PR_PURGING = _ida_idp.PR_PURGING
r"""
there are calling conventions which may purge bytes from the stack
"""

PR_CNDINSNS = _ida_idp.PR_CNDINSNS
r"""
has conditional instructions
"""

PR_USE_TBYTE = _ida_idp.PR_USE_TBYTE
r"""
BTMT_SPECFLT means _TBYTE type
"""

PR_DEFSEG64 = _ida_idp.PR_DEFSEG64
r"""
segments are 64-bit by default
"""

PR_OUTER = _ida_idp.PR_OUTER
r"""
has outer operands (currently only mc68k)
"""

PR2_MAPPINGS = _ida_idp.PR2_MAPPINGS
r"""
the processor module uses memory mapping
"""

PR2_IDP_OPTS = _ida_idp.PR2_IDP_OPTS
r"""
the module has processor-specific configuration options
"""

PR2_REALCVT = _ida_idp.PR2_REALCVT
r"""
the module has a custom 'ev_realcvt' implementation (otherwise IEEE-754 format
is assumed)
"""

PR2_CODE16_BIT = _ida_idp.PR2_CODE16_BIT
r"""
low bit of code addresses has special meaning e.g. ARM Thumb, MIPS16
"""

PR2_MACRO = _ida_idp.PR2_MACRO
r"""
processor supports macro instructions
"""

PR2_USE_CALCREL = _ida_idp.PR2_USE_CALCREL
r"""
(Lumina) the module supports calcrel info
"""

PR2_REL_BITS = _ida_idp.PR2_REL_BITS
r"""
(Lumina) calcrel info has bits granularity, not bytes - construction flag only
"""

PR2_FORCE_16BIT = _ida_idp.PR2_FORCE_16BIT
r"""
use 16-bit basic types despite of 32-bit segments (used by c166)
"""

OP_FP_BASED = _ida_idp.OP_FP_BASED
r"""
operand is FP based
"""

OP_SP_BASED = _ida_idp.OP_SP_BASED
r"""
operand is SP based
"""

OP_SP_ADD = _ida_idp.OP_SP_ADD
r"""
operand value is added to the pointer
"""

OP_SP_SUB = _ida_idp.OP_SP_SUB
r"""
operand value is subtracted from the pointer
"""

CUSTOM_INSN_ITYPE = _ida_idp.CUSTOM_INSN_ITYPE
r"""
Custom instruction codes defined by processor extension plugins must be greater
than or equal to this
"""

REG_SPOIL = _ida_idp.REG_SPOIL
r"""
processor_t::use_regarg_type uses this bit in the return value to indicate that
the register value has been spoiled
"""


def get_ph(*args) -> "processor_t *":
    r"""
    get_ph() -> processor_t *
    """
    return _ida_idp.get_ph(*args)

def get_ash(*args) -> "asm_t *":
    r"""
    get_ash() -> asm_t
    """
    return _ida_idp.get_ash(*args)

def str2reg(*args) -> "int":
    r"""
    str2reg(p) -> int
    Get any reg number (-1 on error)

    @param p: (C++: const char *) char const *
    """
    return _ida_idp.str2reg(*args)

def is_align_insn(*args) -> "int":
    r"""
    is_align_insn(ea) -> int
    If the instruction at 'ea' looks like an alignment instruction, return its
    length in bytes. Otherwise return 0.

    @param ea: (C++: ea_t)
    """
    return _ida_idp.is_align_insn(*args)

def get_reg_name(*args) -> "qstring *":
    r"""
    get_reg_name(reg, width, reghi=-1) -> str
    Get text representation of a register. For most processors this function will
    just return processor_t::reg_names[reg]. If the processor module has implemented
    processor_t::get_reg_name, it will be used instead

    @param reg: (C++: int) internal register number as defined in the processor module
    @param width: (C++: size_t) register width in bytes
    @param reghi: (C++: int) if specified, then this function will return the register pair
    @return: length of register name in bytes or -1 if failure
    """
    return _ida_idp.get_reg_name(*args)
class reg_info_t(object):
    r"""
    Proxy of C++ reg_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    reg = property(_ida_idp.reg_info_t_reg_get, _ida_idp.reg_info_t_reg_set, doc=r"""reg""")
    r"""
    register number
    """
    size = property(_ida_idp.reg_info_t_size_get, _ida_idp.reg_info_t_size_set, doc=r"""size""")
    r"""
    register size
    """

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___ne__(self, *args)

    def __lt__(self, *args) -> "bool":
        r"""
        __lt__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___lt__(self, *args)

    def __gt__(self, *args) -> "bool":
        r"""
        __gt__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___gt__(self, *args)

    def __le__(self, *args) -> "bool":
        r"""
        __le__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___le__(self, *args)

    def __ge__(self, *args) -> "bool":
        r"""
        __ge__(self, r) -> bool

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t___ge__(self, *args)

    def compare(self, *args) -> "int":
        r"""
        compare(self, r) -> int

        @param r: reg_info_t const &
        """
        return _ida_idp.reg_info_t_compare(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_info_t
        """
        _ida_idp.reg_info_t_swiginit(self, _ida_idp.new_reg_info_t(*args))
    __swig_destroy__ = _ida_idp.delete_reg_info_t

# Register reg_info_t in _ida_idp:
_ida_idp.reg_info_t_swigregister(reg_info_t)


def parse_reg_name(*args) -> "bool":
    r"""
    parse_reg_name(ri, regname) -> bool
    Get register info by name.

    @param ri: (C++: reg_info_t *) result
    @param regname: (C++: const char *) name of register
    @return: success
    """
    return _ida_idp.parse_reg_name(*args)
NO_ACCESS = _ida_idp.NO_ACCESS

WRITE_ACCESS = _ida_idp.WRITE_ACCESS

READ_ACCESS = _ida_idp.READ_ACCESS

RW_ACCESS = _ida_idp.RW_ACCESS

class reg_access_t(object):
    r"""
    Proxy of C++ reg_access_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    regnum = property(_ida_idp.reg_access_t_regnum_get, _ida_idp.reg_access_t_regnum_set, doc=r"""regnum""")
    r"""
    register number (only entire registers)
    """
    range = property(_ida_idp.reg_access_t_range_get, _ida_idp.reg_access_t_range_set, doc=r"""range""")
    r"""
    bitrange inside the register
    """
    access_type = property(_ida_idp.reg_access_t_access_type_get, _ida_idp.reg_access_t_access_type_set, doc=r"""access_type""")
    opnum = property(_ida_idp.reg_access_t_opnum_get, _ida_idp.reg_access_t_opnum_set, doc=r"""opnum""")
    r"""
    operand number
    """

    def have_common_bits(self, *args) -> "bool":
        r"""
        have_common_bits(self, r) -> bool

        @param r: reg_access_t const &
        """
        return _ida_idp.reg_access_t_have_common_bits(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: reg_access_t const &
        """
        return _ida_idp.reg_access_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: reg_access_t const &
        """
        return _ida_idp.reg_access_t___ne__(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_access_t
        """
        _ida_idp.reg_access_t_swiginit(self, _ida_idp.new_reg_access_t(*args))
    __swig_destroy__ = _ida_idp.delete_reg_access_t

# Register reg_access_t in _ida_idp:
_ida_idp.reg_access_t_swigregister(reg_access_t)

class reg_accesses_t(reg_access_vec_t):
    r"""
    Proxy of C++ reg_accesses_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> reg_accesses_t
        """
        _ida_idp.reg_accesses_t_swiginit(self, _ida_idp.new_reg_accesses_t(*args))
    __swig_destroy__ = _ida_idp.delete_reg_accesses_t

# Register reg_accesses_t in _ida_idp:
_ida_idp.reg_accesses_t_swigregister(reg_accesses_t)

SETPROC_IDB = _ida_idp.SETPROC_IDB
r"""
set processor type for old idb
"""

SETPROC_LOADER = _ida_idp.SETPROC_LOADER
r"""
set processor type for new idb; if the user has specified a compatible
processor, return success without changing it. if failure, call loader_failure()
"""

SETPROC_LOADER_NON_FATAL = _ida_idp.SETPROC_LOADER_NON_FATAL
r"""
the same as SETPROC_LOADER but non-fatal failures.
"""

SETPROC_USER = _ida_idp.SETPROC_USER
r"""
set user-specified processor used for -p and manual processor change at later
time
"""


def set_processor_type(*args) -> "bool":
    r"""
    set_processor_type(procname, level) -> bool
    Set target processor type. Once a processor module is loaded, it cannot be
    replaced until we close the idb.

    @param procname: (C++: const char *) name of processor type (one of names present in
                     processor_t::psnames)
    @param level: (C++: setproc_level_t) SETPROC_
    @return: success
    """
    return _ida_idp.set_processor_type(*args)

def get_idp_name(*args) -> "size_t":
    r"""
    get_idp_name() -> str
    Get name of the current processor module. The name is derived from the file
    name. For example, for IBM PC the module is named "pc.w32" (windows version),
    then the module name is "PC" (uppercase). If no processor module is loaded, this
    function will return nullptr
    """
    return _ida_idp.get_idp_name(*args)

def set_target_assembler(*args) -> "bool":
    r"""
    set_target_assembler(asmnum) -> bool
    Set target assembler.

    @param asmnum: (C++: int) number of assembler in the current processor module
    @return: success
    """
    return _ida_idp.set_target_assembler(*args)
closebase = _ida_idp.closebase

savebase = _ida_idp.savebase

upgraded = _ida_idp.upgraded

auto_empty = _ida_idp.auto_empty

auto_empty_finally = _ida_idp.auto_empty_finally

determined_main = _ida_idp.determined_main

local_types_changed = _ida_idp.local_types_changed

extlang_changed = _ida_idp.extlang_changed

idasgn_loaded = _ida_idp.idasgn_loaded

kernel_config_loaded = _ida_idp.kernel_config_loaded

loader_finished = _ida_idp.loader_finished

flow_chart_created = _ida_idp.flow_chart_created

compiler_changed = _ida_idp.compiler_changed

changing_ti = _ida_idp.changing_ti

ti_changed = _ida_idp.ti_changed

changing_op_ti = _ida_idp.changing_op_ti

op_ti_changed = _ida_idp.op_ti_changed

changing_op_type = _ida_idp.changing_op_type

op_type_changed = _ida_idp.op_type_changed

enum_created = _ida_idp.enum_created

deleting_enum = _ida_idp.deleting_enum

enum_deleted = _ida_idp.enum_deleted

renaming_enum = _ida_idp.renaming_enum

enum_renamed = _ida_idp.enum_renamed

changing_enum_bf = _ida_idp.changing_enum_bf

enum_bf_changed = _ida_idp.enum_bf_changed

changing_enum_cmt = _ida_idp.changing_enum_cmt

enum_cmt_changed = _ida_idp.enum_cmt_changed

enum_member_created = _ida_idp.enum_member_created

deleting_enum_member = _ida_idp.deleting_enum_member

enum_member_deleted = _ida_idp.enum_member_deleted

struc_created = _ida_idp.struc_created

deleting_struc = _ida_idp.deleting_struc

struc_deleted = _ida_idp.struc_deleted

changing_struc_align = _ida_idp.changing_struc_align

struc_align_changed = _ida_idp.struc_align_changed

renaming_struc = _ida_idp.renaming_struc

struc_renamed = _ida_idp.struc_renamed

expanding_struc = _ida_idp.expanding_struc

struc_expanded = _ida_idp.struc_expanded

struc_member_created = _ida_idp.struc_member_created

deleting_struc_member = _ida_idp.deleting_struc_member

struc_member_deleted = _ida_idp.struc_member_deleted

renaming_struc_member = _ida_idp.renaming_struc_member

struc_member_renamed = _ida_idp.struc_member_renamed

changing_struc_member = _ida_idp.changing_struc_member

struc_member_changed = _ida_idp.struc_member_changed

changing_struc_cmt = _ida_idp.changing_struc_cmt

struc_cmt_changed = _ida_idp.struc_cmt_changed

segm_added = _ida_idp.segm_added

deleting_segm = _ida_idp.deleting_segm

segm_deleted = _ida_idp.segm_deleted

changing_segm_start = _ida_idp.changing_segm_start

segm_start_changed = _ida_idp.segm_start_changed

changing_segm_end = _ida_idp.changing_segm_end

segm_end_changed = _ida_idp.segm_end_changed

changing_segm_name = _ida_idp.changing_segm_name

segm_name_changed = _ida_idp.segm_name_changed

changing_segm_class = _ida_idp.changing_segm_class

segm_class_changed = _ida_idp.segm_class_changed

segm_attrs_updated = _ida_idp.segm_attrs_updated

segm_moved = _ida_idp.segm_moved

allsegs_moved = _ida_idp.allsegs_moved

func_added = _ida_idp.func_added

func_updated = _ida_idp.func_updated

set_func_start = _ida_idp.set_func_start

set_func_end = _ida_idp.set_func_end

deleting_func = _ida_idp.deleting_func

frame_deleted = _ida_idp.frame_deleted

thunk_func_created = _ida_idp.thunk_func_created

func_tail_appended = _ida_idp.func_tail_appended

deleting_func_tail = _ida_idp.deleting_func_tail

func_tail_deleted = _ida_idp.func_tail_deleted

tail_owner_changed = _ida_idp.tail_owner_changed

func_noret_changed = _ida_idp.func_noret_changed

stkpnts_changed = _ida_idp.stkpnts_changed

updating_tryblks = _ida_idp.updating_tryblks

tryblks_updated = _ida_idp.tryblks_updated

deleting_tryblks = _ida_idp.deleting_tryblks

sgr_changed = _ida_idp.sgr_changed

make_code = _ida_idp.make_code

make_data = _ida_idp.make_data

destroyed_items = _ida_idp.destroyed_items

renamed = _ida_idp.renamed

byte_patched = _ida_idp.byte_patched

changing_cmt = _ida_idp.changing_cmt

cmt_changed = _ida_idp.cmt_changed

changing_range_cmt = _ida_idp.changing_range_cmt

range_cmt_changed = _ida_idp.range_cmt_changed

extra_cmt_changed = _ida_idp.extra_cmt_changed

item_color_changed = _ida_idp.item_color_changed

callee_addr_changed = _ida_idp.callee_addr_changed

bookmark_changed = _ida_idp.bookmark_changed

sgr_deleted = _ida_idp.sgr_deleted

adding_segm = _ida_idp.adding_segm

func_deleted = _ida_idp.func_deleted

dirtree_mkdir = _ida_idp.dirtree_mkdir

dirtree_rmdir = _ida_idp.dirtree_rmdir

dirtree_link = _ida_idp.dirtree_link

dirtree_move = _ida_idp.dirtree_move

dirtree_rank = _ida_idp.dirtree_rank

dirtree_rminode = _ida_idp.dirtree_rminode

dirtree_segm_moved = _ida_idp.dirtree_segm_moved

enum_width_changed = _ida_idp.enum_width_changed

enum_flag_changed = _ida_idp.enum_flag_changed

enum_ordinal_changed = _ida_idp.enum_ordinal_changed


def gen_idb_event(*args) -> "void":
    r"""
    gen_idb_event(code)
    the kernel will use this function to generate idb_events

    @param code: (C++: idb_event::event_code_t) enum idb_event::event_code_t
    """
    return _ida_idp.gen_idb_event(*args)

def set_module_data(*args) -> "void *":
    r"""
    set_module_data(data_id, data_ptr) -> void *
    Starting from IDA v7.5 all modules should use the following 3 functions to
    handle idb specific static data because now the kernel supports opening and
    working with multiple idbs files simultaneously. See the source code of the
    processor modules in the SDK for the usage examples. Register pointer to
    database specific module data.

    @param data_id: (C++: int *) initially the pointed-to value must be 0, the kernel will fill
                    it with a unique id. once assigned, the data_id does not change.
    @param data_ptr: (C++: void *) pointer to the data to register
    @return: data_ptr. The registered pointer can later be retrieved using
             get_module_data()
    """
    return _ida_idp.set_module_data(*args)

def clr_module_data(*args) -> "void *":
    r"""
    clr_module_data(data_id) -> void *
    Unregister pointer to database specific module data.

    @param data_id: (C++: int) an data_id that was assigned by set_module_data()
    @return: previously registered pointer for the current database. it can be
             deallocated now. Multiple calls to this function with the same id are
             forbidden.
    """
    return _ida_idp.clr_module_data(*args)

def get_module_data(*args) -> "void *":
    r"""
    get_module_data(data_id) -> void *
    Get pointer to the database specific module data.

    @param data_id: (C++: int) data id that was initialized by set_module_data()
    @return: previously registered pointer for the current database
    """
    return _ida_idp.get_module_data(*args)
IDPOPT_CST = _ida_idp.IDPOPT_CST

IDPOPT_PRI_DEFAULT = _ida_idp.IDPOPT_PRI_DEFAULT

IDPOPT_PRI_HIGH = _ida_idp.IDPOPT_PRI_HIGH

IDPOPT_NUM_INT = _ida_idp.IDPOPT_NUM_INT

IDPOPT_NUM_CHAR = _ida_idp.IDPOPT_NUM_CHAR

IDPOPT_NUM_SHORT = _ida_idp.IDPOPT_NUM_SHORT

IDPOPT_NUM_RANGE = _ida_idp.IDPOPT_NUM_RANGE

IDPOPT_NUM_UNS = _ida_idp.IDPOPT_NUM_UNS

IDPOPT_BIT_UINT = _ida_idp.IDPOPT_BIT_UINT

IDPOPT_BIT_UCHAR = _ida_idp.IDPOPT_BIT_UCHAR

IDPOPT_BIT_USHORT = _ida_idp.IDPOPT_BIT_USHORT

IDPOPT_BIT_BOOL = _ida_idp.IDPOPT_BIT_BOOL

IDPOPT_STR_QSTRING = _ida_idp.IDPOPT_STR_QSTRING

IDPOPT_STR_LONG = _ida_idp.IDPOPT_STR_LONG

IDPOPT_I64_RANGE = _ida_idp.IDPOPT_I64_RANGE

IDPOPT_I64_UNS = _ida_idp.IDPOPT_I64_UNS

IDPOPT_CST_PARAMS = _ida_idp.IDPOPT_CST_PARAMS

IDPOPT_MBROFF = _ida_idp.IDPOPT_MBROFF

class num_range_t(object):
    r"""
    Proxy of C++ cfgopt_t::num_range_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _min, _max) -> num_range_t

        @param _min: int64
        @param _max: int64
        """
        _ida_idp.num_range_t_swiginit(self, _ida_idp.new_num_range_t(*args))
    minval = property(_ida_idp.num_range_t_minval_get, _ida_idp.num_range_t_minval_set, doc=r"""minval""")
    maxval = property(_ida_idp.num_range_t_maxval_get, _ida_idp.num_range_t_maxval_set, doc=r"""maxval""")
    __swig_destroy__ = _ida_idp.delete_num_range_t

# Register num_range_t in _ida_idp:
_ida_idp.num_range_t_swigregister(num_range_t)

class params_t(object):
    r"""
    Proxy of C++ cfgopt_t::params_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _p1, _p2) -> params_t

        @param _p1: int64
        @param _p2: int64
        """
        _ida_idp.params_t_swiginit(self, _ida_idp.new_params_t(*args))
    p1 = property(_ida_idp.params_t_p1_get, _ida_idp.params_t_p1_set, doc=r"""p1""")
    p2 = property(_ida_idp.params_t_p2_get, _ida_idp.params_t_p2_set, doc=r"""p2""")
    __swig_destroy__ = _ida_idp.delete_params_t

# Register params_t in _ida_idp:
_ida_idp.params_t_swigregister(params_t)


def register_cfgopts(*args) -> "bool":
    r"""
    register_cfgopts(opts, nopts, cb=None, obj=None) -> bool

    @param opts: cfgopt_t const []
    @param nopts: size_t
    @param cb: config_changed_cb_t *
    @param obj: void *
    """
    return _ida_idp.register_cfgopts(*args)

def cfg_get_cc_parm(*args) -> "char const *":
    r"""
    cfg_get_cc_parm(compid, name) -> char const *

    @param compid: comp_t
    @param name: char const *
    """
    return _ida_idp.cfg_get_cc_parm(*args)

def cfg_get_cc_header_path(*args) -> "char const *":
    r"""
    cfg_get_cc_header_path(compid) -> char const *

    @param compid: comp_t
    """
    return _ida_idp.cfg_get_cc_header_path(*args)

def cfg_get_cc_predefined_macros(*args) -> "char const *":
    r"""
    cfg_get_cc_predefined_macros(compid) -> char const *

    @param compid: comp_t
    """
    return _ida_idp.cfg_get_cc_predefined_macros(*args)

def process_config_directive(*args) -> "void":
    r"""
    process_config_directive(directive, priority=2)

    @param directive: char const *
    @param priority: int
    """
    return _ida_idp.process_config_directive(*args)

def assemble(*args) -> "bool":
    r"""
    assemble(ea, cs, ip, use32, line) -> bool
    Assemble an instruction into the database (display a warning if an error is found)

    @param ea: linear address of instruction
    @param cs: cs of instruction
    @param ip: ip of instruction
    @param use32: is 32bit segment?
    @param line: line to assemble

    @return: Boolean. True on success.
    """
    return _ida_idp.assemble(*args)

def ph_get_id(*args) -> "size_t":
    r"""
    ph_get_id() -> size_t
    Returns the 'ph.id' field
    """
    return _ida_idp.ph_get_id(*args)

def ph_get_version(*args) -> "size_t":
    r"""
    ph_get_version() -> size_t
    Returns the 'ph.version'
    """
    return _ida_idp.ph_get_version(*args)

def ph_get_flag(*args) -> "size_t":
    r"""
    ph_get_flag() -> size_t
    Returns the 'ph.flag'
    """
    return _ida_idp.ph_get_flag(*args)

def ph_get_cnbits(*args) -> "size_t":
    r"""
    ph_get_cnbits() -> size_t
    Returns the 'ph.cnbits'
    """
    return _ida_idp.ph_get_cnbits(*args)

def ph_get_dnbits(*args) -> "size_t":
    r"""
    ph_get_dnbits() -> size_t
    Returns the 'ph.dnbits'
    """
    return _ida_idp.ph_get_dnbits(*args)

def ph_get_reg_first_sreg(*args) -> "size_t":
    r"""
    ph_get_reg_first_sreg() -> size_t
    Returns the 'ph.reg_first_sreg'
    """
    return _ida_idp.ph_get_reg_first_sreg(*args)

def ph_get_reg_last_sreg(*args) -> "size_t":
    r"""
    ph_get_reg_last_sreg() -> size_t
    Returns the 'ph.reg_last_sreg'
    """
    return _ida_idp.ph_get_reg_last_sreg(*args)

def ph_get_segreg_size(*args) -> "size_t":
    r"""
    ph_get_segreg_size() -> size_t
    Returns the 'ph.segreg_size'
    """
    return _ida_idp.ph_get_segreg_size(*args)

def ph_get_reg_code_sreg(*args) -> "size_t":
    r"""
    ph_get_reg_code_sreg() -> size_t
    Returns the 'ph.reg_code_sreg'
    """
    return _ida_idp.ph_get_reg_code_sreg(*args)

def ph_get_reg_data_sreg(*args) -> "size_t":
    r"""
    ph_get_reg_data_sreg() -> size_t
    Returns the 'ph.reg_data_sreg'
    """
    return _ida_idp.ph_get_reg_data_sreg(*args)

def ph_get_icode_return(*args) -> "size_t":
    r"""
    ph_get_icode_return() -> size_t
    Returns the 'ph.icode_return'
    """
    return _ida_idp.ph_get_icode_return(*args)

def ph_get_instruc_start(*args) -> "size_t":
    r"""
    ph_get_instruc_start() -> size_t
    Returns the 'ph.instruc_start'
    """
    return _ida_idp.ph_get_instruc_start(*args)

def ph_get_instruc_end(*args) -> "size_t":
    r"""
    ph_get_instruc_end() -> size_t
    Returns the 'ph.instruc_end'
    """
    return _ida_idp.ph_get_instruc_end(*args)

def ph_get_tbyte_size(*args) -> "size_t":
    r"""
    ph_get_tbyte_size() -> size_t
    Returns the 'ph.tbyte_size' field as defined in he processor module
    """
    return _ida_idp.ph_get_tbyte_size(*args)

def ph_get_instruc(*args) -> "PyObject *":
    r"""
    ph_get_instruc() -> [(str, int), ...]
    Returns a list of tuples (instruction_name, instruction_feature) containing the
    instructions list as defined in he processor module
    """
    return _ida_idp.ph_get_instruc(*args)

def ph_get_regnames(*args) -> "PyObject *":
    r"""
    ph_get_regnames() -> [str, ...]
    Returns the list of register names as defined in the processor module
    """
    return _ida_idp.ph_get_regnames(*args)

def ph_get_operand_info(*args) -> "PyObject *":
    r"""
    ph_get_operand_info(ea, n) -> (int, int, int, int, int) or None
    Returns the operand information given an ea and operand number.

    @param ea: address
    @param n: operand number

    @return: Returns an idd_opinfo_t as a tuple: (modified, ea, reg_ival, regidx, value_size).
             Please refer to idd_opinfo_t structure in the SDK.
    """
    return _ida_idp.ph_get_operand_info(*args)

def ph_calcrel(*args) -> "bytevec_t *, size_t *":
    r"""
    ph_calcrel(ea)

    @param ea: ea_t
    """
    return _ida_idp.ph_calcrel(*args)

def ph_find_reg_value(*args) -> "uint64 *":
    r"""
    ph_find_reg_value(insn, reg) -> ssize_t

    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param reg: int
    """
    return _ida_idp.ph_find_reg_value(*args)

def ph_find_op_value(*args) -> "uint64 *":
    r"""
    ph_find_op_value(insn, op) -> ssize_t

    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param op: int
    """
    return _ida_idp.ph_find_op_value(*args)

def ph_get_reg_accesses(*args) -> "ssize_t":
    r"""
    ph_get_reg_accesses(accvec, insn, flags) -> ssize_t

    @param accvec: reg_accesses_t *
    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param flags: int
    """
    return _ida_idp.ph_get_reg_accesses(*args)
class IDP_Hooks(object):
    r"""
    Proxy of C++ IDP_Hooks class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _flags=0) -> IDP_Hooks

        @param _flags: uint32
        """
        if self.__class__ == IDP_Hooks:
            _self = None
        else:
            _self = self
        _ida_idp.IDP_Hooks_swiginit(self, _ida_idp.new_IDP_Hooks(_self, *args))

    def hook(self, *args) -> "bool":
        r"""
        hook(self) -> bool
        """
        return _ida_idp.IDP_Hooks_hook(self, *args)

    def unhook(self, *args) -> "bool":
        r"""
        unhook(self) -> bool
        """
        return _ida_idp.IDP_Hooks_unhook(self, *args)

    def ev_init(self, *args) -> "int":
        r"""
        ev_init(self, idp_modname) -> int
        The IDP module is just loaded.

        @param idp_modname: (const char *) processor module name
        @retval <0: on failure
        """
        return _ida_idp.IDP_Hooks_ev_init(self, *args)

    def ev_term(self, *args) -> "int":
        r"""
        ev_term(self) -> int
        The IDP module is being unloaded.
        """
        return _ida_idp.IDP_Hooks_ev_term(self, *args)

    def ev_newprc(self, *args) -> "int":
        r"""
        ev_newprc(self, pnum, keep_cfg) -> int
        Before changing processor type.

        @param pnum: (int) processor number in the array of processor names
        @param keep_cfg: (bool) true: do not modify kernel configuration
        @retval 1: ok
        @retval <0: prohibit
        """
        return _ida_idp.IDP_Hooks_ev_newprc(self, *args)

    def ev_newasm(self, *args) -> "int":
        r"""
        ev_newasm(self, asmnum) -> int
        Before setting a new assembler.

        @param asmnum: (int) See also ev_asm_installed
        """
        return _ida_idp.IDP_Hooks_ev_newasm(self, *args)

    def ev_newfile(self, *args) -> "int":
        r"""
        ev_newfile(self, fname) -> int
        A new file has been loaded.

        @param fname: (char *) input file name
        """
        return _ida_idp.IDP_Hooks_ev_newfile(self, *args)

    def ev_oldfile(self, *args) -> "int":
        r"""
        ev_oldfile(self, fname) -> int
        An old file has been loaded.

        @param fname: (char *) input file name
        """
        return _ida_idp.IDP_Hooks_ev_oldfile(self, *args)

    def ev_newbinary(self, *args) -> "int":
        r"""
        ev_newbinary(self, filename, fileoff, basepara, binoff, nbytes) -> int
        IDA is about to load a binary file.

        @param filename: (char *) binary file name
        @param fileoff: (qoff64_t) offset in the file
        @param basepara: (::ea_t) base loading paragraph
        @param binoff: (::ea_t) loader offset
        @param nbytes: (uint64) number of bytes to load
        """
        return _ida_idp.IDP_Hooks_ev_newbinary(self, *args)

    def ev_endbinary(self, *args) -> "int":
        r"""
        ev_endbinary(self, ok) -> int
        IDA has loaded a binary file.

        @param ok: (bool) file loaded successfully?
        """
        return _ida_idp.IDP_Hooks_ev_endbinary(self, *args)

    def ev_set_idp_options(self, *args) -> "int":
        r"""
        ev_set_idp_options(self, keyword, value_type, value, idb_loaded) -> int
        Set IDP-specific configuration option Also see set_options_t in config.hpp

        @param keyword: (const char *)
        @param value_type: (int)
        @param value: (const void *)
        @param idb_loaded: (bool) true if the ev_oldfile/ev_newfile events have been
                           generated
        @retval 1: ok
        @retval 0: not implemented
        @retval -1: error (and message in errbuf)
        """
        return _ida_idp.IDP_Hooks_ev_set_idp_options(self, *args)

    def ev_set_proc_options(self, *args) -> "int":
        r"""
        ev_set_proc_options(self, options, confidence) -> int
        Called if the user specified an option string in the command line: -p<processor
        name>:<options>. Can be used for setting a processor subtype. Also called if
        option string is passed to set_processor_type() and IDC's SetProcessorType().

        @param options: (const char *)
        @param confidence: (int) 0: loader's suggestion 1: user's decision
        @retval <0: if bad option string
        """
        return _ida_idp.IDP_Hooks_ev_set_proc_options(self, *args)

    def ev_ana_insn(self, *args) -> "bool":
        r"""
        ev_ana_insn(self, out) -> bool
        Analyze one instruction and fill 'out' structure. This function shouldn't change
        the database, flags or anything else. All these actions should be performed only
        by emu_insn() function. insn_t::ea contains address of instruction to analyze.

        @param out: (insn_t *)
        @return: length of the instruction in bytes, 0 if instruction can't be decoded.
        @retval 0: if instruction can't be decoded.
        """
        return _ida_idp.IDP_Hooks_ev_ana_insn(self, *args)

    def ev_emu_insn(self, *args) -> "bool":
        r"""
        ev_emu_insn(self, insn) -> bool
        Emulate instruction, create cross-references, plan to analyze subsequent
        instructions, modify flags etc. Upon entrance to this function, all information
        about the instruction is in 'insn' structure.

        @param insn: (const insn_t *)
        @retval 1: ok
        @retval -1: the kernel will delete the instruction
        """
        return _ida_idp.IDP_Hooks_ev_emu_insn(self, *args)

    def ev_out_header(self, *args) -> "int":
        r"""
        ev_out_header(self, outctx) -> int
        Function to produce start of disassembled text

        @param outctx: (outctx_t *)
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_out_header(self, *args)

    def ev_out_footer(self, *args) -> "int":
        r"""
        ev_out_footer(self, outctx) -> int
        Function to produce end of disassembled text

        @param outctx: (outctx_t *)
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_out_footer(self, *args)

    def ev_out_segstart(self, *args) -> "int":
        r"""
        ev_out_segstart(self, outctx, seg) -> int
        Function to produce start of segment

        @param outctx: (outctx_t *)
        @param seg: (segment_t *)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_out_segstart(self, *args)

    def ev_out_segend(self, *args) -> "int":
        r"""
        ev_out_segend(self, outctx, seg) -> int
        Function to produce end of segment

        @param outctx: (outctx_t *)
        @param seg: (segment_t *)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_out_segend(self, *args)

    def ev_out_assumes(self, *args) -> "int":
        r"""
        ev_out_assumes(self, outctx) -> int
        Function to produce assume directives when segment register value changes.

        @param outctx: (outctx_t *)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_out_assumes(self, *args)

    def ev_out_insn(self, *args) -> "bool":
        r"""
        ev_out_insn(self, outctx) -> bool
        Generate text representation of an instruction in 'ctx.insn' outctx_t provides
        functions to output the generated text. This function shouldn't change the
        database, flags or anything else. All these actions should be performed only by
        emu_insn() function.

        @param outctx: (outctx_t *)
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_out_insn(self, *args)

    def ev_out_mnem(self, *args) -> "int":
        r"""
        ev_out_mnem(self, outctx) -> int
        Generate instruction mnemonics. This callback should append the colored
        mnemonics to ctx.outbuf Optional notification, if absent, out_mnem will be
        called.

        @param outctx: (outctx_t *)
        @retval 1: if appended the mnemonics
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_out_mnem(self, *args)

    def ev_out_operand(self, *args) -> "bool":
        r"""
        ev_out_operand(self, outctx, op) -> bool
        Generate text representation of an instruction operand outctx_t provides
        functions to output the generated text. All these actions should be performed
        only by emu_insn() function.

        @param outctx: (outctx_t *)
        @param op: (const op_t *)
        @retval 1: ok
        @retval -1: operand is hidden
        """
        return _ida_idp.IDP_Hooks_ev_out_operand(self, *args)

    def ev_out_data(self, *args) -> "int":
        r"""
        ev_out_data(self, outctx, analyze_only) -> int
        Generate text representation of data items This function may change the database
        and create cross-references if analyze_only is set

        @param outctx: (outctx_t *)
        @param analyze_only: (bool)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_out_data(self, *args)

    def ev_out_label(self, *args) -> "int":
        r"""
        ev_out_label(self, outctx, colored_name) -> int
        The kernel is going to generate an instruction label line or a function header.

        @param outctx: (outctx_t *)
        @param colored_name: (const char *)
        @retval <0: if the kernel should not generate the label
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_out_label(self, *args)

    def ev_out_special_item(self, *args) -> "int":
        r"""
        ev_out_special_item(self, outctx, segtype) -> int
        Generate text representation of an item in a special segment i.e. absolute
        symbols, externs, communal definitions etc

        @param outctx: (outctx_t *)
        @param segtype: (uchar)
        @retval 1: ok
        @retval 0: not implemented
        @retval -1: overflow
        """
        return _ida_idp.IDP_Hooks_ev_out_special_item(self, *args)

    def ev_gen_stkvar_def(self, *args) -> "int":
        r"""
        ev_gen_stkvar_def(self, outctx, mptr, v) -> int
        Generate stack variable definition line Default line is varname = type ptr
        value, where 'type' is one of byte,word,dword,qword,tbyte

        @param outctx: (outctx_t *)
        @param mptr: (const member_t *)
        @param v: (sval_t)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_gen_stkvar_def(self, *args)

    def ev_gen_regvar_def(self, *args) -> "int":
        r"""
        ev_gen_regvar_def(self, outctx, v) -> int
        Generate register variable definition line.

        @param outctx: (outctx_t *)
        @param v: (regvar_t *)
        @retval >0: ok, generated the definition text
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_gen_regvar_def(self, *args)

    def ev_gen_src_file_lnnum(self, *args) -> "int":
        r"""
        ev_gen_src_file_lnnum(self, outctx, file, lnnum) -> int

        @param outctx: (outctx_t *) output context
        @param file: (const char *) source file (may be nullptr)
        @param lnnum: (size_t) line number
        @retval 1: directive has been generated
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_gen_src_file_lnnum(self, *args)

    def ev_creating_segm(self, *args) -> "int":
        r"""
        ev_creating_segm(self, seg) -> int
        A new segment is about to be created.

        @param seg: (segment_t *)
        @retval 1: ok
        @retval <0: segment should not be created
        """
        return _ida_idp.IDP_Hooks_ev_creating_segm(self, *args)

    def ev_moving_segm(self, *args) -> "int":
        r"""
        ev_moving_segm(self, seg, to, flags) -> int
        May the kernel move the segment?

        @param seg: (segment_t *) segment to move
        @param to: (::ea_t) new segment start address
        @param flags: (int) combination of Move segment flags
        @retval 0: yes
        @retval <0: the kernel should stop
        """
        return _ida_idp.IDP_Hooks_ev_moving_segm(self, *args)

    def ev_coagulate(self, *args) -> "int":
        r"""
        ev_coagulate(self, start_ea) -> int
        Try to define some unexplored bytes. This notification will be called if the
        kernel tried all possibilities and could not find anything more useful than to
        convert to array of bytes. The module can help the kernel and convert the bytes
        into something more useful.

        @param start_ea: (::ea_t)
        @return: number of converted bytes
        """
        return _ida_idp.IDP_Hooks_ev_coagulate(self, *args)

    def ev_undefine(self, *args) -> "int":
        r"""
        ev_undefine(self, ea) -> int
        An item in the database (insn or data) is being deleted.

        @param ea: (ea_t)
        @retval 1: do not delete srranges at the item end
        @retval 0: srranges can be deleted
        """
        return _ida_idp.IDP_Hooks_ev_undefine(self, *args)

    def ev_treat_hindering_item(self, *args) -> "int":
        r"""
        ev_treat_hindering_item(self, hindering_item_ea, new_item_flags, new_item_ea, new_item_length) -> int
        An item hinders creation of another item.

        @param hindering_item_ea: (::ea_t)
        @param new_item_flags: (flags_t) (0 for code)
        @param new_item_ea: (::ea_t)
        @param new_item_length: (::asize_t)
        @retval 0: no reaction
        @retval !=0: the kernel may delete the hindering item
        """
        return _ida_idp.IDP_Hooks_ev_treat_hindering_item(self, *args)

    def ev_rename(self, *args) -> "int":
        r"""
        ev_rename(self, ea, new_name) -> int
        The kernel is going to rename a byte.

        @param ea: (::ea_t)
        @param new_name: (const char *)
        @retval <0: if the kernel should not rename it.
        @retval 2: to inhibit the notification. I.e., the kernel should not rename, but
                   'set_name()' should return 'true'. also see renamed the return value
                   is ignored when kernel is going to delete name
        """
        return _ida_idp.IDP_Hooks_ev_rename(self, *args)

    def ev_is_far_jump(self, *args) -> "int":
        r"""
        ev_is_far_jump(self, icode) -> int
        is indirect far jump or call instruction? meaningful only if the processor has
        'near' and 'far' reference types

        @param icode: (int)
        @retval 0: not implemented
        @retval 1: yes
        @retval -1: no
        """
        return _ida_idp.IDP_Hooks_ev_is_far_jump(self, *args)

    def ev_is_sane_insn(self, *args) -> "int":
        r"""
        ev_is_sane_insn(self, insn, no_crefs) -> int
        Is the instruction sane for the current file type?.

        @param insn: (const insn_t*) the instruction
        @param no_crefs: (int) 1: the instruction has no code refs to it. ida just tries
                         to convert unexplored bytes to an instruction (but there is no
                         other reason to convert them into an instruction) 0: the
                         instruction is created because of some coderef, user request or
                         another weighty reason.
        @retval >=0: ok
        @retval <0: no, the instruction isn't likely to appear in the program
        """
        return _ida_idp.IDP_Hooks_ev_is_sane_insn(self, *args)

    def ev_is_cond_insn(self, *args) -> "int":
        r"""
        ev_is_cond_insn(self, insn) -> int
        Is conditional instruction?

        @param insn: (const insn_t *) instruction address
        @retval 1: yes
        @retval -1: no
        @retval 0: not implemented or not instruction
        """
        return _ida_idp.IDP_Hooks_ev_is_cond_insn(self, *args)

    def ev_is_call_insn(self, *args) -> "int":
        r"""
        ev_is_call_insn(self, insn) -> int
        Is the instruction a "call"?

        @param insn: (const insn_t *) instruction
        @retval 0: unknown
        @retval <0: no
        @retval 1: yes
        """
        return _ida_idp.IDP_Hooks_ev_is_call_insn(self, *args)

    def ev_is_ret_insn(self, *args) -> "int":
        r"""
        ev_is_ret_insn(self, insn, strict) -> int
        Is the instruction a "return"?

        @param insn: (const insn_t *) instruction
        @param strict: (bool) 1: report only ret instructions 0: include instructions
                       like "leave" which begins the function epilog
        @retval 0: unknown
        @retval <0: no
        @retval 1: yes
        """
        return _ida_idp.IDP_Hooks_ev_is_ret_insn(self, *args)

    def ev_may_be_func(self, *args) -> "int":
        r"""
        ev_may_be_func(self, insn, state) -> int
        Can a function start here?

        @param insn: (const insn_t*) the instruction
        @param state: (int) autoanalysis phase 0: creating functions 1: creating chunks
        @return: probability 1..100
        """
        return _ida_idp.IDP_Hooks_ev_may_be_func(self, *args)

    def ev_is_basic_block_end(self, *args) -> "int":
        r"""
        ev_is_basic_block_end(self, insn, call_insn_stops_block) -> int
        Is the current instruction end of a basic block?. This function should be
        defined for processors with delayed jump slots.

        @param insn: (const insn_t*) the instruction
        @param call_insn_stops_block: (bool)
        @retval 0: unknown
        @retval <0: no
        @retval 1: yes
        """
        return _ida_idp.IDP_Hooks_ev_is_basic_block_end(self, *args)

    def ev_is_indirect_jump(self, *args) -> "int":
        r"""
        ev_is_indirect_jump(self, insn) -> int
        Determine if instruction is an indirect jump. If CF_JUMP bit cannot describe all
        jump types jumps, please define this callback.

        @param insn: (const insn_t*) the instruction
        @retval 0: use CF_JUMP
        @retval 1: no
        @retval 2: yes
        """
        return _ida_idp.IDP_Hooks_ev_is_indirect_jump(self, *args)

    def ev_is_insn_table_jump(self, *args) -> "int":
        r"""
        ev_is_insn_table_jump(self) -> int
        Reserved.
        """
        return _ida_idp.IDP_Hooks_ev_is_insn_table_jump(self, *args)

    def ev_is_switch(self, *args) -> "int":
        r"""
        ev_is_switch(self, si, insn) -> int
        Find 'switch' idiom. It will be called for instructions marked with CF_JUMP.

        @param si: (switch_info_t *), out
        @param insn: (const insn_t *) instruction possibly belonging to a switch
        @retval 1: switch is found, 'si' is filled
        @retval -1: no switch found
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_is_switch(self, *args)

    def ev_calc_switch_cases(self, *args) -> "int":
        r"""
        ev_calc_switch_cases(self, casevec, targets, insn_ea, si) -> int
        Calculate case values and targets for a custom jump table.

        @param casevec: (::casevec_t *) vector of case values (may be nullptr)
        @param targets: (eavec_t *) corresponding target addresses (my be nullptr)
        @param insn_ea: (::ea_t) address of the 'indirect jump' instruction
        @param si: (switch_info_t *) switch information
        @retval 1: ok
        @retval <=0: failed
        """
        return _ida_idp.IDP_Hooks_ev_calc_switch_cases(self, *args)

    def ev_create_switch_xrefs(self, *args) -> "int":
        r"""
        ev_create_switch_xrefs(self, jumpea, si) -> int
        Create xrefs for a custom jump table.

        @param jumpea: (::ea_t) address of the jump insn
        @param si: (const switch_info_t *) switch information
        @return: must return 1 Must be implemented if module uses custom jump tables,
                 SWI_CUSTOM
        """
        return _ida_idp.IDP_Hooks_ev_create_switch_xrefs(self, *args)

    def ev_is_align_insn(self, *args) -> "int":
        r"""
        ev_is_align_insn(self, ea) -> int
        Is the instruction created only for alignment purposes?. Do not directly call
        this function, use is_align_insn()

        @param ea: (ea_t) - instruction address
        @retval number: of bytes in the instruction
        """
        return _ida_idp.IDP_Hooks_ev_is_align_insn(self, *args)

    def ev_is_alloca_probe(self, *args) -> "int":
        r"""
        ev_is_alloca_probe(self, ea) -> int
        Does the function at 'ea' behave as __alloca_probe?

        @param ea: (::ea_t)
        @retval 1: yes
        @retval 0: no
        """
        return _ida_idp.IDP_Hooks_ev_is_alloca_probe(self, *args)

    def ev_delay_slot_insn(self, *args) -> "PyObject *":
        r"""
        ev_delay_slot_insn(self, ea, bexec, fexec) -> PyObject *
        Get delay slot instruction

        @param ea: (::ea_t *) in: instruction address in question, out: (if the answer
                   is positive) if the delay slot contains valid insn: the address of
                   the delay slot insn else: BADADDR (invalid insn, e.g. a branch)
        @param bexec: (bool *) execute slot if jumping, initially set to 'true'
        @param fexec: (bool *) execute slot if not jumping, initally set to 'true'
        @retval 1: positive answer
        @retval <=0: ordinary insn
        @note: Input EA may point to the instruction with a delay slot or to the delay
               slot instruction itself.
        """
        return _ida_idp.IDP_Hooks_ev_delay_slot_insn(self, *args)

    def ev_is_sp_based(self, *args) -> "int":
        r"""
        ev_is_sp_based(self, mode, insn, op) -> int
        Check whether the operand is relative to stack pointer or frame pointer This
        event is used to determine how to output a stack variable If not implemented,
        then all operands are sp based by default. Implement this event only if some
        stack references use frame pointer instead of stack pointer.

        @param mode: (int *) out, combination of SP/FP operand flags
        @param insn: (const insn_t *)
        @param op: (const op_t *)
        @retval 0: not implemented
        @retval 1: ok
        """
        return _ida_idp.IDP_Hooks_ev_is_sp_based(self, *args)

    def ev_can_have_type(self, *args) -> "int":
        r"""
        ev_can_have_type(self, op) -> int
        Can the operand have a type as offset, segment, decimal, etc? (for example, a
        register AX can't have a type, meaning that the user can't change its
        representation. see bytes.hpp for information about types and flags)

        @param op: (const op_t *)
        @retval 0: unknown
        @retval <0: no
        @retval 1: yes
        """
        return _ida_idp.IDP_Hooks_ev_can_have_type(self, *args)

    def ev_cmp_operands(self, *args) -> "int":
        r"""
        ev_cmp_operands(self, op1, op2) -> int
        Compare instruction operands

        @param op1: (const op_t*)
        @param op2: (const op_t*)
        @retval 1: equal
        @retval -1: not equal
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_cmp_operands(self, *args)

    def ev_adjust_refinfo(self, *args) -> "int":
        r"""
        ev_adjust_refinfo(self, ri, ea, n, fd) -> int
        Called from apply_fixup before converting operand to reference. Can be used for
        changing the reference info. (e.g. the PPC module adds REFINFO_NOBASE for some
        references)

        @param ri: (refinfo_t *)
        @param ea: (::ea_t) instruction address
        @param n: (int) operand number
        @param fd: (const fixup_data_t *)
        @retval <0: do not create an offset
        @retval 0: not implemented or refinfo adjusted
        """
        return _ida_idp.IDP_Hooks_ev_adjust_refinfo(self, *args)

    def ev_get_operand_string(self, *args) -> "PyObject *":
        r"""
        ev_get_operand_string(self, insn, opnum) -> PyObject *
        Request text string for operand (cli, java, ...).

        @param insn: (const insn_t*) the instruction
        @param opnum: (int) operand number, -1 means any string operand
        @retval 0: no string (or empty string)
        @retval >0: original string length without terminating zero
        """
        return _ida_idp.IDP_Hooks_ev_get_operand_string(self, *args)

    def ev_get_reg_name(self, *args) -> "PyObject *":
        r"""
        ev_get_reg_name(self, reg, width, reghi) -> PyObject *
        Generate text representation of a register. Most processor modules do not need
        to implement this callback. It is useful only if processor_t::reg_names[reg]
        does not provide the correct register name.

        @param reg: (int) internal register number as defined in the processor module
        @param width: (size_t) register width in bytes
        @param reghi: (int) if not -1 then this function will return the register pair
        @retval -1: if error
        @retval strlen(buf): if success
        """
        return _ida_idp.IDP_Hooks_ev_get_reg_name(self, *args)

    def ev_str2reg(self, *args) -> "int":
        r"""
        ev_str2reg(self, regname) -> int
        Convert a register name to a register number. The register number is the
        register index in the processor_t::reg_names array Most processor modules do not
        need to implement this callback It is useful only if processor_t::reg_names[reg]
        does not provide the correct register names

        @param regname: (const char *)
        @retval register: number + 1
        @retval 0: not implemented or could not be decoded
        """
        return _ida_idp.IDP_Hooks_ev_str2reg(self, *args)

    def ev_get_autocmt(self, *args) -> "PyObject *":
        r"""
        ev_get_autocmt(self, insn) -> PyObject *

        @param insn: (const insn_t*) the instruction
        @retval 1: new comment has been generated
        @retval 0: callback has not been handled. the buffer must not be changed in this
                   case
        """
        return _ida_idp.IDP_Hooks_ev_get_autocmt(self, *args)

    def ev_get_bg_color(self, *args) -> "int":
        r"""
        ev_get_bg_color(self, color, ea) -> int
        Get item background color. Plugins can hook this callback to color disassembly
        lines dynamically

        @param color: (bgcolor_t *), out
        @param ea: (::ea_t)
        @retval 0: not implemented
        @retval 1: color set
        """
        return _ida_idp.IDP_Hooks_ev_get_bg_color(self, *args)

    def ev_is_jump_func(self, *args) -> "int":
        r"""
        ev_is_jump_func(self, pfn, jump_target, func_pointer) -> int
        Is the function a trivial "jump" function?.

        @param pfn: (func_t *)
        @param jump_target: (::ea_t *)
        @param func_pointer: (::ea_t *)
        @retval <0: no
        @retval 0: don't know
        @retval 1: yes, see 'jump_target' and 'func_pointer'
        """
        return _ida_idp.IDP_Hooks_ev_is_jump_func(self, *args)

    def ev_func_bounds(self, *args) -> "int":
        r"""
        ev_func_bounds(self, possible_return_code, pfn, max_func_end_ea) -> int
        find_func_bounds() finished its work. The module may fine tune the function
        bounds

        @param possible_return_code: (int *), in/out
        @param pfn: (func_t *)
        @param max_func_end_ea: (::ea_t) (from the kernel's point of view)
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_func_bounds(self, *args)

    def ev_verify_sp(self, *args) -> "int":
        r"""
        ev_verify_sp(self, pfn) -> int
        All function instructions have been analyzed. Now the processor module can
        analyze the stack pointer for the whole function

        @param pfn: (func_t *)
        @retval 0: ok
        @retval <0: bad stack pointer
        """
        return _ida_idp.IDP_Hooks_ev_verify_sp(self, *args)

    def ev_verify_noreturn(self, *args) -> "int":
        r"""
        ev_verify_noreturn(self, pfn) -> int
        The kernel wants to set 'noreturn' flags for a function.

        @param pfn: (func_t *)
        @retval 0: ok. any other value: do not set 'noreturn' flag
        """
        return _ida_idp.IDP_Hooks_ev_verify_noreturn(self, *args)

    def ev_create_func_frame(self, *args) -> "int":
        r"""
        ev_create_func_frame(self, pfn) -> int
        Create a function frame for a newly created function Set up frame size, its
        attributes etc

        @param pfn: (func_t *)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_create_func_frame(self, *args)

    def ev_get_frame_retsize(self, *args) -> "int":
        r"""
        ev_get_frame_retsize(self, frsize, pfn) -> int
        Get size of function return address in bytes If this event is not implemented,
        the kernel will assume
        * 8 bytes for 64-bit function
        * 4 bytes for 32-bit function
        * 2 bytes otherwise

        @param frsize: (int *) frame size (out)
        @param pfn: (const func_t *), can't be nullptr
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_frame_retsize(self, *args)

    def ev_get_stkvar_scale_factor(self, *args) -> "int":
        r"""
        ev_get_stkvar_scale_factor(self) -> int
        Should stack variable references be multiplied by a coefficient before being
        used in the stack frame?. Currently used by TMS320C55 because the references
        into the stack should be multiplied by 2

        @return: scaling factor
        @retval 0: not implemented
        @note: PR_SCALE_STKVARS should be set to use this callback
        """
        return _ida_idp.IDP_Hooks_ev_get_stkvar_scale_factor(self, *args)

    def ev_demangle_name(self, *args) -> "PyObject *":
        r"""
        ev_demangle_name(self, name, disable_mask, demreq) -> PyObject *
        Demangle a C++ (or another language) name into a user-readable string. This
        event is called by demangle_name()

        @param name: (const char *) mangled name
        @param disable_mask: (uint32) flags to inhibit parts of output or compiler
                             info/other (see MNG_)
        @param demreq: (demreq_type_t) operation to perform
        @retval 1: if success
        @retval 0: not implemented
        @note: if you call demangle_name() from the handler, protect against recursion!
        """
        return _ida_idp.IDP_Hooks_ev_demangle_name(self, *args)

    def ev_add_cref(self, *args) -> "int":
        r"""
        ev_add_cref(self, _from, to, type) -> int
        A code reference is being created.

        @param from: (::ea_t)
        @param to: (::ea_t)
        @param type: (cref_t)
        @retval <0: cancel cref creation
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_add_cref(self, *args)

    def ev_add_dref(self, *args) -> "int":
        r"""
        ev_add_dref(self, _from, to, type) -> int
        A data reference is being created.

        @param from: (::ea_t)
        @param to: (::ea_t)
        @param type: (dref_t)
        @retval <0: cancel dref creation
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_add_dref(self, *args)

    def ev_del_cref(self, *args) -> "int":
        r"""
        ev_del_cref(self, _from, to, expand) -> int
        A code reference is being deleted.

        @param from: (::ea_t)
        @param to: (::ea_t)
        @param expand: (bool)
        @retval <0: cancel cref deletion
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_del_cref(self, *args)

    def ev_del_dref(self, *args) -> "int":
        r"""
        ev_del_dref(self, _from, to) -> int
        A data reference is being deleted.

        @param from: (::ea_t)
        @param to: (::ea_t)
        @retval <0: cancel dref deletion
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_del_dref(self, *args)

    def ev_coagulate_dref(self, *args) -> "int":
        r"""
        ev_coagulate_dref(self, _from, to, may_define, code_ea) -> int
        Data reference is being analyzed. plugin may correct 'code_ea' (e.g. for thumb
        mode refs, we clear the last bit)

        @param from: (::ea_t)
        @param to: (::ea_t)
        @param may_define: (bool)
        @param code_ea: (::ea_t *)
        @retval <0: failed dref analysis, >0 done dref analysis
        @retval 0: not implemented or continue
        """
        return _ida_idp.IDP_Hooks_ev_coagulate_dref(self, *args)

    def ev_may_show_sreg(self, *args) -> "int":
        r"""
        ev_may_show_sreg(self, current_ea) -> int
        The kernel wants to display the segment registers in the messages window.

        @param current_ea: (::ea_t)
        @retval <0: if the kernel should not show the segment registers. (assuming that
                    the module has done it)
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_may_show_sreg(self, *args)

    def ev_auto_queue_empty(self, *args) -> "int":
        r"""
        ev_auto_queue_empty(self, type) -> int
        One analysis queue is empty.

        @param type: (atype_t)
        @retval void: see also idb_event::auto_empty_finally
        """
        return _ida_idp.IDP_Hooks_ev_auto_queue_empty(self, *args)

    def ev_validate_flirt_func(self, *args) -> "int":
        r"""
        ev_validate_flirt_func(self, start_ea, funcname) -> int
        Flirt has recognized a library function. This callback can be used by a plugin
        or proc module to intercept it and validate such a function.

        @param start_ea: (::ea_t)
        @param funcname: (const char *)
        @retval -1: do not create a function,
        @retval 0: function is validated
        """
        return _ida_idp.IDP_Hooks_ev_validate_flirt_func(self, *args)

    def ev_adjust_libfunc_ea(self, *args) -> "int":
        r"""
        ev_adjust_libfunc_ea(self, sig, libfun, ea) -> int
        Called when a signature module has been matched against bytes in the database.
        This is used to compute the offset at which a particular module's libfunc should
        be applied.

        @param sig: (const idasgn_t *)
        @param libfun: (const libfunc_t *)
        @param ea: (::ea_t *)
        @note: 'ea' initially contains the ea_t of the start of the pattern match
        @retval 1: the ea_t pointed to by the third argument was modified.
        @retval <=0: not modified. use default algorithm.
        """
        return _ida_idp.IDP_Hooks_ev_adjust_libfunc_ea(self, *args)

    def ev_assemble(self, *args) -> "PyObject *":
        r"""
        ev_assemble(self, ea, cs, ip, use32, line) -> PyObject *
        Assemble an instruction. (display a warning if an error is found).

        @param ea: (::ea_t) linear address of instruction
        @param cs: (::ea_t) cs of instruction
        @param ip: (::ea_t) ip of instruction
        @param use32: (bool) is 32bit segment?
        @param line: (const char *) line to assemble
        @return: size of the instruction in bytes
        """
        return _ida_idp.IDP_Hooks_ev_assemble(self, *args)

    def ev_extract_address(self, *args) -> "int":
        r"""
        ev_extract_address(self, out_ea, screen_ea, string, position) -> int
        Extract address from a string.

        @param out_ea: (ea_t *), out
        @param screen_ea: (ea_t)
        @param string: (const char *)
        @param position: (size_t)
        @retval 1: ok
        @retval 0: kernel should use the standard algorithm
        @retval -1: error
        """
        return _ida_idp.IDP_Hooks_ev_extract_address(self, *args)

    def ev_realcvt(self, *args) -> "int":
        r"""
        ev_realcvt(self, m, e, swt) -> int
        Floating point -> IEEE conversion

        @param m: (void *) ptr to processor-specific floating point value
        @param e: (fpvalue_t *) IDA representation of a floating point value
        @param swt: (uint16) operation (see realcvt() in ieee.h)
        @retval 0: not implemented
        @retval 1: ok
        @retval unknown
        """
        return _ida_idp.IDP_Hooks_ev_realcvt(self, *args)

    def ev_gen_asm_or_lst(self, *args) -> "int":
        r"""
        ev_gen_asm_or_lst(self, starting, fp, is_asm, flags, outline) -> int

        @param starting: (bool) beginning listing generation
        @param fp: (FILE *) output file
        @param is_asm: (bool) true:assembler, false:listing
        @param flags: (int) flags passed to gen_file()
        @param outline: (html_line_cb_t **) ptr to ptr to outline callback. if this
                        callback is defined for this code, it will be used by the kernel
                        to output the generated lines
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_gen_asm_or_lst(self, *args)

    def ev_gen_map_file(self, *args) -> "int":
        r"""
        ev_gen_map_file(self, nlines, fp) -> int
        Generate map file. If not implemented the kernel itself will create the map
        file.

        @param nlines: (int *) number of lines in map file (-1 means write error)
        @param fp: (FILE *) output file
        @retval 0: not implemented
        @retval 1: ok
        @retval -1: write error
        """
        return _ida_idp.IDP_Hooks_ev_gen_map_file(self, *args)

    def ev_create_flat_group(self, *args) -> "int":
        r"""
        ev_create_flat_group(self, image_base, bitness, dataseg_sel) -> int
        Create special segment representing the flat group.

        @param image_base: (::ea_t)
        @param bitness: (int)
        @param dataseg_sel: (::sel_t) return value is ignored
        """
        return _ida_idp.IDP_Hooks_ev_create_flat_group(self, *args)

    def ev_getreg(self, *args) -> "int":
        r"""
        ev_getreg(self, regval, regnum) -> int
        IBM PC only internal request, should never be used for other purpose Get
        register value by internal index

        @param regval: (uval_t *), out
        @param regnum: (int)
        @retval 1: ok
        @retval 0: not implemented
        @retval -1: failed (undefined value or bad regnum)
        """
        return _ida_idp.IDP_Hooks_ev_getreg(self, *args)

    def ev_analyze_prolog(self, *args) -> "int":
        r"""
        ev_analyze_prolog(self, ea) -> int
        Analyzes function prolog, epilog, and updates purge, and function attributes

        @param ea: (::ea_t) start of function
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_analyze_prolog(self, *args)

    def ev_calc_spdelta(self, *args) -> "int":
        r"""
        ev_calc_spdelta(self, spdelta, insn) -> int
        Calculate amount of change to sp for the given insn. This event is required to
        decompile code snippets.

        @param spdelta: (sval_t *)
        @param insn: (const insn_t *)
        @retval 1: ok
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_calc_spdelta(self, *args)

    def ev_calcrel(self, *args) -> "int":
        r"""
        ev_calcrel(self) -> int
        Reserved.
        """
        return _ida_idp.IDP_Hooks_ev_calcrel(self, *args)

    def ev_find_reg_value(self, *args) -> "PyObject *":
        r"""
        ev_find_reg_value(self, pinsn, reg) -> PyObject *
        Find register value via a register tracker. The returned value in 'out' is valid
        before executing the instruction.

        @param pinsn: (const insn_t *) instruction
        @param reg: (int) register index
        @retval 1: if implemented, and value was found
        @retval 0: not implemented, -1 decoding failed, or no value found
        """
        return _ida_idp.IDP_Hooks_ev_find_reg_value(self, *args)

    def ev_find_op_value(self, *args) -> "PyObject *":
        r"""
        ev_find_op_value(self, pinsn, opn) -> PyObject *
        Find operand value via a register tracker. The returned value in 'out' is valid
        before executing the instruction.

        @param pinsn: (const insn_t *) instruction
        @param opn: (int) operand index
        @retval 1: if implemented, and value was found
        @retval 0: not implemented, -1 decoding failed, or no value found
        """
        return _ida_idp.IDP_Hooks_ev_find_op_value(self, *args)

    def ev_replaying_undo(self, *args) -> "int":
        r"""
        ev_replaying_undo(self, action_name, vec, is_undo) -> int
        Replaying an undo/redo buffer

        @param action_name: (const char *) action that we perform undo/redo for. may be
                            nullptr for intermediary buffers.
        @param vec: (const undo_records_t *)
        @param is_undo: (bool) true if performing undo, false if performing redo This
                        event may be generated multiple times per undo/redo
        """
        return _ida_idp.IDP_Hooks_ev_replaying_undo(self, *args)

    def ev_ending_undo(self, *args) -> "int":
        r"""
        ev_ending_undo(self, action_name, is_undo) -> int
        Ended undoing/redoing an action

        @param action_name: (const char *) action that we finished undoing/redoing. is
                            not nullptr.
        @param is_undo: (bool) true if performing undo, false if performing redo
        """
        return _ida_idp.IDP_Hooks_ev_ending_undo(self, *args)

    def ev_set_code16_mode(self, *args) -> "int":
        r"""
        ev_set_code16_mode(self, ea, code16) -> int
        Some processors have ISA 16-bit mode e.g. ARM Thumb mode, PPC VLE, MIPS16 Set
        ISA 16-bit mode

        @param ea: (ea_t) address to set new ISA mode
        @param code16: (bool) true for 16-bit mode, false for 32-bit mode
        """
        return _ida_idp.IDP_Hooks_ev_set_code16_mode(self, *args)

    def ev_get_code16_mode(self, *args) -> "int":
        r"""
        ev_get_code16_mode(self, ea) -> int
        Get ISA 16-bit mode

        @param ea: (ea_t) address to get the ISA mode
        @retval 1: 16-bit mode
        @retval 0: not implemented or 32-bit mode
        """
        return _ida_idp.IDP_Hooks_ev_get_code16_mode(self, *args)

    def ev_get_procmod(self, *args) -> "int":
        r"""
        ev_get_procmod(self) -> int
        Get pointer to the processor module object. All processor modules must implement
        this. The pointer is returned as size_t.
        """
        return _ida_idp.IDP_Hooks_ev_get_procmod(self, *args)

    def ev_asm_installed(self, *args) -> "int":
        r"""
        ev_asm_installed(self, asmnum) -> int
        After setting a new assembler

        @param asmnum: (int) See also ev_newasm
        """
        return _ida_idp.IDP_Hooks_ev_asm_installed(self, *args)

    def ev_get_reg_accesses(self, *args) -> "int":
        r"""
        ev_get_reg_accesses(self, accvec, insn, flags) -> int
        Get info about the registers that are used/changed by an instruction.

        @param accvec: (reg_accesses_t*) out: info about accessed registers
        @param insn: (const insn_t *) instruction in question
        @param flags: (int) reserved, must be 0
        @retval -1: if accvec is nullptr
        @retval 1: found the requested access (and filled accvec)
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_reg_accesses(self, *args)

    def ev_is_control_flow_guard(self, *args) -> "int":
        r"""
        ev_is_control_flow_guard(self, p_reg, insn) -> int
        Detect if an instruction is a "thunk call" to a flow guard function (equivalent
        to call reg/return/nop)

        @param p_reg: (int *) indirect register number, may be -1
        @param insn: (const insn_t *) call/jump instruction
        @retval -1: no thunk detected
        @retval 1: indirect call
        @retval 2: security check routine call (NOP)
        @retval 3: return thunk
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_is_control_flow_guard(self, *args)

    def ev_create_merge_handlers(self, *args) -> "int":
        r"""
        ev_create_merge_handlers(self, md) -> int
        Create merge handlers, if needed

        @param md: (::merge_data_t *) This event is generated immediately after opening
                   idbs.
        @return: must be 0
        """
        return _ida_idp.IDP_Hooks_ev_create_merge_handlers(self, *args)

    def ev_privrange_changed(self, *args) -> "int":
        r"""
        ev_privrange_changed(self, old_privrange, delta) -> int
        Privrange interval has been moved to a new location. Most common actions to be
        done by module in this case: fix indices of netnodes used by module

        @param old_privrange: (const range_t *) - old privrange interval
        @param delta: (::adiff_t)
        @return: 0 Ok
        -1 error (and message in errbuf)
        """
        return _ida_idp.IDP_Hooks_ev_privrange_changed(self, *args)

    def ev_next_exec_insn(self, *args) -> "int":
        r"""
        ev_next_exec_insn(self, target, ea, tid, getreg, regvalues) -> int
        Get next address to be executed This function must return the next address to be
        executed. If the instruction following the current one is executed, then it must
        return BADADDR Usually the instructions to consider are: jumps, branches, calls,
        returns. This function is essential if the 'single step' is not supported in
        hardware.

        @param target: (::ea_t *), out: pointer to the answer
        @param ea: (::ea_t) instruction address
        @param tid: (int) current therad id
        @param getreg: (::processor_t::regval_getter_t *) function to get register
                       values
        @param regvalues: (const regval_t *) register values array
        @retval 0: unimplemented
        @retval 1: implemented
        """
        return _ida_idp.IDP_Hooks_ev_next_exec_insn(self, *args)

    def ev_calc_step_over(self, *args) -> "int":
        r"""
        ev_calc_step_over(self, target, ip) -> int
        Calculate the address of the instruction which will be executed after "step
        over". The kernel will put a breakpoint there. If the step over is equal to step
        into or we cannot calculate the address, return BADADDR.

        @param target: (::ea_t *) pointer to the answer
        @param ip: (::ea_t) instruction address
        @retval 0: unimplemented
        @retval 1: implemented
        """
        return _ida_idp.IDP_Hooks_ev_calc_step_over(self, *args)

    def ev_calc_next_eas(self, *args) -> "int":
        r"""
        ev_calc_next_eas(self, res, insn, over) -> int
        Calculate list of addresses the instruction in 'insn' may pass control to. This
        callback is required for source level debugging.

        @param res: (eavec_t *), out: array for the results.
        @param insn: (const insn_t*) the instruction
        @param over: (bool) calculate for step over (ignore call targets)
        @retval <0: incalculable (indirect jumps, for example)
        @retval >=0: number of addresses of called functions in the array. They must be
                     put at the beginning of the array (0 if over=true)
        """
        return _ida_idp.IDP_Hooks_ev_calc_next_eas(self, *args)

    def ev_get_macro_insn_head(self, *args) -> "int":
        r"""
        ev_get_macro_insn_head(self, head, ip) -> int
        Calculate the start of a macro instruction. This notification is called if IP
        points to the middle of an instruction

        @param head: (::ea_t *), out: answer, BADADDR means normal instruction
        @param ip: (::ea_t) instruction address
        @retval 0: unimplemented
        @retval 1: implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_macro_insn_head(self, *args)

    def ev_get_dbr_opnum(self, *args) -> "int":
        r"""
        ev_get_dbr_opnum(self, opnum, insn) -> int
        Get the number of the operand to be displayed in the debugger reference view
        (text mode).

        @param opnum: (int *) operand number (out, -1 means no such operand)
        @param insn: (const insn_t*) the instruction
        @retval 0: unimplemented
        @retval 1: implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_dbr_opnum(self, *args)

    def ev_insn_reads_tbit(self, *args) -> "int":
        r"""
        ev_insn_reads_tbit(self, insn, getreg, regvalues) -> int
        Check if insn will read the TF bit.

        @param insn: (const insn_t*) the instruction
        @param getreg: (::processor_t::regval_getter_t *) function to get register
                       values
        @param regvalues: (const regval_t *) register values array
        @retval 2: yes, will generate 'step' exception
        @retval 1: yes, will store the TF bit in memory
        @retval 0: no
        """
        return _ida_idp.IDP_Hooks_ev_insn_reads_tbit(self, *args)

    def ev_clean_tbit(self, *args) -> "int":
        r"""
        ev_clean_tbit(self, ea, getreg, regvalues) -> int
        Clear the TF bit after an insn like pushf stored it in memory.

        @param ea: (::ea_t) instruction address
        @param getreg: (::processor_t::regval_getter_t *) function to get register
                       values
        @param regvalues: (const regval_t *) register values array
        @retval 1: ok
        @retval 0: failed
        """
        return _ida_idp.IDP_Hooks_ev_clean_tbit(self, *args)

    def ev_get_reg_info(self, *args) -> "int":
        r"""
        ev_get_reg_info(self, main_regname, bitrange, regname) -> int
        Get register information by its name. example: "ah" returns:
        * main_regname="eax"
        * bitrange_t = { offset==8, nbits==8 }

        This callback may be unimplemented if the register names are all present in
        processor_t::reg_names and they all have the same size

        @param main_regname: (const char **), out
        @param bitrange: (bitrange_t *), out: position and size of the value within
                         'main_regname' (empty bitrange == whole register)
        @param regname: (const char *)
        @retval 1: ok
        @retval -1: failed (not found)
        @retval 0: unimplemented
        """
        return _ida_idp.IDP_Hooks_ev_get_reg_info(self, *args)

    def ev_update_call_stack(self, *args) -> "int":
        r"""
        ev_update_call_stack(self, stack, tid, getreg, regvalues) -> int
        Calculate the call stack trace for the given thread. This callback is invoked
        when the process is suspended and should fill the 'trace' object with the
        information about the current call stack. Note that this callback is NOT invoked
        if the current debugger backend implements stack tracing via
        debugger_t::event_t::ev_update_call_stack. The debugger-specific algorithm takes
        priority. Implementing this callback in the processor module is useful when
        multiple debugging platforms follow similar patterns, and thus the same
        processor-specific algorithm can be used for different platforms.

        @param stack: (call_stack_t *) result
        @param tid: (int) thread id
        @param getreg: (::processor_t::regval_getter_t *) function to get register
                       values
        @param regvalues: (const regval_t *) register values array
        @retval 1: ok
        @retval -1: failed
        @retval 0: unimplemented
        """
        return _ida_idp.IDP_Hooks_ev_update_call_stack(self, *args)

    def ev_setup_til(self, *args) -> "int":
        r"""
        ev_setup_til(self) -> int
        Setup default type libraries. (called after loading a new file into the
        database). The processor module may load tils, setup memory model and perform
        other actions required to set up the type system. This is an optional callback.
        @retval void
        """
        return _ida_idp.IDP_Hooks_ev_setup_til(self, *args)

    def ev_get_abi_info(self, *args) -> "int":
        r"""
        ev_get_abi_info(self, abi_names, abi_opts, comp) -> int
        Get all possible ABI names and optional extensions for given compiler
        abiname/option is a string entirely consisting of letters, digits and underscore

        @param abi_names: (qstrvec_t *) - all possible ABis each in form abiname-
                          opt1-opt2-...
        @param abi_opts: (qstrvec_t *) - array of all possible options in form
                         "opt:description" or opt:hint-line#description
        @param comp: (comp_t) - compiler ID
        @retval 0: not implemented
        @retval 1: ok
        """
        return _ida_idp.IDP_Hooks_ev_get_abi_info(self, *args)

    def ev_max_ptr_size(self, *args) -> "int":
        r"""
        ev_max_ptr_size(self) -> int
        Get maximal size of a pointer in bytes.

        @return: max possible size of a pointer
        """
        return _ida_idp.IDP_Hooks_ev_max_ptr_size(self, *args)

    def ev_get_default_enum_size(self, *args) -> "int":
        r"""
        ev_get_default_enum_size(self) -> int
        Get default enum size. Not generated anymore. inf_get_cc_size_e() is used
        instead
        """
        return _ida_idp.IDP_Hooks_ev_get_default_enum_size(self, *args)

    def ev_get_cc_regs(self, *args) -> "int":
        r"""
        ev_get_cc_regs(self, regs, cc) -> int
        Get register allocation convention for given calling convention

        @param regs: (callregs_t *), out
        @param cc: (cm_t)
        @retval 1
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_cc_regs(self, *args)

    def ev_get_simd_types(self, *args) -> "int":
        r"""
        ev_get_simd_types(self, out, simd_attrs, argloc, create_tifs) -> int
        Get SIMD-related types according to given attributes ant/or argument location

        @param out: (::simd_info_vec_t *)
        @param simd_attrs: (const simd_info_t *), may be nullptr
        @param argloc: (const argloc_t *), may be nullptr
        @param create_tifs: (bool) return valid tinfo_t objects, create if neccessary
        @retval number: of found types
        @retval -1: error If name==nullptr, initialize all SIMD types
        """
        return _ida_idp.IDP_Hooks_ev_get_simd_types(self, *args)

    def ev_calc_cdecl_purged_bytes(self, *args) -> "int":
        r"""
        ev_calc_cdecl_purged_bytes(self, ea) -> int
        Calculate number of purged bytes after call.

        @param ea: (::ea_t) address of the call instruction
        @return: number of purged bytes (usually add sp, N)
        """
        return _ida_idp.IDP_Hooks_ev_calc_cdecl_purged_bytes(self, *args)

    def ev_calc_purged_bytes(self, *args) -> "int":
        r"""
        ev_calc_purged_bytes(self, p_purged_bytes, fti) -> int
        Calculate number of purged bytes by the given function type.

        @param p_purged_bytes: (int *) ptr to output
        @param fti: (const func_type_data_t *) func type details
        @retval 1
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_calc_purged_bytes(self, *args)

    def ev_calc_retloc(self, *args) -> "int":
        r"""
        ev_calc_retloc(self, retloc, rettype, cc) -> int
        Calculate return value location.

        @param retloc: (argloc_t *)
        @param rettype: (const tinfo_t *)
        @param cc: (cm_t)
        @retval 0: not implemented
        @retval 1: ok,
        @retval -1: error
        """
        return _ida_idp.IDP_Hooks_ev_calc_retloc(self, *args)

    def ev_calc_arglocs(self, *args) -> "int":
        r"""
        ev_calc_arglocs(self, fti) -> int
        Calculate function argument locations. This callback should fill retloc, all
        arglocs, and stkargs. This callback is never called for CM_CC_SPECIAL functions.

        @param fti: (func_type_data_t *) points to the func type info
        @retval 0: not implemented
        @retval 1: ok
        @retval -1: error
        """
        return _ida_idp.IDP_Hooks_ev_calc_arglocs(self, *args)

    def ev_calc_varglocs(self, *args) -> "int":
        r"""
        ev_calc_varglocs(self, ftd, aux_regs, aux_stkargs, nfixed) -> int
        Calculate locations of the arguments that correspond to '...'.

        @param ftd: (func_type_data_t *), inout: info about all arguments (including
                    varargs)
        @param aux_regs: (regobjs_t *) buffer for hidden register arguments, may be
                         nullptr
        @param aux_stkargs: (relobj_t *) buffer for hidden stack arguments, may be
                            nullptr
        @param nfixed: (int) number of fixed arguments
        @retval 0: not implemented
        @retval 1: ok
        @retval -1: error On some platforms variadic calls require passing additional
                    information: for example, number of floating variadic arguments must
                    be passed in rax on gcc-x64. The locations and values that
                    constitute this additional information are returned in the buffers
                    pointed by aux_regs and aux_stkargs
        """
        return _ida_idp.IDP_Hooks_ev_calc_varglocs(self, *args)

    def ev_adjust_argloc(self, *args) -> "int":
        r"""
        ev_adjust_argloc(self, argloc, optional_type, size) -> int
        Adjust argloc according to its type/size and platform endianess

        @param argloc: (argloc_t *), inout
        @param type: (const tinfo_t *), may be nullptr nullptr means primitive type of
                     given size
        @param size: (int) 'size' makes no sense if type != nullptr (type->get_size()
                     should be used instead)
        @retval 0: not implemented
        @retval 1: ok
        @retval -1: error
        """
        return _ida_idp.IDP_Hooks_ev_adjust_argloc(self, *args)

    def ev_lower_func_type(self, *args) -> "int":
        r"""
        ev_lower_func_type(self, argnums, fti) -> int
        Get function arguments which should be converted to pointers when lowering
        function prototype. The processor module can also modify 'fti' in order to make
        non-standard conversion of some arguments.

        @param argnums: (intvec_t *), out - numbers of arguments to be converted to
                        pointers in acsending order
        @param fti: (func_type_data_t *), inout func type details (special values -1/-2
                    for return value - position of hidden 'retstr' argument: -1 - at the
                    beginning, -2 - at the end)
        @retval 0: not implemented
        @retval 1: argnums was filled
        @retval 2: argnums was filled and made substantial changes to fti
        """
        return _ida_idp.IDP_Hooks_ev_lower_func_type(self, *args)

    def ev_equal_reglocs(self, *args) -> "int":
        r"""
        ev_equal_reglocs(self, a1, a2) -> int
        Are 2 register arglocs the same?. We need this callback for the pc module.

        @param a1: (argloc_t *)
        @param a2: (argloc_t *)
        @retval 1: yes
        @retval -1: no
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_equal_reglocs(self, *args)

    def ev_use_stkarg_type(self, *args) -> "int":
        r"""
        ev_use_stkarg_type(self, ea, arg) -> int
        Use information about a stack argument.

        @param ea: (::ea_t) address of the push instruction which pushes the function
                   argument into the stack
        @param arg: (const funcarg_t *) argument info
        @retval 1: ok
        @retval <=0: failed, the kernel will create a comment with the argument name or
                     type for the instruction
        """
        return _ida_idp.IDP_Hooks_ev_use_stkarg_type(self, *args)

    def ev_use_regarg_type(self, *args) -> "PyObject *":
        r"""
        ev_use_regarg_type(self, ea, rargs) -> PyObject *
        Use information about register argument.

        @param ea: (::ea_t) address of the instruction
        @param rargs: (const funcargvec_t *) vector of register arguments (including
                      regs extracted from scattered arguments)
        @retval 1
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_use_regarg_type(self, *args)

    def ev_use_arg_types(self, *args) -> "int":
        r"""
        ev_use_arg_types(self, ea, fti, rargs) -> int
        Use information about callee arguments.

        @param ea: (::ea_t) address of the call instruction
        @param fti: (func_type_data_t *) info about function type
        @param rargs: (funcargvec_t *) array of register arguments
        @retval 1: (and removes handled arguments from fti and rargs)
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_use_arg_types(self, *args)

    def ev_arg_addrs_ready(self, *args) -> "int":
        r"""
        ev_arg_addrs_ready(self, caller, n, tif, addrs) -> int
        Argument address info is ready.

        @param caller: (::ea_t)
        @param n: (int) number of formal arguments
        @param tif: (tinfo_t *) call prototype
        @param addrs: (::ea_t *) argument intilization addresses
        @retval <0: do not save into idb; other values mean "ok to save"
        """
        return _ida_idp.IDP_Hooks_ev_arg_addrs_ready(self, *args)

    def ev_decorate_name(self, *args) -> "PyObject *":
        r"""
        ev_decorate_name(self, name, mangle, cc, optional_type) -> PyObject *
        Decorate/undecorate a C symbol name.

        @param name: (const char *) name of symbol
        @param mangle: (bool) true-mangle, false-unmangle
        @param cc: (cm_t) calling convention
        @param optional_type: tinfo_t const *
        @retval 1: if success
        @retval 0: not implemented or failed
        """
        return _ida_idp.IDP_Hooks_ev_decorate_name(self, *args)

    def ev_arch_changed(self, *args) -> "int":
        r"""
        ev_arch_changed(self) -> int
        The loader is done parsing arch-related information, which the processor module
        might want to use to finish its initialization.
        @retval 1: if success
        @retval 0: not implemented or failed
        """
        return _ida_idp.IDP_Hooks_ev_arch_changed(self, *args)

    def ev_get_stkarg_area_info(self, *args) -> "int":
        r"""
        ev_get_stkarg_area_info(self, out, cc) -> int
        Get some metrics of the stack argument area.

        @param out: (stkarg_area_info_t *) ptr to stkarg_area_info_t
        @param cc: (cm_t) calling convention
        @retval 1: if success
        @retval 0: not implemented
        """
        return _ida_idp.IDP_Hooks_ev_get_stkarg_area_info(self, *args)

    def ev_last_cb_before_loader(self, *args) -> "int":
        r"""
        ev_last_cb_before_loader(self) -> int
        """
        return _ida_idp.IDP_Hooks_ev_last_cb_before_loader(self, *args)

    def ev_loader(self, *args) -> "int":
        r"""
        ev_loader(self) -> int
        This code and higher ones are reserved for the loaders. The arguments and the
        return values are defined by the loaders
        """
        return _ida_idp.IDP_Hooks_ev_loader(self, *args)
    __swig_destroy__ = _ida_idp.delete_IDP_Hooks
    def __disown__(self):
        self.this.disown()
        _ida_idp.disown_IDP_Hooks(self)
        return weakref.proxy(self)

# Register IDP_Hooks in _ida_idp:
_ida_idp.IDP_Hooks_swigregister(IDP_Hooks)


def get_idp_notifier_addr(*args) -> "PyObject *":
    r"""
    get_idp_notifier_addr(arg1) -> PyObject *

    @param arg1: PyObject *
    """
    return _ida_idp.get_idp_notifier_addr(*args)

def get_idp_notifier_ud_addr(*args) -> "PyObject *":
    r"""
    get_idp_notifier_ud_addr(hooks) -> PyObject *

    @param hooks: IDP_Hooks *
    """
    return _ida_idp.get_idp_notifier_ud_addr(*args)

def delay_slot_insn(*args) -> "bool":
    r"""
    delay_slot_insn(ea, bexec, fexec) -> bool

    @param ea: ea_t *
    @param bexec: bool *
    @param fexec: bool *
    """
    return _ida_idp.delay_slot_insn(*args)

def get_reg_info(*args) -> "char const *":
    r"""
    get_reg_info(regname, bitrange) -> char const *

    @param regname: char const *
    @param bitrange: bitrange_t *
    """
    return _ida_idp.get_reg_info(*args)

def sizeof_ldbl(*args) -> "size_t":
    r"""
    sizeof_ldbl() -> size_t
    """
    return _ida_idp.sizeof_ldbl(*args)

#<pycode(py_idp)>

#----------------------------------------------------------------------------
#               P R O C E S S O R  M O D U L E S  C O N S T A N T S
#----------------------------------------------------------------------------

# ----------------------------------------------------------------------
# processor_t related constants

REAL_ERROR_FORMAT   = -1   #  not supported format for current .idp
REAL_ERROR_RANGE    = -2   #  number too big (small) for store (mem NOT modifyed)
REAL_ERROR_BADDATA  = -3   #  illegal real data for load (IEEE data not filled)

#
# Set IDP options constants
#
IDPOPT_STR        =  1    # string constant
IDPOPT_NUM        =  2    # number
IDPOPT_BIT        =  3    # bit, yes/no
IDPOPT_FLT        =  4    # float
IDPOPT_I64        =  5    # 64bit number

IDPOPT_OK         =  0    # ok
IDPOPT_BADKEY     =  1    # illegal keyword
IDPOPT_BADTYPE    =  2    # illegal type of value
IDPOPT_BADVALUE   =  3    # illegal value (bad range, for example)

# ----------------------------------------------------------------------
import ida_pro
import ida_funcs
import ida_segment
import ida_ua
class processor_t(IDP_Hooks):
    __idc_cvt_id__ = ida_idaapi.PY_ICID_OPAQUE

    """
    Base class for all processor module scripts

    A processor_t instance is both an ida_idp.IDP_Hooks, and an
    ida_idp.IDB_Hooks at the same time: any method of those two classes
    can be overridden in your processor_t subclass (with the exception of
    'ida_idp.IDP_Hooks.ev_init' (replaced with processor_t.__init__),
    and 'ida_idp.IDP_Hooks.ev_term' (replaced with processor_t.__del__)).
    """
    def __init__(self):
        IDP_Hooks.__init__(self, ida_idaapi.HBF_CALL_WITH_NEW_EXEC)
        self.idb_hooks = _processor_t_Trampoline_IDB_Hooks(self)

    def get_idpdesc(self):
        r"""
        This function must be present and should return the list of
        short processor names similar to the one in ph.psnames.
        This method can be overridden to return to the kernel a different IDP description.
        """
        return '\x01'.join(map(lambda t: '\x01'.join(t), zip(self.plnames, self.psnames)))

    def get_uFlag(self):
        r"""
        Use this utility function to retrieve the 'uFlag' global variable
        """
        return ida_ua.cvar.uFlag

    def get_auxpref(self, insn):
        r"""
        This function returns insn.auxpref value
        """
        return insn.auxpref

    def _get_idp_notifier_addr(self):
        return _ida_idp.get_idp_notifier_addr(self)

    def _get_idp_notifier_ud_addr(self):
        return _ida_idp.get_idp_notifier_ud_addr(self)

    def _get_idb_notifier_addr(self):
        return _ida_idp.get_idb_notifier_addr(self)

    def _get_idb_notifier_ud_addr(self):
        return _ida_idp.get_idb_notifier_ud_addr(self.idb_hooks)

    def _make_forced_value_wrapper(self, val, meth=None):
        def f(*args):
            if meth:
                meth(*args)
            return val
        return f

    def _make_int_returning_wrapper(self, meth, intval=0):
        def f(*args):
            val = meth(*args)
            if val is None:
                val = intval
            return val
        return f

    def _get_notify(self, what, unimp_val=0, imp_forced_val=None, add_prefix=True, mandatory_impl=None):
        """
        This helper is used to implement backward-compatibility
        of pre IDA 7.3 processor_t interfaces.
        """
        if add_prefix:
            what = "notify_%s" % what
        meth = getattr(self, what, None)
        if meth is None:
            if mandatory_impl:
                raise Exception("processor_t.%s() must be implemented" % mandatory_impl)
            meth = self._make_forced_value_wrapper(unimp_val)
        else:
            if imp_forced_val is not None:
                meth = self._make_forced_value_wrapper(imp_forced_val, meth)
            else:
                meth = self._make_int_returning_wrapper(meth)
        return meth

# The default implementations below are what guarantees that
# pre IDA 7.3 processor_t subclasses, will continue working

    def ev_newprc(self, *args):
        return self._get_notify("newprc")(*args)

    def ev_newfile(self, *args):
        return self._get_notify("newfile")(*args)

    def ev_oldfile(self, *args):
        return self._get_notify("oldfile")(*args)

    def ev_newbinary(self, *args):
        return self._get_notify("newbinary")(*args)

    def ev_endbinary(self, *args):
        return self._get_notify("endbinary")(*args)

    def ev_set_idp_options(self, keyword, value_type, value, idb_loaded):
        res = self._get_notify("set_idp_options", unimp_val=None)(keyword, value_type, value)
        if res is None:
            return 0
        return 1 if res == IDPOPT_OK else -1

    def ev_set_proc_options(self, *args):
        return self._get_notify("set_proc_options")(*args)

    def ev_ana_insn(self, *args):
        rc = self._get_notify("ana", mandatory_impl="ev_ana_insn")(*args)
        return rc > 0

    def ev_emu_insn(self, *args):
        rc = self._get_notify("emu", mandatory_impl="ev_emu_insn")(*args)
        return rc > 0

    def ev_out_header(self, *args):
        return self._get_notify("out_header", imp_forced_val=1)(*args)

    def ev_out_footer(self, *args):
        return self._get_notify("out_footer", imp_forced_val=1)(*args)

    def ev_out_segstart(self, ctx, s):
        return self._get_notify("out_segstart", imp_forced_val=1)(ctx, s.start_ea)

    def ev_out_segend(self, ctx, s):
        return self._get_notify("out_segend", imp_forced_val=1)(ctx, s.end_ea)

    def ev_out_assumes(self, *args):
        return self._get_notify("out_assumes", imp_forced_val=1)(*args)

    def ev_out_insn(self, *args):
        return self._get_notify("out_insn", mandatory_impl="ev_out_insn", imp_forced_val=True)(*args)

    def ev_out_mnem(self, *args):
        return self._get_notify("out_mnem", add_prefix=False, imp_forced_val=1)(*args)

    def ev_out_operand(self, *args):
        rc = self._get_notify("out_operand", mandatory_impl="ev_out_operand", imp_forced_val=1)(*args)
        return rc > 0

    def ev_out_data(self, *args):
        return self._get_notify("out_data", imp_forced_val=1)(*args)

    def ev_out_label(self, *args):
        return self._get_notify("out_label")(*args)

    def ev_out_special_item(self, *args):
        return self._get_notify("out_special_item")(*args)

    def ev_gen_regvar_def(self, ctx, v):
        return self._get_notify("gen_regvar_def")(ctx, v.canon, v.user, v.cmt)

    def ev_gen_src_file_lnnum(self, *args):
        return self._get_notify("gen_src_file_lnnum")(*args)

    def ev_creating_segm(self, s):
        sname = ida_segment.get_visible_segm_name(s)
        sclass = ida_segment.get_segm_class(s)
        return self._get_notify("creating_segm")(s.start_ea, sname, sclass)

    def ev_moving_segm(self, s, to_ea, flags):
        sname = ida_segment.get_visible_segm_name(s)
        sclass = ida_segment.get_segm_class(s)
        return self._get_notify("moving_segm")(s.start_ea, sname, sclass, to_ea, flags)

    def ev_coagulate(self, *args):
        return self._get_notify("coagulate")(*args)

    def ev_undefine(self, *args):
        return self._get_notify("undefine")(*args)

    def ev_treat_hindering_item(self, *args):
        return self._get_notify("treat_hindering_item")(*args)

    def ev_rename(self, *args):
        return self._get_notify("rename")(*args)

    def ev_is_far_jump(self, *args):
        rc = self._get_notify("is_far_jump", unimp_val=False)(*args)
        return 1 if rc else -1

    def ev_is_sane_insn(self, *args):
        return self._get_notify("is_sane_insn")(*args)

    def ev_is_call_insn(self, *args):
        return self._get_notify("is_call_insn")(*args)

    def ev_is_ret_insn(self, *args):
        return self._get_notify("is_ret_insn")(*args)

    def ev_may_be_func(self, *args):
        return self._get_notify("may_be_func")(*args)

    def ev_is_basic_block_end(self, *args):
        return self._get_notify("is_basic_block_end")(*args)

    def ev_is_indirect_jump(self, *args):
        return self._get_notify("is_indirect_jump")(*args)

    def ev_is_insn_table_jump(self, *args):
        return self._get_notify("is_insn_table_jump")(*args)

    def ev_is_switch(self, *args):
        rc = self._get_notify("is_switch")(*args)
        return 1 if rc else 0

    def ev_create_switch_xrefs(self, *args):
        return self._get_notify("create_switch_xrefs", imp_forced_val=1)(*args)

    def ev_is_align_insn(self, *args):
        return self._get_notify("is_align_insn")(*args)

    def ev_is_alloca_probe(self, *args):
        return self._get_notify("is_alloca_probe")(*args)

    def ev_is_sp_based(self, mode, insn, op):
        rc = self._get_notify("is_sp_based", unimp_val=None)(insn, op)
        if type(rc) == int:
            ida_pro.int_pointer.frompointer(mode).assign(rc)
            return 1
        return 0

    def ev_can_have_type(self, *args):
        rc = self._get_notify("can_have_type")(*args)
        if rc is True:
            return 1
        elif rc is False:
            return -1
        else:
            return 0

    def ev_cmp_operands(self, *args):
        rc = self._get_notify("cmp_operands")(*args)
        if rc is True:
            return 1
        elif rc is False:
            return -1
        else:
            return 0

    def ev_get_operand_string(self, buf, insn, opnum):
        rc = self._get_notify("get_operand_string")(insn, opnum)
        if rc:
            return 1
        return 0

    def ev_str2reg(self, *args):
        rc = self._get_notify("notify_str2reg", unimp_val=-1)(*args)
        return 0 if rc < 0 else rc + 1

    def ev_get_autocmt(self, *args):
        return self._get_notify("get_autocmt")(*args)

    def ev_func_bounds(self, _possible_return_code, pfn, max_func_end_ea):
        possible_return_code = ida_pro.int_pointer.frompointer(_possible_return_code)
        rc = self._get_notify("func_bounds", unimp_val=None)(
            possible_return_code.value(),
            pfn.start_ea,
            max_func_end_ea)
        if type(rc) == int:
            possible_return_code.assign(rc)
        return 0

    def ev_verify_sp(self, pfn):
        return self._get_notify("verify_sp")(pfn.start_ea)

    def ev_verify_noreturn(self, pfn):
        return self._get_notify("verify_noreturn")(pfn.start_ea)

    def ev_create_func_frame(self, pfn):
        rc = self._get_notify("create_func_frame", imp_forced_val=1)(pfn.start_ea)
        if rc is True:
            return 1
        elif rc is False:
            return -1
        else:
            return rc

    def ev_get_frame_retsize(self, frsize, pfn):
        rc = self._get_notify("get_frame_retsize", unimp_val=None)(pfn.start_ea)
        if type(rc) == int:
            ida_pro.int_pointer.frompointer(frsize).assign(rc)
            return 1
        return 0

    def ev_coagulate_dref(self, from_ea, to_ea, may_define, _code_ea):
        code_ea = ida_pro.ea_pointer.frompointer(_code_ea)
        rc = self._get_notify("coagulate_dref")(from_ea, to_ea, may_define, code_ea.value())
        if rc == -1:
            return -1
        if rc != 0:
            code_ea.assign(rc)
        return 0

    def ev_may_show_sreg(self, *args):
        return self._get_notify("may_show_sreg")(*args)

    def ev_auto_queue_empty(self, *args):
        return self._get_notify("auto_queue_empty")(*args)

    def ev_validate_flirt_func(self, *args):
        return self._get_notify("validate_flirt_func")(*args)

    def ev_assemble(self, *args):
        return self._get_notify("assemble")(*args)

    def ev_gen_map_file(self, nlines, fp):
        import ida_fpro
        qfile = ida_fpro.qfile_t_from_fp(fp)
        rc = self._get_notify("gen_map_file")(qfile)
        if rc > 0:
            ida_pro.int_pointer.frompointer(nlines).assign(rc)
            return 1
        else:
            return 0

    def ev_calc_step_over(self, target, ip):
        rc = self._get_notify("calc_step_over", unimp_val=None)(ip)
        if rc is not None and rc != ida_idaapi.BADADDR:
            ida_pro.ea_pointer.frompointer(target).assign(rc)
            return 1
        return 0

# IDB hooks handling

    def closebase(self, *args):
        self._get_notify("closebase")(*args)

    def savebase(self, *args):
        self._get_notify("savebase")(*args)

    def auto_empty(self, *args):
        self._get_notify("auto_empty")(*args)

    def auto_empty_finally(self, *args):
        self._get_notify("auto_empty_finally")(*args)

    def determined_main(self, *args):
        self._get_notify("determined_main")(*args)

    def idasgn_loaded(self, *args):
        self._get_notify("load_idasgn")(*args)

    def kernel_config_loaded(self, *args):
        self._get_notify("kernel_config_loaded")(*args)

    def compiler_changed(self, *args):
        self._get_notify("set_compiler")(*args)

    def segm_moved(self, from_ea, to_ea, size, changed_netmap):
        s = ida_segment.getseg(to_ea)
        sname = ida_segment.get_visible_segm_name(s)
        sclass = ida_segment.get_segm_class(s)
        self._get_notify("move_segm")(from_ea, to_ea, sname, sclass, changed_netmap)

    def func_added(self, pfn):
        self._get_notify("add_func")(pfn.start_ea)

    def set_func_start(self, *args):
        self._get_notify("set_func_start")(*args)

    def set_func_end(self, *args):
        self._get_notify("set_func_end")(*args)

    def deleting_func(self, pfn):
        self._get_notify("del_func")(pfn.start_ea)

    def sgr_changed(self, *args):
        self._get_notify("setsgr")(*args)

    def make_code(self, *args):
        self._get_notify("make_code")(*args)

    def make_data(self, *args):
        self._get_notify("make_data")(*args)

    def renamed(self, *args):
        self._get_notify("renamed")(*args)


# ----------------------------------------------------------------------
class __ph(object):
    id = property(lambda self: ph_get_id())
    cnbits = property(lambda self: ph_get_cnbits())
    dnbits = property(lambda self: ph_get_dnbits())
    flag = property(lambda self: ph_get_flag())
    icode_return = property(lambda self: ph_get_icode_return())
    instruc = property(lambda self: ph_get_instruc())
    instruc_end = property(lambda self: ph_get_instruc_end())
    instruc_start = property(lambda self: ph_get_instruc_start())
    reg_code_sreg = property(lambda self: ph_get_reg_code_sreg())
    reg_data_sreg = property(lambda self: ph_get_reg_data_sreg())
    reg_first_sreg = property(lambda self: ph_get_reg_first_sreg())
    reg_last_sreg = property(lambda self: ph_get_reg_last_sreg())
    regnames = property(lambda self: ph_get_regnames())
    segreg_size = property(lambda self: ph_get_segreg_size())
    tbyte_size = property(lambda self: ph_get_tbyte_size())
    version = property(lambda self: ph_get_version())

ph = __ph()

class _idp_cvar_t:
    ash = property(lambda self: get_ash())
cvar = _idp_cvar_t()

#</pycode(py_idp)>

class IDB_Hooks(object):
    r"""
    Proxy of C++ IDB_Hooks class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _flags=0) -> IDB_Hooks

        @param _flags: uint32
        """
        if self.__class__ == IDB_Hooks:
            _self = None
        else:
            _self = self
        _ida_idp.IDB_Hooks_swiginit(self, _ida_idp.new_IDB_Hooks(_self, *args))

    def hook(self, *args) -> "bool":
        r"""
        hook(self) -> bool
        """
        return _ida_idp.IDB_Hooks_hook(self, *args)

    def unhook(self, *args) -> "bool":
        r"""
        unhook(self) -> bool
        """
        return _ida_idp.IDB_Hooks_unhook(self, *args)

    def closebase(self, *args) -> "void":
        r"""
        closebase(self)
        The database will be closed now.
        """
        return _ida_idp.IDB_Hooks_closebase(self, *args)

    def savebase(self, *args) -> "void":
        r"""
        savebase(self)
        The database is being saved.
        """
        return _ida_idp.IDB_Hooks_savebase(self, *args)

    def upgraded(self, *args) -> "void":
        r"""
        upgraded(self, _from)
        The database has been upgraded and the receiver can upgrade its info as well

        @param from: (int) - old IDB version
        """
        return _ida_idp.IDB_Hooks_upgraded(self, *args)

    def auto_empty(self, *args) -> "void":
        r"""
        auto_empty(self)
        """
        return _ida_idp.IDB_Hooks_auto_empty(self, *args)

    def auto_empty_finally(self, *args) -> "void":
        r"""
        auto_empty_finally(self)
        """
        return _ida_idp.IDB_Hooks_auto_empty_finally(self, *args)

    def determined_main(self, *args) -> "void":
        r"""
        determined_main(self, main)
        The main() function has been determined.

        @param main: (::ea_t) address of the main() function
        """
        return _ida_idp.IDB_Hooks_determined_main(self, *args)

    def local_types_changed(self, *args) -> "void":
        r"""
        local_types_changed(self)
        Local types have been changed.
        """
        return _ida_idp.IDB_Hooks_local_types_changed(self, *args)

    def extlang_changed(self, *args) -> "void":
        r"""
        extlang_changed(self, kind, el, idx)
        The list of extlangs or the default extlang was changed.

        @param kind: (int) 0: extlang installed 1: extlang removed 2: default extlang
                     changed
        @param el: (extlang_t *) pointer to the extlang affected
        @param idx: (int) extlang index
        """
        return _ida_idp.IDB_Hooks_extlang_changed(self, *args)

    def idasgn_loaded(self, *args) -> "void":
        r"""
        idasgn_loaded(self, short_sig_name)
        FLIRT signature has been loaded for normal processing (not for recognition of
        startup sequences).

        @param short_sig_name: (const char *)
        """
        return _ida_idp.IDB_Hooks_idasgn_loaded(self, *args)

    def kernel_config_loaded(self, *args) -> "void":
        r"""
        kernel_config_loaded(self, pass_number)
        This event is issued when ida.cfg is parsed.

        @param pass_number: (int)
        """
        return _ida_idp.IDB_Hooks_kernel_config_loaded(self, *args)

    def loader_finished(self, *args) -> "void":
        r"""
        loader_finished(self, li, neflags, filetypename)
        External file loader finished its work. Use this event to augment the existing
        loader functionality.

        @param li: (linput_t *)
        @param neflags: (uint16) Load file flags
        @param filetypename: (const char *)
        """
        return _ida_idp.IDB_Hooks_loader_finished(self, *args)

    def flow_chart_created(self, *args) -> "void":
        r"""
        flow_chart_created(self, fc)
        Gui has retrieved a function flow chart. Plugins may modify the flow chart in
        this callback.

        @param fc: (qflow_chart_t *)
        """
        return _ida_idp.IDB_Hooks_flow_chart_created(self, *args)

    def compiler_changed(self, *args) -> "void":
        r"""
        compiler_changed(self, adjust_inf_fields)
        The kernel has changed the compiler information. ( idainfo::cc structure;
        get_abi_name)

        @param adjust_inf_fields: (::bool) may change inf fields?
        """
        return _ida_idp.IDB_Hooks_compiler_changed(self, *args)

    def changing_ti(self, *args) -> "void":
        r"""
        changing_ti(self, ea, new_type, new_fnames)
        An item typestring (c/c++ prototype) is to be changed.

        @param ea: (::ea_t)
        @param new_type: (const type_t *)
        @param new_fnames: (const p_list *)
        """
        return _ida_idp.IDB_Hooks_changing_ti(self, *args)

    def ti_changed(self, *args) -> "void":
        r"""
        ti_changed(self, ea, type, fnames)
        An item typestring (c/c++ prototype) has been changed.

        @param ea: (::ea_t)
        @param type: (const type_t *)
        @param fnames: (const p_list *)
        """
        return _ida_idp.IDB_Hooks_ti_changed(self, *args)

    def changing_op_ti(self, *args) -> "void":
        r"""
        changing_op_ti(self, ea, n, new_type, new_fnames)
        An operand typestring (c/c++ prototype) is to be changed.

        @param ea: (::ea_t)
        @param n: (int)
        @param new_type: (const type_t *)
        @param new_fnames: (const p_list *)
        """
        return _ida_idp.IDB_Hooks_changing_op_ti(self, *args)

    def op_ti_changed(self, *args) -> "void":
        r"""
        op_ti_changed(self, ea, n, type, fnames)
        An operand typestring (c/c++ prototype) has been changed.

        @param ea: (::ea_t)
        @param n: (int)
        @param type: (const type_t *)
        @param fnames: (const p_list *)
        """
        return _ida_idp.IDB_Hooks_op_ti_changed(self, *args)

    def changing_op_type(self, *args) -> "void":
        r"""
        changing_op_type(self, ea, n, opinfo)
        An operand type (offset, hex, etc...) is to be changed.

        @param ea: (::ea_t)
        @param n: (int) eventually or'ed with OPND_OUTER or OPND_ALL
        @param opinfo: (const opinfo_t *) additional operand info
        """
        return _ida_idp.IDB_Hooks_changing_op_type(self, *args)

    def op_type_changed(self, *args) -> "void":
        r"""
        op_type_changed(self, ea, n)
        An operand type (offset, hex, etc...) has been set or deleted.

        @param ea: (::ea_t)
        @param n: (int) eventually or'ed with OPND_OUTER or OPND_ALL
        """
        return _ida_idp.IDB_Hooks_op_type_changed(self, *args)

    def enum_created(self, *args) -> "void":
        r"""
        enum_created(self, id)
        An enum type has been created.

        @param id: (enum_t)
        """
        return _ida_idp.IDB_Hooks_enum_created(self, *args)

    def deleting_enum(self, *args) -> "void":
        r"""
        deleting_enum(self, id)
        An enum type is to be deleted.

        @param id: (enum_t)
        """
        return _ida_idp.IDB_Hooks_deleting_enum(self, *args)

    def enum_deleted(self, *args) -> "void":
        r"""
        enum_deleted(self, id)
        An enum type has been deleted.

        @param id: (enum_t)
        """
        return _ida_idp.IDB_Hooks_enum_deleted(self, *args)

    def renaming_enum(self, *args) -> "void":
        r"""
        renaming_enum(self, id, is_enum, newname)
        An enum or enum member is to be renamed.

        @param id: (tid_t)
        @param is_enum: (bool)
        @param newname: (const char *)
        """
        return _ida_idp.IDB_Hooks_renaming_enum(self, *args)

    def enum_renamed(self, *args) -> "void":
        r"""
        enum_renamed(self, id)
        An enum or member has been renamed.

        @param id: (tid_t)
        """
        return _ida_idp.IDB_Hooks_enum_renamed(self, *args)

    def changing_enum_bf(self, *args) -> "void":
        r"""
        changing_enum_bf(self, id, new_bf)
        An enum type 'bitfield' attribute is to be changed.

        @param id: (enum_t)
        @param new_bf: (bool)
        """
        return _ida_idp.IDB_Hooks_changing_enum_bf(self, *args)

    def enum_bf_changed(self, *args) -> "void":
        r"""
        enum_bf_changed(self, id)
        An enum type 'bitfield' attribute has been changed.

        @param id: (enum_t)
        """
        return _ida_idp.IDB_Hooks_enum_bf_changed(self, *args)

    def changing_enum_cmt(self, *args) -> "void":
        r"""
        changing_enum_cmt(self, id, repeatable, newcmt)
        An enum or member type comment is to be changed.

        @param id: (tid_t)
        @param repeatable: (bool)
        @param newcmt: (const char *)
        """
        return _ida_idp.IDB_Hooks_changing_enum_cmt(self, *args)

    def enum_cmt_changed(self, *args) -> "void":
        r"""
        enum_cmt_changed(self, id, repeatable)
        An enum or member type comment has been changed.

        @param id: (tid_t)
        @param repeatable: (bool)
        """
        return _ida_idp.IDB_Hooks_enum_cmt_changed(self, *args)

    def enum_member_created(self, *args) -> "void":
        r"""
        enum_member_created(self, id, cid)
        An enum member has been created.

        @param id: (enum_t)
        @param cid: (const_t)
        """
        return _ida_idp.IDB_Hooks_enum_member_created(self, *args)

    def deleting_enum_member(self, *args) -> "void":
        r"""
        deleting_enum_member(self, id, cid)
        An enum member is to be deleted.

        @param id: (enum_t)
        @param cid: (const_t)
        """
        return _ida_idp.IDB_Hooks_deleting_enum_member(self, *args)

    def enum_member_deleted(self, *args) -> "void":
        r"""
        enum_member_deleted(self, id, cid)
        An enum member has been deleted.

        @param id: (enum_t)
        @param cid: (const_t)
        """
        return _ida_idp.IDB_Hooks_enum_member_deleted(self, *args)

    def struc_created(self, *args) -> "void":
        r"""
        struc_created(self, struc_id)
        A new structure type has been created.

        @param struc_id: (tid_t)
        """
        return _ida_idp.IDB_Hooks_struc_created(self, *args)

    def deleting_struc(self, *args) -> "void":
        r"""
        deleting_struc(self, sptr)
        A structure type is to be deleted.

        @param sptr: (struc_t *)
        """
        return _ida_idp.IDB_Hooks_deleting_struc(self, *args)

    def struc_deleted(self, *args) -> "void":
        r"""
        struc_deleted(self, struc_id)
        A structure type has been deleted.

        @param struc_id: (tid_t)
        """
        return _ida_idp.IDB_Hooks_struc_deleted(self, *args)

    def changing_struc_align(self, *args) -> "void":
        r"""
        changing_struc_align(self, sptr)
        A structure type is being changed (the struct alignment).

        @param sptr: (struc_t *)
        """
        return _ida_idp.IDB_Hooks_changing_struc_align(self, *args)

    def struc_align_changed(self, *args) -> "void":
        r"""
        struc_align_changed(self, sptr)
        A structure type has been changed (the struct alignment).

        @param sptr: (struc_t *)
        """
        return _ida_idp.IDB_Hooks_struc_align_changed(self, *args)

    def renaming_struc(self, *args) -> "void":
        r"""
        renaming_struc(self, id, oldname, newname)
        A structure type is to be renamed.

        @param id: (tid_t)
        @param oldname: (const char *)
        @param newname: (const char *)
        """
        return _ida_idp.IDB_Hooks_renaming_struc(self, *args)

    def struc_renamed(self, *args) -> "void":
        r"""
        struc_renamed(self, sptr)
        A structure type has been renamed.

        @param sptr: (struc_t *)
        """
        return _ida_idp.IDB_Hooks_struc_renamed(self, *args)

    def expanding_struc(self, *args) -> "void":
        r"""
        expanding_struc(self, sptr, offset, delta)
        A structure type is to be expanded/shrunk.

        @param sptr: (struc_t *)
        @param offset: (::ea_t)
        @param delta: (::adiff_t)
        """
        return _ida_idp.IDB_Hooks_expanding_struc(self, *args)

    def struc_expanded(self, *args) -> "void":
        r"""
        struc_expanded(self, sptr)
        A structure type has been expanded/shrank.

        @param sptr: (struc_t *)
        """
        return _ida_idp.IDB_Hooks_struc_expanded(self, *args)

    def struc_member_created(self, *args) -> "void":
        r"""
        struc_member_created(self, sptr, mptr)
        A structure member has been created.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        """
        return _ida_idp.IDB_Hooks_struc_member_created(self, *args)

    def deleting_struc_member(self, *args) -> "void":
        r"""
        deleting_struc_member(self, sptr, mptr)
        A structure member is to be deleted.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        """
        return _ida_idp.IDB_Hooks_deleting_struc_member(self, *args)

    def struc_member_deleted(self, *args) -> "void":
        r"""
        struc_member_deleted(self, sptr, member_id, offset)
        A structure member has been deleted.

        @param sptr: (struc_t *)
        @param member_id: (tid_t)
        @param offset: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_struc_member_deleted(self, *args)

    def renaming_struc_member(self, *args) -> "void":
        r"""
        renaming_struc_member(self, sptr, mptr, newname)
        A structure member is to be renamed.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        @param newname: (const char *)
        """
        return _ida_idp.IDB_Hooks_renaming_struc_member(self, *args)

    def struc_member_renamed(self, *args) -> "void":
        r"""
        struc_member_renamed(self, sptr, mptr)
        A structure member has been renamed.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        """
        return _ida_idp.IDB_Hooks_struc_member_renamed(self, *args)

    def changing_struc_member(self, *args) -> "void":
        r"""
        changing_struc_member(self, sptr, mptr, flag, ti, nbytes)
        A structure member is to be changed.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        @param flag: (flags_t)
        @param ti: (const opinfo_t *)
        @param nbytes: (::asize_t)
        """
        return _ida_idp.IDB_Hooks_changing_struc_member(self, *args)

    def struc_member_changed(self, *args) -> "void":
        r"""
        struc_member_changed(self, sptr, mptr)
        A structure member has been changed.

        @param sptr: (struc_t *)
        @param mptr: (member_t *)
        """
        return _ida_idp.IDB_Hooks_struc_member_changed(self, *args)

    def changing_struc_cmt(self, *args) -> "void":
        r"""
        changing_struc_cmt(self, struc_id, repeatable, newcmt)
        A structure type comment is to be changed.

        @param struc_id: (tid_t)
        @param repeatable: (bool)
        @param newcmt: (const char *)
        """
        return _ida_idp.IDB_Hooks_changing_struc_cmt(self, *args)

    def struc_cmt_changed(self, *args) -> "void":
        r"""
        struc_cmt_changed(self, struc_id, repeatable_cmt)
        A structure type comment has been changed.

        @param struc_id: (tid_t)
        @param repeatable_cmt: (bool)
        """
        return _ida_idp.IDB_Hooks_struc_cmt_changed(self, *args)

    def segm_added(self, *args) -> "void":
        r"""
        segm_added(self, s)
        A new segment has been created.

        @param s: (segment_t *) See also adding_segm
        """
        return _ida_idp.IDB_Hooks_segm_added(self, *args)

    def deleting_segm(self, *args) -> "void":
        r"""
        deleting_segm(self, start_ea)
        A segment is to be deleted.

        @param start_ea: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_deleting_segm(self, *args)

    def segm_deleted(self, *args) -> "void":
        r"""
        segm_deleted(self, start_ea, end_ea, flags)
        A segment has been deleted.

        @param start_ea: (::ea_t)
        @param end_ea: (::ea_t)
        @param flags: (int)
        """
        return _ida_idp.IDB_Hooks_segm_deleted(self, *args)

    def changing_segm_start(self, *args) -> "void":
        r"""
        changing_segm_start(self, s, new_start, segmod_flags)
        Segment start address is to be changed.

        @param s: (segment_t *)
        @param new_start: (::ea_t)
        @param segmod_flags: (int)
        """
        return _ida_idp.IDB_Hooks_changing_segm_start(self, *args)

    def segm_start_changed(self, *args) -> "void":
        r"""
        segm_start_changed(self, s, oldstart)
        Segment start address has been changed.

        @param s: (segment_t *)
        @param oldstart: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_segm_start_changed(self, *args)

    def changing_segm_end(self, *args) -> "void":
        r"""
        changing_segm_end(self, s, new_end, segmod_flags)
        Segment end address is to be changed.

        @param s: (segment_t *)
        @param new_end: (::ea_t)
        @param segmod_flags: (int)
        """
        return _ida_idp.IDB_Hooks_changing_segm_end(self, *args)

    def segm_end_changed(self, *args) -> "void":
        r"""
        segm_end_changed(self, s, oldend)
        Segment end address has been changed.

        @param s: (segment_t *)
        @param oldend: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_segm_end_changed(self, *args)

    def changing_segm_name(self, *args) -> "void":
        r"""
        changing_segm_name(self, s, oldname)
        Segment name is being changed.

        @param s: (segment_t *)
        @param oldname: (const char *)
        """
        return _ida_idp.IDB_Hooks_changing_segm_name(self, *args)

    def segm_name_changed(self, *args) -> "void":
        r"""
        segm_name_changed(self, s, name)
        Segment name has been changed.

        @param s: (segment_t *)
        @param name: (const char *)
        """
        return _ida_idp.IDB_Hooks_segm_name_changed(self, *args)

    def changing_segm_class(self, *args) -> "void":
        r"""
        changing_segm_class(self, s)
        Segment class is being changed.

        @param s: (segment_t *)
        """
        return _ida_idp.IDB_Hooks_changing_segm_class(self, *args)

    def segm_class_changed(self, *args) -> "void":
        r"""
        segm_class_changed(self, s, sclass)
        Segment class has been changed.

        @param s: (segment_t *)
        @param sclass: (const char *)
        """
        return _ida_idp.IDB_Hooks_segm_class_changed(self, *args)

    def segm_attrs_updated(self, *args) -> "void":
        r"""
        segm_attrs_updated(self, s)
        Segment attributes has been changed.

        @param s: (segment_t *) This event is generated for secondary segment attributes
                  (examples: color, permissions, etc)
        """
        return _ida_idp.IDB_Hooks_segm_attrs_updated(self, *args)

    def segm_moved(self, *args) -> "void":
        r"""
        segm_moved(self, _from, to, size, changed_netmap)
        Segment has been moved.

        @param from: (::ea_t)
        @param to: (::ea_t)
        @param size: (::asize_t)
        @param changed_netmap: (bool) See also idb_event::allsegs_moved
        """
        return _ida_idp.IDB_Hooks_segm_moved(self, *args)

    def allsegs_moved(self, *args) -> "void":
        r"""
        allsegs_moved(self, info)
        Program rebasing is complete. This event is generated after series of segm_moved
        events

        @param info: (segm_move_infos_t *)
        """
        return _ida_idp.IDB_Hooks_allsegs_moved(self, *args)

    def func_added(self, *args) -> "void":
        r"""
        func_added(self, pfn)
        The kernel has added a function.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_func_added(self, *args)

    def func_updated(self, *args) -> "void":
        r"""
        func_updated(self, pfn)
        The kernel has updated a function.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_func_updated(self, *args)

    def set_func_start(self, *args) -> "void":
        r"""
        set_func_start(self, pfn, new_start)
        Function chunk start address will be changed.

        @param pfn: (func_t *)
        @param new_start: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_set_func_start(self, *args)

    def set_func_end(self, *args) -> "void":
        r"""
        set_func_end(self, pfn, new_end)
        Function chunk end address will be changed.

        @param pfn: (func_t *)
        @param new_end: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_set_func_end(self, *args)

    def deleting_func(self, *args) -> "void":
        r"""
        deleting_func(self, pfn)
        The kernel is about to delete a function.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_deleting_func(self, *args)

    def frame_deleted(self, *args) -> "void":
        r"""
        frame_deleted(self, pfn)
        The kernel has deleted a function frame.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_frame_deleted(self, *args)

    def thunk_func_created(self, *args) -> "void":
        r"""
        thunk_func_created(self, pfn)
        A thunk bit has been set for a function.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_thunk_func_created(self, *args)

    def func_tail_appended(self, *args) -> "void":
        r"""
        func_tail_appended(self, pfn, tail)
        A function tail chunk has been appended.

        @param pfn: (func_t *)
        @param tail: (func_t *)
        """
        return _ida_idp.IDB_Hooks_func_tail_appended(self, *args)

    def deleting_func_tail(self, *args) -> "void":
        r"""
        deleting_func_tail(self, pfn, tail)
        A function tail chunk is to be removed.

        @param pfn: (func_t *)
        @param tail: (const range_t *)
        """
        return _ida_idp.IDB_Hooks_deleting_func_tail(self, *args)

    def func_tail_deleted(self, *args) -> "void":
        r"""
        func_tail_deleted(self, pfn, tail_ea)
        A function tail chunk has been removed.

        @param pfn: (func_t *)
        @param tail_ea: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_func_tail_deleted(self, *args)

    def tail_owner_changed(self, *args) -> "void":
        r"""
        tail_owner_changed(self, tail, owner_func, old_owner)
        A tail chunk owner has been changed.

        @param tail: (func_t *)
        @param owner_func: (::ea_t)
        @param old_owner: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_tail_owner_changed(self, *args)

    def func_noret_changed(self, *args) -> "void":
        r"""
        func_noret_changed(self, pfn)
        FUNC_NORET bit has been changed.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_func_noret_changed(self, *args)

    def stkpnts_changed(self, *args) -> "void":
        r"""
        stkpnts_changed(self, pfn)
        Stack change points have been modified.

        @param pfn: (func_t *)
        """
        return _ida_idp.IDB_Hooks_stkpnts_changed(self, *args)

    def updating_tryblks(self, *args) -> "void":
        r"""
        updating_tryblks(self, tbv)
        About to update tryblk information

        @param tbv: (const ::tryblks_t *)
        """
        return _ida_idp.IDB_Hooks_updating_tryblks(self, *args)

    def tryblks_updated(self, *args) -> "void":
        r"""
        tryblks_updated(self, tbv)
        Updated tryblk information

        @param tbv: (const ::tryblks_t *)
        """
        return _ida_idp.IDB_Hooks_tryblks_updated(self, *args)

    def deleting_tryblks(self, *args) -> "void":
        r"""
        deleting_tryblks(self, range)
        About to delete tryblk information in given range

        @param range: (const range_t *)
        """
        return _ida_idp.IDB_Hooks_deleting_tryblks(self, *args)

    def sgr_changed(self, *args) -> "void":
        r"""
        sgr_changed(self, start_ea, end_ea, regnum, value, old_value, tag)
        The kernel has changed a segment register value.

        @param start_ea: (::ea_t)
        @param end_ea: (::ea_t)
        @param regnum: (int)
        @param value: (::sel_t)
        @param old_value: (::sel_t)
        @param tag: (uchar) Segment register range tags
        """
        return _ida_idp.IDB_Hooks_sgr_changed(self, *args)

    def make_code(self, *args) -> "void":
        r"""
        make_code(self, insn)
        An instruction is being created.

        @param insn: (const insn_t*)
        """
        return _ida_idp.IDB_Hooks_make_code(self, *args)

    def make_data(self, *args) -> "void":
        r"""
        make_data(self, ea, flags, tid, len)
        A data item is being created.

        @param ea: (::ea_t)
        @param flags: (flags_t)
        @param tid: (tid_t)
        @param len: (::asize_t)
        """
        return _ida_idp.IDB_Hooks_make_data(self, *args)

    def destroyed_items(self, *args) -> "void":
        r"""
        destroyed_items(self, ea1, ea2, will_disable_range)
        Instructions/data have been destroyed in [ea1,ea2).

        @param ea1: (::ea_t)
        @param ea2: (::ea_t)
        @param will_disable_range: (bool)
        """
        return _ida_idp.IDB_Hooks_destroyed_items(self, *args)

    def renamed(self, *args) -> "void":
        r"""
        renamed(self, ea, new_name, local_name, old_name)
        The kernel has renamed a byte. See also the rename event

        @param ea: (::ea_t)
        @param new_name: (const char *) can be nullptr
        @param local_name: (bool)
        @param old_name: (const char *) can be nullptr
        """
        return _ida_idp.IDB_Hooks_renamed(self, *args)

    def byte_patched(self, *args) -> "void":
        r"""
        byte_patched(self, ea, old_value)
        A byte has been patched.

        @param ea: (::ea_t)
        @param old_value: (uint32)
        """
        return _ida_idp.IDB_Hooks_byte_patched(self, *args)

    def changing_cmt(self, *args) -> "void":
        r"""
        changing_cmt(self, ea, repeatable_cmt, newcmt)
        An item comment is to be changed.

        @param ea: (::ea_t)
        @param repeatable_cmt: (bool)
        @param newcmt: (const char *)
        """
        return _ida_idp.IDB_Hooks_changing_cmt(self, *args)

    def cmt_changed(self, *args) -> "void":
        r"""
        cmt_changed(self, ea, repeatable_cmt)
        An item comment has been changed.

        @param ea: (::ea_t)
        @param repeatable_cmt: (bool)
        """
        return _ida_idp.IDB_Hooks_cmt_changed(self, *args)

    def changing_range_cmt(self, *args) -> "void":
        r"""
        changing_range_cmt(self, kind, a, cmt, repeatable)
        Range comment is to be changed.

        @param kind: (range_kind_t)
        @param a: (const range_t *)
        @param cmt: (const char *)
        @param repeatable: (bool)
        """
        return _ida_idp.IDB_Hooks_changing_range_cmt(self, *args)

    def range_cmt_changed(self, *args) -> "void":
        r"""
        range_cmt_changed(self, kind, a, cmt, repeatable)
        Range comment has been changed.

        @param kind: (range_kind_t)
        @param a: (const range_t *)
        @param cmt: (const char *)
        @param repeatable: (bool)
        """
        return _ida_idp.IDB_Hooks_range_cmt_changed(self, *args)

    def extra_cmt_changed(self, *args) -> "void":
        r"""
        extra_cmt_changed(self, ea, line_idx, cmt)
        An extra comment has been changed.

        @param ea: (::ea_t)
        @param line_idx: (int)
        @param cmt: (const char *)
        """
        return _ida_idp.IDB_Hooks_extra_cmt_changed(self, *args)

    def item_color_changed(self, *args) -> "void":
        r"""
        item_color_changed(self, ea, color)
        An item color has been changed.

        @param ea: (::ea_t)
        @param color: (bgcolor_t) if color==DEFCOLOR, the the color is deleted.
        """
        return _ida_idp.IDB_Hooks_item_color_changed(self, *args)

    def callee_addr_changed(self, *args) -> "void":
        r"""
        callee_addr_changed(self, ea, callee)
        Callee address has been updated by the user.

        @param ea: (::ea_t)
        @param callee: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_callee_addr_changed(self, *args)

    def bookmark_changed(self, *args) -> "void":
        r"""
        bookmark_changed(self, index, pos, desc, operation)
        Boomarked position changed.

        @param index: (uint32)
        @param pos: (::const lochist_entry_t *)
        @param desc: (::const char *)
        @param operation: (int) 0-added, 1-updated, 2-deleted if desc==nullptr, then the
                          bookmark was deleted.
        """
        return _ida_idp.IDB_Hooks_bookmark_changed(self, *args)

    def sgr_deleted(self, *args) -> "void":
        r"""
        sgr_deleted(self, start_ea, end_ea, regnum)
        The kernel has deleted a segment register value.

        @param start_ea: (::ea_t)
        @param end_ea: (::ea_t)
        @param regnum: (int)
        """
        return _ida_idp.IDB_Hooks_sgr_deleted(self, *args)

    def adding_segm(self, *args) -> "void":
        r"""
        adding_segm(self, s)
        A segment is being created.

        @param s: (segment_t *)
        """
        return _ida_idp.IDB_Hooks_adding_segm(self, *args)

    def func_deleted(self, *args) -> "void":
        r"""
        func_deleted(self, func_ea)
        A function has been deleted.

        @param func_ea: (::ea_t)
        """
        return _ida_idp.IDB_Hooks_func_deleted(self, *args)

    def dirtree_mkdir(self, *args) -> "void":
        r"""
        dirtree_mkdir(self, dt, path)

        @param dt: (dirtree_t *)
        @param path: (::const char *)
        """
        return _ida_idp.IDB_Hooks_dirtree_mkdir(self, *args)

    def dirtree_rmdir(self, *args) -> "void":
        r"""
        dirtree_rmdir(self, dt, path)

        @param dt: (dirtree_t *)
        @param path: (::const char *)
        """
        return _ida_idp.IDB_Hooks_dirtree_rmdir(self, *args)

    def dirtree_link(self, *args) -> "void":
        r"""
        dirtree_link(self, dt, path, link)

        @param dt: (dirtree_t *)
        @param path: (::const char *)
        @param link: (::bool)
        """
        return _ida_idp.IDB_Hooks_dirtree_link(self, *args)

    def dirtree_move(self, *args) -> "void":
        r"""
        dirtree_move(self, dt, _from, to)

        @param dt: (dirtree_t *)
        @param from: (::const char *)
        @param to: (::const char *)
        """
        return _ida_idp.IDB_Hooks_dirtree_move(self, *args)

    def dirtree_rank(self, *args) -> "void":
        r"""
        dirtree_rank(self, dt, path, rank)

        @param dt: (dirtree_t *)
        @param path: (::const char *)
        @param rank: (::size_t)
        """
        return _ida_idp.IDB_Hooks_dirtree_rank(self, *args)

    def dirtree_rminode(self, *args) -> "void":
        r"""
        dirtree_rminode(self, dt, inode)

        @param dt: (dirtree_t *)
        @param inode: (inode_t)
        """
        return _ida_idp.IDB_Hooks_dirtree_rminode(self, *args)

    def dirtree_segm_moved(self, *args) -> "void":
        r"""
        dirtree_segm_moved(self, dt)

        @param dt: (dirtree_t *)
        """
        return _ida_idp.IDB_Hooks_dirtree_segm_moved(self, *args)

    def enum_width_changed(self, *args) -> "void":
        r"""
        enum_width_changed(self, id, width)
        Enum width has been changed.

        @param id: (enum_t)
        @param width: (int)
        """
        return _ida_idp.IDB_Hooks_enum_width_changed(self, *args)

    def enum_flag_changed(self, *args) -> "void":
        r"""
        enum_flag_changed(self, id, F)
        Enum flags have been changed.

        @param id: (enum_t)
        @param F: (flags_t)
        """
        return _ida_idp.IDB_Hooks_enum_flag_changed(self, *args)

    def enum_ordinal_changed(self, *args) -> "void":
        r"""
        enum_ordinal_changed(self, id, ord)
        Enum mapping to a local type has been changed.

        @param id: (enum_t)
        @param ord: (int)
        """
        return _ida_idp.IDB_Hooks_enum_ordinal_changed(self, *args)
    __swig_destroy__ = _ida_idp.delete_IDB_Hooks
    def __disown__(self):
        self.this.disown()
        _ida_idp.disown_IDB_Hooks(self)
        return weakref.proxy(self)

# Register IDB_Hooks in _ida_idp:
_ida_idp.IDB_Hooks_swigregister(IDB_Hooks)


def get_idb_notifier_addr(*args) -> "PyObject *":
    r"""
    get_idb_notifier_addr(arg1) -> PyObject *

    @param arg1: PyObject *
    """
    return _ida_idp.get_idb_notifier_addr(*args)

def get_idb_notifier_ud_addr(*args) -> "PyObject *":
    r"""
    get_idb_notifier_ud_addr(hooks) -> PyObject *

    @param hooks: IDB_Hooks *
    """
    return _ida_idp.get_idb_notifier_ud_addr(*args)

#<pycode(py_idp_idbhooks)>

class _processor_t_Trampoline_IDB_Hooks(IDB_Hooks):
    def __init__(self, proc):
        IDB_Hooks.__init__(self, ida_idaapi.HBF_CALL_WITH_NEW_EXEC | ida_idaapi.HBF_VOLATILE_METHOD_SET)
        import weakref
        self.proc = weakref.ref(proc)
        for key in dir(self):
            if not key.startswith("_") and not key in ["proc"]:
                thing = getattr(self, key)
                if hasattr(thing, "__call__"):
                    setattr(self, key, self.__make_parent_caller(key))

    def __dummy(self, *args):
        return 0

    def __make_parent_caller(self, key):
# we can't get the method at this point, as it'll be bound
# to the processor_t instance, which means it'll increase
# the reference counting
        def call_parent(*args):
            return getattr(self.proc(), key, self.__dummy)(*args)
        return call_parent

#</pycode(py_idp_idbhooks)>


#<pycode(py_idp_notify_when)>
import weakref
class _notify_when_dispatcher_t:

    class _callback_t:
        def __init__(self, fun):
            self.fun = fun
            self.slots = 0

    class _IDP_Hooks(IDP_Hooks):
        def __init__(self, dispatcher):
            IDP_Hooks.__init__(self)
            self.dispatcher = weakref.ref(dispatcher)

        def ev_newfile(self, name):
            return self.dispatcher().dispatch(ida_idaapi.NW_OPENIDB, 0)

        def ev_oldfile(self, name):
            return self.dispatcher().dispatch(ida_idaapi.NW_OPENIDB, 1)

    class _IDB_Hooks(IDB_Hooks):
        def __init__(self, dispatcher):
            IDB_Hooks.__init__(self)
            self.dispatcher = weakref.ref(dispatcher)

        def closebase(self):
            return self.dispatcher().dispatch(ida_idaapi.NW_CLOSEIDB)


    def __init__(self):
        self.idp_hooks = self._IDP_Hooks(self)
        self.idp_hooks.hook()
        self.idb_hooks = self._IDB_Hooks(self)
        self.idb_hooks.hook()
        self.callbacks = []

    def _find(self, fun):
        for idx, cb in enumerate(self.callbacks):
            if cb.fun == fun:
                return idx, cb
        return None, None

    def dispatch(self, slot, *args):
        for cb in self.callbacks[:]: # make a copy, since dispatch() could cause some callbacks to disappear
            if (cb.slots & slot) != 0:
                cb.fun(slot, *args)
        return 0

    def notify_when(self, when, fun):
        _, cb = self._find(fun)
        if cb is None:
            cb = self._callback_t(fun)
            self.callbacks.append(cb)
        if (when & ida_idaapi.NW_REMOVE) != 0:
            cb.slots &= ~(when & ~ida_idaapi.NW_REMOVE)
        else:
            cb.slots |= when
        if cb.slots == 0:
            idx, cb = self._find(cb.fun)
            del self.callbacks[idx]
        return True

#</pycode(py_idp_notify_when)>




