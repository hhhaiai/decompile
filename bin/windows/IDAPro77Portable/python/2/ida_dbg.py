"""
Contains functions to control the debugging of a process.

See Debugger functions for a complete explanation of these functions.

These functions are inlined for the kernel. They are not inlined for the user-
interfaces."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_dbg
else:
    import _ida_dbg

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

SWIG_PYTHON_LEGACY_BOOL = _ida_dbg.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_idd
class bpt_vec_t(object):
    r"""
    Proxy of C++ qvector< bpt_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> bpt_vec_t
        __init__(self, x) -> bpt_vec_t

        @param x: qvector< bpt_t > const &
        """
        _ida_dbg.bpt_vec_t_swiginit(self, _ida_dbg.new_bpt_vec_t(*args))
    __swig_destroy__ = _ida_dbg.delete_bpt_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: bpt_t const &

        push_back(self) -> bpt_t
        """
        return _ida_dbg.bpt_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dbg.bpt_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dbg.bpt_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dbg.bpt_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> bpt_t

        @param _idx: size_t
        """
        return _ida_dbg.bpt_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dbg.bpt_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dbg.bpt_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: bpt_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dbg.bpt_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=bpt_t())

        @param x: bpt_t const &
        """
        return _ida_dbg.bpt_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dbg.bpt_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dbg.bpt_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dbg.bpt_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< bpt_t > &
        """
        return _ida_dbg.bpt_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> bpt_t
        """
        return _ida_dbg.bpt_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: bpt_t *
        @param len: size_t
        """
        return _ida_dbg.bpt_vec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> bpt_t
        """
        return _ida_dbg.bpt_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> bpt_t
        """
        return _ida_dbg.bpt_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> bpt_t

        @param it: qvector< bpt_t >::iterator
        @param x: bpt_t const &
        """
        return _ida_dbg.bpt_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> bpt_t

        @param it: qvector< bpt_t >::iterator

        erase(self, first, last) -> bpt_t

        @param first: qvector< bpt_t >::iterator
        @param last: qvector< bpt_t >::iterator
        """
        return _ida_dbg.bpt_vec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dbg.bpt_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> bpt_t

        @param i: size_t
        """
        return _ida_dbg.bpt_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: bpt_t const &
        """
        return _ida_dbg.bpt_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register bpt_vec_t in _ida_dbg:
_ida_dbg.bpt_vec_t_swigregister(bpt_vec_t)

class tev_reg_values_t(object):
    r"""
    Proxy of C++ qvector< tev_reg_value_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> tev_reg_values_t
        __init__(self, x) -> tev_reg_values_t

        @param x: qvector< tev_reg_value_t > const &
        """
        _ida_dbg.tev_reg_values_t_swiginit(self, _ida_dbg.new_tev_reg_values_t(*args))
    __swig_destroy__ = _ida_dbg.delete_tev_reg_values_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: tev_reg_value_t const &

        push_back(self) -> tev_reg_value_t
        """
        return _ida_dbg.tev_reg_values_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dbg.tev_reg_values_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dbg.tev_reg_values_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dbg.tev_reg_values_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> tev_reg_value_t

        @param _idx: size_t
        """
        return _ida_dbg.tev_reg_values_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dbg.tev_reg_values_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dbg.tev_reg_values_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: tev_reg_value_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dbg.tev_reg_values_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=tev_reg_value_t())

        @param x: tev_reg_value_t const &
        """
        return _ida_dbg.tev_reg_values_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dbg.tev_reg_values_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dbg.tev_reg_values_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dbg.tev_reg_values_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< tev_reg_value_t > &
        """
        return _ida_dbg.tev_reg_values_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> tev_reg_value_t
        """
        return _ida_dbg.tev_reg_values_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: tev_reg_value_t *
        @param len: size_t
        """
        return _ida_dbg.tev_reg_values_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> tev_reg_value_t
        """
        return _ida_dbg.tev_reg_values_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> tev_reg_value_t
        """
        return _ida_dbg.tev_reg_values_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> tev_reg_value_t

        @param it: qvector< tev_reg_value_t >::iterator
        @param x: tev_reg_value_t const &
        """
        return _ida_dbg.tev_reg_values_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> tev_reg_value_t

        @param it: qvector< tev_reg_value_t >::iterator

        erase(self, first, last) -> tev_reg_value_t

        @param first: qvector< tev_reg_value_t >::iterator
        @param last: qvector< tev_reg_value_t >::iterator
        """
        return _ida_dbg.tev_reg_values_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dbg.tev_reg_values_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> tev_reg_value_t

        @param i: size_t
        """
        return _ida_dbg.tev_reg_values_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: tev_reg_value_t const &
        """
        return _ida_dbg.tev_reg_values_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register tev_reg_values_t in _ida_dbg:
_ida_dbg.tev_reg_values_t_swigregister(tev_reg_values_t)

class tevinforeg_vec_t(object):
    r"""
    Proxy of C++ qvector< tev_info_reg_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> tevinforeg_vec_t
        __init__(self, x) -> tevinforeg_vec_t

        @param x: qvector< tev_info_reg_t > const &
        """
        _ida_dbg.tevinforeg_vec_t_swiginit(self, _ida_dbg.new_tevinforeg_vec_t(*args))
    __swig_destroy__ = _ida_dbg.delete_tevinforeg_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: tev_info_reg_t const &

        push_back(self) -> tev_info_reg_t
        """
        return _ida_dbg.tevinforeg_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dbg.tevinforeg_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dbg.tevinforeg_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dbg.tevinforeg_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> tev_info_reg_t

        @param _idx: size_t
        """
        return _ida_dbg.tevinforeg_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dbg.tevinforeg_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dbg.tevinforeg_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: tev_info_reg_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dbg.tevinforeg_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=tev_info_reg_t())

        @param x: tev_info_reg_t const &
        """
        return _ida_dbg.tevinforeg_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dbg.tevinforeg_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dbg.tevinforeg_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dbg.tevinforeg_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< tev_info_reg_t > &
        """
        return _ida_dbg.tevinforeg_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> tev_info_reg_t
        """
        return _ida_dbg.tevinforeg_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: tev_info_reg_t *
        @param len: size_t
        """
        return _ida_dbg.tevinforeg_vec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> tev_info_reg_t
        """
        return _ida_dbg.tevinforeg_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> tev_info_reg_t
        """
        return _ida_dbg.tevinforeg_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> tev_info_reg_t

        @param it: qvector< tev_info_reg_t >::iterator
        @param x: tev_info_reg_t const &
        """
        return _ida_dbg.tevinforeg_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> tev_info_reg_t

        @param it: qvector< tev_info_reg_t >::iterator

        erase(self, first, last) -> tev_info_reg_t

        @param first: qvector< tev_info_reg_t >::iterator
        @param last: qvector< tev_info_reg_t >::iterator
        """
        return _ida_dbg.tevinforeg_vec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dbg.tevinforeg_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> tev_info_reg_t

        @param i: size_t
        """
        return _ida_dbg.tevinforeg_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: tev_info_reg_t const &
        """
        return _ida_dbg.tevinforeg_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register tevinforeg_vec_t in _ida_dbg:
_ida_dbg.tevinforeg_vec_t_swigregister(tevinforeg_vec_t)

class memreg_infos_t(object):
    r"""
    Proxy of C++ qvector< memreg_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> memreg_infos_t
        __init__(self, x) -> memreg_infos_t

        @param x: qvector< memreg_info_t > const &
        """
        _ida_dbg.memreg_infos_t_swiginit(self, _ida_dbg.new_memreg_infos_t(*args))
    __swig_destroy__ = _ida_dbg.delete_memreg_infos_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: memreg_info_t const &

        push_back(self) -> memreg_info_t
        """
        return _ida_dbg.memreg_infos_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dbg.memreg_infos_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dbg.memreg_infos_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dbg.memreg_infos_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> memreg_info_t

        @param _idx: size_t
        """
        return _ida_dbg.memreg_infos_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dbg.memreg_infos_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dbg.memreg_infos_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: memreg_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dbg.memreg_infos_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=memreg_info_t())

        @param x: memreg_info_t const &
        """
        return _ida_dbg.memreg_infos_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dbg.memreg_infos_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dbg.memreg_infos_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dbg.memreg_infos_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< memreg_info_t > &
        """
        return _ida_dbg.memreg_infos_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> memreg_info_t
        """
        return _ida_dbg.memreg_infos_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: memreg_info_t *
        @param len: size_t
        """
        return _ida_dbg.memreg_infos_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> memreg_info_t
        """
        return _ida_dbg.memreg_infos_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> memreg_info_t
        """
        return _ida_dbg.memreg_infos_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> memreg_info_t

        @param it: qvector< memreg_info_t >::iterator
        @param x: memreg_info_t const &
        """
        return _ida_dbg.memreg_infos_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> memreg_info_t

        @param it: qvector< memreg_info_t >::iterator

        erase(self, first, last) -> memreg_info_t

        @param first: qvector< memreg_info_t >::iterator
        @param last: qvector< memreg_info_t >::iterator
        """
        return _ida_dbg.memreg_infos_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dbg.memreg_infos_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> memreg_info_t

        @param i: size_t
        """
        return _ida_dbg.memreg_infos_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: memreg_info_t const &
        """
        return _ida_dbg.memreg_infos_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register memreg_infos_t in _ida_dbg:
_ida_dbg.memreg_infos_t_swigregister(memreg_infos_t)


def run_to(*args):
    r"""
    run_to(ea, pid=pid_t(-1), tid=0) -> bool
    Execute the process until the given address is reached. If no process is active,
    a new process is started. Technically, the debugger sets up a temporary
    breakpoint at the given address, and continues (or starts) the execution of the
    whole process. So, all threads continue their execution! \sq{Type, Asynchronous
    function - available as Request, Notification, dbg_run_to}

    @param ea: (C++: ea_t) target address
    @param pid: (C++: pid_t) not used yet. please do not specify this parameter.
    """
    return _ida_dbg.run_to(*args)

def request_run_to(*args):
    r"""
    request_run_to(ea, pid=pid_t(-1), tid=0) -> bool
    Post a run_to() request.

    @param ea: (C++: ea_t)
    @param pid: (C++: pid_t)
    """
    return _ida_dbg.request_run_to(*args)
dbg_null = _ida_dbg.dbg_null

dbg_process_start = _ida_dbg.dbg_process_start
r"""
@note: This event notification is also an asynchronous function result
       notification for start_process() !
"""

dbg_process_exit = _ida_dbg.dbg_process_exit
r"""
@note: This event notification is also an asynchronous function result
       notification for start_process() !
"""

dbg_process_attach = _ida_dbg.dbg_process_attach
r"""
@note: This event notification is also an asynchronous function result
       notification for start_process() !
"""

dbg_process_detach = _ida_dbg.dbg_process_detach
r"""
@note: This event notification is also an asynchronous function result
       notification for start_process() !
"""

dbg_thread_start = _ida_dbg.dbg_thread_start

dbg_thread_exit = _ida_dbg.dbg_thread_exit

dbg_library_load = _ida_dbg.dbg_library_load

dbg_library_unload = _ida_dbg.dbg_library_unload

dbg_information = _ida_dbg.dbg_information

dbg_exception = _ida_dbg.dbg_exception

dbg_suspend_process = _ida_dbg.dbg_suspend_process
r"""
The process is now suspended.

@note: This event notification is also an asynchronous function result
       notification for suspend_process() !
"""

dbg_bpt = _ida_dbg.dbg_bpt
r"""
A user defined breakpoint was reached.
"""

dbg_trace = _ida_dbg.dbg_trace
r"""
A step occurred (one instruction was executed). This event notification is only
generated if step tracing is enabled.

@retval 1: do not log this trace event
@retval 0: log it
"""

dbg_request_error = _ida_dbg.dbg_request_error
r"""
An error occurred during the processing of a request.
"""

dbg_step_into = _ida_dbg.dbg_step_into

dbg_step_over = _ida_dbg.dbg_step_over

dbg_run_to = _ida_dbg.dbg_run_to

dbg_step_until_ret = _ida_dbg.dbg_step_until_ret

dbg_bpt_changed = _ida_dbg.dbg_bpt_changed
r"""
Breakpoint has been changed.
"""

dbg_started_loading_bpts = _ida_dbg.dbg_started_loading_bpts
r"""
Started loading breakpoint info from idb.
"""

dbg_finished_loading_bpts = _ida_dbg.dbg_finished_loading_bpts
r"""
Finished loading breakpoint info from idb.
"""

dbg_last = _ida_dbg.dbg_last
r"""
The last debugger notification code.
"""

BPTEV_ADDED = _ida_dbg.BPTEV_ADDED
r"""
Breakpoint has been added.
"""

BPTEV_REMOVED = _ida_dbg.BPTEV_REMOVED
r"""
Breakpoint has been removed.
"""

BPTEV_CHANGED = _ida_dbg.BPTEV_CHANGED
r"""
Breakpoint has been modified.
"""


def run_requests(*args):
    r"""
    run_requests() -> bool
    Execute requests until all requests are processed or an asynchronous function is
    called. \sq{Type, Synchronous function, Notification, none (synchronous
    function)}

    @return: false if not all requests could be processed (indicates an asynchronous
             function was started)
    @note: If called from a notification handler, the execution of requests will be
           postponed to the end of the execution of all notification handlers.
    """
    return _ida_dbg.run_requests(*args)

def get_running_request(*args):
    r"""
    get_running_request() -> ui_notification_t
    Get the current running request. \sq{Type, Synchronous function, Notification,
    none (synchronous function)}

    @return: ui_null if no running request
    """
    return _ida_dbg.get_running_request(*args)

def is_request_running(*args):
    r"""
    is_request_running() -> bool
    Is a request currently running?
    """
    return _ida_dbg.is_request_running(*args)

def get_running_notification(*args):
    r"""
    get_running_notification() -> dbg_notification_t
    Get the notification associated (if any) with the current running request.
    \sq{Type, Synchronous function, Notification, none (synchronous function)}

    @return: dbg_null if no running request
    """
    return _ida_dbg.get_running_notification(*args)

def clear_requests_queue(*args):
    r"""
    clear_requests_queue()
    Clear the queue of waiting requests. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}
    @note: If a request is currently running, this one isn't stopped.
    """
    return _ida_dbg.clear_requests_queue(*args)

def get_process_state(*args):
    r"""
    get_process_state() -> int
    Return the state of the currently debugged process. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @return: one of Debugged process states
    """
    return _ida_dbg.get_process_state(*args)
DSTATE_SUSP = _ida_dbg.DSTATE_SUSP
r"""
process is suspended and will not continue
"""

DSTATE_NOTASK = _ida_dbg.DSTATE_NOTASK
r"""
no process is currently debugged
"""

DSTATE_RUN = _ida_dbg.DSTATE_RUN
r"""
process is running
"""

DBGINV_MEMORY = _ida_dbg.DBGINV_MEMORY
r"""
invalidate cached memory contents
"""

DBGINV_MEMCFG = _ida_dbg.DBGINV_MEMCFG
r"""
invalidate cached process segmentation
"""

DBGINV_REGS = _ida_dbg.DBGINV_REGS
r"""
invalidate cached register values
"""

DBGINV_ALL = _ida_dbg.DBGINV_ALL
r"""
invalidate everything
"""

DBGINV_REDRAW = _ida_dbg.DBGINV_REDRAW
r"""
refresh the screen
"""

DBGINV_NONE = _ida_dbg.DBGINV_NONE
r"""
invalidate nothing
"""


def set_process_state(*args):
    r"""
    set_process_state(newstate, p_thid, dbginv) -> int
    Set new state for the debugged process. Notifies the IDA kernel about the change
    of the debugged process state. For example, a debugger module could call this
    function when it knows that the process is suspended for a short period of time.
    Some IDA API calls can be made only when the process is suspended. The process
    state is usually restored before returning control to the caller. You must know
    that it is ok to change the process state, doing it at arbitrary moments may
    crash the application or IDA. \sq{Type, Synchronous function, Notification, none
    (synchronous function)}

    @param newstate: (C++: int) new process state (one of Debugged process states) if
                     DSTATE_NOTASK is passed then the state is not changed
    @param p_thid: (C++: thid_t *) ptr to new thread id. may be nullptr or pointer to NO_THREAD. the
                   pointed variable will contain the old thread id upon return
    @param dbginv: (C++: int) Debugged process invalidation options
    @return: old debugger state (one of Debugged process states)
    """
    return _ida_dbg.set_process_state(*args)

def invalidate_dbg_state(*args):
    r"""
    invalidate_dbg_state(dbginv) -> int
    Invalidate cached debugger information. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param dbginv: (C++: int) Debugged process invalidation options
    @return: current debugger state (one of Debugged process states)
    """
    return _ida_dbg.invalidate_dbg_state(*args)

def start_process(*args):
    r"""
    start_process(path=None, args=None, sdir=None) -> int
    Start a process in the debugger. \sq{Type, Asynchronous function - available as
    Request, Notification, dbg_process_start}
    @note: You can also use the run_to() function to easily start the execution of a
           process until a given address is reached.
    @note: For all parameters, a nullptr value indicates the debugger will take the
           value from the defined Process Options.

    @param path: (C++: const char *) path to the executable to start
    @param args: (C++: const char *) arguments to pass to process
    @param sdir: (C++: const char *) starting directory for the process
    @retval -1: impossible to create the process
    @retval 0: the starting of the process was cancelled by the user
    @retval 1: the process was properly started
    """
    return _ida_dbg.start_process(*args)

def request_start_process(*args):
    r"""
    request_start_process(path=None, args=None, sdir=None) -> int
    Post a start_process() request.

    @param path: (C++: const char *) char const *
    @param args: (C++: const char *) char const *
    @param sdir: (C++: const char *) char const *
    """
    return _ida_dbg.request_start_process(*args)

def suspend_process(*args):
    r"""
    suspend_process() -> bool
    Suspend the process in the debugger. \sq{ Type,
    * Synchronous function (if in a notification handler)
    * Asynchronous function (everywhere else)
    * available as Request, Notification,
    * none (if in a notification handler)
    * dbg_suspend_process (everywhere else) }
    @note: The suspend_process() function can be called from a notification handler
           to force the stopping of the process. In this case, no notification will
           be generated. When you suspend a process, the running command is always
           aborted.
    """
    return _ida_dbg.suspend_process(*args)

def request_suspend_process(*args):
    r"""
    request_suspend_process() -> bool
    Post a suspend_process() request.
    """
    return _ida_dbg.request_suspend_process(*args)

def continue_process(*args):
    r"""
    continue_process() -> bool
    Continue the execution of the process in the debugger. \sq{Type, Synchronous
    function - available as Request, Notification, none (synchronous function)}
    @note: The continue_process() function can be called from a notification handler
           to force the continuation of the process. In this case the request queue
           will not be examined, IDA will simply resume execution. Usually it makes
           sense to call request_continue_process() followed by run_requests(), so
           that IDA will first start a queued request (if any) and then resume the
           application.
    """
    return _ida_dbg.continue_process(*args)

def request_continue_process(*args):
    r"""
    request_continue_process() -> bool
    Post a continue_process() request.
    @note: This requires an explicit call to run_requests()
    """
    return _ida_dbg.request_continue_process(*args)

def exit_process(*args):
    r"""
    exit_process() -> bool
    Terminate the debugging of the current process. \sq{Type, Asynchronous function
    - available as Request, Notification, dbg_process_exit}
    """
    return _ida_dbg.exit_process(*args)

def request_exit_process(*args):
    r"""
    request_exit_process() -> bool
    Post an exit_process() request.
    """
    return _ida_dbg.request_exit_process(*args)

def get_processes(*args):
    r"""
    get_processes(proclist) -> ssize_t
    Take a snapshot of running processes and return their description. \sq{Type,
    Synchronous function, Notification, none (synchronous function)}

    @param proclist: (C++: procinfo_vec_t *)
    @return: number of processes or -1 on error
    """
    return _ida_dbg.get_processes(*args)

def attach_process(*args):
    r"""
    attach_process(pid=pid_t(-1), event_id=-1) -> int
    Attach the debugger to a running process. \sq{Type, Asynchronous function -
    available as Request, Notification, dbg_process_attach}
    @note: This function shouldn't be called as a request if NO_PROCESS is used.

    @param pid: (C++: pid_t) PID of the process to attach to. If NO_PROCESS, a dialog box will
                interactively ask the user for the process to attach to.
    @retval -4: debugger was not inited
    @retval -3: the attaching is not supported
    @retval -2: impossible to find a compatible process
    @retval -1: impossible to attach to the given process (process died, privilege
                needed, not supported by the debugger plugin, ...)
    @retval 0: the user cancelled the attaching to the process
    @retval 1: the debugger properly attached to the process
    """
    return _ida_dbg.attach_process(*args)

def request_attach_process(*args):
    r"""
    request_attach_process(pid, event_id) -> int
    Post an attach_process() request.

    @param pid: (C++: pid_t)
    @param event_id: (C++: int)
    """
    return _ida_dbg.request_attach_process(*args)

def detach_process(*args):
    r"""
    detach_process() -> bool
    Detach the debugger from the debugged process. \sq{Type, Asynchronous function -
    available as Request, Notification, dbg_process_detach}
    """
    return _ida_dbg.detach_process(*args)

def request_detach_process(*args):
    r"""
    request_detach_process() -> bool
    Post a detach_process() request.
    """
    return _ida_dbg.request_detach_process(*args)

def is_debugger_busy(*args):
    r"""
    is_debugger_busy() -> bool
    Is the debugger busy?. Some debuggers do not accept any commands while the
    debugged application is running. For such a debugger, it is unsafe to do
    anything with the database (even simple queries like get_byte may lead to
    undesired consequences). Returns: true if the debugged application is running
    under such a debugger
    """
    return _ida_dbg.is_debugger_busy(*args)

def get_thread_qty(*args):
    r"""
    get_thread_qty() -> int
    Get number of threads. \sq{Type, Synchronous function, Notification, none
    (synchronous function)}
    """
    return _ida_dbg.get_thread_qty(*args)

def getn_thread(*args):
    r"""
    getn_thread(n) -> thid_t
    Get the ID of a thread. \sq{Type, Synchronous function, Notification, none
    (synchronous function)}

    @param n: (C++: int) number of thread, is in range 0..get_thread_qty()-1
    @return: NO_THREAD if the thread doesn't exist.
    """
    return _ida_dbg.getn_thread(*args)

def get_current_thread(*args):
    r"""
    get_current_thread() -> thid_t
    Get current thread ID. \sq{Type, Synchronous function, Notification, none
    (synchronous function)}
    """
    return _ida_dbg.get_current_thread(*args)

def getn_thread_name(*args):
    r"""
    getn_thread_name(n) -> char const *
    Get the NAME of a thread \sq{Type, Synchronous function, Notification, none
    (synchronous function)}

    @param n: (C++: int) number of thread, is in range 0..get_thread_qty()-1 or -1 for the
              current thread
    @return: thread name or nullptr if the thread doesn't exist.
    """
    return _ida_dbg.getn_thread_name(*args)

def select_thread(*args):
    r"""
    select_thread(tid) -> bool
    Select the given thread as the current debugged thread. All thread related
    execution functions will work on this thread. The process must be suspended to
    select a new thread. \sq{Type, Synchronous function - available as request,
    Notification, none (synchronous function)}

    @param tid: (C++: thid_t) ID of the thread to select
    @return: false if the thread doesn't exist.
    """
    return _ida_dbg.select_thread(*args)

def request_select_thread(*args):
    r"""
    request_select_thread(tid) -> bool
    Post a select_thread() request.

    @param tid: (C++: thid_t)
    """
    return _ida_dbg.request_select_thread(*args)

def suspend_thread(*args):
    r"""
    suspend_thread(tid) -> int
    Suspend thread. Suspending a thread may deadlock the whole application if the
    suspended was owning some synchronization objects. \sq{Type, Synchronous
    function - available as request, Notification, none (synchronous function)}

    @param tid: (C++: thid_t) thread id
    @retval -1: network error
    @retval 0: failed
    @retval 1: ok
    """
    return _ida_dbg.suspend_thread(*args)

def request_suspend_thread(*args):
    r"""
    request_suspend_thread(tid) -> int
    Post a suspend_thread() request.

    @param tid: (C++: thid_t)
    """
    return _ida_dbg.request_suspend_thread(*args)

def resume_thread(*args):
    r"""
    resume_thread(tid) -> int
    Resume thread. \sq{Type, Synchronous function - available as request,
    Notification, none (synchronous function)}

    @param tid: (C++: thid_t) thread id
    @retval -1: network error
    @retval 0: failed
    @retval 1: ok
    """
    return _ida_dbg.resume_thread(*args)

def request_resume_thread(*args):
    r"""
    request_resume_thread(tid) -> int
    Post a resume_thread() request.

    @param tid: (C++: thid_t)
    """
    return _ida_dbg.request_resume_thread(*args)

def get_first_module(*args):
    r"""
    get_first_module(modinfo) -> bool

    @param modinfo: modinfo_t *
    """
    return _ida_dbg.get_first_module(*args)

def get_next_module(*args):
    r"""
    get_next_module(modinfo) -> bool

    @param modinfo: modinfo_t *
    """
    return _ida_dbg.get_next_module(*args)

def step_into(*args):
    r"""
    step_into() -> bool
    Execute one instruction in the current thread. Other threads are kept suspended.
    \sq{Type, Asynchronous function - available as Request, Notification,
    dbg_step_into}
    """
    return _ida_dbg.step_into(*args)

def request_step_into(*args):
    r"""
    request_step_into() -> bool
    Post a step_into() request.
    """
    return _ida_dbg.request_step_into(*args)

def step_over(*args):
    r"""
    step_over() -> bool
    Execute one instruction in the current thread, but without entering into
    functions. Others threads keep suspended. \sq{Type, Asynchronous function -
    available as Request, Notification, dbg_step_over}
    """
    return _ida_dbg.step_over(*args)

def request_step_over(*args):
    r"""
    request_step_over() -> bool
    Post a step_over() request.
    """
    return _ida_dbg.request_step_over(*args)

def step_until_ret(*args):
    r"""
    step_until_ret() -> bool
    Execute instructions in the current thread until a function return instruction
    is executed (aka "step out"). Other threads are kept suspended. \sq{Type,
    Asynchronous function - available as Request, Notification, dbg_step_until_ret}
    """
    return _ida_dbg.step_until_ret(*args)

def request_step_until_ret(*args):
    r"""
    request_step_until_ret() -> bool
    Post a step_until_ret() request.
    """
    return _ida_dbg.request_step_until_ret(*args)

def set_resume_mode(*args):
    r"""
    set_resume_mode(tid, mode) -> bool
    How to resume the application. Set resume mode but do not resume process.

    @param tid: (C++: thid_t)
    @param mode: (C++: resume_mode_t) enum resume_mode_t
    """
    return _ida_dbg.set_resume_mode(*args)

def request_set_resume_mode(*args):
    r"""
    request_set_resume_mode(tid, mode) -> bool
    Post a set_resume_mode() request.

    @param tid: (C++: thid_t)
    @param mode: (C++: resume_mode_t) enum resume_mode_t
    """
    return _ida_dbg.request_set_resume_mode(*args)

def get_dbg_reg_info(*args):
    r"""
    get_dbg_reg_info(regname, ri) -> bool
    Get register information \sq{Type, Synchronous function, Notification, none
    (synchronous function)}

    @param regname: (C++: const char *) char const *
    @param ri: (C++: register_info_t *)
    """
    return _ida_dbg.get_dbg_reg_info(*args)

def get_sp_val(*args):
    r"""
    get_sp_val() -> bool
    Get value of the SP register for the current thread. Requires a suspended
    debugger.
    """
    return _ida_dbg.get_sp_val(*args)

def get_ip_val(*args):
    r"""
    get_ip_val() -> bool
    Get value of the IP (program counter) register for the current thread. Requires
    a suspended debugger.
    """
    return _ida_dbg.get_ip_val(*args)

def is_reg_integer(*args):
    r"""
    is_reg_integer(regname) -> bool
    Does a register contain an integer value? \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param regname: (C++: const char *) char const *
    """
    return _ida_dbg.is_reg_integer(*args)

def is_reg_float(*args):
    r"""
    is_reg_float(regname) -> bool
    Does a register contain a floating point value? \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param regname: (C++: const char *) char const *
    """
    return _ida_dbg.is_reg_float(*args)

def is_reg_custom(*args):
    r"""
    is_reg_custom(regname) -> bool
    Does a register contain a value of a custom data type? \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param regname: (C++: const char *) char const *
    """
    return _ida_dbg.is_reg_custom(*args)

def set_bptloc_string(*args):
    r"""
    set_bptloc_string(s) -> int

    @param s: char const *
    """
    return _ida_dbg.set_bptloc_string(*args)

def get_bptloc_string(*args):
    r"""
    get_bptloc_string(i) -> char const *

    @param i: int
    """
    return _ida_dbg.get_bptloc_string(*args)
MOVBPT_OK = _ida_dbg.MOVBPT_OK

MOVBPT_NOT_FOUND = _ida_dbg.MOVBPT_NOT_FOUND

MOVBPT_DEST_BUSY = _ida_dbg.MOVBPT_DEST_BUSY

MOVBPT_BAD_TYPE = _ida_dbg.MOVBPT_BAD_TYPE

class bptaddrs_t(object):
    r"""
    Proxy of C++ bptaddrs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    bpt = property(_ida_dbg.bptaddrs_t_bpt_get, _ida_dbg.bptaddrs_t_bpt_set, doc=r"""bpt""")

    def __init__(self, *args):
        r"""
        __init__(self) -> bptaddrs_t
        """
        _ida_dbg.bptaddrs_t_swiginit(self, _ida_dbg.new_bptaddrs_t(*args))
    __swig_destroy__ = _ida_dbg.delete_bptaddrs_t

# Register bptaddrs_t in _ida_dbg:
_ida_dbg.bptaddrs_t_swigregister(bptaddrs_t)

BPLT_ABS = _ida_dbg.BPLT_ABS
r"""
absolute address: ea
"""

BPLT_REL = _ida_dbg.BPLT_REL
r"""
relative address: module_path, offset
"""

BPLT_SYM = _ida_dbg.BPLT_SYM

BPLT_SRC = _ida_dbg.BPLT_SRC
r"""
source level: filename, lineno
"""

class bpt_location_t(object):
    r"""
    Proxy of C++ bpt_location_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    info = property(_ida_dbg.bpt_location_t_info_get, _ida_dbg.bpt_location_t_info_set, doc=r"""info""")
    index = property(_ida_dbg.bpt_location_t_index_get, _ida_dbg.bpt_location_t_index_set, doc=r"""index""")
    loctype = property(_ida_dbg.bpt_location_t_loctype_get, _ida_dbg.bpt_location_t_loctype_set, doc=r"""loctype""")

    def type(self, *args):
        r"""
        type(self) -> bpt_loctype_t
        Get bpt type.
        """
        return _ida_dbg.bpt_location_t_type(self, *args)

    def is_empty_path(self, *args):
        r"""
        is_empty_path(self) -> bool
        No path/filename specified? (BPLT_REL, BPLT_SRC)
        """
        return _ida_dbg.bpt_location_t_is_empty_path(self, *args)

    def path(self, *args):
        r"""
        path(self) -> char const *
        Get path/filename (BPLT_REL, BPLT_SRC)
        """
        return _ida_dbg.bpt_location_t_path(self, *args)

    def symbol(self, *args):
        r"""
        symbol(self) -> char const *
        Get symbol name (BPLT_SYM)
        """
        return _ida_dbg.bpt_location_t_symbol(self, *args)

    def lineno(self, *args):
        r"""
        lineno(self) -> int
        Get line number (BPLT_SRC)
        """
        return _ida_dbg.bpt_location_t_lineno(self, *args)

    def offset(self, *args):
        r"""
        offset(self) -> uval_t
        Get offset (BPLT_REL, BPLT_SYM)
        """
        return _ida_dbg.bpt_location_t_offset(self, *args)

    def ea(self, *args):
        r"""
        ea(self) -> ea_t
        Get address (BPLT_ABS)
        """
        return _ida_dbg.bpt_location_t_ea(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> bpt_location_t
        """
        _ida_dbg.bpt_location_t_swiginit(self, _ida_dbg.new_bpt_location_t(*args))

    def set_abs_bpt(self, *args):
        r"""
        set_abs_bpt(self, a)
        Specify an absolute address location.

        @param a: (C++: ea_t)
        """
        return _ida_dbg.bpt_location_t_set_abs_bpt(self, *args)

    def set_src_bpt(self, *args):
        r"""
        set_src_bpt(self, fn, _lineno)
        Specify a source level location.

        @param fn: (C++: const char *) char const *
        @param _lineno: (C++: int)
        """
        return _ida_dbg.bpt_location_t_set_src_bpt(self, *args)

    def set_sym_bpt(self, *args):
        r"""
        set_sym_bpt(self, _symbol, _offset=0)
        Specify a symbolic location.

        @param _symbol: (C++: const char *) char const *
        @param _offset: (C++: uval_t)
        """
        return _ida_dbg.bpt_location_t_set_sym_bpt(self, *args)

    def set_rel_bpt(self, *args):
        r"""
        set_rel_bpt(self, mod, _offset)
        Specify a relative address location.

        @param mod: (C++: const char *) char const *
        @param _offset: (C++: uval_t)
        """
        return _ida_dbg.bpt_location_t_set_rel_bpt(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int
        Lexically compare two breakpoint locations. Bpt locations are first compared
        based on type (i.e. BPLT_ABS < BPLT_REL). BPLT_ABS locations are compared based
        on their ea values. For all other location types, locations are first compared
        based on their string (path/filename/symbol), then their offset/lineno.

        @param r: (C++: const bpt_location_t &) bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t_compare(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: bpt_location_t const &
        """
        return _ida_dbg.bpt_location_t___ge__(self, *args)
    __swig_destroy__ = _ida_dbg.delete_bpt_location_t

# Register bpt_location_t in _ida_dbg:
_ida_dbg.bpt_location_t_swigregister(bpt_location_t)

class bpt_t(object):
    r"""
    Proxy of C++ bpt_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    cb = property(_ida_dbg.bpt_t_cb_get, _ida_dbg.bpt_t_cb_set, doc=r"""cb""")
    r"""
    size of this structure
    """
    loc = property(_ida_dbg.bpt_t_loc_get, _ida_dbg.bpt_t_loc_set, doc=r"""loc""")
    r"""
    Location.
    """
    pid = property(_ida_dbg.bpt_t_pid_get, _ida_dbg.bpt_t_pid_set, doc=r"""pid""")
    r"""
    breakpoint process id
    """
    tid = property(_ida_dbg.bpt_t_tid_get, _ida_dbg.bpt_t_tid_set, doc=r"""tid""")
    r"""
    breakpoint thread id
    """
    ea = property(_ida_dbg.bpt_t_ea_get, _ida_dbg.bpt_t_ea_set, doc=r"""ea""")
    r"""
    Address, if known. For BPLT_SRC, index into an internal data struct.
    """
    type = property(_ida_dbg.bpt_t_type_get, _ida_dbg.bpt_t_type_set, doc=r"""type""")
    r"""
    Breakpoint type.
    """
    pass_count = property(_ida_dbg.bpt_t_pass_count_get, _ida_dbg.bpt_t_pass_count_set, doc=r"""pass_count""")
    r"""
    Number of times the breakpoint is hit before stopping (default is 0: stop
    always)
    """
    flags = property(_ida_dbg.bpt_t_flags_get, _ida_dbg.bpt_t_flags_set, doc=r"""flags""")
    r"""
    Breakpoint property bits
    """
    props = property(_ida_dbg.bpt_t_props_get, _ida_dbg.bpt_t_props_set, doc=r"""props""")
    r"""
    Internal breakpoint properties
    """
    size = property(_ida_dbg.bpt_t_size_get, _ida_dbg.bpt_t_size_set, doc=r"""size""")
    r"""
    Size of the breakpoint (0 for software breakpoints)
    """
    cndidx = property(_ida_dbg.bpt_t_cndidx_get, _ida_dbg.bpt_t_cndidx_set, doc=r"""cndidx""")
    r"""
    Internal number of the condition (<0-none)
    """
    bptid = property(_ida_dbg.bpt_t_bptid_get, _ida_dbg.bpt_t_bptid_set, doc=r"""bptid""")
    r"""
    Internal breakpoint id.
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> bpt_t
        """
        _ida_dbg.bpt_t_swiginit(self, _ida_dbg.new_bpt_t(*args))

    def is_hwbpt(self, *args):
        r"""
        is_hwbpt(self) -> bool
        Is hardware breakpoint?
        """
        return _ida_dbg.bpt_t_is_hwbpt(self, *args)

    def enabled(self, *args):
        r"""
        enabled(self) -> bool
        Is breakpoint enabled?
        """
        return _ida_dbg.bpt_t_enabled(self, *args)

    def is_low_level(self, *args):
        r"""
        is_low_level(self) -> bool
        Is bpt condition calculated at low level?
        """
        return _ida_dbg.bpt_t_is_low_level(self, *args)

    def badbpt(self, *args):
        r"""
        badbpt(self) -> bool
        Failed to write bpt to process memory?
        """
        return _ida_dbg.bpt_t_badbpt(self, *args)

    def listbpt(self, *args):
        r"""
        listbpt(self) -> bool
        Include in the bpt list?
        """
        return _ida_dbg.bpt_t_listbpt(self, *args)

    def is_compiled(self, *args):
        r"""
        is_compiled(self) -> bool
        Condition has been compiled?
        """
        return _ida_dbg.bpt_t_is_compiled(self, *args)

    def is_active(self, *args):
        r"""
        is_active(self) -> bool
        Written completely to process?
        """
        return _ida_dbg.bpt_t_is_active(self, *args)

    def is_partially_active(self, *args):
        r"""
        is_partially_active(self) -> bool
        Written partially to process?
        """
        return _ida_dbg.bpt_t_is_partially_active(self, *args)

    def is_inactive(self, *args):
        r"""
        is_inactive(self) -> bool
        Not written to process at all?
        """
        return _ida_dbg.bpt_t_is_inactive(self, *args)

    def is_page_bpt(self, *args):
        r"""
        is_page_bpt(self) -> bool
        Page breakpoint?
        """
        return _ida_dbg.bpt_t_is_page_bpt(self, *args)

    def get_size(self, *args):
        r"""
        get_size(self) -> int
        Get bpt size.
        """
        return _ida_dbg.bpt_t_get_size(self, *args)

    def set_abs_bpt(self, *args):
        r"""
        set_abs_bpt(self, a)
        Set bpt location to an absolute address.

        @param a: (C++: ea_t)
        """
        return _ida_dbg.bpt_t_set_abs_bpt(self, *args)

    def set_src_bpt(self, *args):
        r"""
        set_src_bpt(self, fn, lineno)
        Set bpt location to a source line.

        @param fn: (C++: const char *) char const *
        @param lineno: (C++: int)
        """
        return _ida_dbg.bpt_t_set_src_bpt(self, *args)

    def set_sym_bpt(self, *args):
        r"""
        set_sym_bpt(self, sym, o)
        Set bpt location to a symbol.

        @param sym: (C++: const char *) char const *
        @param o: (C++: uval_t)
        """
        return _ida_dbg.bpt_t_set_sym_bpt(self, *args)

    def set_rel_bpt(self, *args):
        r"""
        set_rel_bpt(self, mod, o)
        Set bpt location to a relative address.

        @param mod: (C++: const char *) char const *
        @param o: (C++: uval_t)
        """
        return _ida_dbg.bpt_t_set_rel_bpt(self, *args)

    def is_absbpt(self, *args):
        r"""
        is_absbpt(self) -> bool
        Is absolute address breakpoint?
        """
        return _ida_dbg.bpt_t_is_absbpt(self, *args)

    def is_relbpt(self, *args):
        r"""
        is_relbpt(self) -> bool
        Is relative address breakpoint?
        """
        return _ida_dbg.bpt_t_is_relbpt(self, *args)

    def is_symbpt(self, *args):
        r"""
        is_symbpt(self) -> bool
        Is symbolic breakpoint?
        """
        return _ida_dbg.bpt_t_is_symbpt(self, *args)

    def is_srcbpt(self, *args):
        r"""
        is_srcbpt(self) -> bool
        Is source level breakpoint?
        """
        return _ida_dbg.bpt_t_is_srcbpt(self, *args)

    def is_tracemodebpt(self, *args):
        r"""
        is_tracemodebpt(self) -> bool
        Does breakpoint trace anything?
        """
        return _ida_dbg.bpt_t_is_tracemodebpt(self, *args)

    def is_traceonbpt(self, *args):
        r"""
        is_traceonbpt(self) -> bool
        Is this a tracing breakpoint, and is tracing enabled?
        """
        return _ida_dbg.bpt_t_is_traceonbpt(self, *args)

    def is_traceoffbpt(self, *args):
        r"""
        is_traceoffbpt(self) -> bool
        Is this a tracing breakpoint, and is tracing disabled?
        """
        return _ida_dbg.bpt_t_is_traceoffbpt(self, *args)

    def set_trace_action(self, *args):
        r"""
        set_trace_action(self, enable, trace_types) -> bool
        Configure tracing options.

        @param enable: (C++: bool)
        @param trace_types: (C++: int)
        """
        return _ida_dbg.bpt_t_set_trace_action(self, *args)

    def get_cnd_elang_idx(self, *args):
        r"""
        get_cnd_elang_idx(self) -> size_t
        """
        return _ida_dbg.bpt_t_get_cnd_elang_idx(self, *args)
    condition = property(_ida_dbg.bpt_t_condition_get, _ida_dbg.bpt_t_condition_set, doc=r"""condition""")
    elang = property(_ida_dbg.bpt_t_elang_get, _ida_dbg.bpt_t_elang_set, doc=r"""elang""")
    __swig_destroy__ = _ida_dbg.delete_bpt_t

# Register bpt_t in _ida_dbg:
_ida_dbg.bpt_t_swigregister(bpt_t)
BPT_BRK = _ida_dbg.BPT_BRK
r"""
suspend execution upon hit
"""

BPT_TRACE = _ida_dbg.BPT_TRACE
r"""
add trace information upon hit
"""

BPT_UPDMEM = _ida_dbg.BPT_UPDMEM
r"""
refresh the memory layout and contents before evaluating bpt condition
"""

BPT_ENABLED = _ida_dbg.BPT_ENABLED
r"""
enabled?
"""

BPT_LOWCND = _ida_dbg.BPT_LOWCND
r"""
condition is calculated at low level (on the server side)
"""

BPT_TRACEON = _ida_dbg.BPT_TRACEON
r"""
enable tracing when the breakpoint is reached
"""

BPT_TRACE_INSN = _ida_dbg.BPT_TRACE_INSN
r"""
instruction tracing
"""

BPT_TRACE_FUNC = _ida_dbg.BPT_TRACE_FUNC
r"""
function tracing
"""

BPT_TRACE_BBLK = _ida_dbg.BPT_TRACE_BBLK
r"""
basic block tracing
"""

BPT_TRACE_TYPES = _ida_dbg.BPT_TRACE_TYPES
r"""
trace insns, functions, and basic blocks. if any of BPT_TRACE_TYPES bits are set
but BPT_TRACEON is clear, then turn off tracing for the specified trace types
"""

BPT_ELANG_MASK = _ida_dbg.BPT_ELANG_MASK

BPT_ELANG_SHIFT = _ida_dbg.BPT_ELANG_SHIFT
r"""
index of the extlang (scripting language) of the condition
"""

BKPT_BADBPT = _ida_dbg.BKPT_BADBPT
r"""
failed to write the bpt to the process memory (at least one location)
"""

BKPT_LISTBPT = _ida_dbg.BKPT_LISTBPT
r"""
include in bpt list (user-defined bpt)
"""

BKPT_TRACE = _ida_dbg.BKPT_TRACE
r"""
trace bpt; should not be deleted when the process gets suspended
"""

BKPT_ACTIVE = _ida_dbg.BKPT_ACTIVE
r"""
active?
"""

BKPT_PARTIAL = _ida_dbg.BKPT_PARTIAL
r"""
partially active? (some locations were not written yet)
"""

BKPT_CNDREADY = _ida_dbg.BKPT_CNDREADY
r"""
condition has been compiled
"""

BKPT_FAKEPEND = _ida_dbg.BKPT_FAKEPEND
r"""
fake pending bpt: it is inactive but another bpt of the same type is active at
the same address(es)
"""

BKPT_PAGE = _ida_dbg.BKPT_PAGE
r"""
written to the process as a page bpt. Available only after writing the bpt to
the process.
"""



def get_bpt_qty(*args):
    r"""
    get_bpt_qty() -> int
    Get number of breakpoints. \sq{Type, Synchronous function, Notification, none
    (synchronous function)}
    """
    return _ida_dbg.get_bpt_qty(*args)

def getn_bpt(*args):
    r"""
    getn_bpt(n, bpt) -> bool
    Get the characteristics of a breakpoint. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param n: (C++: int) number of breakpoint, is in range 0..get_bpt_qty()-1
    @param bpt: (C++: bpt_t *) filled with the characteristics.
    @return: false if no breakpoint exists
    """
    return _ida_dbg.getn_bpt(*args)

def get_bpt(*args):
    r"""
    get_bpt(ea, bpt) -> bool
    Get the characteristics of a breakpoint. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param ea: (C++: ea_t) any address in the breakpoint range
    @param bpt: (C++: bpt_t *) if not nullptr, is filled with the characteristics.
    @return: false if no breakpoint exists
    """
    return _ida_dbg.get_bpt(*args)

def exist_bpt(*args):
    r"""
    exist_bpt(ea) -> bool
    Does a breakpoint exist at the given location?

    @param ea: (C++: ea_t)
    """
    return _ida_dbg.exist_bpt(*args)

def add_bpt(*args):
    r"""
    add_bpt(ea, size=0, type=BPT_DEFAULT) -> bool
    Add a new breakpoint in the debugged process. \sq{Type, Synchronous function -
    available as request, Notification, none (synchronous function)}

    @param bpt: (C++: const bpt_t &) Breakpoint to add. It describes the break condition, type, flags,
                location (module relative, source breakpoint or absolute) and other
                attributes.
    @param size: asize_t
    @param type: bpttype_t

    add_bpt(bpt) -> bool

    @param bpt: bpt_t const &
    """
    return _ida_dbg.add_bpt(*args)

def request_add_bpt(*args):
    r"""
    request_add_bpt(ea, size=0, type=BPT_DEFAULT) -> bool
    Post an add_bpt(const bpt_t &) request.

    @param ea: ea_t
    @param size: asize_t
    @param type: bpttype_t

    request_add_bpt(bpt) -> bool

    @param bpt: bpt_t const &
    """
    return _ida_dbg.request_add_bpt(*args)

def del_bpt(*args):
    r"""
    del_bpt(ea) -> bool
    Delete an existing breakpoint in the debugged process. \sq{Type, Synchronous
    function - available as request, Notification, none (synchronous function)}

    @param bptloc: (C++: const bpt_location_t &) Breakpoint location
    del_bpt(bptloc) -> bool

    @param bptloc: bpt_location_t const &
    """
    return _ida_dbg.del_bpt(*args)

def request_del_bpt(*args):
    r"""
    request_del_bpt(ea) -> bool
    Post a del_bpt(const bpt_location_t &) request.

    @param ea: ea_t

    request_del_bpt(bptloc) -> bool

    @param bptloc: bpt_location_t const &
    """
    return _ida_dbg.request_del_bpt(*args)

def update_bpt(*args):
    r"""
    update_bpt(bpt) -> bool
    Update modifiable characteristics of an existing breakpoint. To update the
    breakpoint location, use change_bptlocs() \sq{Type, Synchronous function,
    Notification, none (synchronous function)}
    @note: Only the following fields can be modified:
    * bpt_t::cndbody
    * bpt_t::pass_count
    * bpt_t::flags
    * bpt_t::size
    * bpt_t::type
    @note: Changing some properties will require removing and then re-adding the
           breakpoint to the process memory (or the debugger backend), which can
           lead to race conditions (i.e., breakpoint(s) can be missed) in case the
           process is not suspended. Here are a list of scenarios that will require
           the breakpoint to be removed & then re-added:
    * bpt_t::size is modified
    * bpt_t::type is modified
    * bpt_t::flags's BPT_ENABLED is modified
    * bpt_t::flags's BPT_LOWCND is changed
    * bpt_t::flags's BPT_LOWCND remains set, but cndbody changed

    @param bpt: (C++: const bpt_t *) bpt_t const *
    """
    return _ida_dbg.update_bpt(*args)

def find_bpt(*args):
    r"""
    find_bpt(bptloc, bpt) -> bool
    Find a breakpoint by location. \sq{Type, Synchronous function - available as
    request, Notification, none (synchronous function)}

    @param bptloc: (C++: const bpt_location_t &) Breakpoint location
    @param bpt: (C++: bpt_t *) bpt is filled if the breakpoint was found
    """
    return _ida_dbg.find_bpt(*args)

def enable_bpt(*args):
    r"""
    enable_bpt(ea, enable=True) -> bool

    @param ea: ea_t
    @param enable: bool

    enable_bpt(bptloc, enable=True) -> bool

    @param bptloc: bpt_location_t const &
    @param enable: bool
    """
    return _ida_dbg.enable_bpt(*args)

def disable_bpt(*args):
    r"""
    disable_bpt(ea) -> bool

    @param ea: ea_t

    disable_bpt(bptloc) -> bool

    @param bptloc: bpt_location_t const &
    """
    return _ida_dbg.disable_bpt(*args)

def request_enable_bpt(*args):
    r"""
    request_enable_bpt(ea, enable=True) -> bool

    @param ea: ea_t
    @param enable: bool

    request_enable_bpt(bptloc, enable=True) -> bool

    @param bptloc: bpt_location_t const &
    @param enable: bool
    """
    return _ida_dbg.request_enable_bpt(*args)

def request_disable_bpt(*args):
    r"""
    request_disable_bpt(ea) -> bool

    @param ea: ea_t

    request_disable_bpt(bptloc) -> bool

    @param bptloc: bpt_location_t const &
    """
    return _ida_dbg.request_disable_bpt(*args)

def check_bpt(*args):
    r"""
    check_bpt(ea) -> int
    Check the breakpoint at the specified address.

    @param ea: (C++: ea_t)
    @return: one of Breakpoint status codes
    """
    return _ida_dbg.check_bpt(*args)
BPTCK_NONE = _ida_dbg.BPTCK_NONE
r"""
breakpoint does not exist
"""

BPTCK_NO = _ida_dbg.BPTCK_NO
r"""
breakpoint is disabled
"""

BPTCK_YES = _ida_dbg.BPTCK_YES
r"""
breakpoint is enabled
"""

BPTCK_ACT = _ida_dbg.BPTCK_ACT
r"""
breakpoint is active (written to the process)
"""


def set_trace_size(*args):
    r"""
    set_trace_size(size) -> bool
    Specify the new size of the circular buffer. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param size: (C++: int) if 0, buffer isn't circular and events are never removed. If the
                 new size is smaller than the existing number of trace events, a
                 corresponding number of trace events are removed.
    @note: If you specify 0, all available memory can be quickly used !!!
    """
    return _ida_dbg.set_trace_size(*args)

def clear_trace(*args):
    r"""
    clear_trace()
    Clear all events in the trace buffer. \sq{Type, Synchronous function - available
    as request, Notification, none (synchronous function)}
    """
    return _ida_dbg.clear_trace(*args)

def request_clear_trace(*args):
    r"""
    request_clear_trace()
    Post a clear_trace() request.
    """
    return _ida_dbg.request_clear_trace(*args)

def is_step_trace_enabled(*args):
    r"""
    is_step_trace_enabled() -> bool
    Get current state of step tracing. \sq{Type, Synchronous function, Notification,
    none (synchronous function)}
    """
    return _ida_dbg.is_step_trace_enabled(*args)

def enable_step_trace(*args):
    r"""
    enable_step_trace(enable=1) -> bool

    @param enable: int
    """
    return _ida_dbg.enable_step_trace(*args)

def disable_step_trace(*args):
    r"""
    disable_step_trace() -> bool
    """
    return _ida_dbg.disable_step_trace(*args)

def request_enable_step_trace(*args):
    r"""
    request_enable_step_trace(enable=1) -> bool

    @param enable: int
    """
    return _ida_dbg.request_enable_step_trace(*args)

def request_disable_step_trace(*args):
    r"""
    request_disable_step_trace() -> bool
    """
    return _ida_dbg.request_disable_step_trace(*args)
ST_OVER_DEBUG_SEG = _ida_dbg.ST_OVER_DEBUG_SEG
r"""
step tracing will be disabled when IP is in a debugger segment
"""

ST_OVER_LIB_FUNC = _ida_dbg.ST_OVER_LIB_FUNC
r"""
step tracing will be disabled when IP is in a library function
"""

ST_ALREADY_LOGGED = _ida_dbg.ST_ALREADY_LOGGED
r"""
step tracing will be disabled when IP is already logged
"""

ST_SKIP_LOOPS = _ida_dbg.ST_SKIP_LOOPS
r"""
step tracing will try to skip loops already recorded
"""

ST_DIFFERENTIAL = _ida_dbg.ST_DIFFERENTIAL

ST_OPTIONS_MASK = _ida_dbg.ST_OPTIONS_MASK
r"""
mask of available options, to ensure compatibility with newer IDA versions
"""

ST_OPTIONS_DEFAULT = _ida_dbg.ST_OPTIONS_DEFAULT

IT_LOG_SAME_IP = _ida_dbg.IT_LOG_SAME_IP
r"""
specific options for instruction tracing (see set_insn_trace_options())

instruction tracing will log new instructions even when IP doesn't change
"""

FT_LOG_RET = _ida_dbg.FT_LOG_RET
r"""
specific options for function tracing (see set_func_trace_options())

function tracing will log returning instructions
"""

BT_LOG_INSTS = _ida_dbg.BT_LOG_INSTS
r"""
specific options for basic block tracing (see set_bblk_trace_options())

log all instructions in the current basic block
"""


def get_step_trace_options(*args):
    r"""
    get_step_trace_options() -> int
    Get current step tracing options. \sq{Type, Synchronous function, Notification,
    none (synchronous function)}

    @return: Step trace options
    """
    return _ida_dbg.get_step_trace_options(*args)

def set_step_trace_options(*args):
    r"""
    set_step_trace_options(options)
    Modify step tracing options. \sq{Type, Synchronous function - available as
    request, Notification, none (synchronous function)}

    @param options: (C++: int)
    """
    return _ida_dbg.set_step_trace_options(*args)

def request_set_step_trace_options(*args):
    r"""
    request_set_step_trace_options(options)
    Post a set_step_trace_options() request.

    @param options: (C++: int)
    """
    return _ida_dbg.request_set_step_trace_options(*args)

def is_insn_trace_enabled(*args):
    r"""
    is_insn_trace_enabled() -> bool
    Get current state of instruction tracing. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}
    """
    return _ida_dbg.is_insn_trace_enabled(*args)

def enable_insn_trace(*args):
    r"""
    enable_insn_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.enable_insn_trace(*args)

def disable_insn_trace(*args):
    r"""
    disable_insn_trace() -> bool
    """
    return _ida_dbg.disable_insn_trace(*args)

def request_enable_insn_trace(*args):
    r"""
    request_enable_insn_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.request_enable_insn_trace(*args)

def request_disable_insn_trace(*args):
    r"""
    request_disable_insn_trace() -> bool
    """
    return _ida_dbg.request_disable_insn_trace(*args)

def get_insn_trace_options(*args):
    r"""
    get_insn_trace_options() -> int
    Get current instruction tracing options. Also see IT_LOG_SAME_IP \sq{Type,
    Synchronous function, Notification, none (synchronous function)}
    """
    return _ida_dbg.get_insn_trace_options(*args)

def set_insn_trace_options(*args):
    r"""
    set_insn_trace_options(options)
    Modify instruction tracing options. \sq{Type, Synchronous function - available
    as request, Notification, none (synchronous function)}

    @param options: (C++: int)
    """
    return _ida_dbg.set_insn_trace_options(*args)

def request_set_insn_trace_options(*args):
    r"""
    request_set_insn_trace_options(options)
    Post a set_insn_trace_options() request.

    @param options: (C++: int)
    """
    return _ida_dbg.request_set_insn_trace_options(*args)

def is_func_trace_enabled(*args):
    r"""
    is_func_trace_enabled() -> bool
    Get current state of functions tracing. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}
    """
    return _ida_dbg.is_func_trace_enabled(*args)

def enable_func_trace(*args):
    r"""
    enable_func_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.enable_func_trace(*args)

def disable_func_trace(*args):
    r"""
    disable_func_trace() -> bool
    """
    return _ida_dbg.disable_func_trace(*args)

def request_enable_func_trace(*args):
    r"""
    request_enable_func_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.request_enable_func_trace(*args)

def request_disable_func_trace(*args):
    r"""
    request_disable_func_trace() -> bool
    """
    return _ida_dbg.request_disable_func_trace(*args)

def get_func_trace_options(*args):
    r"""
    get_func_trace_options() -> int
    Get current function tracing options. Also see FT_LOG_RET \sq{Type, Synchronous
    function, Notification, none (synchronous function)}
    """
    return _ida_dbg.get_func_trace_options(*args)

def set_func_trace_options(*args):
    r"""
    set_func_trace_options(options)
    Modify function tracing options. \sq{Type, Synchronous function - available as
    request, Notification, none (synchronous function)}

    @param options: (C++: int)
    """
    return _ida_dbg.set_func_trace_options(*args)

def request_set_func_trace_options(*args):
    r"""
    request_set_func_trace_options(options)
    Post a set_func_trace_options() request.

    @param options: (C++: int)
    """
    return _ida_dbg.request_set_func_trace_options(*args)

def enable_bblk_trace(*args):
    r"""
    enable_bblk_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.enable_bblk_trace(*args)

def disable_bblk_trace(*args):
    r"""
    disable_bblk_trace() -> bool
    """
    return _ida_dbg.disable_bblk_trace(*args)

def request_enable_bblk_trace(*args):
    r"""
    request_enable_bblk_trace(enable=True) -> bool

    @param enable: bool
    """
    return _ida_dbg.request_enable_bblk_trace(*args)

def request_disable_bblk_trace(*args):
    r"""
    request_disable_bblk_trace() -> bool
    """
    return _ida_dbg.request_disable_bblk_trace(*args)

def is_bblk_trace_enabled(*args):
    r"""
    is_bblk_trace_enabled() -> bool
    """
    return _ida_dbg.is_bblk_trace_enabled(*args)

def get_bblk_trace_options(*args):
    r"""
    get_bblk_trace_options() -> int
    Get current basic block tracing options. Also see BT_LOG_INSTS \sq{Type,
    Synchronous function, Notification, none (synchronous function)}
    """
    return _ida_dbg.get_bblk_trace_options(*args)

def set_bblk_trace_options(*args):
    r"""
    set_bblk_trace_options(options)
    Modify basic block tracing options (see BT_LOG_INSTS)

    @param options: (C++: int)
    """
    return _ida_dbg.set_bblk_trace_options(*args)

def request_set_bblk_trace_options(*args):
    r"""
    request_set_bblk_trace_options(options)
    Post a set_bblk_trace_options() request.

    @param options: (C++: int)
    """
    return _ida_dbg.request_set_bblk_trace_options(*args)
tev_none = _ida_dbg.tev_none
r"""
no event
"""

tev_insn = _ida_dbg.tev_insn
r"""
an instruction trace
"""

tev_call = _ida_dbg.tev_call
r"""
a function call trace
"""

tev_ret = _ida_dbg.tev_ret
r"""
a function return trace
"""

tev_bpt = _ida_dbg.tev_bpt
r"""
write, read/write, execution trace
"""

tev_mem = _ida_dbg.tev_mem
r"""
memory layout changed
"""

tev_event = _ida_dbg.tev_event
r"""
debug event occurred
"""

tev_max = _ida_dbg.tev_max
r"""
first unused event type
"""

class tev_info_t(object):
    r"""
    Proxy of C++ tev_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    type = property(_ida_dbg.tev_info_t_type_get, _ida_dbg.tev_info_t_type_set, doc=r"""type""")
    r"""
    trace event type
    """
    tid = property(_ida_dbg.tev_info_t_tid_get, _ida_dbg.tev_info_t_tid_set, doc=r"""tid""")
    r"""
    thread where the event was recorded
    """
    ea = property(_ida_dbg.tev_info_t_ea_get, _ida_dbg.tev_info_t_ea_set, doc=r"""ea""")
    r"""
    address where the event occurred
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> tev_info_t
        """
        _ida_dbg.tev_info_t_swiginit(self, _ida_dbg.new_tev_info_t(*args))
    __swig_destroy__ = _ida_dbg.delete_tev_info_t

# Register tev_info_t in _ida_dbg:
_ida_dbg.tev_info_t_swigregister(tev_info_t)

class memreg_info_t(object):
    r"""
    Proxy of C++ memreg_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = property(_ida_dbg.memreg_info_t_ea_get, _ida_dbg.memreg_info_t_ea_set, doc=r"""ea""")

    def get_bytes(self, *args):
        r"""
        get_bytes(self) -> PyObject *
        """
        return _ida_dbg.memreg_info_t_get_bytes(self, *args)

    bytes = property(get_bytes)


    def __init__(self, *args):
        r"""
        __init__(self) -> memreg_info_t
        """
        _ida_dbg.memreg_info_t_swiginit(self, _ida_dbg.new_memreg_info_t(*args))
    __swig_destroy__ = _ida_dbg.delete_memreg_info_t

# Register memreg_info_t in _ida_dbg:
_ida_dbg.memreg_info_t_swigregister(memreg_info_t)


def get_tev_qty(*args):
    r"""
    get_tev_qty() -> int
    Get number of trace events available in trace buffer. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}
    """
    return _ida_dbg.get_tev_qty(*args)

def get_tev_info(*args):
    r"""
    get_tev_info(n, tev_info) -> bool
    Get main information about a trace event. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @param tev_info: (C++: tev_info_t *) result
    @return: success
    """
    return _ida_dbg.get_tev_info(*args)

def get_insn_tev_reg_val(*args):
    r"""
    get_insn_tev_reg_val(n, regname, regval) -> bool

    @param n: int
    @param regname: char const *
    @param regval: regval_t *
    """
    return _ida_dbg.get_insn_tev_reg_val(*args)

def get_insn_tev_reg_mem(*args):
    r"""
    get_insn_tev_reg_mem(n, memmap) -> bool
    Read the memory pointed by register values from an instruction trace event.
    \sq{Type, Synchronous function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @param memmap: (C++: memreg_infos_t *) result
    @return: false if not an instruction event or no memory is available
    """
    return _ida_dbg.get_insn_tev_reg_mem(*args)

def get_insn_tev_reg_result(*args):
    r"""
    get_insn_tev_reg_result(n, regname, regval) -> bool

    @param n: int
    @param regname: char const *
    @param regval: regval_t *
    """
    return _ida_dbg.get_insn_tev_reg_result(*args)

def get_call_tev_callee(*args):
    r"""
    get_call_tev_callee(n) -> ea_t
    Get the called function from a function call trace event. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @return: BADADDR if not a function call event.
    """
    return _ida_dbg.get_call_tev_callee(*args)

def get_ret_tev_return(*args):
    r"""
    get_ret_tev_return(n) -> ea_t
    Get the return address from a function return trace event. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @return: BADADDR if not a function return event.
    """
    return _ida_dbg.get_ret_tev_return(*args)

def get_bpt_tev_ea(*args):
    r"""
    get_bpt_tev_ea(n) -> ea_t
    Get the address associated to a read, read/write or execution trace event.
    \sq{Type, Synchronous function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @return: BADADDR if not a read, read/write or execution trace event.
    @note: Usually, a breakpoint is associated with a read, read/write or execution
           trace event. However, the returned address could be any address in the
           range of this breakpoint. If the breakpoint was deleted after the trace
           event, the address no longer corresponds to a valid breakpoint.
    """
    return _ida_dbg.get_bpt_tev_ea(*args)

def get_tev_memory_info(*args):
    r"""
    get_tev_memory_info(n, mi) -> bool
    Get the memory layout, if any, for the specified tev object. \sq{Type,
    Synchronous function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @param mi: (C++: meminfo_vec_t *) result
    @return: false if the tev_t object is not of type tev_mem, true otherwise, with
             the new memory layout in "mi".
    """
    return _ida_dbg.get_tev_memory_info(*args)

def get_tev_event(*args):
    r"""
    get_tev_event(n, d) -> bool
    Get the corresponding debug event, if any, for the specified tev object.
    \sq{Type, Synchronous function, Notification, none (synchronous function)}

    @param n: (C++: int) number of trace event, is in range 0..get_tev_qty()-1. 0 represents
              the latest added trace event.
    @param d: (C++: debug_event_t *) result
    @return: false if the tev_t object doesn't have any associated debug event, true
             otherwise, with the debug event in "d".
    """
    return _ida_dbg.get_tev_event(*args)

def get_trace_base_address(*args):
    r"""
    get_trace_base_address() -> ea_t
    Get the base address of the current trace. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @return: the base address of the currently loaded trace
    """
    return _ida_dbg.get_trace_base_address(*args)

def set_trace_base_address(*args):
    r"""
    set_trace_base_address(ea)
    Set the base address of the current trace. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param ea: (C++: ea_t)
    """
    return _ida_dbg.set_trace_base_address(*args)

def dbg_add_thread(*args):
    r"""
    dbg_add_thread(tid)
    Add a thread to the current trace. \sq{Type, Synchronous function, Notification,
    none (synchronous function)}

    @param tid: (C++: thid_t)
    """
    return _ida_dbg.dbg_add_thread(*args)

def dbg_del_thread(*args):
    r"""
    dbg_del_thread(tid)
    Delete a thread from the current trace. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param tid: (C++: thid_t)
    """
    return _ida_dbg.dbg_del_thread(*args)

def dbg_add_tev(*args):
    r"""
    dbg_add_tev(type, tid, address)
    Add a new trace element to the current trace. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param type: (C++: tev_type_t) enum tev_type_t
    @param tid: (C++: thid_t)
    @param address: (C++: ea_t)
    """
    return _ida_dbg.dbg_add_tev(*args)
class tev_reg_value_t(object):
    r"""
    Proxy of C++ tev_reg_value_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    value = property(_ida_dbg.tev_reg_value_t_value_get, _ida_dbg.tev_reg_value_t_value_set, doc=r"""value""")
    reg_idx = property(_ida_dbg.tev_reg_value_t_reg_idx_get, _ida_dbg.tev_reg_value_t_reg_idx_set, doc=r"""reg_idx""")

    def __init__(self, *args):
        r"""
        __init__(self, _reg_idx=-1, _value=uint64(-1)) -> tev_reg_value_t

        @param _reg_idx: int
        @param _value: uint64
        """
        _ida_dbg.tev_reg_value_t_swiginit(self, _ida_dbg.new_tev_reg_value_t(*args))
    __swig_destroy__ = _ida_dbg.delete_tev_reg_value_t

# Register tev_reg_value_t in _ida_dbg:
_ida_dbg.tev_reg_value_t_swigregister(tev_reg_value_t)

class tev_info_reg_t(object):
    r"""
    Proxy of C++ tev_info_reg_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    info = property(_ida_dbg.tev_info_reg_t_info_get, _ida_dbg.tev_info_reg_t_info_set, doc=r"""info""")
    registers = property(_ida_dbg.tev_info_reg_t_registers_get, _ida_dbg.tev_info_reg_t_registers_set, doc=r"""registers""")

    def __init__(self, *args):
        r"""
        __init__(self) -> tev_info_reg_t
        """
        _ida_dbg.tev_info_reg_t_swiginit(self, _ida_dbg.new_tev_info_reg_t(*args))
    __swig_destroy__ = _ida_dbg.delete_tev_info_reg_t

# Register tev_info_reg_t in _ida_dbg:
_ida_dbg.tev_info_reg_t_swigregister(tev_info_reg_t)

SAVE_ALL_VALUES = _ida_dbg.SAVE_ALL_VALUES

SAVE_DIFF = _ida_dbg.SAVE_DIFF

SAVE_NONE = _ida_dbg.SAVE_NONE


def dbg_add_many_tevs(*args):
    r"""
    dbg_add_many_tevs(new_tevs) -> bool
    Add many new trace elements to the current trace. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param new_tevs: (C++: tevinforeg_vec_t *)
    @return: false if the operation failed for any tev_info_t object
    """
    return _ida_dbg.dbg_add_many_tevs(*args)

def dbg_add_insn_tev(*args):
    r"""
    dbg_add_insn_tev(tid, ea, save=SAVE_DIFF) -> bool
    Add a new instruction trace element to the current trace. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param tid: (C++: thid_t)
    @param ea: (C++: ea_t)
    @param save: (C++: save_reg_values_t) enum save_reg_values_t
    @return: false if the operation failed, true otherwise
    """
    return _ida_dbg.dbg_add_insn_tev(*args)

def dbg_add_bpt_tev(*args):
    r"""
    dbg_add_bpt_tev(tid, ea, bp) -> bool
    Add a new breakpoint trace element to the current trace. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param tid: (C++: thid_t)
    @param ea: (C++: ea_t)
    @param bp: (C++: ea_t)
    @return: false if the operation failed, true otherwise
    """
    return _ida_dbg.dbg_add_bpt_tev(*args)

def dbg_add_call_tev(*args):
    r"""
    dbg_add_call_tev(tid, caller, callee)
    Add a new call trace element to the current trace. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param tid: (C++: thid_t)
    @param caller: (C++: ea_t)
    @param callee: (C++: ea_t)
    """
    return _ida_dbg.dbg_add_call_tev(*args)

def dbg_add_ret_tev(*args):
    r"""
    dbg_add_ret_tev(tid, ret_insn, return_to)
    Add a new return trace element to the current trace. \sq{Type, Synchronous
    function, Notification, none (synchronous function)}

    @param tid: (C++: thid_t)
    @param ret_insn: (C++: ea_t)
    @param return_to: (C++: ea_t)
    """
    return _ida_dbg.dbg_add_ret_tev(*args)

def dbg_add_debug_event(*args):
    r"""
    dbg_add_debug_event(event)
    Add a new debug event to the current trace. \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param event: (C++: debug_event_t *)
    """
    return _ida_dbg.dbg_add_debug_event(*args)

def load_trace_file(*args):
    r"""
    load_trace_file(filename) -> str
    Load a recorded trace file in the 'Tracing' window. If the call succeeds and
    'buf' is not null, the description of the trace stored in the binary trace file
    will be returned in 'buf'

    @param filename: (C++: const char *) char const *
    """
    return _ida_dbg.load_trace_file(*args)

def save_trace_file(*args):
    r"""
    save_trace_file(filename, description) -> bool
    Save the current trace in the specified file.

    @param filename: (C++: const char *) char const *
    @param description: (C++: const char *) char const *
    """
    return _ida_dbg.save_trace_file(*args)

def is_valid_trace_file(*args):
    r"""
    is_valid_trace_file(filename) -> bool
    Is the specified file a valid trace file for the current database?

    @param filename: (C++: const char *) char const *
    """
    return _ida_dbg.is_valid_trace_file(*args)

def set_trace_file_desc(*args):
    r"""
    set_trace_file_desc(filename, description) -> bool
    Change the description of the specified trace file.

    @param filename: (C++: const char *) char const *
    @param description: (C++: const char *) char const *
    """
    return _ida_dbg.set_trace_file_desc(*args)

def get_trace_file_desc(*args):
    r"""
    get_trace_file_desc(filename) -> str
    Get the file header of the specified trace file.

    @param filename: (C++: const char *) char const *
    """
    return _ida_dbg.get_trace_file_desc(*args)

def choose_trace_file(*args):
    r"""
    choose_trace_file() -> str
    Show the choose trace dialog.
    """
    return _ida_dbg.choose_trace_file(*args)

def diff_trace_file(*args):
    r"""
    diff_trace_file(NONNULL_filename) -> bool
    Show difference between the current trace and the one from 'filename'.

    @param NONNULL_filename: (C++: const char *) char const *
    """
    return _ida_dbg.diff_trace_file(*args)

def graph_trace(*args):
    r"""
    graph_trace() -> bool
    Show the trace callgraph.
    """
    return _ida_dbg.graph_trace(*args)

def set_highlight_trace_options(*args):
    r"""
    set_highlight_trace_options(hilight, color, diff)
    Set highlight trace parameters.

    @param hilight: (C++: bool)
    @param color: (C++: bgcolor_t)
    @param diff: (C++: bgcolor_t)
    """
    return _ida_dbg.set_highlight_trace_options(*args)

def set_trace_platform(*args):
    r"""
    set_trace_platform(platform)
    Set platform name of current trace.

    @param platform: (C++: const char *) char const *
    """
    return _ida_dbg.set_trace_platform(*args)

def get_trace_platform(*args):
    r"""
    get_trace_platform() -> char const *
    Get platform name of current trace.
    """
    return _ida_dbg.get_trace_platform(*args)

def set_trace_dynamic_register_set(*args):
    r"""
    set_trace_dynamic_register_set(idaregs)
    Set dynamic register set of current trace.

    @param idaregs: (C++: dynamic_register_set_t &)
    """
    return _ida_dbg.set_trace_dynamic_register_set(*args)

def get_trace_dynamic_register_set(*args):
    r"""
    get_trace_dynamic_register_set(idaregs)
    Get dynamic register set of current trace.

    @param idaregs: (C++: dynamic_register_set_t *)
    """
    return _ida_dbg.get_trace_dynamic_register_set(*args)
DEC_NOTASK = _ida_dbg.DEC_NOTASK
r"""
process does not exist
"""

DEC_ERROR = _ida_dbg.DEC_ERROR
r"""
error
"""

DEC_TIMEOUT = _ida_dbg.DEC_TIMEOUT
r"""
timeout
"""

WFNE_ANY = _ida_dbg.WFNE_ANY
r"""
return the first event (even if it doesn't suspend the process)
"""

WFNE_SUSP = _ida_dbg.WFNE_SUSP
r"""
wait until the process gets suspended
"""

WFNE_SILENT = _ida_dbg.WFNE_SILENT
r"""
1: be silent, 0:display modal boxes if necessary
"""

WFNE_CONT = _ida_dbg.WFNE_CONT
r"""
continue from the suspended state
"""

WFNE_NOWAIT = _ida_dbg.WFNE_NOWAIT
r"""
do not wait for any event, immediately return DEC_TIMEOUT (to be used with
WFNE_CONT)
"""

WFNE_USEC = _ida_dbg.WFNE_USEC
r"""
timeout is specified in microseconds (minimum non-zero timeout is 40000us)
"""

DOPT_SEGM_MSGS = _ida_dbg.DOPT_SEGM_MSGS
r"""
log debugger segments modifications
"""

DOPT_START_BPT = _ida_dbg.DOPT_START_BPT
r"""
break on process start
"""

DOPT_THREAD_MSGS = _ida_dbg.DOPT_THREAD_MSGS
r"""
log thread starts/exits
"""

DOPT_THREAD_BPT = _ida_dbg.DOPT_THREAD_BPT
r"""
break on thread start/exit
"""

DOPT_BPT_MSGS = _ida_dbg.DOPT_BPT_MSGS
r"""
log breakpoints
"""

DOPT_LIB_MSGS = _ida_dbg.DOPT_LIB_MSGS
r"""
log library loads/unloads
"""

DOPT_LIB_BPT = _ida_dbg.DOPT_LIB_BPT
r"""
break on library load/unload
"""

DOPT_INFO_MSGS = _ida_dbg.DOPT_INFO_MSGS
r"""
log debugging info events
"""

DOPT_INFO_BPT = _ida_dbg.DOPT_INFO_BPT
r"""
break on debugging information
"""

DOPT_REAL_MEMORY = _ida_dbg.DOPT_REAL_MEMORY
r"""
do not hide breakpoint instructions
"""

DOPT_REDO_STACK = _ida_dbg.DOPT_REDO_STACK
r"""
reconstruct the stack
"""

DOPT_ENTRY_BPT = _ida_dbg.DOPT_ENTRY_BPT
r"""
break on program entry point
"""

DOPT_EXCDLG = _ida_dbg.DOPT_EXCDLG
r"""
exception dialogs:
"""

EXCDLG_NEVER = _ida_dbg.EXCDLG_NEVER
r"""
never display exception dialogs
"""

EXCDLG_UNKNOWN = _ida_dbg.EXCDLG_UNKNOWN
r"""
display for unknown exceptions
"""

EXCDLG_ALWAYS = _ida_dbg.EXCDLG_ALWAYS
r"""
always display
"""

DOPT_LOAD_DINFO = _ida_dbg.DOPT_LOAD_DINFO
r"""
automatically load debug files (pdb)
"""

DOPT_END_BPT = _ida_dbg.DOPT_END_BPT
r"""
evaluate event condition on process end
"""

DOPT_TEMP_HWBPT = _ida_dbg.DOPT_TEMP_HWBPT
r"""
when possible use hardware bpts for temp bpts
"""

DOPT_FAST_STEP = _ida_dbg.DOPT_FAST_STEP
r"""
prevent debugger memory refreshes when single-stepping
"""


def wait_for_next_event(*args):
    r"""
    wait_for_next_event(wfne, timeout) -> dbg_event_code_t
    Wait for the next event.

    This function (optionally) resumes the process execution, and waits for a
    debugger event until a possible timeout occurs.

    @param wfne: (C++: int) combination of Wait for debugger event flags constants
    @param timeout: (C++: int) number of seconds to wait, -1-infinity
    @return: either an event_id_t (if > 0), or a dbg_event_code_t (if <= 0)
    """
    return _ida_dbg.wait_for_next_event(*args)

def get_debug_event(*args):
    r"""
    get_debug_event() -> debug_event_t
    Get the current debugger event.
    """
    return _ida_dbg.get_debug_event(*args)

def set_debugger_options(*args):
    r"""
    set_debugger_options(options) -> uint
    Set debugger options. Replaces debugger options with the specification
    combination Debugger options

    @param options: (C++: uint)
    @return: the old debugger options
    """
    return _ida_dbg.set_debugger_options(*args)

def set_remote_debugger(*args):
    r"""
    set_remote_debugger(host, _pass, port=-1)
    Set remote debugging options. Should be used before starting the debugger.

    @param host: (C++: const char *) If empty, IDA will use local debugger. If nullptr, the host will
                 not be set.
    @param pass: (C++: const char *) If nullptr, the password will not be set
    @param port: (C++: int) If -1, the default port number will be used
    """
    return _ida_dbg.set_remote_debugger(*args)

def get_process_options(*args):
    r"""
    get_process_options()
    Get process options. Any of the arguments may be nullptr
    """
    return _ida_dbg.get_process_options(*args)

def set_process_options(*args):
    r"""
    set_process_options(path, args, sdir, host, _pass, port)
    Set process options. Any of the arguments may be nullptr, which means 'do not
    modify'

    @param path: (C++: const char *) char const *
    @param args: (C++: const char *) char const *
    @param sdir: (C++: const char *) char const *
    @param host: (C++: const char *) char const *
    @param pass: (C++: const char *) char const *
    @param port: (C++: int)
    """
    return _ida_dbg.set_process_options(*args)

def retrieve_exceptions(*args):
    r"""
    retrieve_exceptions() -> excvec_t
    Retrieve the exception information. You may freely modify the returned vector
    and add/edit/delete exceptions You must call store_exceptions() after any
    modifications Note: exceptions with code zero, multiple exception codes or names
    are prohibited
    """
    return _ida_dbg.retrieve_exceptions(*args)

def store_exceptions(*args):
    r"""
    store_exceptions() -> bool
    Update the exception information stored in the debugger module by invoking its
    dbg->set_exception_info callback
    """
    return _ida_dbg.store_exceptions(*args)

def define_exception(*args):
    r"""
    define_exception(code, name, desc, flags) -> char const *
    Convenience function: define new exception code.

    @param code: (C++: uint) exception code (cannot be 0)
    @param name: (C++: const char *) exception name (cannot be empty or nullptr)
    @param desc: (C++: const char *) exception description (maybe nullptr)
    @param flags: (C++: int) combination of Exception info flags
    @return: failure message or nullptr. You must call store_exceptions() if this
             function succeeds
    """
    return _ida_dbg.define_exception(*args)
class eval_ctx_t(object):
    r"""
    Proxy of C++ eval_ctx_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _ea) -> eval_ctx_t

        @param _ea: ea_t
        """
        _ida_dbg.eval_ctx_t_swiginit(self, _ida_dbg.new_eval_ctx_t(*args))
    ea = property(_ida_dbg.eval_ctx_t_ea_get, _ida_dbg.eval_ctx_t_ea_set, doc=r"""ea""")
    __swig_destroy__ = _ida_dbg.delete_eval_ctx_t

# Register eval_ctx_t in _ida_dbg:
_ida_dbg.eval_ctx_t_swigregister(eval_ctx_t)

SRCIT_NONE = _ida_dbg.SRCIT_NONE
r"""
unknown
"""

SRCIT_MODULE = _ida_dbg.SRCIT_MODULE
r"""
module
"""

SRCIT_FUNC = _ida_dbg.SRCIT_FUNC
r"""
function
"""

SRCIT_STMT = _ida_dbg.SRCIT_STMT
r"""
a statement (if/while/for...)
"""

SRCIT_EXPR = _ida_dbg.SRCIT_EXPR
r"""
an expression (a+b*c)
"""

SRCIT_STTVAR = _ida_dbg.SRCIT_STTVAR
r"""
static variable/code
"""

SRCIT_LOCVAR = _ida_dbg.SRCIT_LOCVAR
r"""
a stack, register, or register-relative local variable or parameter
"""

SRCDBG_PROV_VERSION = _ida_dbg.SRCDBG_PROV_VERSION


def create_source_viewer(*args):
    r"""
    create_source_viewer(out_ccv, parent, custview, sf, lines, lnnum, colnum, flags) -> source_view_t *
    Create a source code view.

    @param out_ccv: (C++: TWidget **)
    @param parent: (C++: TWidget *)
    @param custview: (C++: TWidget *)
    @param sf: (C++: source_file_ptr)
    @param lines: (C++: strvec_t *)
    @param lnnum: (C++: int)
    @param colnum: (C++: int)
    @param flags: (C++: int)
    """
    return _ida_dbg.create_source_viewer(*args)

def get_dbg_byte(*args):
    r"""
    get_dbg_byte(x, ea) -> bool
    Get one byte of the debugged process memory.

    @param x: (C++: uint32 *) pointer to byte value
    @param ea: (C++: ea_t) linear address
    @return: true success
    false address inaccessible or debugger not running
    """
    return _ida_dbg.get_dbg_byte(*args)

def put_dbg_byte(*args):
    r"""
    put_dbg_byte(ea, x) -> bool
    Change one byte of the debugged process memory.

    @param ea: (C++: ea_t) linear address
    @param x: (C++: uint32) byte value
    @return: true if the process memory has been modified
    """
    return _ida_dbg.put_dbg_byte(*args)

def invalidate_dbgmem_config(*args):
    r"""
    invalidate_dbgmem_config()
    Invalidate the debugged process memory configuration. Call this function if the
    debugged process might have changed its memory layout (allocated more memory,
    for example)
    """
    return _ida_dbg.invalidate_dbgmem_config(*args)

def invalidate_dbgmem_contents(*args):
    r"""
    invalidate_dbgmem_contents(ea, size)
    Invalidate the debugged process memory contents. Call this function each time
    the process has been stopped or the process memory is modified. If ea ==
    BADADDR, then the whole memory contents will be invalidated

    @param ea: (C++: ea_t)
    @param size: (C++: asize_t)
    """
    return _ida_dbg.invalidate_dbgmem_contents(*args)

def is_debugger_on(*args):
    r"""
    is_debugger_on() -> bool
    Is the debugger currently running?
    """
    return _ida_dbg.is_debugger_on(*args)

def is_debugger_memory(*args):
    r"""
    is_debugger_memory(ea) -> bool
    Is the address mapped to debugger memory?

    @param ea: (C++: ea_t)
    """
    return _ida_dbg.is_debugger_memory(*args)

def get_tev_ea(*args):
    r"""
    get_tev_ea(n) -> ea_t

    @param n: int
    """
    return _ida_dbg.get_tev_ea(*args)

def get_tev_type(*args):
    r"""
    get_tev_type(n) -> int

    @param n: int
    """
    return _ida_dbg.get_tev_type(*args)

def get_tev_tid(*args):
    r"""
    get_tev_tid(n) -> int

    @param n: int
    """
    return _ida_dbg.get_tev_tid(*args)

def bring_debugger_to_front(*args):
    r"""
    bring_debugger_to_front()
    """
    return _ida_dbg.bring_debugger_to_front(*args)

def set_manual_regions(*args):
    r"""
    set_manual_regions(ranges)

    @param ranges: meminfo_vec_t const *
    """
    return _ida_dbg.set_manual_regions(*args)

def edit_manual_regions(*args):
    r"""
    edit_manual_regions()
    """
    return _ida_dbg.edit_manual_regions(*args)

def enable_manual_regions(*args):
    r"""
    enable_manual_regions(enable)

    @param enable: bool
    """
    return _ida_dbg.enable_manual_regions(*args)

def handle_debug_event(*args):
    r"""
    handle_debug_event(ev, rqflags) -> int

    @param ev: debug_event_t const *
    @param rqflags: int
    """
    return _ida_dbg.handle_debug_event(*args)

def add_virt_module(*args):
    r"""
    add_virt_module(mod) -> bool

    @param mod: modinfo_t const *
    """
    return _ida_dbg.add_virt_module(*args)

def del_virt_module(*args):
    r"""
    del_virt_module(base) -> bool

    @param base: ea_t const
    """
    return _ida_dbg.del_virt_module(*args)

def internal_ioctl(*args):
    r"""
    internal_ioctl(fn, buf, poutbuf, poutsize) -> int

    @param fn: int
    @param buf: void const *
    @param poutbuf: void **
    @param poutsize: ssize_t *
    """
    return _ida_dbg.internal_ioctl(*args)

def get_reg_vals(*args):
    r"""
    get_reg_vals(tid, clsmask, values) -> int

    @param tid: thid_t
    @param clsmask: int
    @param values: regval_t *
    """
    return _ida_dbg.get_reg_vals(*args)

def get_dbg_memory_info(*args):
    r"""
    get_dbg_memory_info(ranges) -> int

    @param ranges: meminfo_vec_t *
    """
    return _ida_dbg.get_dbg_memory_info(*args)

def set_bpt_group(*args):
    r"""
    set_bpt_group(bpt, grp_name) -> bool
    Move a bpt into a folder in the breakpoint dirtree if the folder didn't exists,
    it will be created \sq{Type, Synchronous function, Notification, none
    (synchronous function)}

    @param bpt: (C++: bpt_t &) bpt that will be moved
    @param grp_name: (C++: const char *) absolute path to the breakpoint dirtree folder
    @return: success
    """
    return _ida_dbg.set_bpt_group(*args)

def set_bptloc_group(*args):
    r"""
    set_bptloc_group(bptloc, grp_name) -> bool
    Move a bpt into a folder in the breakpoint dirtree based on the bpt_location
    find_bpt is called to retrieve the bpt and then set_bpt_group if the folder
    didn't exists, it will be created \sq{Type, Synchronous function, Notification,
    none (synchronous function)}

    @param bptloc: (C++: const bpt_location_t &) bptlocation of the bpt that will be moved
    @param grp_name: (C++: const char *) absolute path to the breakpoint dirtree folder
    @return: success
    """
    return _ida_dbg.set_bptloc_group(*args)

def get_bpt_group(*args):
    r"""
    get_bpt_group(bptloc) -> str
    Retrieve the absolute path to the folder of the bpt based on the bpt_location
    find_bpt is called to retrieve the bpt \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param bptloc: (C++: const bpt_location_t &) bptlocation of the bpt
    @return: breakpoint correclty moved to the directory
    success
    """
    return _ida_dbg.get_bpt_group(*args)

def rename_bptgrp(*args):
    r"""
    rename_bptgrp(old_name, new_name) -> bool
    Rename a folder of bpt dirtree \sq{Type, Synchronous function, Notification,
    none (synchronous function)}

    @param old_name: (C++: const char *) absolute path to the folder to be renamed
    @param new_name: (C++: const char *) absolute path of the new folder name
    @return: success
    """
    return _ida_dbg.rename_bptgrp(*args)

def del_bptgrp(*args):
    r"""
    del_bptgrp(name) -> bool
    Delete a folder, bpt that were part of this folder are moved to the root folder
    \sq{Type, Synchronous function, Notification, none (synchronous function)}

    @param name: (C++: const char *) full path to the folder to be deleted
    @return: success
    """
    return _ida_dbg.del_bptgrp(*args)

def get_grp_bpts(*args):
    r"""
    get_grp_bpts(bpts, grp_name) -> ssize_t
    Retrieve a copy the bpts stored in a folder \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param output: bpts : pointer to a vector where the copy of bpts are stored
    @param grp_name: (C++: const char *) absolute path to the folder
    @return: number of bpts present in the vector
    """
    return _ida_dbg.get_grp_bpts(*args)

def enable_bptgrp(*args):
    r"""
    enable_bptgrp(bptgrp_name, enable=True) -> int
    Enable (or disable) all bpts in a folder \sq{Type, Synchronous function,
    Notification, none (synchronous function)}

    @param bptgrp_name: (C++: const char *) absolute path to the folder
    @param enable: (C++: bool) by default true, enable bpts, false disable bpts
    @return: -1 an error occured 0 no changes >0 nubmers of bpts udpated
    """
    return _ida_dbg.enable_bptgrp(*args)

def get_local_vars(*args):
    r"""
    get_local_vars(prov, ea, out) -> bool

    @param prov: srcinfo_provider_t *
    @param ea: ea_t
    @param out: source_items_t *
    """
    return _ida_dbg.get_local_vars(*args)

def srcdbg_request_step_into(*args):
    r"""
    srcdbg_request_step_into() -> bool
    """
    return _ida_dbg.srcdbg_request_step_into(*args)

def srcdbg_request_step_over(*args):
    r"""
    srcdbg_request_step_over() -> bool
    """
    return _ida_dbg.srcdbg_request_step_over(*args)

def srcdbg_request_step_until_ret(*args):
    r"""
    srcdbg_request_step_until_ret() -> bool
    """
    return _ida_dbg.srcdbg_request_step_until_ret(*args)

def hide_all_bpts(*args):
    r"""
    hide_all_bpts() -> int
    """
    return _ida_dbg.hide_all_bpts(*args)

def read_dbg_memory(*args):
    r"""
    read_dbg_memory(ea, buffer, size) -> ssize_t

    @param ea: ea_t
    @param buffer: void *
    @param size: size_t
    """
    return _ida_dbg.read_dbg_memory(*args)

def get_module_info(*args):
    r"""
    get_module_info(ea, modinfo) -> bool

    @param ea: ea_t
    @param modinfo: modinfo_t *
    """
    return _ida_dbg.get_module_info(*args)

def dbg_bin_search(*args):
    r"""
    dbg_bin_search(start_ea, end_ea, data, srch_flags) -> str

    @param start_ea: ea_t
    @param end_ea: ea_t
    @param data: compiled_binpat_vec_t const &
    @param srch_flags: int
    """
    return _ida_dbg.dbg_bin_search(*args)

def load_debugger(*args):
    r"""
    load_debugger(dbgname, use_remote) -> bool

    @param dbgname: char const *
    @param use_remote: bool
    """
    return _ida_dbg.load_debugger(*args)

def collect_stack_trace(*args):
    r"""
    collect_stack_trace(tid, trace) -> bool

    @param tid: thid_t
    @param trace: call_stack_t *
    """
    return _ida_dbg.collect_stack_trace(*args)

def get_global_var(*args):
    r"""
    get_global_var(prov, ea, name, out) -> bool

    @param prov: srcinfo_provider_t *
    @param ea: ea_t
    @param name: char const *
    @param out: source_item_ptr *
    """
    return _ida_dbg.get_global_var(*args)

def get_local_var(*args):
    r"""
    get_local_var(prov, ea, name, out) -> bool

    @param prov: srcinfo_provider_t *
    @param ea: ea_t
    @param name: char const *
    @param out: source_item_ptr *
    """
    return _ida_dbg.get_local_var(*args)

def get_srcinfo_provider(*args):
    r"""
    get_srcinfo_provider(name) -> srcinfo_provider_t *

    @param name: char const *
    """
    return _ida_dbg.get_srcinfo_provider(*args)

def get_current_source_file(*args):
    r"""
    get_current_source_file() -> str
    """
    return _ida_dbg.get_current_source_file(*args)

def get_current_source_line(*args):
    r"""
    get_current_source_line() -> int
    """
    return _ida_dbg.get_current_source_line(*args)

def add_path_mapping(*args):
    r"""
    add_path_mapping(src, dst)

    @param src: char const *
    @param dst: char const *
    """
    return _ida_dbg.add_path_mapping(*args)

def srcdbg_step_into(*args):
    r"""
    srcdbg_step_into() -> bool
    """
    return _ida_dbg.srcdbg_step_into(*args)

def srcdbg_step_over(*args):
    r"""
    srcdbg_step_over() -> bool
    """
    return _ida_dbg.srcdbg_step_over(*args)

def srcdbg_step_until_ret(*args):
    r"""
    srcdbg_step_until_ret() -> bool
    """
    return _ida_dbg.srcdbg_step_until_ret(*args)

def set_debugger_event_cond(*args):
    r"""
    set_debugger_event_cond(NONNULL_evcond)

    @param NONNULL_evcond: char const *
    """
    return _ida_dbg.set_debugger_event_cond(*args)

def get_debugger_event_cond(*args):
    r"""
    get_debugger_event_cond() -> char const *
    """
    return _ida_dbg.get_debugger_event_cond(*args)

def get_manual_regions(*args):
    r"""
    get_manual_regions(ranges)
    Returns the manual memory regions

    @param ranges: meminfo_vec_t *

    @return: list(start_ea, end_ea, name, sclass, sbase, bitness, perm)
    get_manual_regions() -> [(int, int, str, str, int, int, int), ...] or None
    """
    return _ida_dbg.get_manual_regions(*args)

def dbg_is_loaded(*args):
    r"""
    dbg_is_loaded() -> bool
    Checks if a debugger is loaded

    @return: Boolean
    """
    return _ida_dbg.dbg_is_loaded(*args)

def refresh_debugger_memory(*args):
    r"""
    refresh_debugger_memory() -> PyObject *
    Refreshes the debugger memory

    @return: Nothing
    """
    return _ida_dbg.refresh_debugger_memory(*args)
class DBG_Hooks(object):
    r"""
    Proxy of C++ DBG_Hooks class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _flags=0) -> DBG_Hooks

        @param _flags: uint32
        """
        if self.__class__ == DBG_Hooks:
            _self = None
        else:
            _self = self
        _ida_dbg.DBG_Hooks_swiginit(self, _ida_dbg.new_DBG_Hooks(_self, *args))

    def hook(self, *args):
        r"""
        hook(self) -> bool
        """
        return _ida_dbg.DBG_Hooks_hook(self, *args)

    def unhook(self, *args):
        r"""
        unhook(self) -> bool
        """
        return _ida_dbg.DBG_Hooks_unhook(self, *args)

    def dbg_process_start(self, *args):
        r"""
        dbg_process_start(self, pid, tid, ea, modinfo_name, modinfo_base, modinfo_size)

        @param event: (const debug_event_t *)
        @note: This event notification is also an asynchronous function result
               notification for start_process() !
        @param tid: thid_t
        @param ea: ea_t
        @param modinfo_name: char const *
        @param modinfo_base: ea_t
        @param modinfo_size: asize_t
        """
        return _ida_dbg.DBG_Hooks_dbg_process_start(self, *args)

    def dbg_process_exit(self, *args):
        r"""
        dbg_process_exit(self, pid, tid, ea, exit_code)

        @param event: (const debug_event_t *)
        @note: This event notification is also an asynchronous function result
               notification for start_process() !
        @param tid: thid_t
        @param ea: ea_t
        @param exit_code: int
        """
        return _ida_dbg.DBG_Hooks_dbg_process_exit(self, *args)

    def dbg_process_attach(self, *args):
        r"""
        dbg_process_attach(self, pid, tid, ea, modinfo_name, modinfo_base, modinfo_size)

        @param event: (const debug_event_t *)
        @note: This event notification is also an asynchronous function result
               notification for start_process() !
        @param tid: thid_t
        @param ea: ea_t
        @param modinfo_name: char const *
        @param modinfo_base: ea_t
        @param modinfo_size: asize_t
        """
        return _ida_dbg.DBG_Hooks_dbg_process_attach(self, *args)

    def dbg_process_detach(self, *args):
        r"""
        dbg_process_detach(self, pid, tid, ea)

        @param event: (const debug_event_t *)
        @note: This event notification is also an asynchronous function result
               notification for start_process() !
        @param tid: thid_t
        @param ea: ea_t
        """
        return _ida_dbg.DBG_Hooks_dbg_process_detach(self, *args)

    def dbg_thread_start(self, *args):
        r"""
        dbg_thread_start(self, pid, tid, ea)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        """
        return _ida_dbg.DBG_Hooks_dbg_thread_start(self, *args)

    def dbg_thread_exit(self, *args):
        r"""
        dbg_thread_exit(self, pid, tid, ea, exit_code)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        @param exit_code: int
        """
        return _ida_dbg.DBG_Hooks_dbg_thread_exit(self, *args)

    def dbg_library_load(self, *args):
        r"""
        dbg_library_load(self, pid, tid, ea, modinfo_name, modinfo_base, modinfo_size)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        @param modinfo_name: char const *
        @param modinfo_base: ea_t
        @param modinfo_size: asize_t
        """
        return _ida_dbg.DBG_Hooks_dbg_library_load(self, *args)

    def dbg_library_unload(self, *args):
        r"""
        dbg_library_unload(self, pid, tid, ea, info)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        @param info: char const *
        """
        return _ida_dbg.DBG_Hooks_dbg_library_unload(self, *args)

    def dbg_information(self, *args):
        r"""
        dbg_information(self, pid, tid, ea, info)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        @param info: char const *
        """
        return _ida_dbg.DBG_Hooks_dbg_information(self, *args)

    def dbg_exception(self, *args):
        r"""
        dbg_exception(self, pid, tid, ea, exc_code, exc_can_cont, exc_ea, exc_info) -> int

        @param event: (const debug_event_t *)
        @param warn: (int *) filled with:
        * -1: display an exception warning dialog if the process is suspended.
        * 0: never display an exception warning dialog.
        * 1: always display an exception warning dialog.
        @param ea: ea_t
        @param exc_code: int
        @param exc_can_cont: bool
        @param exc_ea: ea_t
        @param exc_info: char const *
        """
        return _ida_dbg.DBG_Hooks_dbg_exception(self, *args)

    def dbg_suspend_process(self, *args):
        r"""
        dbg_suspend_process(self)
        The process is now suspended.
        """
        return _ida_dbg.DBG_Hooks_dbg_suspend_process(self, *args)

    def dbg_bpt(self, *args):
        r"""
        dbg_bpt(self, tid, bptea) -> int
        A user defined breakpoint was reached.

        @param tid: (thid_t)
        @param bptea: (::ea_t)
        """
        return _ida_dbg.DBG_Hooks_dbg_bpt(self, *args)

    def dbg_trace(self, *args):
        r"""
        dbg_trace(self, tid, ip) -> int
        A step occurred (one instruction was executed). This event notification is only
        generated if step tracing is enabled.

        @param tid: (thid_t) thread ID
        @param ip: (::ea_t) current instruction pointer. usually points after the
                   executed instruction
        @retval 1: do not log this trace event
        @retval 0: log it
        """
        return _ida_dbg.DBG_Hooks_dbg_trace(self, *args)

    def dbg_request_error(self, *args):
        r"""
        dbg_request_error(self, failed_command, failed_dbg_notification)
        An error occurred during the processing of a request.

        @param failed_command: (ui_notification_t)
        @param failed_dbg_notification: (dbg_notification_t)
        """
        return _ida_dbg.DBG_Hooks_dbg_request_error(self, *args)

    def dbg_step_into(self, *args):
        r"""
        dbg_step_into(self)
        """
        return _ida_dbg.DBG_Hooks_dbg_step_into(self, *args)

    def dbg_step_over(self, *args):
        r"""
        dbg_step_over(self)
        """
        return _ida_dbg.DBG_Hooks_dbg_step_over(self, *args)

    def dbg_run_to(self, *args):
        r"""
        dbg_run_to(self, pid, tid, ea)

        @param event: (const debug_event_t *)
        @param tid: thid_t
        @param ea: ea_t
        """
        return _ida_dbg.DBG_Hooks_dbg_run_to(self, *args)

    def dbg_step_until_ret(self, *args):
        r"""
        dbg_step_until_ret(self)
        """
        return _ida_dbg.DBG_Hooks_dbg_step_until_ret(self, *args)

    def dbg_bpt_changed(self, *args):
        r"""
        dbg_bpt_changed(self, bptev_code, bpt)
        Breakpoint has been changed.

        @param bptev_code: (int) Breakpoint modification events
        @param bpt: (bpt_t *)
        """
        return _ida_dbg.DBG_Hooks_dbg_bpt_changed(self, *args)

    def dbg_started_loading_bpts(self, *args):
        r"""
        dbg_started_loading_bpts(self)
        Started loading breakpoint info from idb.
        """
        return _ida_dbg.DBG_Hooks_dbg_started_loading_bpts(self, *args)

    def dbg_finished_loading_bpts(self, *args):
        r"""
        dbg_finished_loading_bpts(self)
        Finished loading breakpoint info from idb.
        """
        return _ida_dbg.DBG_Hooks_dbg_finished_loading_bpts(self, *args)
    __swig_destroy__ = _ida_dbg.delete_DBG_Hooks
    def __disown__(self):
        self.this.disown()
        _ida_dbg.disown_DBG_Hooks(self)
        return weakref.proxy(self)

# Register DBG_Hooks in _ida_dbg:
_ida_dbg.DBG_Hooks_swigregister(DBG_Hooks)


def list_bptgrps(*args):
    r"""
    list_bptgrps(bptgrps) -> size_t
    Retrieve the list of absolute path of all folders of bpt dirtree \sq{Type,
    Synchronous function, Notification, none (synchronous function)}

    @param output: bptgrps list of absolute path in the bpt dirtree
    @return: number of folders returned
    list_bptgrps() -> [str, ...]
    """
    return _ida_dbg.list_bptgrps(*args)

def internal_get_sreg_base(*args):
    r"""
    internal_get_sreg_base(tid, sreg_value) -> ea_t
    Get the sreg base, for the given thread.

    @param tid: thid_t
    @param sreg_value: int
    @return: The sreg base, or BADADDR on failure.
    """
    return _ida_dbg.internal_get_sreg_base(*args)

def write_dbg_memory(*args):
    r"""
    write_dbg_memory(ea, py_buf, size=size_t(-1)) -> ssize_t

    @param ea: ea_t
    @param py_buf: PyObject *
    @param size: size_t
    """
    return _ida_dbg.write_dbg_memory(*args)

def dbg_can_query(*args):
    r"""
    dbg_can_query() -> bool
    This function can be used to check if the debugger can be queried:
      - debugger is loaded
      - process is suspended
      - process is not suspended but can take requests. In this case some requests like
        memory read/write, bpt management succeed and register querying will fail.
        Check if idaapi.get_process_state() < 0 to tell if the process is suspended

    @return: Boolean
    """
    return _ida_dbg.dbg_can_query(*args)

def set_reg_val(*args):
    r"""
    set_reg_val(regname, o) -> PyObject

    @param regname: char const *
    @param o: PyObject *

    set_reg_val(tid, regidx, o) -> bool, int

    @param tid: thid_t
    @param regidx: int
    @param o: PyObject *
    """
    return _ida_dbg.set_reg_val(*args)

def request_set_reg_val(*args):
    r"""
    request_set_reg_val(regname, o) -> PyObject *
    Post a set_reg_val() request.

    @param regname: (C++: const char *) char const *
    @param o: PyObject *
    """
    return _ida_dbg.request_set_reg_val(*args)

def get_reg_val(*args):
    r"""
    get_reg_val(regname, regval) -> bool
    Get register value as an unsigned 64-bit int.

    @param regname: (C++: const char *) char const *
    @param regval: regval_t *

    get_reg_val(regname, ival) -> bool

    @param regname: char const *
    @param ival: uint64 *

    get_reg_val(regname) -> bool, float, int

    @param regname: char const *
    """
    return _ida_dbg.get_reg_val(*args)

#<pycode(py_dbg)>
import ida_idaapi
import ida_idd
import ida_expr

def get_tev_reg_val(tev, reg):
    rv = ida_idd.regval_t()
    if get_insn_tev_reg_val(tev, reg, rv):
        if rv.rvtype == ida_idd.RVT_INT:
            return rv.ival

def get_tev_reg_mem_qty(tev):
    ti = tev_info_t()
    if get_tev_info(tev, ti):
        mis = memreg_infos_t()
        if get_insn_tev_reg_mem(tev, mis):
            return mis.size()

def get_tev_reg_mem(tev, idx):
    mis = memreg_infos_t()
    if get_insn_tev_reg_mem(tev, mis):
        if idx < mis.size():
            return mis[idx].bytes

def get_tev_reg_mem_ea(tev, idx):
    ti = tev_info_t()
    if get_tev_info(tev, ti):
        mis = memreg_infos_t()
        if get_insn_tev_reg_mem(tev, mis):
            if idx >= 0 and idx < mis.size():
                return mis[idx].ea

def send_dbg_command(command):
    r"""
    Send a direct command to the debugger backend, and
    retrieve the result as a string.

    Note: any double-quotes in 'command' must be backslash-escaped.
    Note: this only works with some debugger backends: Bochs, WinDbg, GDB.

    Returns: (True, <result string>) on success, or (False, <Error message string>) on failure
    """
    rv = ida_expr.idc_value_t()
    err = ida_expr.eval_idc_expr(rv, ida_idaapi.BADADDR, """send_dbg_command("%s");""" % command)
    if err:
        return False, "eval_idc_expr() failed: %s" % err
    vtype = ord(rv.vtype)
    if vtype == ida_expr.VT_STR:
        s = rv.c_str()
        if "IDC_FAILURE" in s:
            return False, "eval_idc_expr() reported an error: %s" % s
        return True, s
    elif vtype == ida_expr.VT_LONG:
        return True, str(rv.num)
    else:
        return False, "eval_idc_expr(): wrong return type: %d" % vtype

move_bpt_to_grp = set_bpt_group

#</pycode(py_dbg)>




