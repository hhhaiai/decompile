"""
Functions that deal with fixup information.

A loader should setup fixup information using set_fixup()."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_fixup
else:
    import _ida_fixup

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

SWIG_PYTHON_LEGACY_BOOL = _ida_fixup.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

FIXUP_OFF8 = _ida_fixup.FIXUP_OFF8
r"""
8-bit offset
"""

FIXUP_OFF16 = _ida_fixup.FIXUP_OFF16
r"""
16-bit offset
"""

FIXUP_SEG16 = _ida_fixup.FIXUP_SEG16
r"""
16-bit base-logical segment base (selector)
"""

FIXUP_PTR16 = _ida_fixup.FIXUP_PTR16
r"""
32-bit long pointer (16-bit base:16-bit offset)
"""

FIXUP_OFF32 = _ida_fixup.FIXUP_OFF32
r"""
32-bit offset
"""

FIXUP_PTR32 = _ida_fixup.FIXUP_PTR32
r"""
48-bit pointer (16-bit base:32-bit offset)
"""

FIXUP_HI8 = _ida_fixup.FIXUP_HI8
r"""
high 8 bits of 16bit offset
"""

FIXUP_HI16 = _ida_fixup.FIXUP_HI16
r"""
high 16 bits of 32bit offset
"""

FIXUP_LOW8 = _ida_fixup.FIXUP_LOW8
r"""
low 8 bits of 16bit offset
"""

FIXUP_LOW16 = _ida_fixup.FIXUP_LOW16
r"""
low 16 bits of 32bit offset
"""

V695_FIXUP_VHIGH = _ida_fixup.V695_FIXUP_VHIGH
r"""
obsolete
"""

V695_FIXUP_VLOW = _ida_fixup.V695_FIXUP_VLOW
r"""
obsolete
"""

FIXUP_OFF64 = _ida_fixup.FIXUP_OFF64
r"""
64-bit offset
"""

FIXUP_OFF8S = _ida_fixup.FIXUP_OFF8S
r"""
8-bit signed offset
"""

FIXUP_OFF16S = _ida_fixup.FIXUP_OFF16S
r"""
16-bit signed offset
"""

FIXUP_OFF32S = _ida_fixup.FIXUP_OFF32S
r"""
32-bit signed offset
"""

FIXUP_CUSTOM = _ida_fixup.FIXUP_CUSTOM
r"""
start of the custom types range
"""


def is_fixup_custom(*args) -> "bool":
    r"""
    is_fixup_custom(type) -> bool
    Is fixup processed by processor module?

    @param type: (C++: fixup_type_t)
    """
    return _ida_fixup.is_fixup_custom(*args)
FIXUPF_REL = _ida_fixup.FIXUPF_REL
r"""
fixup is relative to the linear address `base'. Otherwise fixup is relative to
the start of the segment with `sel' selector.
"""

FIXUPF_EXTDEF = _ida_fixup.FIXUPF_EXTDEF
r"""
target is a location (otherwise - segment). Use this bit if the target is a
symbol rather than an offset from the beginning of a segment.
"""

FIXUPF_UNUSED = _ida_fixup.FIXUPF_UNUSED
r"""
fixup is ignored by IDA
* disallows the kernel to convert operands
* this fixup is not used during output
"""

FIXUPF_CREATED = _ida_fixup.FIXUPF_CREATED
r"""
fixup was not present in the input file
"""

FIXUPF_LOADER_MASK = _ida_fixup.FIXUPF_LOADER_MASK
r"""
additional flags. The bits from this mask are not stored in the database and can
be used by the loader at its discretion.
"""

class fixup_data_t(object):
    r"""
    Proxy of C++ fixup_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    sel = property(_ida_fixup.fixup_data_t_sel_get, _ida_fixup.fixup_data_t_sel_set, doc=r"""sel""")
    r"""
    selector of the target segment. BADSEL means an absolute (zero based) target.
    @see: FIXUPF_REL
    """
    off = property(_ida_fixup.fixup_data_t_off_get, _ida_fixup.fixup_data_t_off_set, doc=r"""off""")
    r"""
    target offset
    @note: The target is calculated as `get_base() + off`.
    """
    displacement = property(_ida_fixup.fixup_data_t_displacement_get, _ida_fixup.fixup_data_t_displacement_set, doc=r"""displacement""")
    r"""
    displacement (offset from the target)
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> fixup_data_t
        __init__(self, type_, flags_=0) -> fixup_data_t

        @param type_: fixup_type_t
        @param flags_: uint32
        """
        _ida_fixup.fixup_data_t_swiginit(self, _ida_fixup.new_fixup_data_t(*args))

    def get_type(self, *args) -> "fixup_type_t":
        r"""
        get_type(self) -> fixup_type_t
        Fixup type Types of fixups.
        """
        return _ida_fixup.fixup_data_t_get_type(self, *args)

    def set_type(self, *args) -> "void":
        r"""
        set_type(self, type_)

        @param type_: fixup_type_t
        """
        return _ida_fixup.fixup_data_t_set_type(self, *args)

    def set_type_and_flags(self, *args) -> "void":
        r"""
        set_type_and_flags(self, type_, flags_=0)

        @param type_: fixup_type_t
        @param flags_: uint32
        """
        return _ida_fixup.fixup_data_t_set_type_and_flags(self, *args)

    def is_custom(self, *args) -> "bool":
        r"""
        is_custom(self) -> bool
        is_fixup_custom()
        """
        return _ida_fixup.fixup_data_t_is_custom(self, *args)

    def get_flags(self, *args) -> "uint32":
        r"""
        get_flags(self) -> uint32
        Fixup flags Fixup flags.
        """
        return _ida_fixup.fixup_data_t_get_flags(self, *args)

    def is_extdef(self, *args) -> "bool":
        r"""
        is_extdef(self) -> bool
        """
        return _ida_fixup.fixup_data_t_is_extdef(self, *args)

    def set_extdef(self, *args) -> "void":
        r"""
        set_extdef(self)
        """
        return _ida_fixup.fixup_data_t_set_extdef(self, *args)

    def clr_extdef(self, *args) -> "void":
        r"""
        clr_extdef(self)
        """
        return _ida_fixup.fixup_data_t_clr_extdef(self, *args)

    def is_unused(self, *args) -> "bool":
        r"""
        is_unused(self) -> bool
        """
        return _ida_fixup.fixup_data_t_is_unused(self, *args)

    def set_unused(self, *args) -> "void":
        r"""
        set_unused(self)
        """
        return _ida_fixup.fixup_data_t_set_unused(self, *args)

    def clr_unused(self, *args) -> "void":
        r"""
        clr_unused(self)
        """
        return _ida_fixup.fixup_data_t_clr_unused(self, *args)

    def has_base(self, *args) -> "bool":
        r"""
        has_base(self) -> bool
        Is fixup relative?
        """
        return _ida_fixup.fixup_data_t_has_base(self, *args)

    def was_created(self, *args) -> "bool":
        r"""
        was_created(self) -> bool
        Is fixup artificial?
        """
        return _ida_fixup.fixup_data_t_was_created(self, *args)

    def get_base(self, *args) -> "ea_t":
        r"""
        get_base(self) -> ea_t
        Get base of fixup.
        @note: The target is calculated as `get_base() + off`.
        @see: FIXUPF_REL
        """
        return _ida_fixup.fixup_data_t_get_base(self, *args)

    def set_base(self, *args) -> "void":
        r"""
        set_base(self, new_base)
        Set base of fixup. The target should be set before a call of this function.

        @param new_base: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_set_base(self, *args)

    def set_sel(self, *args) -> "void":
        r"""
        set_sel(self, seg)

        @param seg: segment_t const *
        """
        return _ida_fixup.fixup_data_t_set_sel(self, *args)

    def set_target_sel(self, *args) -> "void":
        r"""
        set_target_sel(self)
        Set selector of fixup to the target. The target should be set before a call of
        this function.
        """
        return _ida_fixup.fixup_data_t_set_target_sel(self, *args)

    def set(self, *args) -> "void":
        r"""
        set(self, source)
        set_fixup()

        @param source: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_set(self, *args)

    def get(self, *args) -> "bool":
        r"""
        get(self, source) -> bool
        get_fixup()

        @param source: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_get(self, *args)

    def get_handler(self, *args) -> "fixup_handler_t const *":
        r"""
        get_handler(self) -> fixup_handler_t const *
        get_fixup_handler()
        """
        return _ida_fixup.fixup_data_t_get_handler(self, *args)

    def get_desc(self, *args) -> "char const *":
        r"""
        get_desc(self, source) -> char const *
        get_fixup_desc()

        @param source: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_get_desc(self, *args)

    def calc_size(self, *args) -> "int":
        r"""
        calc_size(self) -> int
        calc_fixup_size()
        """
        return _ida_fixup.fixup_data_t_calc_size(self, *args)

    def get_value(self, *args) -> "uval_t":
        r"""
        get_value(self, ea) -> uval_t
        get_fixup_value()

        @param ea: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_get_value(self, *args)

    def patch_value(self, *args) -> "bool":
        r"""
        patch_value(self, ea) -> bool
        patch_fixup_value()

        @param ea: (C++: ea_t)
        """
        return _ida_fixup.fixup_data_t_patch_value(self, *args)
    __swig_destroy__ = _ida_fixup.delete_fixup_data_t

# Register fixup_data_t in _ida_fixup:
_ida_fixup.fixup_data_t_swigregister(fixup_data_t)


def get_fixup(*args) -> "bool":
    r"""
    get_fixup(fd, source) -> bool
    Get fixup information.

    @param fd: (C++: fixup_data_t *)
    @param source: (C++: ea_t)
    """
    return _ida_fixup.get_fixup(*args)

def exists_fixup(*args) -> "bool":
    r"""
    exists_fixup(source) -> bool
    Check that a fixup exists at the given address.

    @param source: (C++: ea_t)
    """
    return _ida_fixup.exists_fixup(*args)

def set_fixup(*args) -> "void":
    r"""
    set_fixup(source, fd)
    Set fixup information. You should fill fixup_data_t and call this function and
    the kernel will remember information in the database.

    @param source: (C++: ea_t) the fixup source address, i.e. the address modified by the fixup
    @param fd: (C++: const fixup_data_t &) fixup data
    """
    return _ida_fixup.set_fixup(*args)

def del_fixup(*args) -> "void":
    r"""
    del_fixup(source)
    Delete fixup information.

    @param source: (C++: ea_t)
    """
    return _ida_fixup.del_fixup(*args)

def get_first_fixup_ea(*args) -> "ea_t":
    r"""
    get_first_fixup_ea() -> ea_t
    Get the first address with fixup information

    @return: the first address with fixup information, or BADADDR
    """
    return _ida_fixup.get_first_fixup_ea(*args)

def get_next_fixup_ea(*args) -> "ea_t":
    r"""
    get_next_fixup_ea(ea) -> ea_t
    Find next address with fixup information

    @param ea: (C++: ea_t) current address
    @return: the next address with fixup information, or BADADDR
    """
    return _ida_fixup.get_next_fixup_ea(*args)

def get_prev_fixup_ea(*args) -> "ea_t":
    r"""
    get_prev_fixup_ea(ea) -> ea_t
    Find previous address with fixup information

    @param ea: (C++: ea_t) current address
    @return: the previous address with fixup information, or BADADDR
    """
    return _ida_fixup.get_prev_fixup_ea(*args)

def get_fixup_handler(*args) -> "fixup_handler_t const *":
    r"""
    get_fixup_handler(type) -> fixup_handler_t const *
    Get handler of standard or custom fixup.

    @param type: (C++: fixup_type_t)
    """
    return _ida_fixup.get_fixup_handler(*args)

def get_fixup_value(*args) -> "uval_t":
    r"""
    get_fixup_value(ea, type) -> uval_t
    Get the operand value. This function get fixup bytes from data or an instruction
    at `ea' and convert them to the operand value (maybe partially). It is opposite
    in meaning to the `patch_fixup_value()`. For example, FIXUP_HI8 read a byte at
    `ea' and shifts it left by 8 bits, or AArch64's custom fixup BRANCH26 get low 26
    bits of the insn at `ea' and shifts it left by 2 bits. This function is mainly
    used to get a relocation addend.

    @param ea: (C++: ea_t) address to get fixup bytes from, the size of the fixup bytes depends
               on the fixup type.
    @see: fixup_handler_t::size
    @param type: (C++: fixup_type_t) fixup type
    @retval operand: value
    """
    return _ida_fixup.get_fixup_value(*args)

def patch_fixup_value(*args) -> "bool":
    r"""
    patch_fixup_value(ea, fd) -> bool
    Patch the fixup bytes. This function updates data or an instruction at `ea' to
    the fixup bytes. For example, FIXUP_HI8 updates a byte at `ea' to the high byte
    of `fd->off', or AArch64's custom fixup BRANCH26 updates low 26 bits of the insn
    at `ea' to the value of `fd->off' shifted right by 2.

    @param ea: (C++: ea_t) address where data are changed, the size of the changed data depends
               on the fixup type.
    @see: fixup_handler_t::size
    @param fd: (C++: const fixup_data_t &) fixup data
    @retval false: the fixup bytes do not fit (e.g. `fd->off' is greater than
                   0xFFFFFFC for BRANCH26). The database is changed even in this
                   case.
    """
    return _ida_fixup.patch_fixup_value(*args)

def get_fixup_desc(*args) -> "fixup_data_t const &":
    r"""
    get_fixup_desc(source, fd) -> str
    Get FIXUP description comment.

    @param source: (C++: ea_t)
    @param fd: (C++: const fixup_data_t &) fixup_data_t const &
    """
    return _ida_fixup.get_fixup_desc(*args)

def calc_fixup_size(*args) -> "int":
    r"""
    calc_fixup_size(type) -> int
    Calculate size of fixup in bytes (the number of bytes the fixup patches)
    @retval -1: means error

    @param type: (C++: fixup_type_t)
    """
    return _ida_fixup.calc_fixup_size(*args)

def find_custom_fixup(*args) -> "fixup_type_t":
    r"""
    find_custom_fixup(name) -> fixup_type_t
    Get id of a custom fixup handler.

    @param name: (C++: const char *) name of the custom fixup handler
    @return: id with FIXUP_CUSTOM bit set or 0
    """
    return _ida_fixup.find_custom_fixup(*args)
class fixup_info_t(object):
    r"""
    Proxy of C++ fixup_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ea = property(_ida_fixup.fixup_info_t_ea_get, _ida_fixup.fixup_info_t_ea_set, doc=r"""ea""")
    fd = property(_ida_fixup.fixup_info_t_fd_get, _ida_fixup.fixup_info_t_fd_set, doc=r"""fd""")

    def __init__(self, *args):
        r"""
        __init__(self) -> fixup_info_t
        """
        _ida_fixup.fixup_info_t_swiginit(self, _ida_fixup.new_fixup_info_t(*args))
    __swig_destroy__ = _ida_fixup.delete_fixup_info_t

# Register fixup_info_t in _ida_fixup:
_ida_fixup.fixup_info_t_swigregister(fixup_info_t)


def get_fixups(*args) -> "bool":
    r"""
    get_fixups(out, ea, size) -> bool

    @param out: fixups_t *
    @param ea: ea_t
    @param size: asize_t
    """
    return _ida_fixup.get_fixups(*args)

def contains_fixups(*args) -> "bool":
    r"""
    contains_fixups(ea, size) -> bool
    Does the specified address range contain any fixup information?

    @param ea: (C++: ea_t)
    @param size: (C++: asize_t)
    """
    return _ida_fixup.contains_fixups(*args)

def gen_fix_fixups(*args) -> "void":
    r"""
    gen_fix_fixups(_from, to, size)
    Relocate the bytes with fixup information once more (generic function). This
    function may be called from loader_t::move_segm() if it suits the goal. If
    loader_t::move_segm is not defined then this function will be called
    automatically when moving segments or rebasing the entire program. Special
    parameter values (from = BADADDR, size = 0, to = delta) are used when the
    function is called from rebase_program(delta).

    @param from: (C++: ea_t)
    @param to: (C++: ea_t)
    @param size: (C++: asize_t)
    """
    return _ida_fixup.gen_fix_fixups(*args)

def handle_fixups_in_macro(*args) -> "bool":
    r"""
    handle_fixups_in_macro(ri, ea, other, macro_reft_and_flags) -> bool
    Handle two fixups in a macro. We often combine two instruction that load parts
    of a value into one macro instruction. For example:
    ARM:   ADRP  X0, #var@PAGE
    ADD   X0, X0, #var@PAGEOFF  --> ADRL X0, var
    MIPS:  lui   $v0, %hi(var)
    addiu $v0, $v0, %lo(var)    --> la   $v0, var
    When applying the fixups that fall inside such a macro, we should convert them
    to one refinfo. This function does exactly that. It should be called from the
    apply() callback of a custom fixup.

    @param ri: (C++: refinfo_t *)
    @param ea: (C++: ea_t)
    @param other: (C++: fixup_type_t)
    @param macro_reft_and_flags: (C++: uint32)
    @return: success ('false' means that RI was not changed)
    """
    return _ida_fixup.handle_fixups_in_macro(*args)



