"""
Contains definition of the interface to IDD modules.

The interface consists of structures describing the target debugged processor
and a debugging API."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_idd
else:
    import _ida_idd

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

SWIG_PYTHON_LEGACY_BOOL = _ida_idd.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
class excvec_t(object):
    r"""
    Proxy of C++ qvector< exception_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> excvec_t
        __init__(self, x) -> excvec_t

        @param x: qvector< exception_info_t > const &
        """
        _ida_idd.excvec_t_swiginit(self, _ida_idd.new_excvec_t(*args))
    __swig_destroy__ = _ida_idd.delete_excvec_t

    def push_back(self, *args) -> "exception_info_t &":
        r"""
        push_back(self, x)

        @param x: exception_info_t const &

        push_back(self) -> exception_info_t
        """
        return _ida_idd.excvec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_idd.excvec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_idd.excvec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_idd.excvec_t_empty(self, *args)

    def at(self, *args) -> "exception_info_t const &":
        r"""
        at(self, _idx) -> exception_info_t

        @param _idx: size_t
        """
        return _ida_idd.excvec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_idd.excvec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_idd.excvec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: exception_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_idd.excvec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=exception_info_t())

        @param x: exception_info_t const &
        """
        return _ida_idd.excvec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_idd.excvec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_idd.excvec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_idd.excvec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< exception_info_t > &
        """
        return _ida_idd.excvec_t_swap(self, *args)

    def extract(self, *args) -> "exception_info_t *":
        r"""
        extract(self) -> exception_info_t
        """
        return _ida_idd.excvec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: exception_info_t *
        @param len: size_t
        """
        return _ida_idd.excvec_t_inject(self, *args)

    def begin(self, *args) -> "qvector< exception_info_t >::const_iterator":
        r"""
        begin(self) -> exception_info_t
        """
        return _ida_idd.excvec_t_begin(self, *args)

    def end(self, *args) -> "qvector< exception_info_t >::const_iterator":
        r"""
        end(self) -> exception_info_t
        """
        return _ida_idd.excvec_t_end(self, *args)

    def insert(self, *args) -> "qvector< exception_info_t >::iterator":
        r"""
        insert(self, it, x) -> exception_info_t

        @param it: qvector< exception_info_t >::iterator
        @param x: exception_info_t const &
        """
        return _ida_idd.excvec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< exception_info_t >::iterator":
        r"""
        erase(self, it) -> exception_info_t

        @param it: qvector< exception_info_t >::iterator

        erase(self, first, last) -> exception_info_t

        @param first: qvector< exception_info_t >::iterator
        @param last: qvector< exception_info_t >::iterator
        """
        return _ida_idd.excvec_t_erase(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_idd.excvec_t___len__(self, *args)

    def __getitem__(self, *args) -> "exception_info_t const &":
        r"""
        __getitem__(self, i) -> exception_info_t

        @param i: size_t
        """
        return _ida_idd.excvec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: exception_info_t const &
        """
        return _ida_idd.excvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register excvec_t in _ida_idd:
_ida_idd.excvec_t_swigregister(excvec_t)

class procinfo_vec_t(object):
    r"""
    Proxy of C++ qvector< process_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> procinfo_vec_t
        __init__(self, x) -> procinfo_vec_t

        @param x: qvector< process_info_t > const &
        """
        _ida_idd.procinfo_vec_t_swiginit(self, _ida_idd.new_procinfo_vec_t(*args))
    __swig_destroy__ = _ida_idd.delete_procinfo_vec_t

    def push_back(self, *args) -> "process_info_t &":
        r"""
        push_back(self, x)

        @param x: process_info_t const &

        push_back(self) -> process_info_t
        """
        return _ida_idd.procinfo_vec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_idd.procinfo_vec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_idd.procinfo_vec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_idd.procinfo_vec_t_empty(self, *args)

    def at(self, *args) -> "process_info_t const &":
        r"""
        at(self, _idx) -> process_info_t

        @param _idx: size_t
        """
        return _ida_idd.procinfo_vec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_idd.procinfo_vec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_idd.procinfo_vec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: process_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_idd.procinfo_vec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=process_info_t())

        @param x: process_info_t const &
        """
        return _ida_idd.procinfo_vec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_idd.procinfo_vec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_idd.procinfo_vec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_idd.procinfo_vec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< process_info_t > &
        """
        return _ida_idd.procinfo_vec_t_swap(self, *args)

    def extract(self, *args) -> "process_info_t *":
        r"""
        extract(self) -> process_info_t
        """
        return _ida_idd.procinfo_vec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: process_info_t *
        @param len: size_t
        """
        return _ida_idd.procinfo_vec_t_inject(self, *args)

    def begin(self, *args) -> "qvector< process_info_t >::const_iterator":
        r"""
        begin(self) -> process_info_t
        """
        return _ida_idd.procinfo_vec_t_begin(self, *args)

    def end(self, *args) -> "qvector< process_info_t >::const_iterator":
        r"""
        end(self) -> process_info_t
        """
        return _ida_idd.procinfo_vec_t_end(self, *args)

    def insert(self, *args) -> "qvector< process_info_t >::iterator":
        r"""
        insert(self, it, x) -> process_info_t

        @param it: qvector< process_info_t >::iterator
        @param x: process_info_t const &
        """
        return _ida_idd.procinfo_vec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< process_info_t >::iterator":
        r"""
        erase(self, it) -> process_info_t

        @param it: qvector< process_info_t >::iterator

        erase(self, first, last) -> process_info_t

        @param first: qvector< process_info_t >::iterator
        @param last: qvector< process_info_t >::iterator
        """
        return _ida_idd.procinfo_vec_t_erase(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_idd.procinfo_vec_t___len__(self, *args)

    def __getitem__(self, *args) -> "process_info_t const &":
        r"""
        __getitem__(self, i) -> process_info_t

        @param i: size_t
        """
        return _ida_idd.procinfo_vec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: process_info_t const &
        """
        return _ida_idd.procinfo_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register procinfo_vec_t in _ida_idd:
_ida_idd.procinfo_vec_t_swigregister(procinfo_vec_t)

class call_stack_info_vec_t(object):
    r"""
    Proxy of C++ qvector< call_stack_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> call_stack_info_vec_t
        __init__(self, x) -> call_stack_info_vec_t

        @param x: qvector< call_stack_info_t > const &
        """
        _ida_idd.call_stack_info_vec_t_swiginit(self, _ida_idd.new_call_stack_info_vec_t(*args))
    __swig_destroy__ = _ida_idd.delete_call_stack_info_vec_t

    def push_back(self, *args) -> "call_stack_info_t &":
        r"""
        push_back(self, x)

        @param x: call_stack_info_t const &

        push_back(self) -> call_stack_info_t
        """
        return _ida_idd.call_stack_info_vec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_idd.call_stack_info_vec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_idd.call_stack_info_vec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_idd.call_stack_info_vec_t_empty(self, *args)

    def at(self, *args) -> "call_stack_info_t const &":
        r"""
        at(self, _idx) -> call_stack_info_t

        @param _idx: size_t
        """
        return _ida_idd.call_stack_info_vec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_idd.call_stack_info_vec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_idd.call_stack_info_vec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: call_stack_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_idd.call_stack_info_vec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=call_stack_info_t())

        @param x: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_vec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_idd.call_stack_info_vec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_idd.call_stack_info_vec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_idd.call_stack_info_vec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< call_stack_info_t > &
        """
        return _ida_idd.call_stack_info_vec_t_swap(self, *args)

    def extract(self, *args) -> "call_stack_info_t *":
        r"""
        extract(self) -> call_stack_info_t
        """
        return _ida_idd.call_stack_info_vec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: call_stack_info_t *
        @param len: size_t
        """
        return _ida_idd.call_stack_info_vec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< call_stack_info_t > const &
        """
        return _ida_idd.call_stack_info_vec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< call_stack_info_t > const &
        """
        return _ida_idd.call_stack_info_vec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< call_stack_info_t >::const_iterator":
        r"""
        begin(self) -> call_stack_info_t
        """
        return _ida_idd.call_stack_info_vec_t_begin(self, *args)

    def end(self, *args) -> "qvector< call_stack_info_t >::const_iterator":
        r"""
        end(self) -> call_stack_info_t
        """
        return _ida_idd.call_stack_info_vec_t_end(self, *args)

    def insert(self, *args) -> "qvector< call_stack_info_t >::iterator":
        r"""
        insert(self, it, x) -> call_stack_info_t

        @param it: qvector< call_stack_info_t >::iterator
        @param x: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_vec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< call_stack_info_t >::iterator":
        r"""
        erase(self, it) -> call_stack_info_t

        @param it: qvector< call_stack_info_t >::iterator

        erase(self, first, last) -> call_stack_info_t

        @param first: qvector< call_stack_info_t >::iterator
        @param last: qvector< call_stack_info_t >::iterator
        """
        return _ida_idd.call_stack_info_vec_t_erase(self, *args)

    def find(self, *args) -> "qvector< call_stack_info_t >::const_iterator":
        r"""
        find(self, x) -> call_stack_info_t

        @param x: call_stack_info_t const &

        """
        return _ida_idd.call_stack_info_vec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_vec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_vec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: call_stack_info_t const &

        """
        return _ida_idd.call_stack_info_vec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_idd.call_stack_info_vec_t___len__(self, *args)

    def __getitem__(self, *args) -> "call_stack_info_t const &":
        r"""
        __getitem__(self, i) -> call_stack_info_t

        @param i: size_t
        """
        return _ida_idd.call_stack_info_vec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register call_stack_info_vec_t in _ida_idd:
_ida_idd.call_stack_info_vec_t_swigregister(call_stack_info_vec_t)

class meminfo_vec_t(object):
    r"""
    Proxy of C++ qvector< memory_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> meminfo_vec_t
        __init__(self, x) -> meminfo_vec_t

        @param x: qvector< memory_info_t > const &
        """
        _ida_idd.meminfo_vec_t_swiginit(self, _ida_idd.new_meminfo_vec_t(*args))
    __swig_destroy__ = _ida_idd.delete_meminfo_vec_t

    def push_back(self, *args) -> "memory_info_t &":
        r"""
        push_back(self, x)

        @param x: memory_info_t const &

        push_back(self) -> memory_info_t
        """
        return _ida_idd.meminfo_vec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_idd.meminfo_vec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_idd.meminfo_vec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_idd.meminfo_vec_t_empty(self, *args)

    def at(self, *args) -> "memory_info_t const &":
        r"""
        at(self, _idx) -> memory_info_t

        @param _idx: size_t
        """
        return _ida_idd.meminfo_vec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_idd.meminfo_vec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_idd.meminfo_vec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: memory_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_idd.meminfo_vec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=memory_info_t())

        @param x: memory_info_t const &
        """
        return _ida_idd.meminfo_vec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_idd.meminfo_vec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_idd.meminfo_vec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_idd.meminfo_vec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< memory_info_t > &
        """
        return _ida_idd.meminfo_vec_t_swap(self, *args)

    def extract(self, *args) -> "memory_info_t *":
        r"""
        extract(self) -> memory_info_t
        """
        return _ida_idd.meminfo_vec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: memory_info_t *
        @param len: size_t
        """
        return _ida_idd.meminfo_vec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< memory_info_t > const &
        """
        return _ida_idd.meminfo_vec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< memory_info_t > const &
        """
        return _ida_idd.meminfo_vec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< memory_info_t >::const_iterator":
        r"""
        begin(self) -> memory_info_t
        """
        return _ida_idd.meminfo_vec_t_begin(self, *args)

    def end(self, *args) -> "qvector< memory_info_t >::const_iterator":
        r"""
        end(self) -> memory_info_t
        """
        return _ida_idd.meminfo_vec_t_end(self, *args)

    def insert(self, *args) -> "qvector< memory_info_t >::iterator":
        r"""
        insert(self, it, x) -> memory_info_t

        @param it: qvector< memory_info_t >::iterator
        @param x: memory_info_t const &
        """
        return _ida_idd.meminfo_vec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< memory_info_t >::iterator":
        r"""
        erase(self, it) -> memory_info_t

        @param it: qvector< memory_info_t >::iterator

        erase(self, first, last) -> memory_info_t

        @param first: qvector< memory_info_t >::iterator
        @param last: qvector< memory_info_t >::iterator
        """
        return _ida_idd.meminfo_vec_t_erase(self, *args)

    def find(self, *args) -> "qvector< memory_info_t >::const_iterator":
        r"""
        find(self, x) -> memory_info_t

        @param x: memory_info_t const &

        """
        return _ida_idd.meminfo_vec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: memory_info_t const &
        """
        return _ida_idd.meminfo_vec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: memory_info_t const &
        """
        return _ida_idd.meminfo_vec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: memory_info_t const &

        """
        return _ida_idd.meminfo_vec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_idd.meminfo_vec_t___len__(self, *args)

    def __getitem__(self, *args) -> "memory_info_t const &":
        r"""
        __getitem__(self, i) -> memory_info_t

        @param i: size_t
        """
        return _ida_idd.meminfo_vec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: memory_info_t const &
        """
        return _ida_idd.meminfo_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register meminfo_vec_t in _ida_idd:
_ida_idd.meminfo_vec_t_swigregister(meminfo_vec_t)

IDD_INTERFACE_VERSION = _ida_idd.IDD_INTERFACE_VERSION
r"""
The IDD interface version number.
"""

NO_THREAD = _ida_idd.NO_THREAD
r"""
No thread. in PROCESS_STARTED this value can be used to specify that the main
thread has not been created. It will be initialized later by a THREAD_STARTED
event.
"""

class process_info_t(object):
    r"""
    Proxy of C++ process_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    pid = property(_ida_idd.process_info_t_pid_get, _ida_idd.process_info_t_pid_set, doc=r"""pid""")
    r"""
    process id
    """
    name = property(_ida_idd.process_info_t_name_get, _ida_idd.process_info_t_name_set, doc=r"""name""")
    r"""
    process name
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> process_info_t
        """
        _ida_idd.process_info_t_swiginit(self, _ida_idd.new_process_info_t(*args))
    __swig_destroy__ = _ida_idd.delete_process_info_t

# Register process_info_t in _ida_idd:
_ida_idd.process_info_t_swigregister(process_info_t)

class debapp_attrs_t(object):
    r"""
    Proxy of C++ debapp_attrs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    cbsize = property(_ida_idd.debapp_attrs_t_cbsize_get, _ida_idd.debapp_attrs_t_cbsize_set, doc=r"""cbsize""")
    r"""
    control field: size of this structure
    """
    addrsize = property(_ida_idd.debapp_attrs_t_addrsize_get, _ida_idd.debapp_attrs_t_addrsize_set, doc=r"""addrsize""")
    r"""
    address size of the process. Since 64-bit debuggers usually can debug 32-bit
    applications, we cannot rely on sizeof(ea_t) to detect the current address size.
    The following variable should be used instead. It is initialized with 8 for
    64-bit debuggers but they should adjust it as soon as they learn that a 32-bit
    application is being debugged. For 32-bit debuggers it is initialized with 4.
    """
    platform = property(_ida_idd.debapp_attrs_t_platform_get, _ida_idd.debapp_attrs_t_platform_set, doc=r"""platform""")
    r"""
    platform name process is running/debugging under. (is used as a key value in
    exceptions.cfg)
    """
    is_be = property(_ida_idd.debapp_attrs_t_is_be_get, _ida_idd.debapp_attrs_t_is_be_set, doc=r"""is_be""")

    def __init__(self, *args):
        r"""
        __init__(self) -> debapp_attrs_t
        """
        _ida_idd.debapp_attrs_t_swiginit(self, _ida_idd.new_debapp_attrs_t(*args))
    __swig_destroy__ = _ida_idd.delete_debapp_attrs_t

# Register debapp_attrs_t in _ida_idd:
_ida_idd.debapp_attrs_t_swigregister(debapp_attrs_t)
DEF_ADDRSIZE = _ida_idd.DEF_ADDRSIZE


class register_info_t(object):
    r"""
    Proxy of C++ register_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_idd.register_info_t_name_get, _ida_idd.register_info_t_name_set, doc=r"""name""")
    r"""
    Register name.
    """
    flags = property(_ida_idd.register_info_t_flags_get, _ida_idd.register_info_t_flags_set, doc=r"""flags""")
    r"""
    Register info attribute flags
    """
    register_class = property(_ida_idd.register_info_t_register_class_get, _ida_idd.register_info_t_register_class_set, doc=r"""register_class""")
    r"""
    segment, mmx, etc.
    """
    dtype = property(_ida_idd.register_info_t_dtype_get, _ida_idd.register_info_t_dtype_set, doc=r"""dtype""")
    r"""
    Register size (see Operand value types)
    """
    bit_strings = property(_ida_idd.register_info_t_bit_strings_get, _ida_idd.register_info_t_bit_strings_set, doc=r"""bit_strings""")
    r"""
    strings corresponding to each bit of the register. (nullptr = no bit, same name
    = multi-bits mask)
    """
    default_bit_strings_mask = property(_ida_idd.register_info_t_default_bit_strings_mask_get, _ida_idd.register_info_t_default_bit_strings_mask_set, doc=r"""default_bit_strings_mask""")
    r"""
    mask of default bits
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> register_info_t
        """
        _ida_idd.register_info_t_swiginit(self, _ida_idd.new_register_info_t(*args))
    __swig_destroy__ = _ida_idd.delete_register_info_t

# Register register_info_t in _ida_idd:
_ida_idd.register_info_t_swigregister(register_info_t)
REGISTER_READONLY = _ida_idd.REGISTER_READONLY
r"""
the user can't modify the current value of this register
"""

REGISTER_IP = _ida_idd.REGISTER_IP
r"""
instruction pointer
"""

REGISTER_SP = _ida_idd.REGISTER_SP
r"""
stack pointer
"""

REGISTER_FP = _ida_idd.REGISTER_FP
r"""
frame pointer
"""

REGISTER_ADDRESS = _ida_idd.REGISTER_ADDRESS
r"""
may contain an address
"""

REGISTER_CS = _ida_idd.REGISTER_CS
r"""
code segment
"""

REGISTER_SS = _ida_idd.REGISTER_SS
r"""
stack segment
"""

REGISTER_NOLF = _ida_idd.REGISTER_NOLF
r"""
displays this register without returning to the next line, allowing the next
register to be displayed to its right (on the same line)
"""

REGISTER_CUSTFMT = _ida_idd.REGISTER_CUSTFMT
r"""
register should be displayed using a custom data format. the format name is in
bit_strings[0]; the corresponding regval_t will use bytevec_t
"""


class memory_info_t(ida_range.range_t):
    r"""
    Proxy of C++ memory_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_idd.memory_info_t_name_get, _ida_idd.memory_info_t_name_set, doc=r"""name""")
    r"""
    Memory range name.
    """
    sclass = property(_ida_idd.memory_info_t_sclass_get, _ida_idd.memory_info_t_sclass_set, doc=r"""sclass""")
    r"""
    Memory range class name.
    """
    sbase = property(_ida_idd.memory_info_t_sbase_get, _ida_idd.memory_info_t_sbase_set, doc=r"""sbase""")
    r"""
    Segment base (meaningful only for segmented architectures, e.g. 16-bit x86) The
    base is specified in paragraphs (i.e. shifted to the right by 4)
    """
    bitness = property(_ida_idd.memory_info_t_bitness_get, _ida_idd.memory_info_t_bitness_set, doc=r"""bitness""")
    r"""
    Number of bits in segment addresses (0-16bit, 1-32bit, 2-64bit)
    """
    perm = property(_ida_idd.memory_info_t_perm_get, _ida_idd.memory_info_t_perm_set, doc=r"""perm""")
    r"""
    Memory range permissions (0-no information): see segment.hpp.
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> memory_info_t
        """
        _ida_idd.memory_info_t_swiginit(self, _ida_idd.new_memory_info_t(*args))

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: memory_info_t const &
        """
        return _ida_idd.memory_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: memory_info_t const &
        """
        return _ida_idd.memory_info_t___ne__(self, *args)
    __swig_destroy__ = _ida_idd.delete_memory_info_t

# Register memory_info_t in _ida_idd:
_ida_idd.memory_info_t_swigregister(memory_info_t)

class scattered_segm_t(ida_range.range_t):
    r"""
    Proxy of C++ scattered_segm_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_idd.scattered_segm_t_name_get, _ida_idd.scattered_segm_t_name_set, doc=r"""name""")
    r"""
    name of the segment
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> scattered_segm_t
        """
        _ida_idd.scattered_segm_t_swiginit(self, _ida_idd.new_scattered_segm_t(*args))
    __swig_destroy__ = _ida_idd.delete_scattered_segm_t

# Register scattered_segm_t in _ida_idd:
_ida_idd.scattered_segm_t_swigregister(scattered_segm_t)

NO_EVENT = _ida_idd.NO_EVENT
r"""
Not an interesting event. This event can be used if the debugger module needs to
return an event but there are no valid events.
"""

PROCESS_STARTED = _ida_idd.PROCESS_STARTED
r"""
New process has been started.
"""

PROCESS_EXITED = _ida_idd.PROCESS_EXITED
r"""
Process has been stopped.
"""

THREAD_STARTED = _ida_idd.THREAD_STARTED
r"""
New thread has been started.
"""

THREAD_EXITED = _ida_idd.THREAD_EXITED
r"""
Thread has been stopped.
"""

BREAKPOINT = _ida_idd.BREAKPOINT
r"""
Breakpoint has been reached. IDA will complain about unknown breakpoints, they
should be reported as exceptions.
"""

STEP = _ida_idd.STEP
r"""
One instruction has been executed. Spurious events of this kind are silently
ignored by IDA.
"""

EXCEPTION = _ida_idd.EXCEPTION
r"""
Exception.
"""

LIB_LOADED = _ida_idd.LIB_LOADED
r"""
New library has been loaded.
"""

LIB_UNLOADED = _ida_idd.LIB_UNLOADED
r"""
Library has been unloaded.
"""

INFORMATION = _ida_idd.INFORMATION
r"""
User-defined information. This event can be used to return empty information
This will cause IDA to call get_debug_event() immediately once more.
"""

PROCESS_ATTACHED = _ida_idd.PROCESS_ATTACHED
r"""
Successfully attached to running process.
"""

PROCESS_DETACHED = _ida_idd.PROCESS_DETACHED
r"""
Successfully detached from process.
"""

PROCESS_SUSPENDED = _ida_idd.PROCESS_SUSPENDED
r"""
Process has been suspended. This event can be used by the debugger module to
signal if the process spontaneously gets suspended (not because of an exception,
breakpoint, or single step). IDA will silently switch to the 'suspended process'
mode without displaying any messages.
"""

TRACE_FULL = _ida_idd.TRACE_FULL
r"""
The trace buffer of the tracer module is full and IDA needs to read it before
continuing
"""


def set_debug_event_code(*args) -> "void":
    r"""
    set_debug_event_code(ev, id)

    @param ev: debug_event_t *
    @param id: enum event_id_t
    """
    return _ida_idd.set_debug_event_code(*args)
class modinfo_t(object):
    r"""
    Proxy of C++ modinfo_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_idd.modinfo_t_name_get, _ida_idd.modinfo_t_name_set, doc=r"""name""")
    r"""
    full name of the module
    """
    base = property(_ida_idd.modinfo_t_base_get, _ida_idd.modinfo_t_base_set, doc=r"""base""")
    r"""
    module base address. if unknown pass BADADDR
    """
    size = property(_ida_idd.modinfo_t_size_get, _ida_idd.modinfo_t_size_set, doc=r"""size""")
    r"""
    module size. if unknown pass 0
    """
    rebase_to = property(_ida_idd.modinfo_t_rebase_to_get, _ida_idd.modinfo_t_rebase_to_set, doc=r"""rebase_to""")
    r"""
    if not BADADDR, then rebase the program to the specified address
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> modinfo_t
        """
        _ida_idd.modinfo_t_swiginit(self, _ida_idd.new_modinfo_t(*args))
    __swig_destroy__ = _ida_idd.delete_modinfo_t

# Register modinfo_t in _ida_idd:
_ida_idd.modinfo_t_swigregister(modinfo_t)

class bptaddr_t(object):
    r"""
    Proxy of C++ bptaddr_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    hea = property(_ida_idd.bptaddr_t_hea_get, _ida_idd.bptaddr_t_hea_set, doc=r"""hea""")
    r"""
    Possible address referenced by hardware breakpoints.
    """
    kea = property(_ida_idd.bptaddr_t_kea_get, _ida_idd.bptaddr_t_kea_set, doc=r"""kea""")
    r"""
    Address of the triggered bpt from the kernel's point of view. (for some systems
    with special memory mappings, the triggered ea might be different from event
    ea). Use to BADADDR for flat memory model.
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> bptaddr_t
        """
        _ida_idd.bptaddr_t_swiginit(self, _ida_idd.new_bptaddr_t(*args))
    __swig_destroy__ = _ida_idd.delete_bptaddr_t

# Register bptaddr_t in _ida_idd:
_ida_idd.bptaddr_t_swigregister(bptaddr_t)

class excinfo_t(object):
    r"""
    Proxy of C++ excinfo_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    code = property(_ida_idd.excinfo_t_code_get, _ida_idd.excinfo_t_code_set, doc=r"""code""")
    r"""
    Exception code.
    """
    can_cont = property(_ida_idd.excinfo_t_can_cont_get, _ida_idd.excinfo_t_can_cont_set, doc=r"""can_cont""")
    r"""
    Execution of the process can continue after this exception?
    """
    ea = property(_ida_idd.excinfo_t_ea_get, _ida_idd.excinfo_t_ea_set, doc=r"""ea""")
    r"""
    Possible address referenced by the exception.
    """
    info = property(_ida_idd.excinfo_t_info_get, _ida_idd.excinfo_t_info_set, doc=r"""info""")
    r"""
    Exception message.
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> excinfo_t
        """
        _ida_idd.excinfo_t_swiginit(self, _ida_idd.new_excinfo_t(*args))
    __swig_destroy__ = _ida_idd.delete_excinfo_t

# Register excinfo_t in _ida_idd:
_ida_idd.excinfo_t_swigregister(excinfo_t)

class debug_event_t(object):
    r"""
    Proxy of C++ debug_event_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    pid = property(_ida_idd.debug_event_t_pid_get, _ida_idd.debug_event_t_pid_set, doc=r"""pid""")
    r"""
    Process where the event occurred.
    """
    tid = property(_ida_idd.debug_event_t_tid_get, _ida_idd.debug_event_t_tid_set, doc=r"""tid""")
    r"""
    Thread where the event occurred.
    """
    ea = property(_ida_idd.debug_event_t_ea_get, _ida_idd.debug_event_t_ea_set, doc=r"""ea""")
    r"""
    Address where the event occurred.
    """
    handled = property(_ida_idd.debug_event_t_handled_get, _ida_idd.debug_event_t_handled_set, doc=r"""handled""")
    r"""
    Is event handled by the debugger?. (from the system's point of view) Meaningful
    for EXCEPTION events
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> debug_event_t
        __init__(self, r) -> debug_event_t

        @param r: debug_event_t const &
        """
        _ida_idd.debug_event_t_swiginit(self, _ida_idd.new_debug_event_t(*args))
    __swig_destroy__ = _ida_idd.delete_debug_event_t

    def copy(self, *args) -> "debug_event_t &":
        r"""
        copy(self, r) -> debug_event_t

        @param r: debug_event_t const &
        """
        return _ida_idd.debug_event_t_copy(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        clear the dependent information (see below), set event code to NO_EVENT
        """
        return _ida_idd.debug_event_t_clear(self, *args)

    def clear_all(self, *args) -> "void":
        r"""
        clear_all(self)
        """
        return _ida_idd.debug_event_t_clear_all(self, *args)

    def eid(self, *args) -> "event_id_t":
        r"""
        eid(self) -> event_id_t
        Event code.
        """
        return _ida_idd.debug_event_t_eid(self, *args)

    def set_eid(self, *args) -> "void":
        r"""
        set_eid(self, id)
        Set event code. If the new event code is compatible with the old one then the
        dependent information (see below) will be preserved. Otherwise the event will be
        cleared and the new event code will be set.

        @param id: (C++: event_id_t) enum event_id_t
        """
        return _ida_idd.debug_event_t_set_eid(self, *args)

    def modinfo(self, *args) -> "modinfo_t const &":
        r"""
        modinfo(self) -> modinfo_t
        """
        return _ida_idd.debug_event_t_modinfo(self, *args)

    def exit_code(self, *args) -> "int const &":
        r"""
        exit_code(self) -> int const &
        """
        return _ida_idd.debug_event_t_exit_code(self, *args)

    def info(self, *args) -> "qstring const &":
        r"""
        info(self) -> qstring
        info(self) -> qstring const &
        """
        return _ida_idd.debug_event_t_info(self, *args)

    def bpt(self, *args) -> "bptaddr_t const &":
        r"""
        bpt(self) -> bptaddr_t
        """
        return _ida_idd.debug_event_t_bpt(self, *args)

    def exc(self, *args) -> "excinfo_t const &":
        r"""
        exc(self) -> excinfo_t
        """
        return _ida_idd.debug_event_t_exc(self, *args)

    def set_modinfo(self, *args) -> "modinfo_t &":
        r"""
        set_modinfo(self, id) -> modinfo_t

        @param id: enum event_id_t
        """
        return _ida_idd.debug_event_t_set_modinfo(self, *args)

    def set_exit_code(self, *args) -> "void":
        r"""
        set_exit_code(self, id, code)

        @param id: enum event_id_t
        @param code: int
        """
        return _ida_idd.debug_event_t_set_exit_code(self, *args)

    def set_info(self, *args) -> "qstring &":
        r"""
        set_info(self, id) -> qstring &

        @param id: enum event_id_t
        """
        return _ida_idd.debug_event_t_set_info(self, *args)

    def set_bpt(self, *args) -> "bptaddr_t &":
        r"""
        set_bpt(self) -> bptaddr_t
        """
        return _ida_idd.debug_event_t_set_bpt(self, *args)

    def set_exception(self, *args) -> "excinfo_t &":
        r"""
        set_exception(self) -> excinfo_t
        """
        return _ida_idd.debug_event_t_set_exception(self, *args)

    def bpt_ea(self, *args) -> "ea_t":
        r"""
        bpt_ea(self) -> ea_t
        On some systems with special memory mappings the triggered ea might be different
        from the actual ea. Calculate the address to use.
        """
        return _ida_idd.debug_event_t_bpt_ea(self, *args)

# Register debug_event_t in _ida_idd:
_ida_idd.debug_event_t_swigregister(debug_event_t)

class exception_info_t(object):
    r"""
    Proxy of C++ exception_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    code = property(_ida_idd.exception_info_t_code_get, _ida_idd.exception_info_t_code_set, doc=r"""code""")
    r"""
    exception code
    """
    flags = property(_ida_idd.exception_info_t_flags_get, _ida_idd.exception_info_t_flags_set, doc=r"""flags""")
    r"""
    Exception info flags
    """

    def break_on(self, *args) -> "bool":
        r"""
        break_on(self) -> bool
        Should we break on the exception?
        """
        return _ida_idd.exception_info_t_break_on(self, *args)

    def handle(self, *args) -> "bool":
        r"""
        handle(self) -> bool
        Should we handle the exception?
        """
        return _ida_idd.exception_info_t_handle(self, *args)
    name = property(_ida_idd.exception_info_t_name_get, _ida_idd.exception_info_t_name_set, doc=r"""name""")
    r"""
    Exception standard name.
    """
    desc = property(_ida_idd.exception_info_t_desc_get, _ida_idd.exception_info_t_desc_set, doc=r"""desc""")
    r"""
    Long message used to display info about the exception.
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> exception_info_t
        __init__(self, _code, _flags, _name, _desc) -> exception_info_t

        @param _code: uint
        @param _flags: uint32
        @param _name: char const *
        @param _desc: char const *
        """
        _ida_idd.exception_info_t_swiginit(self, _ida_idd.new_exception_info_t(*args))
    __swig_destroy__ = _ida_idd.delete_exception_info_t

# Register exception_info_t in _ida_idd:
_ida_idd.exception_info_t_swigregister(exception_info_t)
cvar = _ida_idd.cvar
BPT_WRITE = cvar.BPT_WRITE
r"""
Write access.
"""
BPT_READ = cvar.BPT_READ
r"""
Read access.
"""
BPT_RDWR = cvar.BPT_RDWR
r"""
Read/write access.
"""
BPT_SOFT = cvar.BPT_SOFT
r"""
Software breakpoint.
"""
BPT_EXEC = cvar.BPT_EXEC
r"""
Execute instruction.
"""
BPT_DEFAULT = cvar.BPT_DEFAULT
r"""
Choose bpt type automatically.
"""
EXC_BREAK = _ida_idd.EXC_BREAK
r"""
break on the exception
"""

EXC_HANDLE = _ida_idd.EXC_HANDLE
r"""
should be handled by the debugger?
"""

EXC_MSG = _ida_idd.EXC_MSG
r"""
instead of a warning, log the exception to the output window
"""

EXC_SILENT = _ida_idd.EXC_SILENT
r"""
do not warn or log to the output window
"""


class regval_t(object):
    r"""
    Proxy of C++ regval_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    rvtype = property(_ida_idd.regval_t_rvtype_get, _ida_idd.regval_t_rvtype_set, doc=r"""rvtype""")
    r"""
    one of Register value types
    """
    ival = property(_ida_idd.regval_t_ival_get, _ida_idd.regval_t_ival_set, doc=r"""ival""")
    r"""
    8: integer value
    """
    fval = property(_ida_idd.regval_t_fval_get, _ida_idd.regval_t_fval_set, doc=r"""fval""")
    r"""
    12: floating point value in the internal representation (see ieee.h)
    """
    __swig_destroy__ = _ida_idd.delete_regval_t

    def __init__(self, *args):
        r"""
        __init__(self) -> regval_t
        __init__(self, r) -> regval_t

        @param r: regval_t const &
        """
        _ida_idd.regval_t_swiginit(self, _ida_idd.new_regval_t(*args))

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        Clear register value.
        """
        return _ida_idd.regval_t_clear(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: regval_t const &
        """
        return _ida_idd.regval_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: regval_t const &
        """
        return _ida_idd.regval_t___ne__(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)
        Set this = r and r = this.

        @param r: (C++: regval_t &)
        """
        return _ida_idd.regval_t_swap(self, *args)

    def set_int(self, *args) -> "void":
        r"""
        set_int(self, x)
        Set int value (ival)

        @param x: (C++: uint64)
        """
        return _ida_idd.regval_t_set_int(self, *args)

    def set_float(self, *args) -> "void":
        r"""
        set_float(self, x)
        Set float value (fval)

        @param x: (C++: const fpvalue_t &) fpvalue_t const &
        """
        return _ida_idd.regval_t_set_float(self, *args)

    def set_bytes(self, *args) -> "bytevec_t &":
        r"""
        set_bytes(self, data, size)
        Initialize this regval to an empty custom value.

        @param data: uchar const *
        @param size: size_t

        set_bytes(self, v)

        @param v: bytevec_t const &

        set_bytes(self) -> bytevec_t &
        """
        return _ida_idd.regval_t_set_bytes(self, *args)

    def set_unavailable(self, *args) -> "void":
        r"""
        set_unavailable(self)
        Mark as unavailable.
        """
        return _ida_idd.regval_t_set_unavailable(self, *args)

    def bytes(self, *args) -> "bytevec_t const &":
        r"""
        bytes(self) -> bytevec_t
        Get const custom value.
        bytes(self) -> bytevec_t const &
        """
        return _ida_idd.regval_t_bytes(self, *args)

    def get_data(self, *args) -> "void const *":
        r"""
        get_data(self)
        Get const pointer to value.
        get_data(self) -> void const *
        """
        return _ida_idd.regval_t_get_data(self, *args)

    def get_data_size(self, *args) -> "size_t":
        r"""
        get_data_size(self) -> size_t
        Get size of value.
        """
        return _ida_idd.regval_t_get_data_size(self, *args)

# Register regval_t in _ida_idd:
_ida_idd.regval_t_swigregister(regval_t)
RVT_INT = _ida_idd.RVT_INT
r"""
integer
"""

RVT_FLOAT = _ida_idd.RVT_FLOAT
r"""
floating point
"""

RVT_UNAVAILABLE = _ida_idd.RVT_UNAVAILABLE
r"""
unavailable; other values mean custom data type
"""


class call_stack_info_t(object):
    r"""
    Proxy of C++ call_stack_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    callea = property(_ida_idd.call_stack_info_t_callea_get, _ida_idd.call_stack_info_t_callea_set, doc=r"""callea""")
    r"""
    the address of the call instruction. for the 0th frame this is usually just the
    current value of EIP.
    """
    funcea = property(_ida_idd.call_stack_info_t_funcea_get, _ida_idd.call_stack_info_t_funcea_set, doc=r"""funcea""")
    r"""
    the address of the called function
    """
    fp = property(_ida_idd.call_stack_info_t_fp_get, _ida_idd.call_stack_info_t_fp_set, doc=r"""fp""")
    r"""
    the value of the frame pointer of the called function
    """
    funcok = property(_ida_idd.call_stack_info_t_funcok_get, _ida_idd.call_stack_info_t_funcok_set, doc=r"""funcok""")
    r"""
    is the function present?
    """

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: call_stack_info_t const &
        """
        return _ida_idd.call_stack_info_t___ne__(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> call_stack_info_t
        """
        _ida_idd.call_stack_info_t_swiginit(self, _ida_idd.new_call_stack_info_t(*args))
    __swig_destroy__ = _ida_idd.delete_call_stack_info_t

# Register call_stack_info_t in _ida_idd:
_ida_idd.call_stack_info_t_swigregister(call_stack_info_t)

class call_stack_t(call_stack_info_vec_t):
    r"""
    Proxy of C++ call_stack_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> call_stack_t
        """
        _ida_idd.call_stack_t_swiginit(self, _ida_idd.new_call_stack_t(*args))
    __swig_destroy__ = _ida_idd.delete_call_stack_t

# Register call_stack_t in _ida_idd:
_ida_idd.call_stack_t_swigregister(call_stack_t)


def dbg_appcall(*args) -> "error_t":
    r"""
    dbg_appcall(retval, func_ea, tid, ptif, argv, argnum) -> error_t
    Call a function from the debugged application.

    @param retval: (C++: idc_value_t *)
    @param func_ea: (C++: ea_t) address to call
    @param tid: (C++: thid_t) thread to use. NO_THREAD means to use the current thread
    @param ptif: (C++: const tinfo_t *) pointer to type of the function to call
    @param argv: (C++: idc_value_t *) array of arguments
    @param argnum: (C++: size_t) number of actual arguments
    @return: eOk if successful, otherwise an error code
    """
    return _ida_idd.dbg_appcall(*args)

def cleanup_appcall(*args) -> "error_t":
    r"""
    cleanup_appcall(tid) -> error_t
    Cleanup after manual appcall.

    @param tid: (C++: thid_t) thread to use. NO_THREAD means to use the current thread The
                application state is restored as it was before calling the last
                appcall(). Nested appcalls are supported.
    @return: eOk if successful, otherwise an error code
    """
    return _ida_idd.cleanup_appcall(*args)
class thread_name_t(object):
    r"""
    Proxy of C++ thread_name_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    tid = property(_ida_idd.thread_name_t_tid_get, _ida_idd.thread_name_t_tid_set, doc=r"""tid""")
    r"""
    thread
    """
    name = property(_ida_idd.thread_name_t_name_get, _ida_idd.thread_name_t_name_set, doc=r"""name""")
    r"""
    new thread name
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> thread_name_t
        """
        _ida_idd.thread_name_t_swiginit(self, _ida_idd.new_thread_name_t(*args))
    __swig_destroy__ = _ida_idd.delete_thread_name_t

# Register thread_name_t in _ida_idd:
_ida_idd.thread_name_t_swigregister(thread_name_t)

RESMOD_NONE = _ida_idd.RESMOD_NONE
r"""
no stepping, run freely
"""

RESMOD_INTO = _ida_idd.RESMOD_INTO
r"""
step into call (the most typical single stepping)
"""

RESMOD_OVER = _ida_idd.RESMOD_OVER
r"""
step over call
"""

RESMOD_OUT = _ida_idd.RESMOD_OUT
r"""
step out of the current function (run until return)
"""

RESMOD_SRCINTO = _ida_idd.RESMOD_SRCINTO
r"""
until control reaches a different source line
"""

RESMOD_SRCOVER = _ida_idd.RESMOD_SRCOVER
r"""
next source line in the current stack frame
"""

RESMOD_SRCOUT = _ida_idd.RESMOD_SRCOUT
r"""
next source line in the previous stack frame
"""

RESMOD_USER = _ida_idd.RESMOD_USER
r"""
step out to the user code
"""

RESMOD_HANDLE = _ida_idd.RESMOD_HANDLE
r"""
step into the exception handler
"""

RESMOD_MAX = _ida_idd.RESMOD_MAX

STEP_TRACE = _ida_idd.STEP_TRACE

INSN_TRACE = _ida_idd.INSN_TRACE

FUNC_TRACE = _ida_idd.FUNC_TRACE

BBLK_TRACE = _ida_idd.BBLK_TRACE

DRC_EVENTS = _ida_idd.DRC_EVENTS
r"""
success, there are pending events
"""

DRC_CRC = _ida_idd.DRC_CRC
r"""
success, but the input file crc does not match
"""

DRC_OK = _ida_idd.DRC_OK
r"""
success
"""

DRC_NONE = _ida_idd.DRC_NONE
r"""
reaction to the event not implemented
"""

DRC_FAILED = _ida_idd.DRC_FAILED
r"""
failed or false
"""

DRC_NETERR = _ida_idd.DRC_NETERR
r"""
network error
"""

DRC_NOFILE = _ida_idd.DRC_NOFILE
r"""
file not found
"""

DRC_IDBSEG = _ida_idd.DRC_IDBSEG
r"""
use idb segmentation
"""

DRC_NOPROC = _ida_idd.DRC_NOPROC
r"""
the process does not exist anymore
"""

DRC_NOCHG = _ida_idd.DRC_NOCHG
r"""
no changes
"""

DRC_ERROR = _ida_idd.DRC_ERROR
r"""
unclassified error, may be complemented by errbuf
"""

RQ_MASKING = _ida_idd.RQ_MASKING

RQ_SUSPEND = _ida_idd.RQ_SUSPEND

RQ_NOSUSP = _ida_idd.RQ_NOSUSP

RQ_IGNWERR = _ida_idd.RQ_IGNWERR

RQ_SILENT = _ida_idd.RQ_SILENT

RQ_VERBOSE = _ida_idd.RQ_VERBOSE

RQ_SWSCREEN = _ida_idd.RQ_SWSCREEN

RQ__NOTHRRF = _ida_idd.RQ__NOTHRRF

RQ_PROCEXIT = _ida_idd.RQ_PROCEXIT

RQ_IDAIDLE = _ida_idd.RQ_IDAIDLE

RQ_SUSPRUN = _ida_idd.RQ_SUSPRUN

RQ_RESUME = _ida_idd.RQ_RESUME

RQ_RESMOD = _ida_idd.RQ_RESMOD

RQ_RESMOD_SHIFT = _ida_idd.RQ_RESMOD_SHIFT


def dbg_get_registers(*args) -> "PyObject *":
    r"""
    dbg_get_registers() -> PyObject *
    This function returns the register definition from the currently loaded debugger.
    Basically, it returns an array of structure similar to to idd.hpp / register_info_t

    @return:     None if no debugger is loaded
        tuple(name, flags, class, dtype, bit_strings, default_bit_strings_mask)
        The bit_strings can be a tuple of strings or None (if the register does not have bit_strings)
    """
    return _ida_idd.dbg_get_registers(*args)

def dbg_get_thread_sreg_base(*args) -> "PyObject *":
    r"""
    dbg_get_thread_sreg_base(tid, sreg_value) -> PyObject *
    Returns the segment register base value

    @param tid: thread id
    @param sreg_value: segment register (selector) value
    @return:     - The base as an 'ea'
        - Or None on failure
    """
    return _ida_idd.dbg_get_thread_sreg_base(*args)

def dbg_read_memory(*args) -> "PyObject *":
    r"""
    dbg_read_memory(ea, sz) -> PyObject *
    Reads from the debugee's memory at the specified ea

    @param ea: ea_t
    @param sz: size_t
    @return:     - The read buffer (as a string)
        - Or None on failure
    """
    return _ida_idd.dbg_read_memory(*args)

def dbg_write_memory(*args) -> "PyObject *":
    r"""
    dbg_write_memory(ea, buf) -> bool
    Writes a buffer to the debugee's memory

    @param ea: ea_t
    @param buf: bytevec_t const &
    @return: Boolean
    """
    return _ida_idd.dbg_write_memory(*args)

def dbg_get_name(*args) -> "PyObject *":
    r"""
    dbg_get_name() -> PyObject *
    This function returns the current debugger's name.

    @return: Debugger name or None if no debugger is active
    """
    return _ida_idd.dbg_get_name(*args)

def dbg_get_memory_info(*args) -> "PyObject *":
    r"""
    dbg_get_memory_info() -> PyObject *
    This function returns the memory configuration of a debugged process.

    @return:     None if no debugger is active
        tuple(start_ea, end_ea, name, sclass, sbase, bitness, perm)
    """
    return _ida_idd.dbg_get_memory_info(*args)

def appcall(*args) -> "PyObject *":
    r"""
    appcall(func_ea, tid, _type_or_none, _fields, arg_list) -> PyObject *

    @param func_ea: ea_t
    @param tid: thid_t
    @param _type_or_none: bytevec_t const &
    @param _fields: bytevec_t const &
    @param arg_list: PyObject *
    """
    return _ida_idd.appcall(*args)

def get_event_module_name(*args) -> "size_t":
    r"""
    get_event_module_name(ev) -> str

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_module_name(*args)

def get_event_module_base(*args) -> "ea_t":
    r"""
    get_event_module_base(ev) -> ea_t

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_module_base(*args)

def get_event_module_size(*args) -> "asize_t":
    r"""
    get_event_module_size(ev) -> asize_t

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_module_size(*args)

def get_event_exc_info(*args) -> "size_t":
    r"""
    get_event_exc_info(ev) -> str

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_exc_info(*args)

def get_event_info(*args) -> "size_t":
    r"""
    get_event_info(ev) -> str

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_info(*args)

def get_event_bpt_hea(*args) -> "ea_t":
    r"""
    get_event_bpt_hea(ev) -> ea_t

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_bpt_hea(*args)

def get_event_exc_code(*args) -> "uint":
    r"""
    get_event_exc_code(ev) -> uint

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_exc_code(*args)

def get_event_exc_ea(*args) -> "ea_t":
    r"""
    get_event_exc_ea(ev) -> ea_t

    @param ev: debug_event_t const *
    """
    return _ida_idd.get_event_exc_ea(*args)

def can_exc_continue(*args) -> "bool":
    r"""
    can_exc_continue(ev) -> bool

    @param ev: debug_event_t const *
    """
    return _ida_idd.can_exc_continue(*args)

#<pycode(py_idd)>
NO_PROCESS = 0xFFFFFFFF
r"""
No process.
"""
NO_THREAD  = 0

import types
import _ida_idaapi
import _ida_dbg
import _ida_typeinf
import _ida_name
import _ida_bytes
import _ida_ida
import ida_idaapi
import ida_typeinf

dbg_can_query = _ida_dbg.dbg_can_query

# -----------------------------------------------------------------------
class Appcall_array__(object):
    r"""
    This class is used with Appcall.array() method
    """
    def __init__(self, tp):
        self.__type = tp

    def pack(self, L):
        r"""
        Packs a list or tuple into a byref buffer
        """
        t = type(L)
        if not (t == list or t == tuple):
            raise ValueError("Either a list or a tuple must be passed")
        self.__size = len(L)
        if self.__size == 1:
            self.__typedobj = Appcall__.typedobj(self.__type + ";")
        else:
            self.__typedobj = Appcall__.typedobj("%s x[%d];" % (self.__type, self.__size))
# Now store the object in a string buffer
        ok, buf = self.__typedobj.store(L)
        if ok:
            return Appcall__.byref(buf)
        else:
            return None

    def try_to_convert_to_list(self, obj):
        r"""
        Is this object a list? We check for the existance of attribute zero and attribute self.size-1
        """
        if not (hasattr(obj, "0") and hasattr(obj, str(self.__size-1))):
            return obj
# at this point, we are sure we have an "idc list"
# let us convert to a Python list
        return [getattr(obj, str(x)) for x in range(0, self.__size)]

    def unpack(self, buf, as_list=True):
        r"""
        Unpacks an array back into a list or an object
        """
# take the value from the special ref object
        if isinstance(buf, ida_idaapi.PyIdc_cvt_refclass__):
            buf = buf.value

# we can only unpack from strings
        if type(buf) != bytes:
            raise ValueError("Cannot unpack this type!")
# now unpack
        ok, obj = self.__typedobj.retrieve(buf)
        if not ok:
            raise ValueError("Failed while unpacking!")
        if not as_list:
            return obj
        return self.try_to_convert_to_list(obj)


# -----------------------------------------------------------------------
# Wrapper class for the appcall()
class Appcall_callable__(object):
    r"""
    Helper class to issue appcalls using a natural syntax:
      appcall.FunctionNameInTheDatabase(arguments, ....)
    or
      appcall["Function@8"](arguments, ...)
    or
      f8 = appcall["Function@8"]
      f8(arg1, arg2, ...)
    or
      o = appcall.obj()
      i = byref(5)
      appcall.funcname(arg1, i, "hello", o)
    """
    def __init__(self, ea, tinfo_or_typestr = None, fields = None):
        r"""
        Initializes an appcall with a given function ea
        """
        self.__ea      = ea
        self.__tif     = None
        self.__type    = None
        self.__fields  = None
        self.__options = None # Appcall options
        self.__timeout = None # Appcall timeout

        if tinfo_or_typestr:
          if isinstance(tinfo_or_typestr, ida_idaapi.string_types):
# a type string? assume (typestr, fields), try to deserialize
            tif = ida_typeinf.tinfo_t()
            if not tif.deserialize(None, tinfo_or_typestr, fields):
              raise ValueError("Could not deserialize type string")
          else:
            if not isinstance(tinfo_or_typestr, ida_typeinf.tinfo_t):
              raise ValueError("Invalid argument 'tinfo_or_typestr'")
            tif = tinfo_or_typestr
          self.__tif = tif
          (self.__type, self.__fields, _) = tif.serialize()

    def __get_timeout(self):
        return self.__timeout

    def __set_timeout(self, v):
        self.__timeout = v

    timeout = property(__get_timeout, __set_timeout)
    r"""
    An Appcall instance can change its timeout value with this attribute
    """

    def __get_options(self):
        return self.__options if self.__options != None else Appcall__.get_appcall_options()

    def __set_options(self, v):
        if self.timeout:
# If timeout value is set, then put the timeout flag and encode the timeout value
            v |= Appcall__.APPCALL_TIMEOUT | (self.timeout << 16)
        else:
# Timeout is not set, then clear the timeout flag
            v &= ~Appcall__.APPCALL_TIMEOUT

        self.__options = v

    options = property(__get_options, __set_options)
    r"""
    Sets the Appcall options locally to this Appcall instance
    """

    def __call__(self, *args):
        r"""
        Make object callable. We redirect execution to idaapi.appcall()
        """
        if self.ea is None:
            raise ValueError("Object not callable!")

# convert arguments to a list
        arg_list = list(args)

# Save appcall options and set new global options
        old_opt = Appcall__.get_appcall_options()
        Appcall__.set_appcall_options(self.options)

# Do the Appcall (use the wrapped version)
        try:
            return _ida_idd.appcall(
                self.ea,
                _ida_dbg.get_current_thread(),
                self.type,
                self.fields,
                arg_list)
        finally:
# Restore appcall options
            Appcall__.set_appcall_options(old_opt)

    def __get_ea(self):
        return self.__ea

    def __set_ea(self, val):
        self.__ea = val

    ea = property(__get_ea, __set_ea)
    r"""
    Returns or sets the EA associated with this object
    """

    def __get_tif(self):
        return self.__tif

    tif = property(__get_tif)
    r"""
    Returns the tinfo_t object
    """

    def __get_size(self):
        if self.__type == None:
            return -1
        r = _ida_typeinf.calc_type_size(None, self.__type)
        if not r:
            return -1
        return r

    size = property(__get_size)
    r"""
    Returns the size of the type
    """

    def __get_type(self):
        return self.__type

    type = property(__get_type)
    r"""
    Returns the typestring
    """

    def __get_fields(self):
        return self.__fields

    fields = property(__get_fields)
    r"""
    Returns the field names
    """


    def retrieve(self, src=None, flags=0):
        r"""
        Unpacks a typed object from the database if an ea is given or from a string if a string was passed
        @param src: the address of the object or a string
        @return: Returns a tuple of boolean and object or error number (Bool, Error | Object).
        """

# Nothing passed? Take the address and unpack from the database
        if src is None:
            src = self.ea

        if type(src) == bytes:
            return _ida_typeinf.unpack_object_from_bv(None, self.type, self.fields, src, flags)
        else:
            return _ida_typeinf.unpack_object_from_idb(None, self.type, self.fields, src, flags)

    def store(self, obj, dest_ea=None, base_ea=0, flags=0):
        r"""
        Packs an object into a given ea if provided or into a string if no address was passed.
        @param obj: The object to pack
        @param dest_ea: If packing to idb this will be the store location
        @param base_ea: If packing to a buffer, this will be the base that will be used to relocate the pointers

        @return:     - If packing to a string then a Tuple(Boolean, packed_string or error code)
            - If packing to the database then a return code is returned (0 is success)
        """

# no ea passed? thus pack to a string
        if dest_ea is None:
            return _ida_typeinf.pack_object_to_bv(obj,
                                             None,
                                             self.type,
                                             self.fields,
                                             base_ea,
                                             flags)
        else:
            return _ida_typeinf.pack_object_to_idb(obj,
                                              None,
                                              self.type,
                                              self.fields,
                                              dest_ea,
                                              flags)

# -----------------------------------------------------------------------
class Appcall_consts__(object):
    r"""
    Helper class used by Appcall.Consts attribute
    It is used to retrieve constants via attribute access
    """
    def __init__(self, default=None):
        self.__default = default

    def __getattr__(self, attr):
        v = Appcall__.valueof(attr, self.__default)
        if v is None:
            raise AttributeError("No constant with name " + attr)
        return v

# -----------------------------------------------------------------------
class Appcall__(object):
    APPCALL_MANUAL = 0x1
    r"""
    Only set up the appcall, do not run it.
    you should call CleanupAppcall() when finished
    """

    APPCALL_DEBEV  = 0x2
    r"""
    Return debug event information
    If this bit is set, exceptions during appcall
    will generate idc exceptions with full
    information about the exception
    """

    APPCALL_TIMEOUT = 0x4
    r"""
    Appcall with timeout
    The timeout value in milliseconds is specified
    in the high 2 bytes of the 'options' argument:
    If timed out, errbuf will contain "timeout".
    """

    __name__ = "Appcall__"

    def __init__(self):
        self.__consts = Appcall_consts__()

    def __get_consts(self):
        return self.__consts

    Consts = property(__get_consts)
    r"""
    Use Appcall.Consts.CONST_NAME to access constants
    """

    @staticmethod
    def __name_or_ea(name_or_ea):
        r"""
        Function that accepts a name or an ea and checks if the address is enabled.
        If a name is passed then idaapi.get_name_ea() is applied to retrieve the name
        @return:     - Returns the resolved EA or
            - Raises an exception if the address is not enabled
        """

# a string? try to resolve it
        if type(name_or_ea) in ida_idaapi.string_types:
            ea = _ida_name.get_name_ea(_ida_idaapi.BADADDR, name_or_ea)
        else:
            ea = name_or_ea
# could not resolve name or invalid address?
        if ea == _ida_idaapi.BADADDR or not _ida_bytes.is_mapped(ea):
            raise AttributeError("Undefined function " + name_or_ea)
        return ea

    @staticmethod
    def __typedecl_or_tinfo(typedecl_or_tinfo, flags = None):
        r"""
        Function that accepts a tinfo_t object or type declaration as a string
        If a type declaration is passed then ida_typeinf.parse_decl() is applied to prepare tinfo_t object
        @return:     - Returns the tinfo_t object
            - Raises an exception if the declaration cannot be parsed
        """

# a string? try to parse it
        if isinstance(typedecl_or_tinfo, ida_idaapi.string_types):
          if flags is None:
              flags = ida_typeinf.PT_SIL|ida_typeinf.PT_NDC|ida_typeinf.PT_TYP
          tif = ida_typeinf.tinfo_t()
          if ida_typeinf.parse_decl(tif, None, typedecl_or_tinfo, flags) == None:
            raise ValueError("Could not parse type: " + typedecl_or_tinfo)
        else:
            if not isinstance(typedecl_or_tinfo, ida_typeinf.tinfo_t):
              raise ValueError("Invalid argument 'typedecl_or_tinfo'")
            tif = typedecl_or_tinfo
        return tif

    @staticmethod
    def proto(name_or_ea, proto_or_tinfo, flags = None):
        r"""
        Allows you to instantiate an appcall (callable object) with the desired prototype
        @param name_or_ea: The name of the function (will be resolved with LocByName())
        @param proto_or_tinfo: function prototype as a string or type of the function as tinfo_t object
        @return:     - On failure it raises an exception if the prototype could not be parsed
              or the address is not resolvable
            - Returns a callbable Appcall instance with the given prototypes and flags
        """

# resolve and raise exception on error
        ea = Appcall__.__name_or_ea(name_or_ea)

# parse the type if it is given as (prototype, flags)
        tif = Appcall__.__typedecl_or_tinfo(proto_or_tinfo, flags)

# Return the callable method with type info
        return Appcall_callable__(ea, tif)

    def __getattr__(self, name_or_ea):
        r"""
        Allows you to call functions as if they were member functions (by returning a callable object)
        """
# resolve and raise exception on error
        ea = self.__name_or_ea(name_or_ea)
        if ea == _ida_idaapi.BADADDR:
            raise AttributeError("Undefined function " + name)
# Return the callable method
        return Appcall_callable__(ea)

    def __getitem__(self, idx):
        r"""
        Use self[func_name] syntax if the function name contains invalid characters for an attribute name
        See __getattr___
        """
        return self.__getattr__(idx)

    @staticmethod
    def valueof(name, default=0):
        r"""
        Returns the numeric value of a given name string.
        If the name could not be resolved then the default value will be returned
        """
        t, v = _ida_name.get_name_value(_ida_idaapi.BADADDR, name)
        if t == 0: # NT_NONE
          v = default
        return v

    @staticmethod
    def int64(v):
        r"""
        Whenever a 64bit number is needed use this method to construct an object
        """
        return ida_idaapi.PyIdc_cvt_int64__(v)

    @staticmethod
    def byref(val):
        r"""
        Method to create references to immutable objects
        Currently we support references to int/strings
        Objects need not be passed by reference (this will be done automatically)
        """
        return ida_idaapi.PyIdc_cvt_refclass__(val)

    @staticmethod
    def buffer(str = None, size = 0, fill="\x00"):
        r"""
        Creates a string buffer. The returned value (r) will be a byref object.
        Use r.value to get the contents and r.size to get the buffer's size
        """
        if str is None:
            str = ""
        left = size - len(str)
        if left > 0:
            str = str + (fill * left)
        r = Appcall__.byref(str)
        r.size = size
        return r

    @staticmethod
    def obj(**kwds):
        r"""
        Returns an empty object or objects with attributes as passed via its keywords arguments
        """
        return ida_idaapi.object_t(**kwds)

    @staticmethod
    def cstr(val):
        return ida_idaapi.as_cstr(val)

    @staticmethod
    def UTF16(s):
        return ida_idaapi.as_UTF16(s)
    unicode = UTF16

    @staticmethod
    def array(type_name):
        r"""
        Defines an array type. Later you need to pack() / unpack()
        """
        return Appcall_array__(type_name)

    @staticmethod
    def typedobj(typedecl_or_tinfo, ea=None):
        r"""
        Returns an appcall object for a type (can be given as tinfo_t object or
        as a string declaration)
        One can then use retrieve() member method
        @param ea: Optional parameter that later can be used to retrieve the type
        @return: Appcall object or raises ValueError exception
        """
# parse the type if it is given as string
        tif = Appcall__.__typedecl_or_tinfo(typedecl_or_tinfo)
# Return the callable method with type info
        return Appcall_callable__(ea, tif)

    @staticmethod
    def set_appcall_options(opt):
        r"""
        Method to change the Appcall options globally (not per Appcall)
        """
        old_opt = Appcall__.get_appcall_options()
        _ida_ida.cvar.inf.appcall_options = opt
        return old_opt

    @staticmethod
    def get_appcall_options():
        r"""
        Return the global Appcall options
        """
        return _ida_ida.cvar.inf.appcall_options

    @staticmethod
    def cleanup_appcall(tid = 0):
        r"""
        Equivalent to IDC's CleanupAppcall()
        """
        return _ida_idd.cleanup_appcall(tid)

Appcall = Appcall__()
#</pycode(py_idd)>




