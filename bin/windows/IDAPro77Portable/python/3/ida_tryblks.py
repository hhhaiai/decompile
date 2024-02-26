"""
Architecture independent exception handling info.

Try blocks have the following general properties:
* A try block specifies a possibly fragmented guarded code region.
* Each try block has always at least one catch/except block description
* Each catch block contains its boundaries and a filter.
* Additionally a catch block can hold sp adjustment and the offset to the
exception object offset (C++).
* Try blocks can be nested. Nesting is automatically calculated at the retrieval
time.
* There may be (nested) multiple try blocks starting at the same address.

See examples in tests/input/src/eh_tests."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_tryblks
else:
    import _ida_tryblks

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

SWIG_PYTHON_LEGACY_BOOL = _ida_tryblks.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
class tryblks_t(object):
    r"""
    Proxy of C++ qvector< tryblk_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> tryblks_t
        __init__(self, x) -> tryblks_t

        @param x: qvector< tryblk_t > const &
        """
        _ida_tryblks.tryblks_t_swiginit(self, _ida_tryblks.new_tryblks_t(*args))
    __swig_destroy__ = _ida_tryblks.delete_tryblks_t

    def push_back(self, *args) -> "tryblk_t &":
        r"""
        push_back(self, x)

        @param x: tryblk_t const &

        push_back(self) -> tryblk_t
        """
        return _ida_tryblks.tryblks_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_tryblks.tryblks_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_tryblks.tryblks_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_tryblks.tryblks_t_empty(self, *args)

    def at(self, *args) -> "tryblk_t const &":
        r"""
        at(self, _idx) -> tryblk_t

        @param _idx: size_t
        """
        return _ida_tryblks.tryblks_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_tryblks.tryblks_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_tryblks.tryblks_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: tryblk_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_tryblks.tryblks_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=tryblk_t())

        @param x: tryblk_t const &
        """
        return _ida_tryblks.tryblks_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_tryblks.tryblks_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_tryblks.tryblks_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_tryblks.tryblks_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< tryblk_t > &
        """
        return _ida_tryblks.tryblks_t_swap(self, *args)

    def extract(self, *args) -> "tryblk_t *":
        r"""
        extract(self) -> tryblk_t
        """
        return _ida_tryblks.tryblks_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: tryblk_t *
        @param len: size_t
        """
        return _ida_tryblks.tryblks_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< tryblk_t > const &
        """
        return _ida_tryblks.tryblks_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< tryblk_t > const &
        """
        return _ida_tryblks.tryblks_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< tryblk_t >::const_iterator":
        r"""
        begin(self) -> tryblk_t
        """
        return _ida_tryblks.tryblks_t_begin(self, *args)

    def end(self, *args) -> "qvector< tryblk_t >::const_iterator":
        r"""
        end(self) -> tryblk_t
        """
        return _ida_tryblks.tryblks_t_end(self, *args)

    def insert(self, *args) -> "qvector< tryblk_t >::iterator":
        r"""
        insert(self, it, x) -> tryblk_t

        @param it: qvector< tryblk_t >::iterator
        @param x: tryblk_t const &
        """
        return _ida_tryblks.tryblks_t_insert(self, *args)

    def erase(self, *args) -> "qvector< tryblk_t >::iterator":
        r"""
        erase(self, it) -> tryblk_t

        @param it: qvector< tryblk_t >::iterator

        erase(self, first, last) -> tryblk_t

        @param first: qvector< tryblk_t >::iterator
        @param last: qvector< tryblk_t >::iterator
        """
        return _ida_tryblks.tryblks_t_erase(self, *args)

    def find(self, *args) -> "qvector< tryblk_t >::const_iterator":
        r"""
        find(self, x) -> tryblk_t

        @param x: tryblk_t const &

        """
        return _ida_tryblks.tryblks_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: tryblk_t const &
        """
        return _ida_tryblks.tryblks_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: tryblk_t const &
        """
        return _ida_tryblks.tryblks_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: tryblk_t const &

        """
        return _ida_tryblks.tryblks_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_tryblks.tryblks_t___len__(self, *args)

    def __getitem__(self, *args) -> "tryblk_t const &":
        r"""
        __getitem__(self, i) -> tryblk_t

        @param i: size_t
        """
        return _ida_tryblks.tryblks_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: tryblk_t const &
        """
        return _ida_tryblks.tryblks_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register tryblks_t in _ida_tryblks:
_ida_tryblks.tryblks_t_swigregister(tryblks_t)

class catchvec_t(object):
    r"""
    Proxy of C++ qvector< catch_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> catchvec_t
        __init__(self, x) -> catchvec_t

        @param x: qvector< catch_t > const &
        """
        _ida_tryblks.catchvec_t_swiginit(self, _ida_tryblks.new_catchvec_t(*args))
    __swig_destroy__ = _ida_tryblks.delete_catchvec_t

    def push_back(self, *args) -> "catch_t &":
        r"""
        push_back(self, x)

        @param x: catch_t const &

        push_back(self) -> catch_t
        """
        return _ida_tryblks.catchvec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_tryblks.catchvec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_tryblks.catchvec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_tryblks.catchvec_t_empty(self, *args)

    def at(self, *args) -> "catch_t const &":
        r"""
        at(self, _idx) -> catch_t

        @param _idx: size_t
        """
        return _ida_tryblks.catchvec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_tryblks.catchvec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_tryblks.catchvec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: catch_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_tryblks.catchvec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=catch_t())

        @param x: catch_t const &
        """
        return _ida_tryblks.catchvec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_tryblks.catchvec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_tryblks.catchvec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_tryblks.catchvec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< catch_t > &
        """
        return _ida_tryblks.catchvec_t_swap(self, *args)

    def extract(self, *args) -> "catch_t *":
        r"""
        extract(self) -> catch_t
        """
        return _ida_tryblks.catchvec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: catch_t *
        @param len: size_t
        """
        return _ida_tryblks.catchvec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< catch_t > const &
        """
        return _ida_tryblks.catchvec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< catch_t > const &
        """
        return _ida_tryblks.catchvec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< catch_t >::const_iterator":
        r"""
        begin(self) -> catch_t
        """
        return _ida_tryblks.catchvec_t_begin(self, *args)

    def end(self, *args) -> "qvector< catch_t >::const_iterator":
        r"""
        end(self) -> catch_t
        """
        return _ida_tryblks.catchvec_t_end(self, *args)

    def insert(self, *args) -> "qvector< catch_t >::iterator":
        r"""
        insert(self, it, x) -> catch_t

        @param it: qvector< catch_t >::iterator
        @param x: catch_t const &
        """
        return _ida_tryblks.catchvec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< catch_t >::iterator":
        r"""
        erase(self, it) -> catch_t

        @param it: qvector< catch_t >::iterator

        erase(self, first, last) -> catch_t

        @param first: qvector< catch_t >::iterator
        @param last: qvector< catch_t >::iterator
        """
        return _ida_tryblks.catchvec_t_erase(self, *args)

    def find(self, *args) -> "qvector< catch_t >::const_iterator":
        r"""
        find(self, x) -> catch_t

        @param x: catch_t const &

        """
        return _ida_tryblks.catchvec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: catch_t const &
        """
        return _ida_tryblks.catchvec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: catch_t const &
        """
        return _ida_tryblks.catchvec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: catch_t const &

        """
        return _ida_tryblks.catchvec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_tryblks.catchvec_t___len__(self, *args)

    def __getitem__(self, *args) -> "catch_t const &":
        r"""
        __getitem__(self, i) -> catch_t

        @param i: size_t
        """
        return _ida_tryblks.catchvec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: catch_t const &
        """
        return _ida_tryblks.catchvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register catchvec_t in _ida_tryblks:
_ida_tryblks.catchvec_t_swigregister(catchvec_t)

class try_handler_t(ida_range.rangevec_t):
    r"""
    Proxy of C++ try_handler_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    disp = property(_ida_tryblks.try_handler_t_disp_get, _ida_tryblks.try_handler_t_disp_set, doc=r"""disp""")
    fpreg = property(_ida_tryblks.try_handler_t_fpreg_get, _ida_tryblks.try_handler_t_fpreg_set, doc=r"""fpreg""")

    def __init__(self, *args):
        r"""
        __init__(self) -> try_handler_t
        """
        _ida_tryblks.try_handler_t_swiginit(self, _ida_tryblks.new_try_handler_t(*args))

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_tryblks.try_handler_t_clear(self, *args)
    __swig_destroy__ = _ida_tryblks.delete_try_handler_t

# Register try_handler_t in _ida_tryblks:
_ida_tryblks.try_handler_t_swigregister(try_handler_t)

class seh_t(try_handler_t):
    r"""
    Proxy of C++ seh_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    filter = property(_ida_tryblks.seh_t_filter_get, _ida_tryblks.seh_t_filter_set, doc=r"""filter""")
    seh_code = property(_ida_tryblks.seh_t_seh_code_get, _ida_tryblks.seh_t_seh_code_set, doc=r"""seh_code""")

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_tryblks.seh_t_clear(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> seh_t
        """
        _ida_tryblks.seh_t_swiginit(self, _ida_tryblks.new_seh_t(*args))
    __swig_destroy__ = _ida_tryblks.delete_seh_t

# Register seh_t in _ida_tryblks:
_ida_tryblks.seh_t_swigregister(seh_t)

class catch_t(try_handler_t):
    r"""
    Proxy of C++ catch_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    obj = property(_ida_tryblks.catch_t_obj_get, _ida_tryblks.catch_t_obj_set, doc=r"""obj""")
    type_id = property(_ida_tryblks.catch_t_type_id_get, _ida_tryblks.catch_t_type_id_set, doc=r"""type_id""")

    def __init__(self, *args):
        r"""
        __init__(self) -> catch_t
        """
        _ida_tryblks.catch_t_swiginit(self, _ida_tryblks.new_catch_t(*args))
    __swig_destroy__ = _ida_tryblks.delete_catch_t

# Register catch_t in _ida_tryblks:
_ida_tryblks.catch_t_swigregister(catch_t)

class tryblk_t(ida_range.rangevec_t):
    r"""
    Proxy of C++ tryblk_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    level = property(_ida_tryblks.tryblk_t_level_get, _ida_tryblks.tryblk_t_level_set, doc=r"""level""")

    def cpp(self, *args) -> "catchvec_t &":
        r"""
        cpp(self) -> catchvec_t
        """
        return _ida_tryblks.tryblk_t_cpp(self, *args)

    def seh(self, *args) -> "seh_t &":
        r"""
        seh(self) -> seh_t
        """
        return _ida_tryblks.tryblk_t_seh(self, *args)
    __swig_destroy__ = _ida_tryblks.delete_tryblk_t

    def __init__(self, *args):
        r"""
        __init__(self) -> tryblk_t
        __init__(self, r) -> tryblk_t

        @param r: tryblk_t const &
        """
        _ida_tryblks.tryblk_t_swiginit(self, _ida_tryblks.new_tryblk_t(*args))

    def get_kind(self, *args) -> "uchar":
        r"""
        get_kind(self) -> uchar
        """
        return _ida_tryblks.tryblk_t_get_kind(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_tryblks.tryblk_t_empty(self, *args)

    def is_seh(self, *args) -> "bool":
        r"""
        is_seh(self) -> bool
        """
        return _ida_tryblks.tryblk_t_is_seh(self, *args)

    def is_cpp(self, *args) -> "bool":
        r"""
        is_cpp(self) -> bool
        """
        return _ida_tryblks.tryblk_t_is_cpp(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_tryblks.tryblk_t_clear(self, *args)

    def set_seh(self, *args) -> "seh_t &":
        r"""
        set_seh(self) -> seh_t
        """
        return _ida_tryblks.tryblk_t_set_seh(self, *args)

    def set_cpp(self, *args) -> "catchvec_t &":
        r"""
        set_cpp(self) -> catchvec_t
        """
        return _ida_tryblks.tryblk_t_set_cpp(self, *args)

# Register tryblk_t in _ida_tryblks:
_ida_tryblks.tryblk_t_swigregister(tryblk_t)


def get_tryblks(*args) -> "size_t":
    r"""
    get_tryblks(tbv, range) -> size_t
    Retrieve try block information from the specified address range. Try blocks are
    sorted by starting address and their nest levels calculated.

    @param tbv: (C++: tryblks_t *) output buffer; may be nullptr
    @param range: (C++: const range_t &) address range to change
    @return: number of found try blocks
    """
    return _ida_tryblks.get_tryblks(*args)

def del_tryblks(*args) -> "void":
    r"""
    del_tryblks(range)
    Delete try block information in the specified range.

    @param range: (C++: const range_t &) the range to be cleared
    """
    return _ida_tryblks.del_tryblks(*args)

def add_tryblk(*args) -> "int":
    r"""
    add_tryblk(tb) -> int
    Add one try block information.

    @param tb: (C++: const tryblk_t &) try block to add.
    @return: error code; 0 means good
    """
    return _ida_tryblks.add_tryblk(*args)
TBERR_OK = _ida_tryblks.TBERR_OK
r"""
ok
"""

TBERR_START = _ida_tryblks.TBERR_START
r"""
bad start address
"""

TBERR_END = _ida_tryblks.TBERR_END
r"""
bad end address
"""

TBERR_ORDER = _ida_tryblks.TBERR_ORDER
r"""
bad address order
"""

TBERR_EMPTY = _ida_tryblks.TBERR_EMPTY
r"""
empty try block
"""

TBERR_KIND = _ida_tryblks.TBERR_KIND
r"""
illegal try block kind
"""

TBERR_NO_CATCHES = _ida_tryblks.TBERR_NO_CATCHES
r"""
no catch blocks at all
"""

TBERR_INTERSECT = _ida_tryblks.TBERR_INTERSECT
r"""
range would intersect inner tryblk
"""


def find_syseh(*args) -> "ea_t":
    r"""
    find_syseh(ea) -> ea_t
    Find the start address of the system eh region including the argument.

    @param ea: (C++: ea_t) search address
    @return: start address of surrounding tryblk, otherwise BADADDR
    """
    return _ida_tryblks.find_syseh(*args)
TBEA_TRY = _ida_tryblks.TBEA_TRY

TBEA_CATCH = _ida_tryblks.TBEA_CATCH

TBEA_SEHTRY = _ida_tryblks.TBEA_SEHTRY

TBEA_SEHLPAD = _ida_tryblks.TBEA_SEHLPAD

TBEA_SEHFILT = _ida_tryblks.TBEA_SEHFILT

TBEA_ANY = _ida_tryblks.TBEA_ANY

TBEA_FALLTHRU = _ida_tryblks.TBEA_FALLTHRU


def is_ea_tryblks(*args) -> "bool":
    r"""
    is_ea_tryblks(ea, flags) -> bool
    Check if the given address ea is part of tryblks description.

    @param ea: (C++: ea_t) address to check
    @param flags: (C++: uint32) combination of flags for is_ea_tryblks()
    """
    return _ida_tryblks.is_ea_tryblks(*args)



