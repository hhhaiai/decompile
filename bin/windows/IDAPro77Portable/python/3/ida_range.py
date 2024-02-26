"""
Contains the definition of range_t.

A range is a non-empty continuous range of addresses (specified by its start and
end addresses, the end address is excluded from the range).

Ranges are stored in the Btree part of the IDA database. To learn more about
Btrees (Balanced Trees): \link{http://www.bluerwhite.org/btree/}"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_range
else:
    import _ida_range

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

SWIG_PYTHON_LEGACY_BOOL = _ida_range.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class rangevec_base_t(object):
    r"""
    Proxy of C++ qvector< range_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangevec_base_t
        __init__(self, x) -> rangevec_base_t

        @param x: qvector< range_t > const &
        """
        _ida_range.rangevec_base_t_swiginit(self, _ida_range.new_rangevec_base_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_base_t

    def push_back(self, *args) -> "range_t &":
        r"""
        push_back(self, x)

        @param x: range_t const &

        push_back(self) -> range_t
        """
        return _ida_range.rangevec_base_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_range.rangevec_base_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_range.rangevec_base_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_range.rangevec_base_t_empty(self, *args)

    def at(self, *args) -> "range_t const &":
        r"""
        at(self, _idx) -> range_t

        @param _idx: size_t
        """
        return _ida_range.rangevec_base_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_range.rangevec_base_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_range.rangevec_base_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: range_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_range.rangevec_base_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=range_t())

        @param x: range_t const &
        """
        return _ida_range.rangevec_base_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_range.rangevec_base_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_range.rangevec_base_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_range.rangevec_base_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< range_t > &
        """
        return _ida_range.rangevec_base_t_swap(self, *args)

    def extract(self, *args) -> "range_t *":
        r"""
        extract(self) -> range_t
        """
        return _ida_range.rangevec_base_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: range_t *
        @param len: size_t
        """
        return _ida_range.rangevec_base_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< range_t > const &
        """
        return _ida_range.rangevec_base_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< range_t > const &
        """
        return _ida_range.rangevec_base_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< range_t >::const_iterator":
        r"""
        begin(self) -> range_t
        """
        return _ida_range.rangevec_base_t_begin(self, *args)

    def end(self, *args) -> "qvector< range_t >::const_iterator":
        r"""
        end(self) -> range_t
        """
        return _ida_range.rangevec_base_t_end(self, *args)

    def insert(self, *args) -> "qvector< range_t >::iterator":
        r"""
        insert(self, it, x) -> range_t

        @param it: qvector< range_t >::iterator
        @param x: range_t const &
        """
        return _ida_range.rangevec_base_t_insert(self, *args)

    def erase(self, *args) -> "qvector< range_t >::iterator":
        r"""
        erase(self, it) -> range_t

        @param it: qvector< range_t >::iterator

        erase(self, first, last) -> range_t

        @param first: qvector< range_t >::iterator
        @param last: qvector< range_t >::iterator
        """
        return _ida_range.rangevec_base_t_erase(self, *args)

    def find(self, *args) -> "qvector< range_t >::const_iterator":
        r"""
        find(self, x) -> range_t

        @param x: range_t const &

        """
        return _ida_range.rangevec_base_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: range_t const &
        """
        return _ida_range.rangevec_base_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: range_t const &
        """
        return _ida_range.rangevec_base_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: range_t const &

        """
        return _ida_range.rangevec_base_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_range.rangevec_base_t___len__(self, *args)

    def __getitem__(self, *args) -> "range_t const &":
        r"""
        __getitem__(self, i) -> range_t

        @param i: size_t
        """
        return _ida_range.rangevec_base_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: range_t const &
        """
        return _ida_range.rangevec_base_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register rangevec_base_t in _ida_range:
_ida_range.rangevec_base_t_swigregister(rangevec_base_t)

class array_of_rangesets(object):
    r"""
    Proxy of C++ qvector< rangeset_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> array_of_rangesets
        __init__(self, x) -> array_of_rangesets

        @param x: qvector< rangeset_t > const &
        """
        _ida_range.array_of_rangesets_swiginit(self, _ida_range.new_array_of_rangesets(*args))
    __swig_destroy__ = _ida_range.delete_array_of_rangesets

    def push_back(self, *args) -> "rangeset_t &":
        r"""
        push_back(self, x)

        @param x: rangeset_t const &

        push_back(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_range.array_of_rangesets_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_range.array_of_rangesets_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_range.array_of_rangesets_empty(self, *args)

    def at(self, *args) -> "rangeset_t const &":
        r"""
        at(self, _idx) -> rangeset_t

        @param _idx: size_t
        """
        return _ida_range.array_of_rangesets_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_range.array_of_rangesets_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_range.array_of_rangesets_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: rangeset_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_range.array_of_rangesets_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=rangeset_t())

        @param x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_range.array_of_rangesets_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_range.array_of_rangesets_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_range.array_of_rangesets_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< rangeset_t > &
        """
        return _ida_range.array_of_rangesets_swap(self, *args)

    def extract(self, *args) -> "rangeset_t *":
        r"""
        extract(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: rangeset_t *
        @param len: size_t
        """
        return _ida_range.array_of_rangesets_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< rangeset_t > const &
        """
        return _ida_range.array_of_rangesets___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< rangeset_t > const &
        """
        return _ida_range.array_of_rangesets___ne__(self, *args)

    def begin(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""
        begin(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_begin(self, *args)

    def end(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""
        end(self) -> rangeset_t
        """
        return _ida_range.array_of_rangesets_end(self, *args)

    def insert(self, *args) -> "qvector< rangeset_t >::iterator":
        r"""
        insert(self, it, x) -> rangeset_t

        @param it: qvector< rangeset_t >::iterator
        @param x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_insert(self, *args)

    def erase(self, *args) -> "qvector< rangeset_t >::iterator":
        r"""
        erase(self, it) -> rangeset_t

        @param it: qvector< rangeset_t >::iterator

        erase(self, first, last) -> rangeset_t

        @param first: qvector< rangeset_t >::iterator
        @param last: qvector< rangeset_t >::iterator
        """
        return _ida_range.array_of_rangesets_erase(self, *args)

    def find(self, *args) -> "qvector< rangeset_t >::const_iterator":
        r"""
        find(self, x) -> rangeset_t

        @param x: rangeset_t const &

        """
        return _ida_range.array_of_rangesets_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: rangeset_t const &
        """
        return _ida_range.array_of_rangesets_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: rangeset_t const &

        """
        return _ida_range.array_of_rangesets__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_range.array_of_rangesets___len__(self, *args)

    def __getitem__(self, *args) -> "rangeset_t const &":
        r"""
        __getitem__(self, i) -> rangeset_t

        @param i: size_t
        """
        return _ida_range.array_of_rangesets___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: rangeset_t const &
        """
        return _ida_range.array_of_rangesets___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register array_of_rangesets in _ida_range:
_ida_range.array_of_rangesets_swigregister(array_of_rangesets)


#<pycode(py_range)>
import ida_idaapi
#</pycode(py_range)>

class range_t(object):
    r"""
    Proxy of C++ range_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    start_ea = property(_ida_range.range_t_start_ea_get, _ida_range.range_t_start_ea_set, doc=r"""start_ea""")
    r"""
    start_ea included
    """
    end_ea = property(_ida_range.range_t_end_ea_get, _ida_range.range_t_end_ea_set, doc=r"""end_ea""")
    r"""
    end_ea excluded
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> range_t
        __init__(self, ea1, ea2) -> range_t

        @param ea1: ea_t
        @param ea2: ea_t
        """
        _ida_range.range_t_swiginit(self, _ida_range.new_range_t(*args))

    def compare(self, *args) -> "int":
        r"""
        compare(self, r) -> int
        Compare two range_t instances, based on the start_ea.

        @param r: (C++: const range_t &) range_t const &
        """
        return _ida_range.range_t_compare(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: range_t const &
        """
        return _ida_range.range_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: range_t const &
        """
        return _ida_range.range_t___ne__(self, *args)

    def __gt__(self, *args) -> "bool":
        r"""
        __gt__(self, r) -> bool

        @param r: range_t const &
        """
        return _ida_range.range_t___gt__(self, *args)

    def __lt__(self, *args) -> "bool":
        r"""
        __lt__(self, r) -> bool

        @param r: range_t const &
        """
        return _ida_range.range_t___lt__(self, *args)

    def contains(self, *args) -> "bool":
        r"""
        contains(self, ea) -> bool
        Is every ea in 'r' also in this range_t?

        @param ea: ea_t

        contains(self, r) -> bool

        @param r: range_t const &
        """
        return _ida_range.range_t_contains(self, *args)

    def overlaps(self, *args) -> "bool":
        r"""
        overlaps(self, r) -> bool
        Is there an ea in 'r' that is also in this range_t?

        @param r: (C++: const range_t &) range_t const &
        """
        return _ida_range.range_t_overlaps(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        Set start_ea, end_ea to 0.
        """
        return _ida_range.range_t_clear(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        Is the size of the range_t <= 0?
        """
        return _ida_range.range_t_empty(self, *args)

    def size(self, *args) -> "asize_t":
        r"""
        size(self) -> asize_t
        Get end_ea - start_ea.
        """
        return _ida_range.range_t_size(self, *args)

    def intersect(self, *args) -> "void":
        r"""
        intersect(self, r)
        Assign the range_t to the intersection between the range_t and 'r'.

        @param r: (C++: const range_t &) range_t const &
        """
        return _ida_range.range_t_intersect(self, *args)

    def extend(self, *args) -> "void":
        r"""
        extend(self, ea)
        Ensure that the range_t includes 'ea'.

        @param ea: (C++: ea_t)
        """
        return _ida_range.range_t_extend(self, *args)

    def _print(self, *args) -> "size_t":
        r"""_print(self) -> size_t"""
        return _ida_range.range_t__print(self, *args)

    startEA = ida_idaapi._make_badattr_property("startEA", "start_ea")
    endEA = ida_idaapi._make_badattr_property("endEA", "end_ea")

    __swig_destroy__ = _ida_range.delete_range_t

# Register range_t in _ida_range:
_ida_range.range_t_swigregister(range_t)

def range_t_print(*args) -> "size_t":
    r"""
    range_t_print(cb) -> str
    Helper function. Should not be called directly!

    @param cb: range_t const *
    """
    return _ida_range.range_t_print(*args)

class rangevec_t(rangevec_base_t):
    r"""
    Proxy of C++ rangevec_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangevec_t
        """
        _ida_range.rangevec_t_swiginit(self, _ida_range.new_rangevec_t(*args))
    __swig_destroy__ = _ida_range.delete_rangevec_t

# Register rangevec_t in _ida_range:
_ida_range.rangevec_t_swigregister(rangevec_t)

RANGE_KIND_UNKNOWN = _ida_range.RANGE_KIND_UNKNOWN

RANGE_KIND_FUNC = _ida_range.RANGE_KIND_FUNC
r"""
func_t
"""

RANGE_KIND_SEGMENT = _ida_range.RANGE_KIND_SEGMENT
r"""
segment_t
"""

RANGE_KIND_HIDDEN_RANGE = _ida_range.RANGE_KIND_HIDDEN_RANGE
r"""
hidden_range_t
"""

class rangeset_t(object):
    r"""
    Proxy of C++ rangeset_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> rangeset_t
        __init__(self, range) -> rangeset_t

        @param range: range_t const &

        __init__(self, ivs) -> rangeset_t

        @param ivs: rangeset_t const &
        """
        _ida_range.rangeset_t_swiginit(self, _ida_range.new_rangeset_t(*args))

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)
        Set this = 'r' and 'r' = this. See qvector::swap()

        @param r: (C++: rangeset_t &)
        """
        return _ida_range.rangeset_t_swap(self, *args)

    def add(self, *args) -> "bool":
        r"""
        add(self, range) -> bool
        Add each element of 'aset' to the set.

        @param range: range_t const &

        @return: false if no elements were added (the set was unchanged)
        add(self, start, _end) -> bool

        @param start: ea_t
        @param _end: ea_t

        add(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_add(self, *args)

    def sub(self, *args) -> "bool":
        r"""
        sub(self, range) -> bool
        Subtract each range in 'aset' from the set

        @param range: range_t const &

        @return: false if nothing was subtracted (the set was unchanged)
        sub(self, ea) -> bool

        @param ea: ea_t

        sub(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_sub(self, *args)

    def includes(self, *args) -> "bool":
        r"""
        includes(self, range) -> bool
        Is every ea in 'range' contained in the rangeset?

        @param range: (C++: const range_t &) range_t const &
        """
        return _ida_range.rangeset_t_includes(self, *args)

    def _print(self, *args) -> "size_t":
        r"""_print(self) -> size_t"""
        return _ida_range.rangeset_t__print(self, *args)

    def getrange(self, *args) -> "range_t const &":
        r"""
        getrange(self, idx) -> range_t
        Get the range_t at index 'idx'.

        @param idx: (C++: int)
        """
        return _ida_range.rangeset_t_getrange(self, *args)

    def lastrange(self, *args) -> "range_t const &":
        r"""
        lastrange(self) -> range_t
        Get the last range_t in the set.
        """
        return _ida_range.rangeset_t_lastrange(self, *args)

    def nranges(self, *args) -> "size_t":
        r"""
        nranges(self) -> size_t
        Get the number of range_t elements in the set.
        """
        return _ida_range.rangeset_t_nranges(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        Does the set have zero elements.
        """
        return _ida_range.rangeset_t_empty(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        Delete all elements from the set. See qvector::clear()
        """
        return _ida_range.rangeset_t_clear(self, *args)

    def has_common(self, *args) -> "bool":
        r"""
        has_common(self, range) -> bool
        Does any element of 'aset' overlap with an element in this rangeset?. See
        range_t::overlaps()

        @param range: range_t const &

        has_common(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_has_common(self, *args)

    def contains(self, *args) -> "bool":
        r"""
        contains(self, ea) -> bool
        Is every element in 'aset' contained in an element of this rangeset?. See
        range_t::contains(range_t)

        @param ea: ea_t

        contains(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t_contains(self, *args)

    def intersect(self, *args) -> "bool":
        r"""
        intersect(self, aset) -> bool
        Set the rangeset to its intersection with 'aset'.

        @param aset: (C++: const rangeset_t &) rangeset_t const &
        @return: false if the set was unchanged
        """
        return _ida_range.rangeset_t_intersect(self, *args)

    def is_subset_of(self, *args) -> "bool":
        r"""
        is_subset_of(self, aset) -> bool
        Is every element in the rangeset contained in an element of 'aset'?

        @param aset: (C++: const rangeset_t &) rangeset_t const &
        """
        return _ida_range.rangeset_t_is_subset_of(self, *args)

    def is_equal(self, *args) -> "bool":
        r"""
        is_equal(self, aset) -> bool
        Do this rangeset and 'aset' have identical elements?

        @param aset: (C++: const rangeset_t &) rangeset_t const &
        """
        return _ida_range.rangeset_t_is_equal(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, aset) -> bool

        @param aset: rangeset_t const &
        """
        return _ida_range.rangeset_t___ne__(self, *args)

    def begin(self, *args) -> "rangeset_t::iterator":
        r"""
        begin(self) -> range_t
        Get an iterator that points to the first element in the set.
        """
        return _ida_range.rangeset_t_begin(self, *args)

    def end(self, *args) -> "rangeset_t::iterator":
        r"""
        end(self) -> range_t
        Get an iterator that points to the end of the set. (This is NOT the last
        element)
        """
        return _ida_range.rangeset_t_end(self, *args)

    def find_range(self, *args) -> "range_t const *":
        r"""
        find_range(self, ea) -> range_t
        Get the element from the set that contains 'ea'.

        @param ea: (C++: ea_t)
        @return: nullptr if there is no such element
        """
        return _ida_range.rangeset_t_find_range(self, *args)

    def cached_range(self, *args) -> "range_t const *":
        r"""
        cached_range(self) -> range_t
        When searching the rangeset, we keep a cached element to help speed up searches.

        @return: a pointer to the cached element
        """
        return _ida_range.rangeset_t_cached_range(self, *args)

    def next_addr(self, *args) -> "ea_t":
        r"""
        next_addr(self, ea) -> ea_t
        Get the smallest ea_t value greater than 'ea' contained in the rangeset.

        @param ea: (C++: ea_t)
        """
        return _ida_range.rangeset_t_next_addr(self, *args)

    def prev_addr(self, *args) -> "ea_t":
        r"""
        prev_addr(self, ea) -> ea_t
        Get the largest ea_t value less than 'ea' contained in the rangeset.

        @param ea: (C++: ea_t)
        """
        return _ida_range.rangeset_t_prev_addr(self, *args)

    def next_range(self, *args) -> "ea_t":
        r"""
        next_range(self, ea) -> ea_t
        Get the smallest ea_t value greater than 'ea' that is not in the same range as
        'ea'.

        @param ea: (C++: ea_t)
        """
        return _ida_range.rangeset_t_next_range(self, *args)

    def prev_range(self, *args) -> "ea_t":
        r"""
        prev_range(self, ea) -> ea_t
        Get the largest ea_t value less than 'ea' that is not in the same range as 'ea'.

        @param ea: (C++: ea_t)
        """
        return _ida_range.rangeset_t_prev_range(self, *args)

    def __getitem__(self, idx):
        return self.getrange(idx)

    __len__ = nranges
    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_range.delete_rangeset_t

# Register rangeset_t in _ida_range:
_ida_range.rangeset_t_swigregister(rangeset_t)




