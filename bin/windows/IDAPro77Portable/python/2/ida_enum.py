"""
Assembly level enum management.

Enums and bitfields are represented as enum_t."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_enum
else:
    import _ida_enum

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


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

SWIG_PYTHON_LEGACY_BOOL = _ida_enum.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

DEFMASK = _ida_enum.DEFMASK
r"""
default bitmask
"""


def get_enum_qty(*args):
    r"""
    get_enum_qty() -> size_t
    Get number of declared enum_t types.
    """
    return _ida_enum.get_enum_qty(*args)

def getn_enum(*args):
    r"""
    getn_enum(idx) -> enum_t
    Get enum by its index in the list of enums (0..get_enum_qty()-1).

    @param idx: (C++: size_t)
    """
    return _ida_enum.getn_enum(*args)

def get_enum_idx(*args):
    r"""
    get_enum_idx(id) -> uval_t
    Get the index in the list of enums.

    @param id: (C++: enum_t)
    """
    return _ida_enum.get_enum_idx(*args)

def get_enum(*args):
    r"""
    get_enum(name) -> enum_t
    Get enum by name.

    @param name: (C++: const char *) char const *
    """
    return _ida_enum.get_enum(*args)

def is_bf(*args):
    r"""
    is_bf(id) -> bool
    Is enum a bitfield? (otherwise - plain enum, no bitmasks except for DEFMASK are
    allowed)

    @param id: (C++: enum_t)
    """
    return _ida_enum.is_bf(*args)

def is_enum_hidden(*args):
    r"""
    is_enum_hidden(id) -> bool
    Is enum collapsed?

    @param id: (C++: enum_t)
    """
    return _ida_enum.is_enum_hidden(*args)

def set_enum_hidden(*args):
    r"""
    set_enum_hidden(id, hidden) -> bool
    Collapse enum.

    @param id: (C++: enum_t)
    @param hidden: (C++: bool)
    """
    return _ida_enum.set_enum_hidden(*args)

def is_enum_fromtil(*args):
    r"""
    is_enum_fromtil(id) -> bool
    Does enum come from type library?

    @param id: (C++: enum_t)
    """
    return _ida_enum.is_enum_fromtil(*args)

def set_enum_fromtil(*args):
    r"""
    set_enum_fromtil(id, fromtil) -> bool
    Specify that enum comes from a type library.

    @param id: (C++: enum_t)
    @param fromtil: (C++: bool)
    """
    return _ida_enum.set_enum_fromtil(*args)

def is_ghost_enum(*args):
    r"""
    is_ghost_enum(id) -> bool
    Is a ghost copy of a local type?

    @param id: (C++: enum_t)
    """
    return _ida_enum.is_ghost_enum(*args)

def set_enum_ghost(*args):
    r"""
    set_enum_ghost(id, ghost) -> bool
    Specify that enum is a ghost copy of a local type.

    @param id: (C++: enum_t)
    @param ghost: (C++: bool)
    """
    return _ida_enum.set_enum_ghost(*args)

def get_enum_name(*args):
    r"""
    get_enum_name(id) -> str

    @param id: enum_t
    """
    return _ida_enum.get_enum_name(*args)

def get_enum_name2(*args):
    r"""
    get_enum_name2(id, flags=0) -> str
    Get name of enum

    @param id: (C++: enum_t) enum id
    @param flags: (C++: int) Enum name flags
    """
    return _ida_enum.get_enum_name2(*args)
ENFL_REGEX = _ida_enum.ENFL_REGEX
r"""
apply regular expressions to beautify the name
"""


def get_enum_width(*args):
    r"""
    get_enum_width(id) -> size_t
    Get the width of a enum element allowed values: 0 (unspecified),1,2,4,8,16,32,64

    @param id: (C++: enum_t)
    """
    return _ida_enum.get_enum_width(*args)

def set_enum_width(*args):
    r"""
    set_enum_width(id, width) -> bool
    See comment for get_enum_width()

    @param id: (C++: enum_t)
    @param width: (C++: int)
    """
    return _ida_enum.set_enum_width(*args)

def get_enum_cmt(*args):
    r"""
    get_enum_cmt(id, repeatable) -> str
    Get enum comment.

    @param id: (C++: enum_t)
    @param repeatable: (C++: bool)
    """
    return _ida_enum.get_enum_cmt(*args)

def get_enum_size(*args):
    r"""
    get_enum_size(id) -> size_t
    Get the number of the members of the enum.

    @param id: (C++: enum_t)
    """
    return _ida_enum.get_enum_size(*args)

def get_enum_flag(*args):
    r"""
    get_enum_flag(id) -> flags_t
    Get flags determining the representation of the enum. (currently they define the
    numeric base: octal, decimal, hex, bin) and signness.

    @param id: (C++: enum_t)
    """
    return _ida_enum.get_enum_flag(*args)

def get_enum_member_by_name(*args):
    r"""
    get_enum_member_by_name(name) -> const_t
    Get a reference to an enum member by its name.

    @param name: (C++: const char *) char const *
    """
    return _ida_enum.get_enum_member_by_name(*args)

def get_enum_member_value(*args):
    r"""
    get_enum_member_value(id) -> uval_t
    Get value of an enum member.

    @param id: (C++: const_t)
    """
    return _ida_enum.get_enum_member_value(*args)

def get_enum_member_enum(*args):
    r"""
    get_enum_member_enum(id) -> enum_t
    Get the parent enum of an enum member.

    @param id: (C++: const_t)
    """
    return _ida_enum.get_enum_member_enum(*args)

def get_enum_member_bmask(*args):
    r"""
    get_enum_member_bmask(id) -> bmask_t
    Get bitmask of an enum member.

    @param id: (C++: const_t)
    """
    return _ida_enum.get_enum_member_bmask(*args)

def get_enum_member(*args):
    r"""
    get_enum_member(id, value, serial, mask) -> const_t
    Find an enum member by enum, value and bitmask
    @note: if serial -1, return a member with any serial

    @param id: (C++: enum_t)
    @param value: (C++: uval_t)
    @param serial: (C++: int)
    @param mask: (C++: bmask_t)
    """
    return _ida_enum.get_enum_member(*args)

def get_first_bmask(*args):
    r"""
    get_first_bmask(id) -> bmask_t
    Get first bitmask in the enum (bitfield)

    @param enum_id: id of enum (bitfield)
    @return: the smallest bitmask for enum, or DEFMASK
    """
    return _ida_enum.get_first_bmask(*args)

def get_last_bmask(*args):
    r"""
    get_last_bmask(id) -> bmask_t
    Get last bitmask in the enum (bitfield)

    @param enum_id: id of enum
    @return: the biggest bitmask for enum, or DEFMASK
    """
    return _ida_enum.get_last_bmask(*args)

def get_next_bmask(*args):
    r"""
    get_next_bmask(id, bmask) -> bmask_t
    Get next bitmask in the enum (bitfield)

    @param enum_id: id of enum
    @param bmask: (C++: bmask_t)
    @return: value of a bitmask with value higher than the specified value, or
             DEFMASK
    """
    return _ida_enum.get_next_bmask(*args)

def get_prev_bmask(*args):
    r"""
    get_prev_bmask(id, bmask) -> bmask_t
    Get prev bitmask in the enum (bitfield)

    @param enum_id: id of enum
    @param bmask: (C++: bmask_t)
    @return: value of a bitmask with value lower than the specified value, or
             DEFMASK
    """
    return _ida_enum.get_prev_bmask(*args)

def get_first_enum_member(*args):
    r"""
    get_first_enum_member(id, bmask=(bmask_t(-1))) -> uval_t

    @param id: enum_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_first_enum_member(*args)

def get_last_enum_member(*args):
    r"""
    get_last_enum_member(id, bmask=(bmask_t(-1))) -> uval_t

    @param id: enum_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_last_enum_member(*args)

def get_next_enum_member(*args):
    r"""
    get_next_enum_member(id, value, bmask=(bmask_t(-1))) -> uval_t

    @param id: enum_t
    @param value: uval_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_next_enum_member(*args)

def get_prev_enum_member(*args):
    r"""
    get_prev_enum_member(id, value, bmask=(bmask_t(-1))) -> uval_t

    @param id: enum_t
    @param value: uval_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_prev_enum_member(*args)

def get_enum_member_name(*args):
    r"""
    get_enum_member_name(id) -> str
    Get name of an enum member by const_t.

    @param id: (C++: const_t)
    """
    return _ida_enum.get_enum_member_name(*args)

def get_enum_member_cmt(*args):
    r"""
    get_enum_member_cmt(id, repeatable) -> str
    Get enum member's comment.

    @param id: (C++: const_t)
    @param repeatable: (C++: bool)
    """
    return _ida_enum.get_enum_member_cmt(*args)

def get_first_serial_enum_member(*args):
    r"""
    get_first_serial_enum_member(id, value, bmask) -> const_t

    @param id: enum_t
    @param value: uval_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_first_serial_enum_member(*args)

def get_last_serial_enum_member(*args):
    r"""
    get_last_serial_enum_member(id, value, bmask) -> const_t

    @param id: enum_t
    @param value: uval_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_last_serial_enum_member(*args)

def get_next_serial_enum_member(*args):
    r"""
    get_next_serial_enum_member(in_out_serial, first_cid) -> const_t

    @param in_out_serial: uchar *
    @param first_cid: const_t
    """
    return _ida_enum.get_next_serial_enum_member(*args)

def get_prev_serial_enum_member(*args):
    r"""
    get_prev_serial_enum_member(in_out_serial, first_cid) -> const_t

    @param in_out_serial: uchar *
    @param first_cid: const_t
    """
    return _ida_enum.get_prev_serial_enum_member(*args)
class enum_member_visitor_t(object):
    r"""
    Proxy of C++ enum_member_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def visit_enum_member(self, *args):
        r"""
        visit_enum_member(self, cid, value) -> int
        Implements action to take when enum member is visited.

        @param cid: (C++: const_t)
        @param value: (C++: uval_t)
        @return: nonzero to stop the iteration
        """
        return _ida_enum.enum_member_visitor_t_visit_enum_member(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> enum_member_visitor_t

        @param self: PyObject *
        """
        if self.__class__ == enum_member_visitor_t:
            _self = None
        else:
            _self = self
        _ida_enum.enum_member_visitor_t_swiginit(self, _ida_enum.new_enum_member_visitor_t(_self, *args))
    __swig_destroy__ = _ida_enum.delete_enum_member_visitor_t
    def __disown__(self):
        self.this.disown()
        _ida_enum.disown_enum_member_visitor_t(self)
        return weakref.proxy(self)

# Register enum_member_visitor_t in _ida_enum:
_ida_enum.enum_member_visitor_t_swigregister(enum_member_visitor_t)
cvar = _ida_enum.cvar
MAX_ENUM_SERIAL = cvar.MAX_ENUM_SERIAL
r"""
Max number of identical constants allowed for one enum type.
"""


def for_all_enum_members(*args):
    r"""
    for_all_enum_members(id, cv) -> int
    Visit all members of a given enum.

    @param id: (C++: enum_t)
    @param cv: (C++: enum_member_visitor_t &)
    """
    return _ida_enum.for_all_enum_members(*args)

def get_enum_member_serial(*args):
    r"""
    get_enum_member_serial(cid) -> uchar
    Get serial number of an enum member.

    @param cid: (C++: const_t)
    """
    return _ida_enum.get_enum_member_serial(*args)

def get_enum_type_ordinal(*args):
    r"""
    get_enum_type_ordinal(id) -> int32
    Get corresponding type ordinal number.

    @param id: (C++: enum_t)
    """
    return _ida_enum.get_enum_type_ordinal(*args)

def set_enum_type_ordinal(*args):
    r"""
    set_enum_type_ordinal(id, ord)
    Set corresponding type ordinal number.

    @param id: (C++: enum_t)
    @param ord: (C++: int32)
    """
    return _ida_enum.set_enum_type_ordinal(*args)

def add_enum(*args):
    r"""
    add_enum(idx, name, flag) -> enum_t
    Add new enum type.
    * if idx==BADADDR then add as the last idx
    * if name==nullptr then generate a unique name "enum_%d"

    @param idx: (C++: size_t)
    @param name: (C++: const char *) char const *
    @param flag: (C++: flags_t)
    """
    return _ida_enum.add_enum(*args)

def del_enum(*args):
    r"""
    del_enum(id)
    Delete an enum type.

    @param id: (C++: enum_t)
    """
    return _ida_enum.del_enum(*args)

def set_enum_idx(*args):
    r"""
    set_enum_idx(id, idx) -> bool
    Set serial number of enum. Also see get_enum_idx().

    @param id: (C++: enum_t)
    @param idx: (C++: size_t)
    """
    return _ida_enum.set_enum_idx(*args)

def set_enum_bf(*args):
    r"""
    set_enum_bf(id, bf) -> bool
    Set 'bitfield' bit of enum (i.e. convert it to a bitfield)

    @param id: (C++: enum_t)
    @param bf: (C++: bool)
    """
    return _ida_enum.set_enum_bf(*args)

def set_enum_name(*args):
    r"""
    set_enum_name(id, name) -> bool
    Set name of enum type.

    @param id: (C++: enum_t)
    @param name: (C++: const char *) char const *
    """
    return _ida_enum.set_enum_name(*args)

def set_enum_cmt(*args):
    r"""
    set_enum_cmt(id, cmt, repeatable) -> bool
    Set comment for enum type.

    @param id: (C++: enum_t)
    @param cmt: (C++: const char *) char const *
    @param repeatable: (C++: bool)
    """
    return _ida_enum.set_enum_cmt(*args)

def set_enum_flag(*args):
    r"""
    set_enum_flag(id, flag) -> bool
    Set data representation flags.

    @param id: (C++: enum_t)
    @param flag: (C++: flags_t)
    """
    return _ida_enum.set_enum_flag(*args)

def add_enum_member(*args):
    r"""
    add_enum_member(id, name, value, bmask=(bmask_t(-1))) -> int
    Add member to enum type.

    @param id: (C++: enum_t)
    @param name: (C++: const char *) char const *
    @param value: (C++: uval_t)
    @param bmask: (C++: bmask_t)
    @return: 0 if ok, otherwise one of Add enum member result codes
    """
    return _ida_enum.add_enum_member(*args)
ENUM_MEMBER_ERROR_NAME = _ida_enum.ENUM_MEMBER_ERROR_NAME
r"""
already have member with this name (bad name)
"""

ENUM_MEMBER_ERROR_VALUE = _ida_enum.ENUM_MEMBER_ERROR_VALUE
r"""
already have 256 members with this value
"""

ENUM_MEMBER_ERROR_ENUM = _ida_enum.ENUM_MEMBER_ERROR_ENUM
r"""
bad enum id
"""

ENUM_MEMBER_ERROR_MASK = _ida_enum.ENUM_MEMBER_ERROR_MASK
r"""
bad bmask
"""

ENUM_MEMBER_ERROR_ILLV = _ida_enum.ENUM_MEMBER_ERROR_ILLV
r"""
bad bmask and value combination (~bmask & value != 0)
"""


def del_enum_member(*args):
    r"""
    del_enum_member(id, value, serial, bmask) -> bool
    Delete member of enum type.

    @param id: (C++: enum_t)
    @param value: (C++: uval_t)
    @param serial: (C++: uchar)
    @param bmask: (C++: bmask_t)
    """
    return _ida_enum.del_enum_member(*args)

def set_enum_member_name(*args):
    r"""
    set_enum_member_name(id, name) -> bool
    Set name of enum member.

    @param id: (C++: const_t)
    @param name: (C++: const char *) char const *
    """
    return _ida_enum.set_enum_member_name(*args)

def set_enum_member_cmt(*args):
    r"""
    set_enum_member_cmt(id, cmt, repeatable) -> bool
    Set comment for enum member.

    @param id: (C++: const_t)
    @param cmt: (C++: const char *) char const *
    @param repeatable: (C++: bool)
    """
    return _ida_enum.set_enum_member_cmt(*args)

def is_one_bit_mask(*args):
    r"""
    is_one_bit_mask(mask) -> bool
    Is bitmask one bit?

    @param mask: (C++: bmask_t)
    """
    return _ida_enum.is_one_bit_mask(*args)

def set_bmask_name(*args):
    r"""
    set_bmask_name(id, bmask, name) -> bool

    @param id: enum_t
    @param bmask: bmask_t
    @param name: char const *
    """
    return _ida_enum.set_bmask_name(*args)

def get_bmask_name(*args):
    r"""
    get_bmask_name(id, bmask) -> str

    @param id: enum_t
    @param bmask: bmask_t
    """
    return _ida_enum.get_bmask_name(*args)

def set_bmask_cmt(*args):
    r"""
    set_bmask_cmt(id, bmask, cmt, repeatable) -> bool

    @param id: enum_t
    @param bmask: bmask_t
    @param cmt: char const *
    @param repeatable: bool
    """
    return _ida_enum.set_bmask_cmt(*args)

def get_bmask_cmt(*args):
    r"""
    get_bmask_cmt(id, bmask, repeatable) -> str

    @param id: enum_t
    @param bmask: bmask_t
    @param repeatable: bool
    """
    return _ida_enum.get_bmask_cmt(*args)



