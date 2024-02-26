"""
Functions that deal with the segment registers.

If your processor doesn't use segment registers, then these functions are of no
use for you. However, you should define two virtual segment registers - CS and
DS (for code segment and data segment) and specify their internal numbers in the
LPH structure (processor_t::reg_code_sreg and processor_t::reg_data_sreg)."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_segregs
else:
    import _ida_segregs

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

SWIG_PYTHON_LEGACY_BOOL = _ida_segregs.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
R_es = _ida_segregs.R_es

R_cs = _ida_segregs.R_cs

R_ss = _ida_segregs.R_ss

R_ds = _ida_segregs.R_ds

R_fs = _ida_segregs.R_fs

R_gs = _ida_segregs.R_gs

class sreg_range_t(ida_range.range_t):
    r"""
    Proxy of C++ sreg_range_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    val = property(_ida_segregs.sreg_range_t_val_get, _ida_segregs.sreg_range_t_val_set, doc=r"""val""")
    r"""
    segment register value
    """
    tag = property(_ida_segregs.sreg_range_t_tag_get, _ida_segregs.sreg_range_t_tag_set, doc=r"""tag""")
    r"""
    Segment register range tags
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> sreg_range_t
        """
        _ida_segregs.sreg_range_t_swiginit(self, _ida_segregs.new_sreg_range_t(*args))
    __swig_destroy__ = _ida_segregs.delete_sreg_range_t

# Register sreg_range_t in _ida_segregs:
_ida_segregs.sreg_range_t_swigregister(sreg_range_t)
SR_inherit = _ida_segregs.SR_inherit
r"""
the value is inherited from the previous range
"""

SR_user = _ida_segregs.SR_user
r"""
the value is specified by the user
"""

SR_auto = _ida_segregs.SR_auto
r"""
the value is determined by IDA
"""

SR_autostart = _ida_segregs.SR_autostart
r"""
used as SR_auto for segment starting address
"""



def get_sreg(*args) -> "sel_t":
    r"""
    get_sreg(ea, rg) -> sel_t
    Get value of a segment register. This function uses segment register range and
    default segment register values stored in the segment structure.

    @param ea: (C++: ea_t) linear address in the program
    @param rg: (C++: int) number of the segment register
    @return: value of the segment register, BADSEL if value is unknown.
    """
    return _ida_segregs.get_sreg(*args)

def split_sreg_range(*args) -> "bool":
    r"""
    split_sreg_range(ea, rg, v, tag, silent=False) -> bool
    Create a new segment register range. This function is used when the IDP emulator
    detects that a segment register changes its value.

    @param ea: (C++: ea_t) linear address where the segment register will have a new value. if
               ea==BADADDR, nothing to do.
    @param rg: (C++: int) the number of the segment register
    @param v: (C++: sel_t) the new value of the segment register. If the value is unknown, you
              should specify BADSEL.
    @param tag: (C++: uchar) the register info tag. see Segment register range tags
    @param silent: (C++: bool) if false, display a warning() in the case of failure
    @return: success
    """
    return _ida_segregs.split_sreg_range(*args)

def set_default_sreg_value(*args) -> "bool":
    r"""
    set_default_sreg_value(sg, rg, value) -> bool
    Set default value of a segment register for a segment.

    @param sg: (C++: segment_t *) pointer to segment structure if nullptr, then set the register for
               all segments
    @param rg: (C++: int) number of segment register
    @param value: (C++: sel_t) its default value. this value will be used by get_sreg() if value
                  of the register is unknown at the specified address.
    @return: success
    """
    return _ida_segregs.set_default_sreg_value(*args)

def set_sreg_at_next_code(*args) -> "void":
    r"""
    set_sreg_at_next_code(ea1, ea2, rg, value)
    Set the segment register value at the next instruction. This function is
    designed to be called from idb_event::sgr_changed handler in order to contain
    the effect of changing a segment register value only until the next instruction.

    It is useful, for example, in the ARM module: the modification of the T register
    does not affect existing instructions later in the code.

    @param ea1: (C++: ea_t) address to start to search for an instruction
    @param ea2: (C++: ea_t) the maximal address
    @param rg: (C++: int) the segment register number
    @param value: (C++: sel_t) the segment register value
    """
    return _ida_segregs.set_sreg_at_next_code(*args)

def get_sreg_range(*args) -> "bool":
    r"""
    get_sreg_range(out, ea, rg) -> bool
    Get segment register range by linear address.

    @param out: (C++: sreg_range_t *) segment register range
    @param ea: (C++: ea_t) any linear address in the program
    @param rg: (C++: int) the segment register number
    @return: success
    """
    return _ida_segregs.get_sreg_range(*args)

def get_prev_sreg_range(*args) -> "bool":
    r"""
    get_prev_sreg_range(out, ea, rg) -> bool
    Get segment register range previous to one with address.
    @note: more efficient then get_sreg_range(reg, ea-1)

    @param out: (C++: sreg_range_t *) segment register range
    @param ea: (C++: ea_t) any linear address in the program
    @param rg: (C++: int) the segment register number
    @return: success
    """
    return _ida_segregs.get_prev_sreg_range(*args)

def set_default_dataseg(*args) -> "void":
    r"""
    set_default_dataseg(ds_sel)
    Set default value of DS register for all segments.

    @param ds_sel: (C++: sel_t)
    """
    return _ida_segregs.set_default_dataseg(*args)

def get_sreg_ranges_qty(*args) -> "size_t":
    r"""
    get_sreg_ranges_qty(rg) -> size_t
    Get number of segment register ranges.

    @param rg: (C++: int) the segment register number
    """
    return _ida_segregs.get_sreg_ranges_qty(*args)

def getn_sreg_range(*args) -> "bool":
    r"""
    getn_sreg_range(out, rg, n) -> bool
    Get segment register range by its number.

    @param out: (C++: sreg_range_t *) segment register range
    @param rg: (C++: int) the segment register number
    @param n: (C++: int) number of range (0..qty()-1)
    @return: success
    """
    return _ida_segregs.getn_sreg_range(*args)

def get_sreg_range_num(*args) -> "int":
    r"""
    get_sreg_range_num(ea, rg) -> int
    Get number of segment register range by address.

    @param ea: (C++: ea_t) any address in the range
    @param rg: (C++: int) the segment register number
    @return: -1 if no range occupies the specified address. otherwise returns number
             of the specified range (0..get_srranges_qty()-1)
    """
    return _ida_segregs.get_sreg_range_num(*args)

def del_sreg_range(*args) -> "bool":
    r"""
    del_sreg_range(ea, rg) -> bool
    Delete segment register range started at ea. When a segment register range is
    deleted, the previous range is extended to cover the empty space. The segment
    register range at the beginning of a segment cannot be deleted.

    @param ea: (C++: ea_t) start_ea of the deleted range
    @param rg: (C++: int) the segment register number
    @return: success
    """
    return _ida_segregs.del_sreg_range(*args)

def copy_sreg_ranges(*args) -> "void":
    r"""
    copy_sreg_ranges(dst_rg, src_rg, map_selector=False)
    Duplicate segment register ranges.

    @param dst_rg: (C++: int) number of destination segment register
    @param src_rg: (C++: int) copy ranges from
    @param map_selector: (C++: bool) map selectors to linear addresses using sel2ea()
    """
    return _ida_segregs.copy_sreg_ranges(*args)



