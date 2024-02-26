"""
Describes the type information records in IDA.

The recommended way of using type info is to use the tinfo_t class. The type
information is internally kept as an array of bytes terminated by 0.

Items in brackets [] are optional and sometimes are omitted. type_t... means a
sequence of type_t bytes which defines a type.

@note: to work with the types of instructions or data in the database, use
       get_tinfo()/set_tinfo() and similar functions."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_typeinf
else:
    import _ida_typeinf

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

SWIG_PYTHON_LEGACY_BOOL = _ida_typeinf.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_idp
class funcargvec_t(object):
    r"""
    Proxy of C++ qvector< funcarg_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> funcargvec_t
        __init__(self, x) -> funcargvec_t

        @param x: qvector< funcarg_t > const &
        """
        _ida_typeinf.funcargvec_t_swiginit(self, _ida_typeinf.new_funcargvec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_funcargvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: funcarg_t const &

        push_back(self) -> funcarg_t
        """
        return _ida_typeinf.funcargvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.funcargvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.funcargvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.funcargvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> funcarg_t

        @param _idx: size_t
        """
        return _ida_typeinf.funcargvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.funcargvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.funcargvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: funcarg_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.funcargvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=funcarg_t())

        @param x: funcarg_t const &
        """
        return _ida_typeinf.funcargvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.funcargvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.funcargvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.funcargvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< funcarg_t > &
        """
        return _ida_typeinf.funcargvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> funcarg_t
        """
        return _ida_typeinf.funcargvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: funcarg_t *
        @param len: size_t
        """
        return _ida_typeinf.funcargvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< funcarg_t > const &
        """
        return _ida_typeinf.funcargvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< funcarg_t > const &
        """
        return _ida_typeinf.funcargvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> funcarg_t
        """
        return _ida_typeinf.funcargvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> funcarg_t
        """
        return _ida_typeinf.funcargvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> funcarg_t

        @param it: qvector< funcarg_t >::iterator
        @param x: funcarg_t const &
        """
        return _ida_typeinf.funcargvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> funcarg_t

        @param it: qvector< funcarg_t >::iterator

        erase(self, first, last) -> funcarg_t

        @param first: qvector< funcarg_t >::iterator
        @param last: qvector< funcarg_t >::iterator
        """
        return _ida_typeinf.funcargvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> funcarg_t

        @param x: funcarg_t const &

        """
        return _ida_typeinf.funcargvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: funcarg_t const &
        """
        return _ida_typeinf.funcargvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: funcarg_t const &
        """
        return _ida_typeinf.funcargvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: funcarg_t const &

        """
        return _ida_typeinf.funcargvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.funcargvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> funcarg_t

        @param i: size_t
        """
        return _ida_typeinf.funcargvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: funcarg_t const &
        """
        return _ida_typeinf.funcargvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register funcargvec_t in _ida_typeinf:
_ida_typeinf.funcargvec_t_swigregister(funcargvec_t)

class reginfovec_t(object):
    r"""
    Proxy of C++ qvector< reg_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> reginfovec_t
        __init__(self, x) -> reginfovec_t

        @param x: qvector< reg_info_t > const &
        """
        _ida_typeinf.reginfovec_t_swiginit(self, _ida_typeinf.new_reginfovec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_reginfovec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: reg_info_t const &

        push_back(self) -> reg_info_t
        """
        return _ida_typeinf.reginfovec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.reginfovec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.reginfovec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.reginfovec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> reg_info_t

        @param _idx: size_t
        """
        return _ida_typeinf.reginfovec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.reginfovec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.reginfovec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: reg_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.reginfovec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=reg_info_t())

        @param x: reg_info_t const &
        """
        return _ida_typeinf.reginfovec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.reginfovec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.reginfovec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.reginfovec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< reg_info_t > &
        """
        return _ida_typeinf.reginfovec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> reg_info_t
        """
        return _ida_typeinf.reginfovec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: reg_info_t *
        @param len: size_t
        """
        return _ida_typeinf.reginfovec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< reg_info_t > const &
        """
        return _ida_typeinf.reginfovec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< reg_info_t > const &
        """
        return _ida_typeinf.reginfovec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> reg_info_t
        """
        return _ida_typeinf.reginfovec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> reg_info_t
        """
        return _ida_typeinf.reginfovec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> reg_info_t

        @param it: qvector< reg_info_t >::iterator
        @param x: reg_info_t const &
        """
        return _ida_typeinf.reginfovec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> reg_info_t

        @param it: qvector< reg_info_t >::iterator

        erase(self, first, last) -> reg_info_t

        @param first: qvector< reg_info_t >::iterator
        @param last: qvector< reg_info_t >::iterator
        """
        return _ida_typeinf.reginfovec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> reg_info_t

        @param x: reg_info_t const &

        """
        return _ida_typeinf.reginfovec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: reg_info_t const &
        """
        return _ida_typeinf.reginfovec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: reg_info_t const &
        """
        return _ida_typeinf.reginfovec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: reg_info_t const &

        """
        return _ida_typeinf.reginfovec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.reginfovec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> reg_info_t

        @param i: size_t
        """
        return _ida_typeinf.reginfovec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: reg_info_t const &
        """
        return _ida_typeinf.reginfovec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register reginfovec_t in _ida_typeinf:
_ida_typeinf.reginfovec_t_swigregister(reginfovec_t)

class enum_member_vec_t(object):
    r"""
    Proxy of C++ qvector< enum_member_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> enum_member_vec_t
        __init__(self, x) -> enum_member_vec_t

        @param x: qvector< enum_member_t > const &
        """
        _ida_typeinf.enum_member_vec_t_swiginit(self, _ida_typeinf.new_enum_member_vec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_enum_member_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: enum_member_t const &

        push_back(self) -> enum_member_t
        """
        return _ida_typeinf.enum_member_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.enum_member_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.enum_member_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.enum_member_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> enum_member_t

        @param _idx: size_t
        """
        return _ida_typeinf.enum_member_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.enum_member_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.enum_member_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: enum_member_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.enum_member_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=enum_member_t())

        @param x: enum_member_t const &
        """
        return _ida_typeinf.enum_member_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.enum_member_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.enum_member_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.enum_member_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< enum_member_t > &
        """
        return _ida_typeinf.enum_member_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> enum_member_t
        """
        return _ida_typeinf.enum_member_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: enum_member_t *
        @param len: size_t
        """
        return _ida_typeinf.enum_member_vec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< enum_member_t > const &
        """
        return _ida_typeinf.enum_member_vec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< enum_member_t > const &
        """
        return _ida_typeinf.enum_member_vec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> enum_member_t
        """
        return _ida_typeinf.enum_member_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> enum_member_t
        """
        return _ida_typeinf.enum_member_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> enum_member_t

        @param it: qvector< enum_member_t >::iterator
        @param x: enum_member_t const &
        """
        return _ida_typeinf.enum_member_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> enum_member_t

        @param it: qvector< enum_member_t >::iterator

        erase(self, first, last) -> enum_member_t

        @param first: qvector< enum_member_t >::iterator
        @param last: qvector< enum_member_t >::iterator
        """
        return _ida_typeinf.enum_member_vec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> enum_member_t

        @param x: enum_member_t const &

        """
        return _ida_typeinf.enum_member_vec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: enum_member_t const &
        """
        return _ida_typeinf.enum_member_vec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: enum_member_t const &
        """
        return _ida_typeinf.enum_member_vec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: enum_member_t const &

        """
        return _ida_typeinf.enum_member_vec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.enum_member_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> enum_member_t

        @param i: size_t
        """
        return _ida_typeinf.enum_member_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: enum_member_t const &
        """
        return _ida_typeinf.enum_member_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register enum_member_vec_t in _ida_typeinf:
_ida_typeinf.enum_member_vec_t_swigregister(enum_member_vec_t)

class argpartvec_t(object):
    r"""
    Proxy of C++ qvector< argpart_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> argpartvec_t
        __init__(self, x) -> argpartvec_t

        @param x: qvector< argpart_t > const &
        """
        _ida_typeinf.argpartvec_t_swiginit(self, _ida_typeinf.new_argpartvec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_argpartvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: argpart_t const &

        push_back(self) -> argpart_t
        """
        return _ida_typeinf.argpartvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.argpartvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.argpartvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.argpartvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> argpart_t

        @param _idx: size_t
        """
        return _ida_typeinf.argpartvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.argpartvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.argpartvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: argpart_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.argpartvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=argpart_t())

        @param x: argpart_t const &
        """
        return _ida_typeinf.argpartvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.argpartvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.argpartvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.argpartvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< argpart_t > &
        """
        return _ida_typeinf.argpartvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> argpart_t
        """
        return _ida_typeinf.argpartvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: argpart_t *
        @param len: size_t
        """
        return _ida_typeinf.argpartvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< argpart_t > const &
        """
        return _ida_typeinf.argpartvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< argpart_t > const &
        """
        return _ida_typeinf.argpartvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> argpart_t
        """
        return _ida_typeinf.argpartvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> argpart_t
        """
        return _ida_typeinf.argpartvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> argpart_t

        @param it: qvector< argpart_t >::iterator
        @param x: argpart_t const &
        """
        return _ida_typeinf.argpartvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> argpart_t

        @param it: qvector< argpart_t >::iterator

        erase(self, first, last) -> argpart_t

        @param first: qvector< argpart_t >::iterator
        @param last: qvector< argpart_t >::iterator
        """
        return _ida_typeinf.argpartvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> argpart_t

        @param x: argpart_t const &

        """
        return _ida_typeinf.argpartvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: argpart_t const &
        """
        return _ida_typeinf.argpartvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: argpart_t const &
        """
        return _ida_typeinf.argpartvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: argpart_t const &

        """
        return _ida_typeinf.argpartvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.argpartvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> argpart_t

        @param i: size_t
        """
        return _ida_typeinf.argpartvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: argpart_t const &
        """
        return _ida_typeinf.argpartvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register argpartvec_t in _ida_typeinf:
_ida_typeinf.argpartvec_t_swigregister(argpartvec_t)

class valstrvec_t(object):
    r"""
    Proxy of C++ qvector< valstr_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> valstrvec_t
        __init__(self, x) -> valstrvec_t

        @param x: qvector< valstr_t > const &
        """
        _ida_typeinf.valstrvec_t_swiginit(self, _ida_typeinf.new_valstrvec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_valstrvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: valstr_t const &

        push_back(self) -> valstr_t
        """
        return _ida_typeinf.valstrvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.valstrvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.valstrvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.valstrvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> valstr_t

        @param _idx: size_t
        """
        return _ida_typeinf.valstrvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.valstrvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.valstrvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: valstr_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.valstrvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=valstr_t())

        @param x: valstr_t const &
        """
        return _ida_typeinf.valstrvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.valstrvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.valstrvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.valstrvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< valstr_t > &
        """
        return _ida_typeinf.valstrvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> valstr_t
        """
        return _ida_typeinf.valstrvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: valstr_t *
        @param len: size_t
        """
        return _ida_typeinf.valstrvec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> valstr_t
        """
        return _ida_typeinf.valstrvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> valstr_t
        """
        return _ida_typeinf.valstrvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> valstr_t

        @param it: qvector< valstr_t >::iterator
        @param x: valstr_t const &
        """
        return _ida_typeinf.valstrvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> valstr_t

        @param it: qvector< valstr_t >::iterator

        erase(self, first, last) -> valstr_t

        @param first: qvector< valstr_t >::iterator
        @param last: qvector< valstr_t >::iterator
        """
        return _ida_typeinf.valstrvec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.valstrvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> valstr_t

        @param i: size_t
        """
        return _ida_typeinf.valstrvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: valstr_t const &
        """
        return _ida_typeinf.valstrvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register valstrvec_t in _ida_typeinf:
_ida_typeinf.valstrvec_t_swigregister(valstrvec_t)

class regobjvec_t(object):
    r"""
    Proxy of C++ qvector< regobj_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> regobjvec_t
        __init__(self, x) -> regobjvec_t

        @param x: qvector< regobj_t > const &
        """
        _ida_typeinf.regobjvec_t_swiginit(self, _ida_typeinf.new_regobjvec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_regobjvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: regobj_t const &

        push_back(self) -> regobj_t
        """
        return _ida_typeinf.regobjvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.regobjvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.regobjvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.regobjvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> regobj_t

        @param _idx: size_t
        """
        return _ida_typeinf.regobjvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.regobjvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.regobjvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: regobj_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.regobjvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=regobj_t())

        @param x: regobj_t const &
        """
        return _ida_typeinf.regobjvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.regobjvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.regobjvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.regobjvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< regobj_t > &
        """
        return _ida_typeinf.regobjvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> regobj_t
        """
        return _ida_typeinf.regobjvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: regobj_t *
        @param len: size_t
        """
        return _ida_typeinf.regobjvec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> regobj_t
        """
        return _ida_typeinf.regobjvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> regobj_t
        """
        return _ida_typeinf.regobjvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> regobj_t

        @param it: qvector< regobj_t >::iterator
        @param x: regobj_t const &
        """
        return _ida_typeinf.regobjvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> regobj_t

        @param it: qvector< regobj_t >::iterator

        erase(self, first, last) -> regobj_t

        @param first: qvector< regobj_t >::iterator
        @param last: qvector< regobj_t >::iterator
        """
        return _ida_typeinf.regobjvec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.regobjvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> regobj_t

        @param i: size_t
        """
        return _ida_typeinf.regobjvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: regobj_t const &
        """
        return _ida_typeinf.regobjvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register regobjvec_t in _ida_typeinf:
_ida_typeinf.regobjvec_t_swigregister(regobjvec_t)

class type_attrs_t(object):
    r"""
    Proxy of C++ qvector< type_attr_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> type_attrs_t
        __init__(self, x) -> type_attrs_t

        @param x: qvector< type_attr_t > const &
        """
        _ida_typeinf.type_attrs_t_swiginit(self, _ida_typeinf.new_type_attrs_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_type_attrs_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: type_attr_t const &

        push_back(self) -> type_attr_t
        """
        return _ida_typeinf.type_attrs_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.type_attrs_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.type_attrs_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.type_attrs_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> type_attr_t

        @param _idx: size_t
        """
        return _ida_typeinf.type_attrs_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.type_attrs_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.type_attrs_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: type_attr_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.type_attrs_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=type_attr_t())

        @param x: type_attr_t const &
        """
        return _ida_typeinf.type_attrs_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.type_attrs_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.type_attrs_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.type_attrs_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< type_attr_t > &
        """
        return _ida_typeinf.type_attrs_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> type_attr_t
        """
        return _ida_typeinf.type_attrs_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: type_attr_t *
        @param len: size_t
        """
        return _ida_typeinf.type_attrs_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> type_attr_t
        """
        return _ida_typeinf.type_attrs_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> type_attr_t
        """
        return _ida_typeinf.type_attrs_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> type_attr_t

        @param it: qvector< type_attr_t >::iterator
        @param x: type_attr_t const &
        """
        return _ida_typeinf.type_attrs_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> type_attr_t

        @param it: qvector< type_attr_t >::iterator

        erase(self, first, last) -> type_attr_t

        @param first: qvector< type_attr_t >::iterator
        @param last: qvector< type_attr_t >::iterator
        """
        return _ida_typeinf.type_attrs_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.type_attrs_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> type_attr_t

        @param i: size_t
        """
        return _ida_typeinf.type_attrs_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: type_attr_t const &
        """
        return _ida_typeinf.type_attrs_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register type_attrs_t in _ida_typeinf:
_ida_typeinf.type_attrs_t_swigregister(type_attrs_t)

class udtmembervec_template_t(object):
    r"""
    Proxy of C++ qvector< udt_member_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> udtmembervec_template_t
        __init__(self, x) -> udtmembervec_template_t

        @param x: qvector< udt_member_t > const &
        """
        _ida_typeinf.udtmembervec_template_t_swiginit(self, _ida_typeinf.new_udtmembervec_template_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_udtmembervec_template_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: udt_member_t const &

        push_back(self) -> udt_member_t
        """
        return _ida_typeinf.udtmembervec_template_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_typeinf.udtmembervec_template_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.udtmembervec_template_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_typeinf.udtmembervec_template_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> udt_member_t

        @param _idx: size_t
        """
        return _ida_typeinf.udtmembervec_template_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_typeinf.udtmembervec_template_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.udtmembervec_template_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: udt_member_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_typeinf.udtmembervec_template_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=udt_member_t())

        @param x: udt_member_t const &
        """
        return _ida_typeinf.udtmembervec_template_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_typeinf.udtmembervec_template_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_typeinf.udtmembervec_template_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_typeinf.udtmembervec_template_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< udt_member_t > &
        """
        return _ida_typeinf.udtmembervec_template_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> udt_member_t
        """
        return _ida_typeinf.udtmembervec_template_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: udt_member_t *
        @param len: size_t
        """
        return _ida_typeinf.udtmembervec_template_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< udt_member_t > const &
        """
        return _ida_typeinf.udtmembervec_template_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< udt_member_t > const &
        """
        return _ida_typeinf.udtmembervec_template_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> udt_member_t
        """
        return _ida_typeinf.udtmembervec_template_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> udt_member_t
        """
        return _ida_typeinf.udtmembervec_template_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> udt_member_t

        @param it: qvector< udt_member_t >::iterator
        @param x: udt_member_t const &
        """
        return _ida_typeinf.udtmembervec_template_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> udt_member_t

        @param it: qvector< udt_member_t >::iterator

        erase(self, first, last) -> udt_member_t

        @param first: qvector< udt_member_t >::iterator
        @param last: qvector< udt_member_t >::iterator
        """
        return _ida_typeinf.udtmembervec_template_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> udt_member_t

        @param x: udt_member_t const &

        """
        return _ida_typeinf.udtmembervec_template_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: udt_member_t const &
        """
        return _ida_typeinf.udtmembervec_template_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: udt_member_t const &
        """
        return _ida_typeinf.udtmembervec_template_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: udt_member_t const &

        """
        return _ida_typeinf.udtmembervec_template_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_typeinf.udtmembervec_template_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> udt_member_t

        @param i: size_t
        """
        return _ida_typeinf.udtmembervec_template_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: udt_member_t const &
        """
        return _ida_typeinf.udtmembervec_template_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register udtmembervec_template_t in _ida_typeinf:
_ida_typeinf.udtmembervec_template_t_swigregister(udtmembervec_template_t)

RESERVED_BYTE = _ida_typeinf.RESERVED_BYTE
r"""
multifunctional purpose
"""


def is_type_const(*args):
    r"""
    is_type_const(t) -> bool
    See BTM_CONST.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_const(*args)

def is_type_volatile(*args):
    r"""
    is_type_volatile(t) -> bool
    See BTM_VOLATILE.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_volatile(*args)

def get_base_type(*args):
    r"""
    get_base_type(t) -> type_t
    Get get basic type bits (TYPE_BASE_MASK)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.get_base_type(*args)

def get_type_flags(*args):
    r"""
    get_type_flags(t) -> type_t
    Get type flags (TYPE_FLAGS_MASK)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.get_type_flags(*args)

def get_full_type(*args):
    r"""
    get_full_type(t) -> type_t
    Get basic type bits + type flags (TYPE_FULL_MASK)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.get_full_type(*args)

def is_typeid_last(*args):
    r"""
    is_typeid_last(t) -> bool
    Is the type_t the last byte of type declaration? (there are no additional bytes
    after a basic type, see _BT_LAST_BASIC)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_typeid_last(*args)

def is_type_partial(*args):
    r"""
    is_type_partial(t) -> bool
    Identifies an unknown or void type with a known size (see Basic type: unknown &
    void)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_partial(*args)

def is_type_void(*args):
    r"""
    is_type_void(t) -> bool
    See BTF_VOID.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_void(*args)

def is_type_unknown(*args):
    r"""
    is_type_unknown(t) -> bool
    See BT_UNKNOWN.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_unknown(*args)

def is_type_ptr(*args):
    r"""
    is_type_ptr(t) -> bool
    See BT_PTR.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_ptr(*args)

def is_type_complex(*args):
    r"""
    is_type_complex(t) -> bool
    See BT_COMPLEX.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_complex(*args)

def is_type_func(*args):
    r"""
    is_type_func(t) -> bool
    See BT_FUNC.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_func(*args)

def is_type_array(*args):
    r"""
    is_type_array(t) -> bool
    See BT_ARRAY.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_array(*args)

def is_type_typedef(*args):
    r"""
    is_type_typedef(t) -> bool
    See BTF_TYPEDEF.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_typedef(*args)

def is_type_sue(*args):
    r"""
    is_type_sue(t) -> bool
    Is the type a struct/union/enum?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_sue(*args)

def is_type_struct(*args):
    r"""
    is_type_struct(t) -> bool
    See BTF_STRUCT.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_struct(*args)

def is_type_union(*args):
    r"""
    is_type_union(t) -> bool
    See BTF_UNION.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_union(*args)

def is_type_struni(*args):
    r"""
    is_type_struni(t) -> bool
    Is the type a struct or union?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_struni(*args)

def is_type_enum(*args):
    r"""
    is_type_enum(t) -> bool
    See BTF_ENUM.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_enum(*args)

def is_type_bitfld(*args):
    r"""
    is_type_bitfld(t) -> bool
    See BT_BITFIELD.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_bitfld(*args)

def is_type_int(*args):
    r"""
    is_type_int(bt) -> bool
    Does the type_t specify one of the basic types in Basic type: integer?

    @param bt: (C++: type_t)
    """
    return _ida_typeinf.is_type_int(*args)

def is_type_int128(*args):
    r"""
    is_type_int128(t) -> bool
    Does the type specify a 128-bit value? (signed or unsigned, see Basic type:
    integer)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_int128(*args)

def is_type_int64(*args):
    r"""
    is_type_int64(t) -> bool
    Does the type specify a 64-bit value? (signed or unsigned, see Basic type:
    integer)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_int64(*args)

def is_type_int32(*args):
    r"""
    is_type_int32(t) -> bool
    Does the type specify a 32-bit value? (signed or unsigned, see Basic type:
    integer)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_int32(*args)

def is_type_int16(*args):
    r"""
    is_type_int16(t) -> bool
    Does the type specify a 16-bit value? (signed or unsigned, see Basic type:
    integer)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_int16(*args)

def is_type_char(*args):
    r"""
    is_type_char(t) -> bool
    Does the type specify a char value? (signed or unsigned, see Basic type:
    integer)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_char(*args)

def is_type_paf(*args):
    r"""
    is_type_paf(t) -> bool
    Is the type a pointer, array, or function type?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_paf(*args)

def is_type_ptr_or_array(*args):
    r"""
    is_type_ptr_or_array(t) -> bool
    Is the type a pointer or array type?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_ptr_or_array(*args)

def is_type_floating(*args):
    r"""
    is_type_floating(t) -> bool
    Is the type a floating point type?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_floating(*args)

def is_type_integral(*args):
    r"""
    is_type_integral(t) -> bool
    Is the type an integral type (char/short/int/long/bool)?

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_integral(*args)

def is_type_ext_integral(*args):
    r"""
    is_type_ext_integral(t) -> bool
    Is the type an extended integral type? (integral or enum)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_ext_integral(*args)

def is_type_arithmetic(*args):
    r"""
    is_type_arithmetic(t) -> bool
    Is the type an arithmetic type? (floating or integral)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_arithmetic(*args)

def is_type_ext_arithmetic(*args):
    r"""
    is_type_ext_arithmetic(t) -> bool
    Is the type an extended arithmetic type? (arithmetic or enum)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_ext_arithmetic(*args)

def is_type_uint(*args):
    r"""
    is_type_uint(t) -> bool
    See BTF_UINT.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uint(*args)

def is_type_uchar(*args):
    r"""
    is_type_uchar(t) -> bool
    See BTF_UCHAR.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uchar(*args)

def is_type_uint16(*args):
    r"""
    is_type_uint16(t) -> bool
    See BTF_UINT16.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uint16(*args)

def is_type_uint32(*args):
    r"""
    is_type_uint32(t) -> bool
    See BTF_UINT32.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uint32(*args)

def is_type_uint64(*args):
    r"""
    is_type_uint64(t) -> bool
    See BTF_UINT64.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uint64(*args)

def is_type_uint128(*args):
    r"""
    is_type_uint128(t) -> bool
    See BTF_UINT128.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_uint128(*args)

def is_type_ldouble(*args):
    r"""
    is_type_ldouble(t) -> bool
    See BTF_LDOUBLE.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_ldouble(*args)

def is_type_double(*args):
    r"""
    is_type_double(t) -> bool
    See BTF_DOUBLE.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_double(*args)

def is_type_float(*args):
    r"""
    is_type_float(t) -> bool
    See BTF_FLOAT.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_float(*args)

def is_type_tbyte(*args):
    r"""
    is_type_tbyte(t) -> bool
    See BTF_FLOAT.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_tbyte(*args)

def is_type_bool(*args):
    r"""
    is_type_bool(t) -> bool
    See BTF_BOOL.

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_type_bool(*args)
TAH_BYTE = _ida_typeinf.TAH_BYTE
r"""
type attribute header byte
"""

FAH_BYTE = _ida_typeinf.FAH_BYTE
r"""
function argument attribute header byte
"""

MAX_DECL_ALIGN = _ida_typeinf.MAX_DECL_ALIGN

TAH_HASATTRS = _ida_typeinf.TAH_HASATTRS
r"""
has extended attributes
"""

TAUDT_UNALIGNED = _ida_typeinf.TAUDT_UNALIGNED

TAUDT_MSSTRUCT = _ida_typeinf.TAUDT_MSSTRUCT

TAUDT_CPPOBJ = _ida_typeinf.TAUDT_CPPOBJ

TAUDT_VFTABLE = _ida_typeinf.TAUDT_VFTABLE

TAFLD_BASECLASS = _ida_typeinf.TAFLD_BASECLASS

TAFLD_UNALIGNED = _ida_typeinf.TAFLD_UNALIGNED

TAFLD_VIRTBASE = _ida_typeinf.TAFLD_VIRTBASE

TAFLD_VFTABLE = _ida_typeinf.TAFLD_VFTABLE

TAFLD_METHOD = _ida_typeinf.TAFLD_METHOD
r"""
denotes a udt member function
"""

TAPTR_PTR32 = _ida_typeinf.TAPTR_PTR32

TAPTR_PTR64 = _ida_typeinf.TAPTR_PTR64

TAPTR_RESTRICT = _ida_typeinf.TAPTR_RESTRICT

TAPTR_SHIFTED = _ida_typeinf.TAPTR_SHIFTED

TAENUM_64BIT = _ida_typeinf.TAENUM_64BIT

TAENUM_UNSIGNED = _ida_typeinf.TAENUM_UNSIGNED

TAENUM_SIGNED = _ida_typeinf.TAENUM_SIGNED

TAH_ALL = _ida_typeinf.TAH_ALL
r"""
all defined bits
"""


def is_tah_byte(*args):
    r"""
    is_tah_byte(t) -> bool
    The TAH byte (type attribute header byte) denotes the start of type attributes.
    (see "tah-typeattrs" in the type bit definitions)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_tah_byte(*args)

def is_sdacl_byte(*args):
    r"""
    is_sdacl_byte(t) -> bool
    Identify an sdacl byte. The first sdacl byte has the following format: 11xx000x.
    The sdacl bytes are appended to udt fields. They indicate the start of type
    attributes (as the tah-bytes do). The sdacl bytes are used in the udt headers
    instead of the tah-byte. This is done for compatibility with old databases, they
    were already using sdacl bytes in udt headers and as udt field postfixes. (see
    "sdacl-typeattrs" in the type bit definitions)

    @param t: (C++: type_t)
    """
    return _ida_typeinf.is_sdacl_byte(*args)
class type_attr_t(object):
    r"""
    Proxy of C++ type_attr_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    key = property(_ida_typeinf.type_attr_t_key_get, _ida_typeinf.type_attr_t_key_set, doc=r"""key""")
    r"""
    one symbol keys are reserved to be used by the kernel the ones starting with an
    underscore are reserved too
    """
    value = property(_ida_typeinf.type_attr_t_value_get, _ida_typeinf.type_attr_t_value_set, doc=r"""value""")
    r"""
    attribute bytes
    """

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: type_attr_t const &
        """
        return _ida_typeinf.type_attr_t___lt__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: type_attr_t const &
        """
        return _ida_typeinf.type_attr_t___ge__(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> type_attr_t
        """
        _ida_typeinf.type_attr_t_swiginit(self, _ida_typeinf.new_type_attr_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_type_attr_t

# Register type_attr_t in _ida_typeinf:
_ida_typeinf.type_attr_t_swigregister(type_attr_t)
cvar = _ida_typeinf.cvar
TYPE_BASE_MASK = cvar.TYPE_BASE_MASK
r"""
the low 4 bits define the basic type
"""
TYPE_FLAGS_MASK = cvar.TYPE_FLAGS_MASK
r"""
type flags - they have different meaning depending on the basic type
"""
TYPE_MODIF_MASK = cvar.TYPE_MODIF_MASK
r"""
modifiers.
* for BT_ARRAY see Derived type: array
* BT_VOID can have them ONLY in 'void *'
"""
TYPE_FULL_MASK = cvar.TYPE_FULL_MASK
r"""
basic type with type flags
"""
BT_UNK = cvar.BT_UNK
r"""
unknown
"""
BT_VOID = cvar.BT_VOID
r"""
void
"""
BTMT_SIZE0 = cvar.BTMT_SIZE0
r"""
BT_VOID - normal void; BT_UNK - don't use
"""
BTMT_SIZE12 = cvar.BTMT_SIZE12
r"""
size = 1 byte if BT_VOID; 2 if BT_UNK
"""
BTMT_SIZE48 = cvar.BTMT_SIZE48
r"""
size = 4 bytes if BT_VOID; 8 if BT_UNK
"""
BTMT_SIZE128 = cvar.BTMT_SIZE128
r"""
size = 16 bytes if BT_VOID; unknown if BT_UNK (IN struct alignment - see below)
"""
BT_INT8 = cvar.BT_INT8
r"""
__int8
"""
BT_INT16 = cvar.BT_INT16
r"""
__int16
"""
BT_INT32 = cvar.BT_INT32
r"""
__int32
"""
BT_INT64 = cvar.BT_INT64
r"""
__int64
"""
BT_INT128 = cvar.BT_INT128
r"""
__int128 (for alpha & future use)
"""
BT_INT = cvar.BT_INT
r"""
natural int. (size provided by idp module)
"""
BTMT_UNKSIGN = cvar.BTMT_UNKSIGN
r"""
unknown signedness
"""
BTMT_SIGNED = cvar.BTMT_SIGNED
r"""
signed
"""
BTMT_USIGNED = cvar.BTMT_USIGNED
r"""
unsigned
"""
BTMT_UNSIGNED = cvar.BTMT_UNSIGNED
BTMT_CHAR = cvar.BTMT_CHAR
r"""
specify char or segment register
* BT_INT8 - char
* BT_INT - segment register
* other BT_INT... - don't use
"""
BT_BOOL = cvar.BT_BOOL
r"""
bool
"""
BTMT_DEFBOOL = cvar.BTMT_DEFBOOL
r"""
size is model specific or unknown(?)
"""
BTMT_BOOL1 = cvar.BTMT_BOOL1
r"""
size 1byte
"""
BTMT_BOOL2 = cvar.BTMT_BOOL2
r"""
size 2bytes - !inf_is_64bit()
"""
BTMT_BOOL8 = cvar.BTMT_BOOL8
r"""
size 8bytes - inf_is_64bit()
"""
BTMT_BOOL4 = cvar.BTMT_BOOL4
r"""
size 4bytes
"""
BT_FLOAT = cvar.BT_FLOAT
r"""
float
"""
BTMT_FLOAT = cvar.BTMT_FLOAT
r"""
float (4 bytes)
"""
BTMT_DOUBLE = cvar.BTMT_DOUBLE
r"""
double (8 bytes)
"""
BTMT_LNGDBL = cvar.BTMT_LNGDBL
r"""
long double (compiler specific)
"""
BTMT_SPECFLT = cvar.BTMT_SPECFLT
r"""
float (variable size). if processor_t::use_tbyte() then use
processor_t::tbyte_size, otherwise 2 bytes
"""
_BT_LAST_BASIC = cvar._BT_LAST_BASIC
r"""
the last basic type, all basic types may be followed by [tah-typeattrs]
"""
BT_PTR = cvar.BT_PTR
r"""
pointer. has the following format: [db sizeof(ptr)]; [tah-typeattrs]; type_t...
"""
BTMT_DEFPTR = cvar.BTMT_DEFPTR
r"""
default for model
"""
BTMT_NEAR = cvar.BTMT_NEAR
r"""
near
"""
BTMT_FAR = cvar.BTMT_FAR
r"""
far
"""
BTMT_CLOSURE = cvar.BTMT_CLOSURE
r"""
closure.
* if ptr to BT_FUNC - __closure. in this case next byte MUST be RESERVED_BYTE,
and after it BT_FUNC
* else the next byte contains sizeof(ptr) allowed values are 1 - ph.max_ptr_size
* if value is bigger than ph.max_ptr_size, based_ptr_name_and_size() is called
to find out the typeinfo
"""
BT_ARRAY = cvar.BT_ARRAY
r"""
array
"""
BTMT_NONBASED = cvar.BTMT_NONBASED
r"""
if set
array base==0
format: dt num_elem; [tah-typeattrs]; type_t...
if num_elem==0 then the array size is unknown
else
format: da num_elem, base; [tah-typeattrs]; type_t...
used only for serialization
"""
BTMT_ARRESERV = cvar.BTMT_ARRESERV
r"""
reserved bit
"""
BT_FUNC = cvar.BT_FUNC
r"""
function. format:
optional: CM_CC_SPOILED | num_of_spoiled_regs
                if num_of_spoiled_reg == BFA_FUNC_MARKER:
                  ::bfa_byte
                  if (bfa_byte & BFA_FUNC_EXT_FORMAT) != 0
                   ::fti_bits (only low bits: FTI_SPOILED,...,FTI_VIRTUAL)
                   num_of_spoiled_reg times: spoiled reg info (see
extract_spoiledreg)
                  else
                    bfa_byte is function attribute byte (see Function attribute
byte...)
                else:
                  num_of_spoiled_reg times: spoiled reg info (see
extract_spoiledreg)
      cm_t ... calling convention and memory model
      [tah-typeattrs];
      type_t ... return type;
      [serialized argloc_t of returned value (if CM_CC_SPECIAL{PE} && !return
void);
      if !CM_CC_VOIDARG:
        dt N (N=number of parameters)
        if ( N == 0 )
        if CM_CC_ELLIPSIS or CM_CC_SPECIALE
            func(...)
          else
            parameters are unknown
        else
          N records:
            type_t ... (i.e. type of each parameter)
            [serialized argloc_t (if CM_CC_SPECIAL{PE})] (i.e. place of each
parameter)
            [FAH_BYTE + de( funcarg_t::flags )]
"""
BTMT_DEFCALL = cvar.BTMT_DEFCALL
r"""
call method - default for model or unknown
"""
BTMT_NEARCALL = cvar.BTMT_NEARCALL
r"""
function returns by retn
"""
BTMT_FARCALL = cvar.BTMT_FARCALL
r"""
function returns by retf
"""
BTMT_INTCALL = cvar.BTMT_INTCALL
r"""
function returns by iret in this case cc MUST be 'unknown'
"""
BT_COMPLEX = cvar.BT_COMPLEX
r"""
struct/union/enum/typedef. format:
[dt N (N=field count) if !BTMT_TYPEDEF]
       if N == 0:
         p_string name (unnamed types have names "anon_...")
         [sdacl-typeattrs];
       else, for struct & union:
         if N == 0x7FFE   // Support for high (i.e., > 4095) members count
           N = deserialize_de()
         ALPOW = N & 0x7
         MCNT = N >> 3
         if MCNT == 0
           empty struct
         if ALPOW == 0
           ALIGN = get_default_align()
         else
           ALIGN = (1 << (ALPOW - 1))
         [sdacl-typeattrs];
       else, for enums:
         if N == 0x7FFE   // Support for high enum entries count.
           N = deserialize_de()
         [tah-typeattrs];
"""
BTMT_STRUCT = cvar.BTMT_STRUCT
BTMT_UNION = cvar.BTMT_UNION
BTMT_ENUM = cvar.BTMT_ENUM
BTMT_TYPEDEF = cvar.BTMT_TYPEDEF
r"""
named reference always p_string name
"""
BT_BITFIELD = cvar.BT_BITFIELD
r"""
bitfield (only in struct) ['bitmasked' enum see below] next byte is dt ((size in
bits << 1) | (unsigned ? 1 : 0))
"""
BTMT_BFLDI8 = cvar.BTMT_BFLDI8
r"""
__int8
"""
BTMT_BFLDI16 = cvar.BTMT_BFLDI16
r"""
__int16
"""
BTMT_BFLDI32 = cvar.BTMT_BFLDI32
r"""
__int32
"""
BTMT_BFLDI64 = cvar.BTMT_BFLDI64
r"""
__int64
"""
BT_RESERVED = cvar.BT_RESERVED
r"""
RESERVED.
"""
BTM_CONST = cvar.BTM_CONST
r"""
const
"""
BTM_VOLATILE = cvar.BTM_VOLATILE
r"""
volatile
"""
BTE_SIZE_MASK = cvar.BTE_SIZE_MASK
r"""
storage size.
* if == 0 then inf_get_cc_size_e()
* else 1 << (n -1) = 1,2,4...64
"""
BTE_RESERVED = cvar.BTE_RESERVED
r"""
must be 0, in order to distinguish from a tah-byte
"""
BTE_BITFIELD = cvar.BTE_BITFIELD
r"""
'subarrays'. In this case ANY record has the following format:
* 'de' mask (has name)
* 'dt' cnt
* cnt records of 'de' values (cnt CAN be 0)
@note: delta for ALL subsegment is ONE
"""
BTE_OUT_MASK = cvar.BTE_OUT_MASK
r"""
output style mask
"""
BTE_HEX = cvar.BTE_HEX
r"""
hex
"""
BTE_CHAR = cvar.BTE_CHAR
r"""
char or hex
"""
BTE_SDEC = cvar.BTE_SDEC
r"""
signed decimal
"""
BTE_UDEC = cvar.BTE_UDEC
r"""
unsigned decimal
"""
BTE_ALWAYS = cvar.BTE_ALWAYS
r"""
this bit MUST be present
"""
BT_SEGREG = cvar.BT_SEGREG
r"""
segment register
"""
BT_UNK_BYTE = cvar.BT_UNK_BYTE
r"""
1 byte
"""
BT_UNK_WORD = cvar.BT_UNK_WORD
r"""
2 bytes
"""
BT_UNK_DWORD = cvar.BT_UNK_DWORD
r"""
4 bytes
"""
BT_UNK_QWORD = cvar.BT_UNK_QWORD
r"""
8 bytes
"""
BT_UNK_OWORD = cvar.BT_UNK_OWORD
r"""
16 bytes
"""
BT_UNKNOWN = cvar.BT_UNKNOWN
r"""
unknown size - for parameters
"""
BTF_BYTE = cvar.BTF_BYTE
r"""
byte
"""
BTF_UNK = cvar.BTF_UNK
r"""
unknown
"""
BTF_VOID = cvar.BTF_VOID
r"""
void
"""
BTF_INT8 = cvar.BTF_INT8
r"""
signed byte
"""
BTF_CHAR = cvar.BTF_CHAR
r"""
signed char
"""
BTF_UCHAR = cvar.BTF_UCHAR
r"""
unsigned char
"""
BTF_UINT8 = cvar.BTF_UINT8
r"""
unsigned byte
"""
BTF_INT16 = cvar.BTF_INT16
r"""
signed short
"""
BTF_UINT16 = cvar.BTF_UINT16
r"""
unsigned short
"""
BTF_INT32 = cvar.BTF_INT32
r"""
signed int
"""
BTF_UINT32 = cvar.BTF_UINT32
r"""
unsigned int
"""
BTF_INT64 = cvar.BTF_INT64
r"""
signed long
"""
BTF_UINT64 = cvar.BTF_UINT64
r"""
unsigned long
"""
BTF_INT128 = cvar.BTF_INT128
r"""
signed 128-bit value
"""
BTF_UINT128 = cvar.BTF_UINT128
r"""
unsigned 128-bit value
"""
BTF_INT = cvar.BTF_INT
r"""
int, unknown signedness
"""
BTF_UINT = cvar.BTF_UINT
r"""
unsigned int
"""
BTF_SINT = cvar.BTF_SINT
r"""
singed int
"""
BTF_BOOL = cvar.BTF_BOOL
r"""
boolean
"""
BTF_FLOAT = cvar.BTF_FLOAT
r"""
float
"""
BTF_DOUBLE = cvar.BTF_DOUBLE
r"""
double
"""
BTF_LDOUBLE = cvar.BTF_LDOUBLE
r"""
long double
"""
BTF_TBYTE = cvar.BTF_TBYTE
r"""
see BTMT_SPECFLT
"""
BTF_STRUCT = cvar.BTF_STRUCT
r"""
struct
"""
BTF_UNION = cvar.BTF_UNION
r"""
union
"""
BTF_ENUM = cvar.BTF_ENUM
r"""
enum
"""
BTF_TYPEDEF = cvar.BTF_TYPEDEF
r"""
typedef
"""


def append_argloc(*args):
    r"""
    append_argloc(out, vloc) -> bool
    Serialize argument location

    @param out: (C++: qtype *)
    @param vloc: (C++: const argloc_t &) argloc_t const &
    """
    return _ida_typeinf.append_argloc(*args)

def extract_argloc(*args):
    r"""
    extract_argloc(vloc, ptype, forbid_stkoff) -> bool
    Deserialize an argument location. Argument FORBID_STKOFF checks location type.
    It can be used, for example, to check the return location of a function that
    cannot return a value in the stack

    @param vloc: (C++: argloc_t *)
    @param ptype: (C++: const type_t **) type_t const **
    @param forbid_stkoff: (C++: bool)
    """
    return _ida_typeinf.extract_argloc(*args)

def resolve_typedef(*args):
    r"""
    resolve_typedef(til, type) -> type_t const *

    @param til: til_t const *
    @param type: type_t const *
    """
    return _ida_typeinf.resolve_typedef(*args)

def is_restype_void(*args):
    r"""
    is_restype_void(til, type) -> bool

    @param til: til_t const *
    @param type: type_t const *
    """
    return _ida_typeinf.is_restype_void(*args)

def is_restype_enum(*args):
    r"""
    is_restype_enum(til, type) -> bool

    @param til: til_t const *
    @param type: type_t const *
    """
    return _ida_typeinf.is_restype_enum(*args)

def is_restype_struni(*args):
    r"""
    is_restype_struni(til, type) -> bool

    @param til: til_t const *
    @param type: type_t const *
    """
    return _ida_typeinf.is_restype_struni(*args)

def is_restype_struct(*args):
    r"""
    is_restype_struct(til, type) -> bool

    @param til: til_t const *
    @param type: type_t const *
    """
    return _ida_typeinf.is_restype_struct(*args)

def get_scalar_bt(*args):
    r"""
    get_scalar_bt(size) -> type_t

    @param size: int
    """
    return _ida_typeinf.get_scalar_bt(*args)
class til_t(object):
    r"""
    Proxy of C++ til_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = property(_ida_typeinf.til_t_name_get, _ida_typeinf.til_t_name_set, doc=r"""name""")
    r"""
    short file name (without path and extension)
    """
    desc = property(_ida_typeinf.til_t_desc_get, _ida_typeinf.til_t_desc_set, doc=r"""desc""")
    r"""
    human readable til description
    """
    nbases = property(_ida_typeinf.til_t_nbases_get, _ida_typeinf.til_t_nbases_set, doc=r"""nbases""")
    r"""
    number of base tils
    """
    flags = property(_ida_typeinf.til_t_flags_get, _ida_typeinf.til_t_flags_set, doc=r"""flags""")
    r"""
    Type info library property bits
    """

    def is_dirty(self, *args):
        r"""
        is_dirty(self) -> bool
        Has the til been modified? (TIL_MOD)
        """
        return _ida_typeinf.til_t_is_dirty(self, *args)

    def set_dirty(self, *args):
        r"""
        set_dirty(self)
        Mark the til as modified (TIL_MOD)
        """
        return _ida_typeinf.til_t_set_dirty(self, *args)
    cc = property(_ida_typeinf.til_t_cc_get, _ida_typeinf.til_t_cc_set, doc=r"""cc""")
    r"""
    information about the target compiler
    """
    nrefs = property(_ida_typeinf.til_t_nrefs_get, _ida_typeinf.til_t_nrefs_set, doc=r"""nrefs""")
    r"""
    number of references to the til
    """
    nstreams = property(_ida_typeinf.til_t_nstreams_get, _ida_typeinf.til_t_nstreams_set, doc=r"""nstreams""")
    r"""
    number of extra streams
    """
    streams = property(_ida_typeinf.til_t_streams_get, _ida_typeinf.til_t_streams_set, doc=r"""streams""")
    r"""
    symbol stream storage
    """

    def base(self, *args):
        r"""
        base(self, n) -> til_t
        tils that our til is based on

        @param n: int
        """
        return _ida_typeinf.til_t_base(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> til_t
        """
        _ida_typeinf.til_t_swiginit(self, _ida_typeinf.new_til_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_til_t

# Register til_t in _ida_typeinf:
_ida_typeinf.til_t_swigregister(til_t)
no_sign = cvar.no_sign
r"""
no sign, or unknown
"""
type_signed = cvar.type_signed
r"""
signed type
"""
type_unsigned = cvar.type_unsigned
r"""
unsigned type
"""
TIL_ZIP = _ida_typeinf.TIL_ZIP
r"""
pack buckets using zip
"""

TIL_MAC = _ida_typeinf.TIL_MAC
r"""
til has macro table
"""

TIL_ESI = _ida_typeinf.TIL_ESI
r"""
extended sizeof info (short, long, longlong)
"""

TIL_UNI = _ida_typeinf.TIL_UNI
r"""
universal til for any compiler
"""

TIL_ORD = _ida_typeinf.TIL_ORD
r"""
type ordinal numbers are present
"""

TIL_ALI = _ida_typeinf.TIL_ALI
r"""
type aliases are present (this bit is used only on the disk)
"""

TIL_MOD = _ida_typeinf.TIL_MOD
r"""
til has been modified, should be saved
"""

TIL_STM = _ida_typeinf.TIL_STM
r"""
til has extra streams
"""

TIL_SLD = _ida_typeinf.TIL_SLD
r"""
sizeof(long double)
"""



def new_til(*args):
    r"""
    new_til(name, desc) -> til_t
    Initialize a til.

    @param name: (C++: const char *) char const *
    @param desc: (C++: const char *) char const *
    """
    return _ida_typeinf.new_til(*args)
TIL_ADD_FAILED = _ida_typeinf.TIL_ADD_FAILED
r"""
see errbuf
"""

TIL_ADD_OK = _ida_typeinf.TIL_ADD_OK
r"""
some tils were added
"""

TIL_ADD_ALREADY = _ida_typeinf.TIL_ADD_ALREADY
r"""
the base til was already added
"""


def load_til(*args):
    r"""
    load_til(name, tildir=None) -> til_t
    Load til from a file without adding it to the database list (see also add_til).
    Failure to load base tils are reported into 'errbuf'. They do not prevent
    loading of the main til.

    @param name: (C++: const char *) filename of the til. If it's an absolute path, tildir is ignored.
    * NB: the file extension is forced to .til
    @param tildir: (C++: const char *) directory where to load the til from. nullptr means default til
                   subdirectories.
    @return: pointer to resulting til, nullptr if failed and error message is in
             errbuf
    """
    return _ida_typeinf.load_til(*args)

def compact_til(*args):
    r"""
    compact_til(ti) -> bool
    Collect garbage in til. Must be called before storing the til.

    @param ti: (C++: til_t *)
    @return: true if any memory was freed
    """
    return _ida_typeinf.compact_til(*args)

def store_til(*args):
    r"""
    store_til(ti, tildir, name) -> bool
    Store til to a file. If the til contains garbage, it will be collected before
    storing the til. Your plugin should call compact_til() before calling
    store_til().

    @param ti: (C++: til_t *) type library to store
    @param tildir: (C++: const char *) directory where to store the til. nullptr means current
                   directory.
    @param name: (C++: const char *) filename of the til. If it's an absolute path, tildir is ignored.
    * NB: the file extension is forced to .til
    @return: success
    """
    return _ida_typeinf.store_til(*args)

def free_til(*args):
    r"""
    free_til(ti)
    Free memory allocated by til.

    @param ti: (C++: til_t *)
    """
    return _ida_typeinf.free_til(*args)

def load_til_header(*args):
    r"""
    load_til_header(tildir, name) -> til_t
    Get human-readable til description.

    @param tildir: (C++: const char *) char const *
    @param name: (C++: const char *) char const *
    """
    return _ida_typeinf.load_til_header(*args)

def is_code_far(*args):
    r"""
    is_code_far(cm) -> bool
    Does the given model specify far code?.

    @param cm: (C++: cm_t)
    """
    return _ida_typeinf.is_code_far(*args)

def is_data_far(*args):
    r"""
    is_data_far(cm) -> bool
    Does the given model specify far data?.

    @param cm: (C++: cm_t)
    """
    return _ida_typeinf.is_data_far(*args)
class rrel_t(object):
    r"""
    Proxy of C++ rrel_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    off = property(_ida_typeinf.rrel_t_off_get, _ida_typeinf.rrel_t_off_set, doc=r"""off""")
    r"""
    displacement from the address pointed by the register
    """
    reg = property(_ida_typeinf.rrel_t_reg_get, _ida_typeinf.rrel_t_reg_set, doc=r"""reg""")
    r"""
    register index (into ph.reg_names)
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> rrel_t
        """
        _ida_typeinf.rrel_t_swiginit(self, _ida_typeinf.new_rrel_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_rrel_t

# Register rrel_t in _ida_typeinf:
_ida_typeinf.rrel_t_swigregister(rrel_t)
CM_MASK = cvar.CM_MASK
CM_UNKNOWN = cvar.CM_UNKNOWN
r"""
unknown
"""
CM_N8_F16 = cvar.CM_N8_F16
r"""
if sizeof(int)<=2: near 1 byte, far 2 bytes
"""
CM_N64 = cvar.CM_N64
r"""
if sizeof(int)>2: near 8 bytes, far 8 bytes
"""
CM_N16_F32 = cvar.CM_N16_F32
r"""
near 2 bytes, far 4 bytes
"""
CM_N32_F48 = cvar.CM_N32_F48
r"""
near 4 bytes, far 6 bytes
"""
CM_M_MASK = cvar.CM_M_MASK
CM_M_NN = cvar.CM_M_NN
CM_M_FF = cvar.CM_M_FF
CM_M_NF = cvar.CM_M_NF
CM_M_FN = cvar.CM_M_FN
CM_CC_MASK = cvar.CM_CC_MASK
CM_CC_INVALID = cvar.CM_CC_INVALID
r"""
this value is invalid
"""
CM_CC_UNKNOWN = cvar.CM_CC_UNKNOWN
r"""
unknown calling convention
"""
CM_CC_VOIDARG = cvar.CM_CC_VOIDARG
r"""
function without arguments if has other cc and argnum == 0, represent as f() -
unknown list
"""
CM_CC_CDECL = cvar.CM_CC_CDECL
r"""
stack
"""
CM_CC_ELLIPSIS = cvar.CM_CC_ELLIPSIS
r"""
cdecl + ellipsis
"""
CM_CC_STDCALL = cvar.CM_CC_STDCALL
r"""
stack, purged
"""
CM_CC_PASCAL = cvar.CM_CC_PASCAL
r"""
stack, purged, reverse order of args
"""
CM_CC_FASTCALL = cvar.CM_CC_FASTCALL
r"""
stack, purged (x86), first args are in regs (compiler-dependent)
"""
CM_CC_THISCALL = cvar.CM_CC_THISCALL
r"""
stack, purged (x86), first arg is in reg (compiler-dependent)
"""
CM_CC_MANUAL = cvar.CM_CC_MANUAL
r"""
special case for compiler specific (not used)
"""
CM_CC_SPOILED = cvar.CM_CC_SPOILED
r"""
This is NOT a cc! Mark of __spoil record the low nibble is count and after n
{spoilreg_t} present real cm_t byte. if n == BFA_FUNC_MARKER, the next byte is
the function attribute byte.
"""
CM_CC_GOLANG = cvar.CM_CC_GOLANG
CM_CC_RESERVE3 = cvar.CM_CC_RESERVE3
CM_CC_SPECIALE = cvar.CM_CC_SPECIALE
r"""
CM_CC_SPECIAL with ellipsis
"""
CM_CC_SPECIALP = cvar.CM_CC_SPECIALP
r"""
Equal to CM_CC_SPECIAL, but with purged stack.
"""
CM_CC_SPECIAL = cvar.CM_CC_SPECIAL
BFA_NORET = cvar.BFA_NORET
r"""
__noreturn
"""
BFA_PURE = cvar.BFA_PURE
r"""
__pure
"""
BFA_HIGH = cvar.BFA_HIGH
r"""
high level prototype (with possibly hidden args)
"""
BFA_STATIC = cvar.BFA_STATIC
r"""
static
"""
BFA_VIRTUAL = cvar.BFA_VIRTUAL
r"""
virtual
"""
BFA_FUNC_MARKER = cvar.BFA_FUNC_MARKER
r"""
This is NOT a cc! (used internally as a marker)
"""
BFA_FUNC_EXT_FORMAT = cvar.BFA_FUNC_EXT_FORMAT
r"""
This is NOT a real attribute (used internally as marker for extended format)
"""
ALOC_NONE = cvar.ALOC_NONE
r"""
none
"""
ALOC_STACK = cvar.ALOC_STACK
r"""
stack offset
"""
ALOC_DIST = cvar.ALOC_DIST
r"""
distributed (scattered)
"""
ALOC_REG1 = cvar.ALOC_REG1
r"""
one register (and offset within it)
"""
ALOC_REG2 = cvar.ALOC_REG2
r"""
register pair
"""
ALOC_RREL = cvar.ALOC_RREL
r"""
register relative
"""
ALOC_STATIC = cvar.ALOC_STATIC
r"""
global address
"""
ALOC_CUSTOM = cvar.ALOC_CUSTOM
r"""
custom argloc (7 or higher)
"""

class argloc_t(object):
    r"""
    Proxy of C++ argloc_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> argloc_t
        __init__(self, r) -> argloc_t

        @param r: argloc_t const &
        """
        _ida_typeinf.argloc_t_swiginit(self, _ida_typeinf.new_argloc_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_argloc_t

    def swap(self, *args):
        r"""
        swap(self, r)
        Assign this == r and r == this.

        @param r: (C++: argloc_t &)
        """
        return _ida_typeinf.argloc_t_swap(self, *args)

    def atype(self, *args):
        r"""
        atype(self) -> argloc_type_t
        Get type (Argument location types)
        """
        return _ida_typeinf.argloc_t_atype(self, *args)

    def is_reg1(self, *args):
        r"""
        is_reg1(self) -> bool
        See ALOC_REG1.
        """
        return _ida_typeinf.argloc_t_is_reg1(self, *args)

    def is_reg2(self, *args):
        r"""
        is_reg2(self) -> bool
        See ALOC_REG2.
        """
        return _ida_typeinf.argloc_t_is_reg2(self, *args)

    def is_reg(self, *args):
        r"""
        is_reg(self) -> bool
        is_reg1() || is_reg2()
        """
        return _ida_typeinf.argloc_t_is_reg(self, *args)

    def is_rrel(self, *args):
        r"""
        is_rrel(self) -> bool
        See ALOC_RREL.
        """
        return _ida_typeinf.argloc_t_is_rrel(self, *args)

    def is_ea(self, *args):
        r"""
        is_ea(self) -> bool
        See ALOC_STATIC.
        """
        return _ida_typeinf.argloc_t_is_ea(self, *args)

    def is_stkoff(self, *args):
        r"""
        is_stkoff(self) -> bool
        See ALOC_STACK.
        """
        return _ida_typeinf.argloc_t_is_stkoff(self, *args)

    def is_scattered(self, *args):
        r"""
        is_scattered(self) -> bool
        See ALOC_DIST.
        """
        return _ida_typeinf.argloc_t_is_scattered(self, *args)

    def has_reg(self, *args):
        r"""
        has_reg(self) -> bool
        TRUE if argloc has a register part.
        """
        return _ida_typeinf.argloc_t_has_reg(self, *args)

    def has_stkoff(self, *args):
        r"""
        has_stkoff(self) -> bool
        TRUE if argloc has a stack part.
        """
        return _ida_typeinf.argloc_t_has_stkoff(self, *args)

    def is_mixed_scattered(self, *args):
        r"""
        is_mixed_scattered(self) -> bool
        mixed scattered: consists of register and stack parts
        """
        return _ida_typeinf.argloc_t_is_mixed_scattered(self, *args)

    def in_stack(self, *args):
        r"""
        in_stack(self) -> bool
        TRUE if argloc is in stack entirely.
        """
        return _ida_typeinf.argloc_t_in_stack(self, *args)

    def is_fragmented(self, *args):
        r"""
        is_fragmented(self) -> bool
        is_scattered() || is_reg2()
        """
        return _ida_typeinf.argloc_t_is_fragmented(self, *args)

    def is_custom(self, *args):
        r"""
        is_custom(self) -> bool
        See ALOC_CUSTOM.
        """
        return _ida_typeinf.argloc_t_is_custom(self, *args)

    def is_badloc(self, *args):
        r"""
        is_badloc(self) -> bool
        See ALOC_NONE.
        """
        return _ida_typeinf.argloc_t_is_badloc(self, *args)

    def reg1(self, *args):
        r"""
        reg1(self) -> int
        Get the register info. Use when atype() == ALOC_REG1 or ALOC_REG2
        """
        return _ida_typeinf.argloc_t_reg1(self, *args)

    def regoff(self, *args):
        r"""
        regoff(self) -> int
        Get offset from the beginning of the register in bytes. Use when atype() ==
        ALOC_REG1
        """
        return _ida_typeinf.argloc_t_regoff(self, *args)

    def reg2(self, *args):
        r"""
        reg2(self) -> int
        Get info for the second register. Use when atype() == ALOC_REG2
        """
        return _ida_typeinf.argloc_t_reg2(self, *args)

    def get_reginfo(self, *args):
        r"""
        get_reginfo(self) -> uint32
        Get all register info. Use when atype() == ALOC_REG1 or ALOC_REG2
        """
        return _ida_typeinf.argloc_t_get_reginfo(self, *args)

    def stkoff(self, *args):
        r"""
        stkoff(self) -> sval_t
        Get the stack offset. Use if atype() == ALOC_STACK
        """
        return _ida_typeinf.argloc_t_stkoff(self, *args)

    def get_ea(self, *args):
        r"""
        get_ea(self) -> ea_t
        Get the global address. Use when atype() == ALOC_STATIC
        """
        return _ida_typeinf.argloc_t_get_ea(self, *args)

    def scattered(self, *args):
        r"""
        scattered(self) -> scattered_aloc_t
        Get scattered argument info. Use when atype() == ALOC_DIST
        """
        return _ida_typeinf.argloc_t_scattered(self, *args)

    def get_rrel(self, *args):
        r"""
        get_rrel(self) -> rrel_t
        Get register-relative info. Use when atype() == ALOC_RREL
        """
        return _ida_typeinf.argloc_t_get_rrel(self, *args)

    def get_custom(self, *args):
        r"""
        get_custom(self) -> void *
        Get custom argloc info. Use if atype() == ALOC_CUSTOM
        """
        return _ida_typeinf.argloc_t_get_custom(self, *args)

    def get_biggest(self, *args):
        r"""
        get_biggest(self) -> argloc_t::biggest_t
        Get largest element in internal union.
        """
        return _ida_typeinf.argloc_t_get_biggest(self, *args)

    def _set_badloc(self, *args):
        r"""_set_badloc(self)"""
        return _ida_typeinf.argloc_t__set_badloc(self, *args)

    def _set_reg1(self, *args):
        r"""
        _set_reg1(self, reg, off=0)

        Parameters
        ----------
        reg: int
        off: int

        """
        return _ida_typeinf.argloc_t__set_reg1(self, *args)

    def _set_reg2(self, *args):
        r"""
        _set_reg2(self, _reg1, _reg2)

        Parameters
        ----------
        _reg1: int
        _reg2: int

        """
        return _ida_typeinf.argloc_t__set_reg2(self, *args)

    def _set_stkoff(self, *args):
        r"""
        _set_stkoff(self, off)

        Parameters
        ----------
        off: sval_t

        """
        return _ida_typeinf.argloc_t__set_stkoff(self, *args)

    def _set_ea(self, *args):
        r"""
        _set_ea(self, _ea)

        Parameters
        ----------
        _ea: ea_t

        """
        return _ida_typeinf.argloc_t__set_ea(self, *args)

    def _consume_rrel(self, *args):
        r"""
        _consume_rrel(self, p) -> bool

        Parameters
        ----------
        p: rrel_t *

        """
        return _ida_typeinf.argloc_t__consume_rrel(self, *args)

    def _consume_scattered(self, *args):
        r"""
        _consume_scattered(self, p) -> bool

        Parameters
        ----------
        p: scattered_aloc_t *

        """
        return _ida_typeinf.argloc_t__consume_scattered(self, *args)

    def _set_custom(self, *args):
        r"""
        _set_custom(self, ct, pdata)

        Parameters
        ----------
        ct: argloc_type_t
        pdata: void *

        """
        return _ida_typeinf.argloc_t__set_custom(self, *args)

    def _set_biggest(self, *args):
        r"""
        _set_biggest(self, ct, data)

        Parameters
        ----------
        ct: argloc_type_t
        data: argloc_t::biggest_t

        """
        return _ida_typeinf.argloc_t__set_biggest(self, *args)

    def set_reg1(self, *args):
        r"""
        set_reg1(self, reg, off=0)
        Set register location.

        @param reg: (C++: int)
        @param off: (C++: int)
        """
        return _ida_typeinf.argloc_t_set_reg1(self, *args)

    def set_reg2(self, *args):
        r"""
        set_reg2(self, _reg1, _reg2)
        Set secondary register location.

        @param _reg1: (C++: int)
        @param _reg2: (C++: int)
        """
        return _ida_typeinf.argloc_t_set_reg2(self, *args)

    def set_stkoff(self, *args):
        r"""
        set_stkoff(self, off)
        Set stack offset location.

        @param off: (C++: sval_t)
        """
        return _ida_typeinf.argloc_t_set_stkoff(self, *args)

    def set_ea(self, *args):
        r"""
        set_ea(self, _ea)
        Set static ea location.

        @param _ea: (C++: ea_t)
        """
        return _ida_typeinf.argloc_t_set_ea(self, *args)

    def consume_rrel(self, *args):
        r"""
        consume_rrel(self, p)
        Set register-relative location - can't be nullptr.

        @param p: (C++: rrel_t *)
        """
        return _ida_typeinf.argloc_t_consume_rrel(self, *args)

    def set_badloc(self, *args):
        r"""
        set_badloc(self)
        Set to invalid location.
        """
        return _ida_typeinf.argloc_t_set_badloc(self, *args)

    def calc_offset(self, *args):
        r"""
        calc_offset(self) -> sval_t
        Calculate offset that can be used to compare 2 similar arglocs.
        """
        return _ida_typeinf.argloc_t_calc_offset(self, *args)

    def advance(self, *args):
        r"""
        advance(self, delta) -> bool
        Move the location to point 'delta' bytes further.

        @param delta: (C++: int)
        """
        return _ida_typeinf.argloc_t_advance(self, *args)

    def align_reg_high(self, *args):
        r"""
        align_reg_high(self, size, _slotsize)
        Set register offset to align it to the upper part of _SLOTSIZE.

        @param size: (C++: size_t)
        @param _slotsize: (C++: size_t)
        """
        return _ida_typeinf.argloc_t_align_reg_high(self, *args)

    def align_stkoff_high(self, *args):
        r"""
        align_stkoff_high(self, size, _slotsize)
        Set stack offset to align to the upper part of _SLOTSIZE.

        @param size: (C++: size_t)
        @param _slotsize: (C++: size_t)
        """
        return _ida_typeinf.argloc_t_align_stkoff_high(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: argloc_t const &
        """
        return _ida_typeinf.argloc_t_compare(self, *args)

    def consume_scattered(self, *args):
        r"""
        consume_scattered(self, p)
        Set distributed argument location.

        @param p: (C++: scattered_aloc_t *) scattered_aloc_t const &
        """
        return _ida_typeinf.argloc_t_consume_scattered(self, *args)

# Register argloc_t in _ida_typeinf:
_ida_typeinf.argloc_t_swigregister(argloc_t)

class argpart_t(argloc_t):
    r"""
    Proxy of C++ argpart_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    off = property(_ida_typeinf.argpart_t_off_get, _ida_typeinf.argpart_t_off_set, doc=r"""off""")
    r"""
    offset from the beginning of the argument
    """
    size = property(_ida_typeinf.argpart_t_size_get, _ida_typeinf.argpart_t_size_set, doc=r"""size""")
    r"""
    the number of bytes
    """

    def __init__(self, *args):
        r"""
        __init__(self, a) -> argpart_t

        @param a: argloc_t const &

        __init__(self) -> argpart_t
        """
        _ida_typeinf.argpart_t_swiginit(self, _ida_typeinf.new_argpart_t(*args))

    def bad_offset(self, *args):
        r"""
        bad_offset(self) -> bool
        Does this argpart have a valid offset?
        """
        return _ida_typeinf.argpart_t_bad_offset(self, *args)

    def bad_size(self, *args):
        r"""
        bad_size(self) -> bool
        Does this argpart have a valid size?
        """
        return _ida_typeinf.argpart_t_bad_size(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: argpart_t const &
        """
        return _ida_typeinf.argpart_t___lt__(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)
        Assign this = r and r = this.

        @param r: (C++: argpart_t &)
        """
        return _ida_typeinf.argpart_t_swap(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_argpart_t

# Register argpart_t in _ida_typeinf:
_ida_typeinf.argpart_t_swigregister(argpart_t)

class scattered_aloc_t(argpartvec_t):
    r"""
    Proxy of C++ scattered_aloc_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> scattered_aloc_t
        """
        _ida_typeinf.scattered_aloc_t_swiginit(self, _ida_typeinf.new_scattered_aloc_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_scattered_aloc_t

# Register scattered_aloc_t in _ida_typeinf:
_ida_typeinf.scattered_aloc_t_swigregister(scattered_aloc_t)


def verify_argloc(*args):
    r"""
    verify_argloc(vloc, size, gaps) -> int
    Verify argloc_t.

    @param vloc: (C++: const argloc_t &) argloc_t const &
    @param size: (C++: int) total size of the variable
    @param gaps: (C++: const rangeset_t *) if not nullptr, specifies gaps in structure definition. these gaps
                 should not map to any argloc, but everything else must be covered
    @return: 0 if ok, otherwise an interr code.
    """
    return _ida_typeinf.verify_argloc(*args)

def optimize_argloc(*args):
    r"""
    optimize_argloc(vloc, size, gaps) -> bool
    Verify and optimize scattered argloc into simple form. All new arglocs must be
    processed by this function.
    @retval true: success
    @retval false: the input argloc was illegal

    @param vloc: (C++: argloc_t *)
    @param size: (C++: int)
    @param gaps: (C++: const rangeset_t *) rangeset_t const *
    """
    return _ida_typeinf.optimize_argloc(*args)

def print_argloc(*args):
    r"""
    print_argloc(vloc, size=0, vflags=0) -> str
    Convert an argloc to human readable form.

    @param vloc: (C++: const argloc_t &) argloc_t const &
    @param size: (C++: int)
    @param vflags: (C++: int)
    """
    return _ida_typeinf.print_argloc(*args)
PRALOC_VERIFY = _ida_typeinf.PRALOC_VERIFY
r"""
interr if illegal argloc
"""

PRALOC_STKOFF = _ida_typeinf.PRALOC_STKOFF
r"""
print stack offsets
"""

class aloc_visitor_t(object):
    r"""
    Proxy of C++ aloc_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def visit_location(self, *args):
        r"""
        visit_location(self, v, off, size) -> int

        @param v: argloc_t &
        @param off: int
        @param size: int
        """
        return _ida_typeinf.aloc_visitor_t_visit_location(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_aloc_visitor_t

    def __init__(self, *args):
        r"""
        __init__(self) -> aloc_visitor_t

        @param self: PyObject *
        """
        if self.__class__ == aloc_visitor_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.aloc_visitor_t_swiginit(self, _ida_typeinf.new_aloc_visitor_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_aloc_visitor_t(self)
        return weakref.proxy(self)

# Register aloc_visitor_t in _ida_typeinf:
_ida_typeinf.aloc_visitor_t_swigregister(aloc_visitor_t)


def for_all_arglocs(*args):
    r"""
    for_all_arglocs(vv, vloc, size, off=0) -> int
    Compress larger argloc types and initiate the aloc visitor.

    @param vv: (C++: aloc_visitor_t &)
    @param vloc: (C++: argloc_t &)
    @param size: (C++: int)
    @param off: (C++: int)
    """
    return _ida_typeinf.for_all_arglocs(*args)
class const_aloc_visitor_t(object):
    r"""
    Proxy of C++ const_aloc_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def visit_location(self, *args):
        r"""
        visit_location(self, v, off, size) -> int

        @param v: argloc_t const &
        @param off: int
        @param size: int
        """
        return _ida_typeinf.const_aloc_visitor_t_visit_location(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_const_aloc_visitor_t

    def __init__(self, *args):
        r"""
        __init__(self) -> const_aloc_visitor_t

        @param self: PyObject *
        """
        if self.__class__ == const_aloc_visitor_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.const_aloc_visitor_t_swiginit(self, _ida_typeinf.new_const_aloc_visitor_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_const_aloc_visitor_t(self)
        return weakref.proxy(self)

# Register const_aloc_visitor_t in _ida_typeinf:
_ida_typeinf.const_aloc_visitor_t_swigregister(const_aloc_visitor_t)


def for_all_const_arglocs(*args):
    r"""
    for_all_const_arglocs(vv, vloc, size, off=0) -> int
    See for_all_arglocs()

    @param vv: (C++: const_aloc_visitor_t &)
    @param vloc: (C++: const argloc_t &) argloc_t const &
    @param size: (C++: int)
    @param off: (C++: int)
    """
    return _ida_typeinf.for_all_const_arglocs(*args)

def is_user_cc(*args):
    r"""
    is_user_cc(cm) -> bool
    Does the calling convention specify argument locations explicitly?

    @param cm: (C++: cm_t)
    """
    return _ida_typeinf.is_user_cc(*args)

def is_vararg_cc(*args):
    r"""
    is_vararg_cc(cm) -> bool
    Does the calling convention use ellipsis?

    @param cm: (C++: cm_t)
    """
    return _ida_typeinf.is_vararg_cc(*args)

def is_purging_cc(*args):
    r"""
    is_purging_cc(cm) -> bool
    Does the calling convention clean the stack arguments upon return?.
    @note: this function is valid only for x86 code

    @param cm: (C++: cm_t)
    """
    return _ida_typeinf.is_purging_cc(*args)

def is_golang_cc(*args):
    r"""
    is_golang_cc(cc) -> bool
    GO language calling convention (return value in stack)?

    @param cc: (C++: cm_t)
    """
    return _ida_typeinf.is_golang_cc(*args)
ARGREGS_POLICY_UNDEFINED = _ida_typeinf.ARGREGS_POLICY_UNDEFINED

ARGREGS_GP_ONLY = _ida_typeinf.ARGREGS_GP_ONLY
r"""
GP registers used for all arguments.
"""

ARGREGS_INDEPENDENT = _ida_typeinf.ARGREGS_INDEPENDENT
r"""
FP/GP registers used separately (like gcc64)
"""

ARGREGS_BY_SLOTS = _ida_typeinf.ARGREGS_BY_SLOTS
r"""
fixed FP/GP register per each slot (like vc64)
"""

ARGREGS_FP_CONSUME_GP = _ida_typeinf.ARGREGS_FP_CONSUME_GP
r"""
FP register also consumes one or more GP regs but not vice versa (aix ppc ABI)
"""

ARGREGS_MIPS_O32 = _ida_typeinf.ARGREGS_MIPS_O32
r"""
MIPS ABI o32.
"""

class callregs_t(object):
    r"""
    Proxy of C++ callregs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    policy = property(_ida_typeinf.callregs_t_policy_get, _ida_typeinf.callregs_t_policy_set, doc=r"""policy""")
    r"""
    argument policy
    """
    nregs = property(_ida_typeinf.callregs_t_nregs_get, _ida_typeinf.callregs_t_nregs_set, doc=r"""nregs""")
    r"""
    max number of registers that can be used in a call
    """
    gpregs = property(_ida_typeinf.callregs_t_gpregs_get, _ida_typeinf.callregs_t_gpregs_set, doc=r"""gpregs""")
    r"""
    array of gp registers
    """
    fpregs = property(_ida_typeinf.callregs_t_fpregs_get, _ida_typeinf.callregs_t_fpregs_set, doc=r"""fpregs""")
    r"""
    array of fp registers
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> callregs_t
        __init__(self, cc) -> callregs_t

        @param cc: cm_t
        """
        _ida_typeinf.callregs_t_swiginit(self, _ida_typeinf.new_callregs_t(*args))

    def init_regs(self, *args):
        r"""
        init_regs(self, cc)
        Init policy & registers for given CC.

        @param cc: (C++: cm_t)
        """
        return _ida_typeinf.callregs_t_init_regs(self, *args)

    def by_slots(self, *args):
        r"""
        by_slots(self) -> bool
        """
        return _ida_typeinf.callregs_t_by_slots(self, *args)

    def set(self, *args):
        r"""
        set(self, _policy, gprs, fprs)
        Init policy & registers (arrays are -1-terminated)

        @param _policy: (C++: argreg_policy_t) enum argreg_policy_t
        @param gprs: (C++: const int *) int const *
        @param fprs: (C++: const int *) int const *
        """
        return _ida_typeinf.callregs_t_set(self, *args)

    def reset(self, *args):
        r"""
        reset(self)
        Set policy and registers to invalid values.
        """
        return _ida_typeinf.callregs_t_reset(self, *args)

    @staticmethod
    def regcount(*args):
        r"""
        regcount(cc) -> int
        Get max number of registers may be used in a function call.

        @param cc: (C++: cm_t)
        """
        return _ida_typeinf.callregs_t_regcount(*args)

    def reginds(self, *args):
        r"""
        reginds(self, gp_ind, fp_ind, r) -> bool
        Get register indexes within GP/FP arrays. (-1 -> is not present in the
        corresponding array)

        @param gp_ind: (C++: int *)
        @param fp_ind: (C++: int *)
        @param r: (C++: int)
        """
        return _ida_typeinf.callregs_t_reginds(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_callregs_t

# Register callregs_t in _ida_typeinf:
_ida_typeinf.callregs_t_swigregister(callregs_t)
C_PC_TINY = cvar.C_PC_TINY
C_PC_SMALL = cvar.C_PC_SMALL
C_PC_COMPACT = cvar.C_PC_COMPACT
C_PC_MEDIUM = cvar.C_PC_MEDIUM
C_PC_LARGE = cvar.C_PC_LARGE
C_PC_HUGE = cvar.C_PC_HUGE
C_PC_FLAT = cvar.C_PC_FLAT

def callregs_t_regcount(*args):
    r"""
    callregs_t_regcount(cc) -> int

    @param cc: cm_t
    """
    return _ida_typeinf.callregs_t_regcount(*args)


def get_comp(*args):
    r"""
    get_comp(comp) -> comp_t
    Get compiler bits.

    @param comp: (C++: comp_t)
    """
    return _ida_typeinf.get_comp(*args)

def get_compiler_name(*args):
    r"""
    get_compiler_name(id) -> char const *
    Get full compiler name.

    @param id: (C++: comp_t)
    """
    return _ida_typeinf.get_compiler_name(*args)

def get_compiler_abbr(*args):
    r"""
    get_compiler_abbr(id) -> char const *
    Get abbreviated compiler name.

    @param id: (C++: comp_t)
    """
    return _ida_typeinf.get_compiler_abbr(*args)

def get_compilers(*args):
    r"""
    get_compilers(ids, names, abbrs)
    Get names of all built-in compilers.

    @param ids: (C++: compvec_t *)
    @param names: (C++: qstrvec_t *)
    @param abbrs: (C++: qstrvec_t *)
    """
    return _ida_typeinf.get_compilers(*args)

def is_comp_unsure(*args):
    r"""
    is_comp_unsure(comp) -> comp_t
    See COMP_UNSURE.

    @param comp: (C++: comp_t)
    """
    return _ida_typeinf.is_comp_unsure(*args)

def default_compiler(*args):
    r"""
    default_compiler() -> comp_t
    Get compiler specified by inf.cc.
    """
    return _ida_typeinf.default_compiler(*args)

def is_gcc(*args):
    r"""
    is_gcc() -> bool
    Is the target compiler COMP_GNU?
    """
    return _ida_typeinf.is_gcc(*args)

def is_gcc32(*args):
    r"""
    is_gcc32() -> bool
    Is the target compiler 32 bit gcc?
    """
    return _ida_typeinf.is_gcc32(*args)

def is_gcc64(*args):
    r"""
    is_gcc64() -> bool
    Is the target compiler 64 bit gcc?
    """
    return _ida_typeinf.is_gcc64(*args)

def gcc_layout(*args):
    r"""
    gcc_layout() -> bool
    Should use the struct/union layout as done by gcc?
    """
    return _ida_typeinf.gcc_layout(*args)

def set_compiler(*args):
    r"""
    set_compiler(cc, flags, abiname=None) -> bool
    Change current compiler.

    @param cc: (C++: const compiler_info_t &) compiler to switch to
    @param flags: (C++: int) Set compiler flags
    @param abiname: (C++: const char *) ABI name
    @return: success
    """
    return _ida_typeinf.set_compiler(*args)
SETCOMP_OVERRIDE = _ida_typeinf.SETCOMP_OVERRIDE
r"""
may override old compiler info
"""

SETCOMP_ONLY_ID = _ida_typeinf.SETCOMP_ONLY_ID
r"""
cc has only 'id' field; the rest will be set to defaults corresponding to the
program bitness
"""

SETCOMP_ONLY_ABI = _ida_typeinf.SETCOMP_ONLY_ABI
r"""
ignore cc field complete, use only abiname
"""

SETCOMP_BY_USER = _ida_typeinf.SETCOMP_BY_USER
r"""
invoked by user, cannot be replaced by module/loader
"""


def set_compiler_id(*args):
    r"""
    set_compiler_id(id, abiname=None) -> bool
    Set the compiler id (see Compiler IDs)

    @param id: (C++: comp_t)
    @param abiname: (C++: const char *) char const *
    """
    return _ida_typeinf.set_compiler_id(*args)

def set_abi_name(*args):
    r"""
    set_abi_name(abiname, user_level=False) -> bool
    Set abi name (see Compiler IDs)

    @param abiname: (C++: const char *) char const *
    @param user_level: (C++: bool)
    """
    return _ida_typeinf.set_abi_name(*args)

def get_abi_name(*args):
    r"""
    get_abi_name() -> str
    Get ABI name.

    @return: length of the name (>=0)
    """
    return _ida_typeinf.get_abi_name(*args)

def append_abi_opts(*args):
    r"""
    append_abi_opts(abi_opts, user_level=False) -> bool
    Add/remove/check ABI option General form of full abi name: abiname-opt1-opt2-...
    or -opt1-opt2-...

    @param abi_opts: (C++: const char *) - ABI options to add/remove in form opt1-opt2-...
    @param user_level: (C++: bool) - initiated by user if TRUE (==SETCOMP_BY_USER)
    @return: success
    """
    return _ida_typeinf.append_abi_opts(*args)

def remove_abi_opts(*args):
    r"""
    remove_abi_opts(abi_opts, user_level=False) -> bool

    @param abi_opts: char const *
    @param user_level: bool
    """
    return _ida_typeinf.remove_abi_opts(*args)

def set_compiler_string(*args):
    r"""
    set_compiler_string(compstr, user_level) -> bool

    @param compstr: (C++: const char *) - compiler description in form <abbr>:<abiname>
    @param user_level: (C++: bool) - initiated by user if TRUE
    @return: success
    """
    return _ida_typeinf.set_compiler_string(*args)

def use_golang_cc(*args):
    r"""
    use_golang_cc() -> bool
    is GOLANG calling convention used by default?
    """
    return _ida_typeinf.use_golang_cc(*args)

def switch_to_golang(*args):
    r"""
    switch_to_golang()
    switch to GOLANG calling convention (to be used as default CC)
    """
    return _ida_typeinf.switch_to_golang(*args)
MAX_FUNC_ARGS = _ida_typeinf.MAX_FUNC_ARGS
r"""
max number of function arguments
"""

abs_unk = _ida_typeinf.abs_unk

abs_no = _ida_typeinf.abs_no

abs_yes = _ida_typeinf.abs_yes

sc_unk = _ida_typeinf.sc_unk
r"""
unknown
"""

sc_type = _ida_typeinf.sc_type
r"""
typedef
"""

sc_ext = _ida_typeinf.sc_ext
r"""
extern
"""

sc_stat = _ida_typeinf.sc_stat
r"""
static
"""

sc_reg = _ida_typeinf.sc_reg
r"""
register
"""

sc_auto = _ida_typeinf.sc_auto
r"""
auto
"""

sc_friend = _ida_typeinf.sc_friend
r"""
friend
"""

sc_virt = _ida_typeinf.sc_virt
r"""
virtual
"""

HTI_CPP = _ida_typeinf.HTI_CPP
r"""
C++ mode (not implemented)
"""

HTI_INT = _ida_typeinf.HTI_INT

HTI_EXT = _ida_typeinf.HTI_EXT

HTI_LEX = _ida_typeinf.HTI_LEX

HTI_UNP = _ida_typeinf.HTI_UNP

HTI_TST = _ida_typeinf.HTI_TST
r"""
test mode: discard the result
"""

HTI_FIL = _ida_typeinf.HTI_FIL
r"""
"input" is file name, otherwise "input" contains a C declaration
"""

HTI_MAC = _ida_typeinf.HTI_MAC
r"""
define macros from the base tils
"""

HTI_NWR = _ida_typeinf.HTI_NWR
r"""
no warning messages
"""

HTI_NER = _ida_typeinf.HTI_NER
r"""
ignore all errors but display them
"""

HTI_DCL = _ida_typeinf.HTI_DCL
r"""
don't complain about redeclarations
"""

HTI_NDC = _ida_typeinf.HTI_NDC
r"""
don't decorate names
"""

HTI_PAK = _ida_typeinf.HTI_PAK
r"""
explicit structure pack value (#pragma pack)
"""

HTI_PAK_SHIFT = _ida_typeinf.HTI_PAK_SHIFT
r"""
shift for HTI_PAK. This field should be used if you want to remember an explicit
pack value for each structure/union type. See HTI_PAK... definitions
"""

HTI_PAKDEF = _ida_typeinf.HTI_PAKDEF
r"""
default pack value
"""

HTI_PAK1 = _ida_typeinf.HTI_PAK1
r"""
#pragma pack(1)
"""

HTI_PAK2 = _ida_typeinf.HTI_PAK2
r"""
#pragma pack(2)
"""

HTI_PAK4 = _ida_typeinf.HTI_PAK4
r"""
#pragma pack(4)
"""

HTI_PAK8 = _ida_typeinf.HTI_PAK8
r"""
#pragma pack(8)
"""

HTI_PAK16 = _ida_typeinf.HTI_PAK16
r"""
#pragma pack(16)
"""

HTI_HIGH = _ida_typeinf.HTI_HIGH
r"""
assume high level prototypes (with hidden args, etc)
"""

HTI_LOWER = _ida_typeinf.HTI_LOWER
r"""
lower the function prototypes
"""

HTI_RAWARGS = _ida_typeinf.HTI_RAWARGS
r"""
leave argument names unchanged (do not remove underscores)
"""


def parse_decl(*args):
    r"""
    parse_decl(tif, til, decl, flags) -> str
    Parse ONE declaration. If the input string contains more than one declaration,
    the first complete type declaration (PT_TYP) or the last variable declaration
    (PT_VAR) will be used.
    @note: name & tif may be empty after the call!

    @param tif: (C++: tinfo_t *) type info
    @param til: (C++: til_t *) type library to use. may be nullptr
    @param decl: (C++: const char *) C declaration to parse
    @param flags: (C++: int) combination of Type parsing flags bits
    @retval true: ok
    @retval false: declaration is bad, the error message is displayed if !PT_SIL
    """
    return _ida_typeinf.parse_decl(*args)
PT_SIL = _ida_typeinf.PT_SIL
r"""
silent, no messages
"""

PT_NDC = _ida_typeinf.PT_NDC
r"""
don't decorate names
"""

PT_TYP = _ida_typeinf.PT_TYP
r"""
return declared type information
"""

PT_VAR = _ida_typeinf.PT_VAR
r"""
return declared object information
"""

PT_PACKMASK = _ida_typeinf.PT_PACKMASK
r"""
mask for pack alignment values
"""

PT_HIGH = _ida_typeinf.PT_HIGH
r"""
assume high level prototypes (with hidden args, etc)
"""

PT_LOWER = _ida_typeinf.PT_LOWER
r"""
lower the function prototypes
"""

PT_REPLACE = _ida_typeinf.PT_REPLACE
r"""
replace the old type (used in idc)
"""

PT_RAWARGS = _ida_typeinf.PT_RAWARGS
r"""
leave argument names unchanged (do not remove underscores)
"""


def convert_pt_flags_to_hti(*args):
    r"""
    convert_pt_flags_to_hti(pt_flags) -> int
    Convert Type parsing flags to Type formatting flags. Type parsing flags lesser
    than 0x10 don't have stable meaning and will be ignored (more on these flags can
    be seen in idc.idc)

    @param pt_flags: (C++: int)
    """
    return _ida_typeinf.convert_pt_flags_to_hti(*args)

def parse_decls(*args):
    r"""
    parse_decls(til, input, printer, hti_flags) -> int
    Parse many declarations and store them in a til. If there are any errors, they
    will be printed using 'printer'. This function uses default include path and
    predefined macros from the database settings. It always uses the HTI_DCL bit.

    @param til: (C++: til_t *) type library to store the result
    @param input: (C++: const char *) input string or file name (see hti_flags)
    @param printer: (C++: printer_t *) function to output error messages (use msg or nullptr or your
                    own callback)
    @param hti_flags: (C++: int) combination of Type formatting flags
    @return: number of errors, 0 means ok.
    """
    return _ida_typeinf.parse_decls(*args)

def print_type(*args):
    r"""
    print_type(ea, prtype_flags) -> str
    Get type declaration for the specified address.

    @param ea: (C++: ea_t) address
    @param prtype_flags: (C++: int) combination of Type printing flags
    @return: success
    """
    return _ida_typeinf.print_type(*args)
PRTYPE_1LINE = _ida_typeinf.PRTYPE_1LINE
r"""
print to one line
"""

PRTYPE_MULTI = _ida_typeinf.PRTYPE_MULTI
r"""
print to many lines
"""

PRTYPE_TYPE = _ida_typeinf.PRTYPE_TYPE
r"""
print type declaration (not variable declaration)
"""

PRTYPE_PRAGMA = _ida_typeinf.PRTYPE_PRAGMA
r"""
print pragmas for alignment
"""

PRTYPE_SEMI = _ida_typeinf.PRTYPE_SEMI
r"""
append ; to the end
"""

PRTYPE_CPP = _ida_typeinf.PRTYPE_CPP
r"""
use c++ name (only for print_type())
"""

PRTYPE_DEF = _ida_typeinf.PRTYPE_DEF

PRTYPE_NOARGS = _ida_typeinf.PRTYPE_NOARGS

PRTYPE_NOARRS = _ida_typeinf.PRTYPE_NOARRS

PRTYPE_NORES = _ida_typeinf.PRTYPE_NORES

PRTYPE_RESTORE = _ida_typeinf.PRTYPE_RESTORE

PRTYPE_NOREGEX = _ida_typeinf.PRTYPE_NOREGEX
r"""
do not apply regular expressions to beautify name
"""

PRTYPE_COLORED = _ida_typeinf.PRTYPE_COLORED
r"""
add color tag COLOR_SYMBOL for any parentheses, commas and colons
"""

PRTYPE_METHODS = _ida_typeinf.PRTYPE_METHODS

NTF_TYPE = _ida_typeinf.NTF_TYPE
r"""
type name
"""

NTF_SYMU = _ida_typeinf.NTF_SYMU
r"""
symbol, name is unmangled ('func')
"""

NTF_SYMM = _ida_typeinf.NTF_SYMM
r"""
symbol, name is mangled ('_func'); only one of NTF_TYPE and NTF_SYMU, NTF_SYMM
can be used
"""

NTF_NOBASE = _ida_typeinf.NTF_NOBASE
r"""
don't inspect base tils (for get_named_type)
"""

NTF_REPLACE = _ida_typeinf.NTF_REPLACE
r"""
replace original type (for set_named_type)
"""

NTF_UMANGLED = _ida_typeinf.NTF_UMANGLED
r"""
name is unmangled (don't use this flag)
"""

NTF_NOCUR = _ida_typeinf.NTF_NOCUR
r"""
don't inspect current til file (for get_named_type)
"""

NTF_64BIT = _ida_typeinf.NTF_64BIT
r"""
value is 64bit
"""

NTF_FIXNAME = _ida_typeinf.NTF_FIXNAME
r"""
force-validate the name of the type when setting (set_named_type,
set_numbered_type only)
"""

NTF_IDBENC = _ida_typeinf.NTF_IDBENC
r"""
the name is given in the IDB encoding; non-ASCII bytes will be decoded
accordingly (set_named_type, set_numbered_type only)
"""

NTF_CHKSYNC = _ida_typeinf.NTF_CHKSYNC
r"""
check that synchronization to IDB passed OK (set_numbered_type, set_named_type)
"""

TERR_OK = _ida_typeinf.TERR_OK
r"""
ok
"""

TERR_SAVE = _ida_typeinf.TERR_SAVE
r"""
failed to save
"""

TERR_SERIALIZE = _ida_typeinf.TERR_SERIALIZE
r"""
failed to serialize
"""

TERR_WRONGNAME = _ida_typeinf.TERR_WRONGNAME
r"""
name is not acceptable
"""

TERR_BADSYNC = _ida_typeinf.TERR_BADSYNC
r"""
failed to synchronize with IDB
"""


def del_named_type(*args):
    r"""
    del_named_type(ti, name, ntf_flags) -> bool
    Delete information about a symbol.

    @param ti: (C++: til_t *) type library
    @param name: (C++: const char *) name of symbol
    @param ntf_flags: (C++: int) combination of Flags for named types
    @return: success
    """
    return _ida_typeinf.del_named_type(*args)

def first_named_type(*args):
    r"""
    first_named_type(ti, ntf_flags) -> char const *
    Enumerate types. Returns mangled names. Never returns anonymous types. To
    include it, enumerate types by ordinals.

    @param ti: (C++: const til_t *) til_t const *
    @param ntf_flags: (C++: int)
    """
    return _ida_typeinf.first_named_type(*args)

def next_named_type(*args):
    r"""
    next_named_type(ti, name, ntf_flags) -> char const *
    Enumerate types. Returns mangled names. Never returns anonymous types. To
    include it, enumerate types by ordinals.

    @param ti: (C++: const til_t *) til_t const *
    @param name: (C++: const char *) char const *
    @param ntf_flags: (C++: int)
    """
    return _ida_typeinf.next_named_type(*args)

def copy_named_type(*args):
    r"""
    copy_named_type(dsttil, srctil, name) -> uint32
    Copy a named type from one til to another. This function will copy the specified
    type and all dependent types from the source type library to the destination
    library.

    @param dsttil: (C++: til_t *) Destination til. It must have orginal types enabled
    @param srctil: (C++: const til_t *) Source til.
    @param name: (C++: const char *) name of the type to copy
    @return: ordinal number of the copied type. 0 means error
    """
    return _ida_typeinf.copy_named_type(*args)

def gen_decorate_name(*args):
    r"""
    gen_decorate_name(name, mangle, cc, type) -> str
    Generic function for decorate_name() (may be used in IDP modules)

    @param name: (C++: const char *) char const *
    @param mangle: (C++: bool)
    @param cc: (C++: cm_t)
    @param type: (C++: const tinfo_t *) tinfo_t const *
    """
    return _ida_typeinf.gen_decorate_name(*args)

def calc_c_cpp_name(*args):
    r"""
    calc_c_cpp_name(name, type, ccn_flags) -> str
    Get C or C++ form of the name.

    @param name: (C++: const char *) original (mangled or decorated) name
    @param type: (C++: const tinfo_t *) name type if known, otherwise nullptr
    @param ccn_flags: (C++: int) one of C/C++ naming flags
    """
    return _ida_typeinf.calc_c_cpp_name(*args)
CCN_C = _ida_typeinf.CCN_C

CCN_CPP = _ida_typeinf.CCN_CPP


def alloc_type_ordinals(*args):
    r"""
    alloc_type_ordinals(ti, qty) -> uint32
    Allocate a range of ordinal numbers for new types.

    @param ti: (C++: til_t *) type library
    @param qty: (C++: int) number of ordinals to allocate
    @return: the first ordinal. 0 means failure.
    """
    return _ida_typeinf.alloc_type_ordinals(*args)

def alloc_type_ordinal(*args):
    r"""
    alloc_type_ordinal(ti) -> uint32
    alloc_type_ordinals(ti, 1)

    @param ti: (C++: til_t *)
    """
    return _ida_typeinf.alloc_type_ordinal(*args)

def get_ordinal_qty(*args):
    r"""
    get_ordinal_qty(ti) -> uint32
    Get number of allocated ordinals.

    @param ti: (C++: const til_t *) til_t const *
    @return: uint32(-1) if failed
    """
    return _ida_typeinf.get_ordinal_qty(*args)

def set_numbered_type(*args):
    r"""
    set_numbered_type(ti, ordinal, ntf_flags, name, type, fields=None, cmt=None, fldcmts=None, sclass=None) -> tinfo_code_t
    Store a type in the til. 'name' may be nullptr for anonymous types. The
    specified ordinal must be free (no other type is using it). For ntf_flags, only
    NTF_REPLACE is consulted.

    @param ti: (C++: til_t *)
    @param ordinal: (C++: uint32)
    @param ntf_flags: (C++: int)
    @param name: (C++: const char *) char const *
    @param type: (C++: const type_t *) type_t const *
    @param fields: (C++: const p_list *) p_list const *
    @param cmt: (C++: const char *) char const *
    @param fldcmts: (C++: const p_list *) p_list const *
    @param sclass: (C++: const sclass_t *) sclass_t const *
    """
    return _ida_typeinf.set_numbered_type(*args)

def del_numbered_type(*args):
    r"""
    del_numbered_type(ti, ordinal) -> bool
    Delete a numbered type.

    @param ti: (C++: til_t *)
    @param ordinal: (C++: uint32)
    """
    return _ida_typeinf.del_numbered_type(*args)

def set_type_alias(*args):
    r"""
    set_type_alias(ti, src_ordinal, dst_ordinal) -> bool
    Create a type alias. Redirects all references to source type to the destination
    type. This is equivalent to instantaneous replacement all reference to srctype
    by dsttype.

    @param ti: (C++: til_t *)
    @param src_ordinal: (C++: uint32)
    @param dst_ordinal: (C++: uint32)
    """
    return _ida_typeinf.set_type_alias(*args)

def get_alias_target(*args):
    r"""
    get_alias_target(ti, ordinal) -> uint32
    Find the final alias destination. If the ordinal has not been aliased, return
    the specified ordinal itself If failed, returns 0.

    @param ti: (C++: const til_t *) til_t const *
    @param ordinal: (C++: uint32)
    """
    return _ida_typeinf.get_alias_target(*args)

def get_type_ordinal(*args):
    r"""
    get_type_ordinal(ti, name) -> int32
    Get type ordinal by its name.

    @param ti: (C++: const til_t *) til_t const *
    @param name: (C++: const char *) char const *
    """
    return _ida_typeinf.get_type_ordinal(*args)

def get_numbered_type_name(*args):
    r"""
    get_numbered_type_name(ti, ordinal) -> char const *
    Get type name (if exists) by its ordinal. If the type is anonymous, returns "".
    If failed, returns nullptr

    @param ti: (C++: const til_t *) til_t const *
    @param ordinal: (C++: uint32)
    """
    return _ida_typeinf.get_numbered_type_name(*args)

def create_numbered_type_name(*args):
    r"""
    create_numbered_type_name(ord) -> str
    Create anonymous name for numbered type. This name can be used to reference a
    numbered type by its ordinal Ordinal names have the following format: '#' +
    set_de(ord) Returns: -1 if error, otherwise the name length

    @param ord: (C++: int32)
    """
    return _ida_typeinf.create_numbered_type_name(*args)

def is_ordinal_name(*args):
    r"""
    is_ordinal_name(name, ord=None) -> bool
    Check if the name is an ordinal name. Ordinal names have the following format:
    '#' + set_de(ord)

    @param name: (C++: const char *) char const *
    @param ord: (C++: uint32 *)
    """
    return _ida_typeinf.is_ordinal_name(*args)

def get_ordinal_from_idb_type(*args):
    r"""
    get_ordinal_from_idb_type(name, type) -> int
    Get ordinal number of an idb type (struct/enum). The 'type' parameter is used
    only to determine the kind of the type (struct or enum) Use this function to
    find out the correspondence between idb types and til types

    @param name: (C++: const char *) char const *
    @param type: (C++: const type_t *) type_t const *
    """
    return _ida_typeinf.get_ordinal_from_idb_type(*args)

def is_autosync(*args):
    r"""
    is_autosync(name, type) -> bool
    Is the specified idb type automatically synchronized?

    @param name: (C++: const char *) char const *
    @param type: type_t const *

    is_autosync(name, tif) -> bool

    @param name: char const *
    @param tif: tinfo_t const &
    """
    return _ida_typeinf.is_autosync(*args)

def get_vftable_ea(*args):
    r"""
    get_vftable_ea(ordinal) -> ea_t
    Get address of a virtual function table.

    @param ordinal: (C++: uint32) ordinal number of a vftable type.
    @return: address of the corresponding virtual function table in the current
             database.
    """
    return _ida_typeinf.get_vftable_ea(*args)

def get_vftable_ordinal(*args):
    r"""
    get_vftable_ordinal(vftable_ea) -> uint32
    Get ordinal number of the virtual function table.

    @param vftable_ea: (C++: ea_t) address of a virtual function table.
    @return: ordinal number of the corresponding vftable type. 0 - failure.
    """
    return _ida_typeinf.get_vftable_ordinal(*args)

def set_vftable_ea(*args):
    r"""
    set_vftable_ea(ordinal, vftable_ea) -> bool
    Set the address of a vftable instance for a vftable type.

    @param ordinal: (C++: uint32) ordinal number of the corresponding vftable type.
    @param vftable_ea: (C++: ea_t) address of a virtual function table.
    @return: success
    """
    return _ida_typeinf.set_vftable_ea(*args)

def del_vftable_ea(*args):
    r"""
    del_vftable_ea(ordinal) -> bool
    Delete the address of a vftable instance for a vftable type.

    @param ordinal: (C++: uint32) ordinal number of a vftable type.
    @return: success
    """
    return _ida_typeinf.del_vftable_ea(*args)

def deref_ptr(*args):
    r"""
    deref_ptr(ptr_ea, tif, closure_obj=None) -> bool
    Dereference a pointer.

    @param ptr_ea: (C++: ea_t *) in/out parameter
    * in: address of the pointer
    * out: the pointed address
    @param tif: (C++: const tinfo_t &) type of the pointer
    @param closure_obj: (C++: ea_t *) closure object (not used yet)
    @return: success
    """
    return _ida_typeinf.deref_ptr(*args)

def import_type(*args):
    r"""
    import_type(til, idx, name, flags=0) -> tid_t
    Copy a named type from til to idb.

    @param til: (C++: const til_t *) type library
    @param idx: (C++: int) the position of the new type in the list of types (structures or
                enums). -1 means at the end of the list
    @param name: (C++: const char *) the type name
    @param flags: (C++: int) combination of Import type flags
    @return: BADNODE on error
    """
    return _ida_typeinf.import_type(*args)
IMPTYPE_VERBOSE = _ida_typeinf.IMPTYPE_VERBOSE
r"""
more verbose output (dialog boxes may appear)
"""

IMPTYPE_OVERRIDE = _ida_typeinf.IMPTYPE_OVERRIDE
r"""
override existing type
"""

IMPTYPE_LOCAL = _ida_typeinf.IMPTYPE_LOCAL
r"""
the type is local, the struct/enum won't be marked as til type. there is no need
to specify this bit if til==idati, the kernel will set it automatically
"""


def add_til(*args):
    r"""
    add_til(name, flags) -> int
    Load a til file and add it the database type libraries list. IDA will also apply
    function prototypes for matching function names.

    @param name: (C++: const char *) til name
    @param flags: (C++: int) combination of Load TIL flags
    @return: one of Load TIL result codes
    """
    return _ida_typeinf.add_til(*args)
ADDTIL_DEFAULT = _ida_typeinf.ADDTIL_DEFAULT
r"""
default behavior
"""

ADDTIL_INCOMP = _ida_typeinf.ADDTIL_INCOMP
r"""
load incompatible tils
"""

ADDTIL_SILENT = _ida_typeinf.ADDTIL_SILENT
r"""
do not ask any questions
"""

ADDTIL_FAILED = _ida_typeinf.ADDTIL_FAILED
r"""
something bad, the warning is displayed
"""

ADDTIL_OK = _ida_typeinf.ADDTIL_OK
r"""
ok, til is loaded
"""

ADDTIL_COMP = _ida_typeinf.ADDTIL_COMP
r"""
ok, but til is not compatible with the current compiler
"""

ADDTIL_ABORTED = _ida_typeinf.ADDTIL_ABORTED
r"""
til was not loaded (incompatible til rejected by user)
"""


def del_til(*args):
    r"""
    del_til(name) -> bool
    Unload a til file.

    @param name: (C++: const char *) char const *
    """
    return _ida_typeinf.del_til(*args)

def apply_named_type(*args):
    r"""
    apply_named_type(ea, name) -> bool
    Apply the specified named type to the address.

    @param ea: (C++: ea_t) linear address
    @param name: (C++: const char *) the type name, e.g. "FILE"
    @return: success
    """
    return _ida_typeinf.apply_named_type(*args)

def apply_tinfo(*args):
    r"""
    apply_tinfo(ea, tif, flags) -> bool
    Apply the specified type to the specified address. This function sets the type
    and tries to convert the item at the specified address to conform the type.

    @param ea: (C++: ea_t) linear address
    @param tif: (C++: const tinfo_t &) type string in internal format
    @param flags: (C++: uint32) combination of Apply tinfo flags
    @return: success
    """
    return _ida_typeinf.apply_tinfo(*args)
TINFO_GUESSED = _ida_typeinf.TINFO_GUESSED
r"""
this is a guessed type
"""

TINFO_DEFINITE = _ida_typeinf.TINFO_DEFINITE
r"""
this is a definite type
"""

TINFO_DELAYFUNC = _ida_typeinf.TINFO_DELAYFUNC
r"""
if type is a function and no function exists at ea, schedule its creation and
argument renaming to auto-analysis, otherwise try to create it immediately
"""

TINFO_STRICT = _ida_typeinf.TINFO_STRICT
r"""
never convert given type to another one before applying
"""


def apply_cdecl(*args):
    r"""
    apply_cdecl(til, ea, decl, flags=0) -> bool
    Apply the specified type to the address. This function parses the declaration
    and calls apply_tinfo()

    @param til: (C++: til_t *) type library
    @param ea: (C++: ea_t) linear address
    @param decl: (C++: const char *) type declaration in C form
    @param flags: (C++: int) flags to pass to apply_tinfo (TINFO_DEFINITE is always passed)
    @return: success
    """
    return _ida_typeinf.apply_cdecl(*args)

def apply_callee_tinfo(*args):
    r"""
    apply_callee_tinfo(caller, tif) -> bool
    Apply the type of the called function to the calling instruction. This function
    will append parameter comments and rename the local variables of the calling
    function. It also stores information about the instructions that initialize call
    arguments in the database. Use get_arg_addrs() to retrieve it if necessary.
    Alternatively it is possible to hook to processor_t::arg_addrs_ready event.

    @param caller: (C++: ea_t) linear address of the calling instruction. must belong to a
                   function.
    @param tif: (C++: const tinfo_t &) type info
    @return: success
    """
    return _ida_typeinf.apply_callee_tinfo(*args)

def apply_once_tinfo_and_name(*args):
    r"""
    apply_once_tinfo_and_name(dea, tif, name) -> bool
    Apply the specified type and name to the address. This function checks if the
    address already has a type. If the old type
    does not exist or the new type is 'better' than the old type, then the
    new type will be applied. A type is considered better if it has more
    information (e.g. BTMT_STRUCT is better than BT_INT).
    The same logic is with the name: if the address already have a meaningful
    name, it will be preserved. Only if the old name does not exist or it
    is a dummy name like byte_123, it will be replaced by the new name.

    @param dea: (C++: ea_t) linear address
    @param tif: (C++: const tinfo_t &) type string in the internal format
    @param name: (C++: const char *) new name for the address
    @return: success
    """
    return _ida_typeinf.apply_once_tinfo_and_name(*args)

def guess_tinfo(*args):
    r"""
    guess_tinfo(tif, id) -> int
    Generate a type information about the id from the disassembly. id can be a
    structure/union/enum id or an address.

    @param tif: (C++: tinfo_t *)
    @param id: (C++: tid_t)
    @return: one of Guess tinfo codes
    """
    return _ida_typeinf.guess_tinfo(*args)
GUESS_FUNC_FAILED = _ida_typeinf.GUESS_FUNC_FAILED
r"""
couldn't guess the function type
"""

GUESS_FUNC_TRIVIAL = _ida_typeinf.GUESS_FUNC_TRIVIAL
r"""
the function type doesn't have interesting info
"""

GUESS_FUNC_OK = _ida_typeinf.GUESS_FUNC_OK
r"""
ok, some non-trivial information is gathered
"""


def set_c_header_path(*args):
    r"""
    set_c_header_path(incdir)
    Set include directory path the target compiler.

    @param incdir: (C++: const char *) char const *
    """
    return _ida_typeinf.set_c_header_path(*args)

def get_c_header_path(*args):
    r"""
    get_c_header_path() -> str
    Get the include directory path of the target compiler.
    """
    return _ida_typeinf.get_c_header_path(*args)

def set_c_macros(*args):
    r"""
    set_c_macros(macros)
    Set predefined macros for the target compiler.

    @param macros: (C++: const char *) char const *
    """
    return _ida_typeinf.set_c_macros(*args)

def get_c_macros(*args):
    r"""
    get_c_macros() -> str
    Get predefined macros for the target compiler.
    """
    return _ida_typeinf.get_c_macros(*args)

def get_idati(*args):
    r"""
    get_idati() -> til_t
    Pointer to the local type library - this til is private for each IDB file
    Function that accepts til_t* uses local type library instead of nullptr.
    """
    return _ida_typeinf.get_idati(*args)

def get_idainfo_by_type(*args):
    r"""
    get_idainfo_by_type(tif) -> bool
    Extract information from a tinfo_t.

    @param tif: (C++: const tinfo_t &) the type to inspect
    """
    return _ida_typeinf.get_idainfo_by_type(*args)
STI_PCHAR = _ida_typeinf.STI_PCHAR
r"""
char *
"""

STI_PUCHAR = _ida_typeinf.STI_PUCHAR
r"""
uint8 *
"""

STI_PCCHAR = _ida_typeinf.STI_PCCHAR
r"""
const char *
"""

STI_PCUCHAR = _ida_typeinf.STI_PCUCHAR
r"""
const uint8 *
"""

STI_PBYTE = _ida_typeinf.STI_PBYTE
r"""
_BYTE *
"""

STI_PINT = _ida_typeinf.STI_PINT
r"""
int *
"""

STI_PUINT = _ida_typeinf.STI_PUINT
r"""
unsigned int *
"""

STI_PVOID = _ida_typeinf.STI_PVOID
r"""
void *
"""

STI_PPVOID = _ida_typeinf.STI_PPVOID
r"""
void **
"""

STI_PCVOID = _ida_typeinf.STI_PCVOID
r"""
const void *
"""

STI_ACHAR = _ida_typeinf.STI_ACHAR
r"""
char[]
"""

STI_AUCHAR = _ida_typeinf.STI_AUCHAR
r"""
uint8[]
"""

STI_ACCHAR = _ida_typeinf.STI_ACCHAR
r"""
const char[]
"""

STI_ACUCHAR = _ida_typeinf.STI_ACUCHAR
r"""
const uint8[]
"""

STI_FPURGING = _ida_typeinf.STI_FPURGING
r"""
void __userpurge(int)
"""

STI_FDELOP = _ida_typeinf.STI_FDELOP
r"""
void __cdecl(void *)
"""

STI_MSGSEND = _ida_typeinf.STI_MSGSEND
r"""
void *(void *, const char *, ...)
"""

STI_AEABI_LCMP = _ida_typeinf.STI_AEABI_LCMP
r"""
int __fastcall(int64 x, int64 y)
"""

STI_AEABI_ULCMP = _ida_typeinf.STI_AEABI_ULCMP
r"""
int __fastcall(uint64 x, uint64 y)
"""

STI_DONT_USE = _ida_typeinf.STI_DONT_USE
r"""
unused stock type id; should not be used
"""

STI_SIZE_T = _ida_typeinf.STI_SIZE_T
r"""
size_t
"""

STI_SSIZE_T = _ida_typeinf.STI_SSIZE_T
r"""
ssize_t
"""

STI_AEABI_MEMCPY = _ida_typeinf.STI_AEABI_MEMCPY
r"""
void __fastcall(void *, const void *, size_t)
"""

STI_AEABI_MEMSET = _ida_typeinf.STI_AEABI_MEMSET
r"""
void __fastcall(void *, size_t, int)
"""

STI_AEABI_MEMCLR = _ida_typeinf.STI_AEABI_MEMCLR
r"""
void __fastcall(void *, size_t)
"""

STI_RTC_CHECK_2 = _ida_typeinf.STI_RTC_CHECK_2
r"""
int16 __fastcall(int16 x)
"""

STI_RTC_CHECK_4 = _ida_typeinf.STI_RTC_CHECK_4
r"""
int32 __fastcall(int32 x)
"""

STI_RTC_CHECK_8 = _ida_typeinf.STI_RTC_CHECK_8
r"""
int64 __fastcall(int64 x)
"""

STI_COMPLEX64 = _ida_typeinf.STI_COMPLEX64
r"""
struct complex64_t { float real, imag; }
"""

STI_COMPLEX128 = _ida_typeinf.STI_COMPLEX128
r"""
struct complex128_t { double real, imag; }
"""

STI_LAST = _ida_typeinf.STI_LAST

GTD_CALC_LAYOUT = _ida_typeinf.GTD_CALC_LAYOUT
r"""
calculate udt layout
"""

GTD_NO_LAYOUT = _ida_typeinf.GTD_NO_LAYOUT
r"""
don't calculate udt layout please note that udt layout may have been calculated
earlier
"""

GTD_DEL_BITFLDS = _ida_typeinf.GTD_DEL_BITFLDS
r"""
delete udt bitfields
"""

GTD_CALC_ARGLOCS = _ida_typeinf.GTD_CALC_ARGLOCS
r"""
calculate func arg locations
"""

GTD_NO_ARGLOCS = _ida_typeinf.GTD_NO_ARGLOCS
r"""
don't calculate func arg locations please note that the locations may have been
calculated earlier
"""

GTS_NESTED = _ida_typeinf.GTS_NESTED
r"""
nested type (embedded into a udt)
"""

GTS_BASECLASS = _ida_typeinf.GTS_BASECLASS
r"""
is baseclass of a udt
"""

SUDT_SORT = _ida_typeinf.SUDT_SORT
r"""
fields are not sorted by offset, sort them first
"""

SUDT_ALIGN = _ida_typeinf.SUDT_ALIGN
r"""
recalculate field alignments, struct packing, etc to match the offsets and size
info
"""

SUDT_GAPS = _ida_typeinf.SUDT_GAPS
r"""
allow to fill gaps with additional members (_BYTE[])
"""

SUDT_UNEX = _ida_typeinf.SUDT_UNEX
r"""
references to nonexistent member types are acceptable; in this case it is better
to set the corresponding udt_member_t::fda field to the type alignment. If this
field is not set, ida will try to guess the alignment.
"""

SUDT_FAST = _ida_typeinf.SUDT_FAST
r"""
serialize without verifying offsets and alignments
"""

SUDT_CONST = _ida_typeinf.SUDT_CONST
r"""
only for serialize_udt: make type const
"""

SUDT_VOLATILE = _ida_typeinf.SUDT_VOLATILE
r"""
only for serialize_udt: make type volatile
"""

SUDT_TRUNC = _ida_typeinf.SUDT_TRUNC


def copy_tinfo_t(*args):
    r"""
    copy_tinfo_t(_this, r)

    @param _this: tinfo_t *
    @param r: tinfo_t const &
    """
    return _ida_typeinf.copy_tinfo_t(*args)

def clear_tinfo_t(*args):
    r"""
    clear_tinfo_t(_this)

    @param _this: tinfo_t *
    """
    return _ida_typeinf.clear_tinfo_t(*args)

def create_tinfo(*args):
    r"""
    create_tinfo(_this, bt, bt2, ptr) -> bool

    @param _this: tinfo_t *
    @param bt: type_t
    @param bt2: type_t
    @param ptr: void *
    """
    return _ida_typeinf.create_tinfo(*args)

def verify_tinfo(*args):
    r"""
    verify_tinfo(typid) -> int

    @param typid: uint32
    """
    return _ida_typeinf.verify_tinfo(*args)

def get_tinfo_details(*args):
    r"""
    get_tinfo_details(typid, bt2, buf) -> bool

    @param typid: uint32
    @param bt2: type_t
    @param buf: void *
    """
    return _ida_typeinf.get_tinfo_details(*args)

def get_tinfo_size(*args):
    r"""
    get_tinfo_size(p_effalign, typid, gts_code) -> size_t

    @param p_effalign: uint32 *
    @param typid: uint32
    @param gts_code: int
    """
    return _ida_typeinf.get_tinfo_size(*args)

def get_tinfo_pdata(*args):
    r"""
    get_tinfo_pdata(outptr, typid, what) -> size_t

    @param outptr: void *
    @param typid: uint32
    @param what: int
    """
    return _ida_typeinf.get_tinfo_pdata(*args)

def get_tinfo_property(*args):
    r"""
    get_tinfo_property(typid, gta_prop) -> size_t

    @param typid: uint32
    @param gta_prop: int
    """
    return _ida_typeinf.get_tinfo_property(*args)

def set_tinfo_property(*args):
    r"""
    set_tinfo_property(tif, sta_prop, x) -> size_t

    @param tif: tinfo_t *
    @param sta_prop: int
    @param x: size_t
    """
    return _ida_typeinf.set_tinfo_property(*args)

def serialize_tinfo(*args):
    r"""
    serialize_tinfo(type, fields, fldcmts, tif, sudt_flags) -> bool

    @param type: qtype *
    @param fields: qtype *
    @param fldcmts: qtype *
    @param tif: tinfo_t const *
    @param sudt_flags: int
    """
    return _ida_typeinf.serialize_tinfo(*args)

def deserialize_tinfo(*args):
    r"""
    deserialize_tinfo(tif, til, ptype, pfields, pfldcmts) -> bool

    @param tif: tinfo_t *
    @param til: til_t const *
    @param ptype: type_t const **
    @param pfields: p_list const **
    @param pfldcmts: p_list const **
    """
    return _ida_typeinf.deserialize_tinfo(*args)

def find_tinfo_udt_member(*args):
    r"""
    find_tinfo_udt_member(udm, typid, strmem_flags) -> int

    @param udm: udt_member_t *
    @param typid: uint32
    @param strmem_flags: int
    """
    return _ida_typeinf.find_tinfo_udt_member(*args)

def print_tinfo(*args):
    r"""
    print_tinfo(prefix, indent, cmtindent, flags, tif, name, cmt) -> str

    @param prefix: char const *
    @param indent: int
    @param cmtindent: int
    @param flags: int
    @param tif: tinfo_t const *
    @param name: char const *
    @param cmt: char const *
    """
    return _ida_typeinf.print_tinfo(*args)

def dstr_tinfo(*args):
    r"""
    dstr_tinfo(tif) -> char const *

    @param tif: tinfo_t const *
    """
    return _ida_typeinf.dstr_tinfo(*args)

def visit_subtypes(*args):
    r"""
    visit_subtypes(visitor, out, tif, name, cmt) -> int

    @param visitor: tinfo_visitor_t *
    @param out: type_mods_t *
    @param tif: tinfo_t const &
    @param name: char const *
    @param cmt: char const *
    """
    return _ida_typeinf.visit_subtypes(*args)

def compare_tinfo(*args):
    r"""
    compare_tinfo(t1, t2, tcflags) -> bool

    @param t1: uint32
    @param t2: uint32
    @param tcflags: int
    """
    return _ida_typeinf.compare_tinfo(*args)

def lexcompare_tinfo(*args):
    r"""
    lexcompare_tinfo(t1, t2, arg3) -> int

    @param t1: uint32
    @param t2: uint32
    @param arg3: int
    """
    return _ida_typeinf.lexcompare_tinfo(*args)

def get_stock_tinfo(*args):
    r"""
    get_stock_tinfo(tif, id) -> bool

    @param tif: tinfo_t *
    @param id: enum stock_type_id_t
    """
    return _ida_typeinf.get_stock_tinfo(*args)

def read_tinfo_bitfield_value(*args):
    r"""
    read_tinfo_bitfield_value(typid, v, bitoff) -> uint64

    @param typid: uint32
    @param v: uint64
    @param bitoff: int
    """
    return _ida_typeinf.read_tinfo_bitfield_value(*args)

def write_tinfo_bitfield_value(*args):
    r"""
    write_tinfo_bitfield_value(typid, dst, v, bitoff) -> uint64

    @param typid: uint32
    @param dst: uint64
    @param v: uint64
    @param bitoff: int
    """
    return _ida_typeinf.write_tinfo_bitfield_value(*args)

def get_tinfo_attr(*args):
    r"""
    get_tinfo_attr(typid, key, bv, all_attrs) -> bool

    @param typid: uint32
    @param key: qstring const &
    @param bv: bytevec_t *
    @param all_attrs: bool
    """
    return _ida_typeinf.get_tinfo_attr(*args)

def set_tinfo_attr(*args):
    r"""
    set_tinfo_attr(tif, ta, may_overwrite) -> bool

    @param tif: tinfo_t *
    @param ta: type_attr_t const &
    @param may_overwrite: bool
    """
    return _ida_typeinf.set_tinfo_attr(*args)

def del_tinfo_attr(*args):
    r"""
    del_tinfo_attr(tif, key, make_copy) -> bool

    @param tif: tinfo_t *
    @param key: qstring const &
    @param make_copy: bool
    """
    return _ida_typeinf.del_tinfo_attr(*args)

def get_tinfo_attrs(*args):
    r"""
    get_tinfo_attrs(typid, tav, include_ref_attrs) -> bool

    @param typid: uint32
    @param tav: type_attrs_t *
    @param include_ref_attrs: bool
    """
    return _ida_typeinf.get_tinfo_attrs(*args)

def set_tinfo_attrs(*args):
    r"""
    set_tinfo_attrs(tif, ta) -> bool

    @param tif: tinfo_t *
    @param ta: type_attrs_t *
    """
    return _ida_typeinf.set_tinfo_attrs(*args)

def score_tinfo(*args):
    r"""
    score_tinfo(tif) -> uint32

    @param tif: tinfo_t const *
    """
    return _ida_typeinf.score_tinfo(*args)

def save_tinfo(*args):
    r"""
    save_tinfo(tif, til, ord, name, ntf_flags) -> tinfo_code_t

    @param tif: tinfo_t *
    @param til: til_t *
    @param ord: size_t
    @param name: char const *
    @param ntf_flags: int
    """
    return _ida_typeinf.save_tinfo(*args)

def append_tinfo_covered(*args):
    r"""
    append_tinfo_covered(out, typid, offset) -> bool

    @param out: rangeset_t *
    @param typid: uint32
    @param offset: uint64
    """
    return _ida_typeinf.append_tinfo_covered(*args)

def calc_tinfo_gaps(*args):
    r"""
    calc_tinfo_gaps(out, typid) -> bool

    @param out: rangeset_t *
    @param typid: uint32
    """
    return _ida_typeinf.calc_tinfo_gaps(*args)
class tinfo_t(object):
    r"""
    Proxy of C++ tinfo_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> tinfo_t
        __init__(self, decl_type) -> tinfo_t

        @param decl_type: type_t

        __init__(self, r) -> tinfo_t

        @param r: tinfo_t const &
        """
        _ida_typeinf.tinfo_t_swiginit(self, _ida_typeinf.new_tinfo_t(*args))

    def clear(self, *args):
        r"""
        clear(self)
        Clear contents of this tinfo, and remove from the type system.
        """
        return _ida_typeinf.tinfo_t_clear(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)
        Assign this = r and r = this.

        @param r: (C++: tinfo_t &)
        """
        return _ida_typeinf.tinfo_t_swap(self, *args)

    def get_named_type(self, *args):
        r"""
        get_named_type(self, til, name, decl_type=BTF_TYPEDEF, resolve=True, try_ordinal=True) -> bool
        Create a tinfo_t object for an existing named type.

        @param til: (C++: const til_t *) type library to use
        @param name: (C++: const char *) name of the type to link to
        @param decl_type: (C++: type_t) if the reference was explicitly specified with the type tag
        (BTF_STRUCT/BTF_UNION/BTF_ENUM) you may specify it.
        the kernel will accept only the specified tag after resolving
        the type. If the resolved type does not correspond to the
        explicitly specified tag, the type will be considered as undefined
        @param resolve: (C++: bool) true: immediately resolve the type and return success code.
        @param try_ordinal: (C++: bool) true: try to replace name reference by an ordinal reference
        """
        return _ida_typeinf.tinfo_t_get_named_type(self, *args)

    def get_numbered_type(self, *args):
        r"""
        get_numbered_type(self, til, ordinal, decl_type=BTF_TYPEDEF, resolve=True) -> bool
        Create a tinfo_t object for an existing ordinal type.

        @param til: (C++: const til_t *) type library to use
        @param ordinal: (C++: uint32) number of the type to link to
        @param decl_type: (C++: type_t) if the reference was explicitly specified with the type tag
                          (BTF_STRUCT/BTF_UNION/BTF_ENUM) you may specify it. the kernel
                          will accept only the specified tag after resolving the type.
                          If the resolved type does not correspond to the explicitly
                          specified tag, the type will be considered as undefined
        @param resolve: (C++: bool) true: immediately resolve the type and return success code
        """
        return _ida_typeinf.tinfo_t_get_numbered_type(self, *args)

    def is_correct(self, *args):
        r"""
        is_correct(self) -> bool
        Is the type object correct?. It is possible to create incorrect types. For
        example, we can define a function that returns a enum and then delete the enum
        type. If this function returns false, the type should not be used in
        disassembly. Please note that this function does not verify all involved types:
        for example, pointers to undefined types are permitted.
        """
        return _ida_typeinf.tinfo_t_is_correct(self, *args)

    def get_realtype(self, *args):
        r"""
        get_realtype(self, full=False) -> type_t
        Get the resolved base type. Deserialization options:
        * if full=true, the referenced type will be deserialized fully, this may not
        always be desirable (slows down things)
        * if full=false, we just return the base type, the referenced type will be
        resolved again later if necessary (this may lead to multiple resolvings of the
        same type) imho full=false is a better approach because it does not perform
        unnecessary actions just in case. however, in some cases the caller knows that
        it is very likely that full type info will be required. in those cases full=true
        makes sense

        @param full: (C++: bool)
        """
        return _ida_typeinf.tinfo_t_get_realtype(self, *args)

    def get_decltype(self, *args):
        r"""
        get_decltype(self) -> type_t
        Get declared type (without resolving type references; they are returned as is).
        Obviously this is a very fast function and should be used instead of
        get_realtype() if possible.
        """
        return _ida_typeinf.tinfo_t_get_decltype(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        Was tinfo_t initialized with some type info or not?
        """
        return _ida_typeinf.tinfo_t_empty(self, *args)

    def present(self, *args):
        r"""
        present(self) -> bool
        Is the type really present? (not a reference to a missing type, for example)
        """
        return _ida_typeinf.tinfo_t_present(self, *args)

    def get_size(self, *args):
        r"""
        get_size(self, p_effalign=None, gts_code=0) -> size_t
        Get the type size in bytes.

        @param p_effalign: (C++: uint32 *) buffer for the alignment value
        @param gts_code: (C++: int) combination of GTS_... constants
        @return: BADSIZE in case of problems
        """
        return _ida_typeinf.tinfo_t_get_size(self, *args)

    def get_unpadded_size(self, *args):
        r"""
        get_unpadded_size(self) -> size_t
        Get the type size in bytes without the final padding, in bytes. For some UDTs
        get_unpadded_size() != get_size()
        """
        return _ida_typeinf.tinfo_t_get_unpadded_size(self, *args)

    def get_sign(self, *args):
        r"""
        get_sign(self) -> type_sign_t
        Get type sign.
        """
        return _ida_typeinf.tinfo_t_get_sign(self, *args)

    def is_signed(self, *args):
        r"""
        is_signed(self) -> bool
        Is this a signed type?
        """
        return _ida_typeinf.tinfo_t_is_signed(self, *args)

    def is_unsigned(self, *args):
        r"""
        is_unsigned(self) -> bool
        Is this an unsigned type?
        """
        return _ida_typeinf.tinfo_t_is_unsigned(self, *args)

    def get_declalign(self, *args):
        r"""
        get_declalign(self) -> uchar
        Get declared alignment of the type.
        """
        return _ida_typeinf.tinfo_t_get_declalign(self, *args)

    def set_declalign(self, *args):
        r"""
        set_declalign(self, declalign) -> bool
        Set declared alignment of the type.

        @param declalign: (C++: uchar)
        """
        return _ida_typeinf.tinfo_t_set_declalign(self, *args)

    def is_typeref(self, *args):
        r"""
        is_typeref(self) -> bool
        Is this type a type reference?. Type references cannot be modified. Once
        created, they do not change. Because of this, the set_... functions applied to
        typerefs create a new type id. Other types are modified directly.
        """
        return _ida_typeinf.tinfo_t_is_typeref(self, *args)

    def has_details(self, *args):
        r"""
        has_details(self) -> bool
        Does this type refer to a nontrivial type?
        """
        return _ida_typeinf.tinfo_t_has_details(self, *args)

    def get_type_name(self, *args):
        r"""
        get_type_name(self) -> bool
        Does a type refer to a name?. If yes, fill the provided buffer with the type
        name and return true. Names are returned for numbered types too: either a user-
        defined nice name or, if a user-provided name does not exist, an ordinal name
        (like #xx, see create_numbered_type_name()).
        """
        return _ida_typeinf.tinfo_t_get_type_name(self, *args)

    def get_final_type_name(self, *args):
        r"""
        get_final_type_name(self) -> bool
        Use in the case of typedef chain (TYPE1 -> TYPE2 -> TYPE3...TYPEn).

        @return: the name of the last type in the chain (TYPEn). if there is no chain,
                 returns TYPE1
        """
        return _ida_typeinf.tinfo_t_get_final_type_name(self, *args)

    def get_next_type_name(self, *args):
        r"""
        get_next_type_name(self) -> bool
        Use In the case of typedef chain (TYPE1 -> TYPE2 -> TYPE3...TYPEn).

        @return: the name of the next type in the chain (TYPE2). if there is no chain,
                 returns failure
        """
        return _ida_typeinf.tinfo_t_get_next_type_name(self, *args)

    def get_ordinal(self, *args):
        r"""
        get_ordinal(self) -> uint32
        Get type ordinal (only if the type was created as a numbered type, 0 if none)
        """
        return _ida_typeinf.tinfo_t_get_ordinal(self, *args)

    def get_final_ordinal(self, *args):
        r"""
        get_final_ordinal(self) -> uint32
        Get final type ordinal (0 is none)
        """
        return _ida_typeinf.tinfo_t_get_final_ordinal(self, *args)

    def get_til(self, *args):
        r"""
        get_til(self) -> til_t
        Get the type library for tinfo_t.
        """
        return _ida_typeinf.tinfo_t_get_til(self, *args)

    def is_from_subtil(self, *args):
        r"""
        is_from_subtil(self) -> bool
        Was the named type found in some base type library (not the top level type
        library)?. If yes, it usually means that the type comes from some loaded type
        library, not the local type library for the database
        """
        return _ida_typeinf.tinfo_t_is_from_subtil(self, *args)

    def is_forward_decl(self, *args):
        r"""
        is_forward_decl(self) -> bool
        Is this a forward declaration?. Forward declarations are placeholders: the type
        definition does not exist
        """
        return _ida_typeinf.tinfo_t_is_forward_decl(self, *args)

    def is_decl_const(self, *args):
        r"""
        is_decl_const(self) -> bool
        is_type_const(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_const(self, *args)

    def is_decl_volatile(self, *args):
        r"""
        is_decl_volatile(self) -> bool
        is_type_volatile(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_volatile(self, *args)

    def is_decl_void(self, *args):
        r"""
        is_decl_void(self) -> bool
        is_type_void(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_void(self, *args)

    def is_decl_partial(self, *args):
        r"""
        is_decl_partial(self) -> bool
        is_type_partial(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_partial(self, *args)

    def is_decl_unknown(self, *args):
        r"""
        is_decl_unknown(self) -> bool
        is_type_unknown(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_unknown(self, *args)

    def is_decl_last(self, *args):
        r"""
        is_decl_last(self) -> bool
        is_typeid_last(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_last(self, *args)

    def is_decl_ptr(self, *args):
        r"""
        is_decl_ptr(self) -> bool
        is_type_ptr(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_ptr(self, *args)

    def is_decl_array(self, *args):
        r"""
        is_decl_array(self) -> bool
        is_type_array(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_array(self, *args)

    def is_decl_func(self, *args):
        r"""
        is_decl_func(self) -> bool
        is_type_func(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_func(self, *args)

    def is_decl_complex(self, *args):
        r"""
        is_decl_complex(self) -> bool
        is_type_complex(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_complex(self, *args)

    def is_decl_typedef(self, *args):
        r"""
        is_decl_typedef(self) -> bool
        is_type_typedef(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_typedef(self, *args)

    def is_decl_sue(self, *args):
        r"""
        is_decl_sue(self) -> bool
        is_type_sue(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_sue(self, *args)

    def is_decl_struct(self, *args):
        r"""
        is_decl_struct(self) -> bool
        is_type_struct(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_struct(self, *args)

    def is_decl_union(self, *args):
        r"""
        is_decl_union(self) -> bool
        is_type_union(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_union(self, *args)

    def is_decl_udt(self, *args):
        r"""
        is_decl_udt(self) -> bool
        is_type_struni(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_udt(self, *args)

    def is_decl_enum(self, *args):
        r"""
        is_decl_enum(self) -> bool
        is_type_enum(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_enum(self, *args)

    def is_decl_bitfield(self, *args):
        r"""
        is_decl_bitfield(self) -> bool
        is_type_bitfld(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_bitfield(self, *args)

    def is_decl_int128(self, *args):
        r"""
        is_decl_int128(self) -> bool
        is_type_int128(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_int128(self, *args)

    def is_decl_int64(self, *args):
        r"""
        is_decl_int64(self) -> bool
        is_type_int64(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_int64(self, *args)

    def is_decl_int32(self, *args):
        r"""
        is_decl_int32(self) -> bool
        is_type_int32(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_int32(self, *args)

    def is_decl_int16(self, *args):
        r"""
        is_decl_int16(self) -> bool
        is_type_int16(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_int16(self, *args)

    def is_decl_int(self, *args):
        r"""
        is_decl_int(self) -> bool
        is_type_int(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_int(self, *args)

    def is_decl_char(self, *args):
        r"""
        is_decl_char(self) -> bool
        is_type_char(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_char(self, *args)

    def is_decl_uint(self, *args):
        r"""
        is_decl_uint(self) -> bool
        is_type_uint(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uint(self, *args)

    def is_decl_uchar(self, *args):
        r"""
        is_decl_uchar(self) -> bool
        is_type_uchar(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uchar(self, *args)

    def is_decl_uint16(self, *args):
        r"""
        is_decl_uint16(self) -> bool
        is_type_uint16(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uint16(self, *args)

    def is_decl_uint32(self, *args):
        r"""
        is_decl_uint32(self) -> bool
        is_type_uint32(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uint32(self, *args)

    def is_decl_uint64(self, *args):
        r"""
        is_decl_uint64(self) -> bool
        is_type_uint64(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uint64(self, *args)

    def is_decl_uint128(self, *args):
        r"""
        is_decl_uint128(self) -> bool
        is_type_uint128(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_uint128(self, *args)

    def is_decl_ldouble(self, *args):
        r"""
        is_decl_ldouble(self) -> bool
        is_type_ldouble(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_ldouble(self, *args)

    def is_decl_double(self, *args):
        r"""
        is_decl_double(self) -> bool
        is_type_double(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_double(self, *args)

    def is_decl_float(self, *args):
        r"""
        is_decl_float(self) -> bool
        is_type_float(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_float(self, *args)

    def is_decl_tbyte(self, *args):
        r"""
        is_decl_tbyte(self) -> bool
        is_type_tbyte(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_tbyte(self, *args)

    def is_decl_floating(self, *args):
        r"""
        is_decl_floating(self) -> bool
        is_type_floating(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_floating(self, *args)

    def is_decl_bool(self, *args):
        r"""
        is_decl_bool(self) -> bool
        is_type_bool(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_bool(self, *args)

    def is_decl_paf(self, *args):
        r"""
        is_decl_paf(self) -> bool
        is_type_paf(get_decltype())
        """
        return _ida_typeinf.tinfo_t_is_decl_paf(self, *args)

    def is_well_defined(self, *args):
        r"""
        is_well_defined(self) -> bool
        !(empty()) && !(is_decl_partial())
        """
        return _ida_typeinf.tinfo_t_is_well_defined(self, *args)

    def is_const(self, *args):
        r"""
        is_const(self) -> bool
        is_type_const(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_const(self, *args)

    def is_volatile(self, *args):
        r"""
        is_volatile(self) -> bool
        is_type_volatile(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_volatile(self, *args)

    def is_void(self, *args):
        r"""
        is_void(self) -> bool
        is_type_void(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_void(self, *args)

    def is_partial(self, *args):
        r"""
        is_partial(self) -> bool
        is_type_partial(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_partial(self, *args)

    def is_unknown(self, *args):
        r"""
        is_unknown(self) -> bool
        is_type_unknown(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_unknown(self, *args)

    def is_ptr(self, *args):
        r"""
        is_ptr(self) -> bool
        is_type_ptr(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_ptr(self, *args)

    def is_array(self, *args):
        r"""
        is_array(self) -> bool
        is_type_array(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_array(self, *args)

    def is_func(self, *args):
        r"""
        is_func(self) -> bool
        is_type_func(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_func(self, *args)

    def is_complex(self, *args):
        r"""
        is_complex(self) -> bool
        is_type_complex(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_complex(self, *args)

    def is_struct(self, *args):
        r"""
        is_struct(self) -> bool
        is_type_struct(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_struct(self, *args)

    def is_union(self, *args):
        r"""
        is_union(self) -> bool
        is_type_union(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_union(self, *args)

    def is_udt(self, *args):
        r"""
        is_udt(self) -> bool
        is_type_struni(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_udt(self, *args)

    def is_enum(self, *args):
        r"""
        is_enum(self) -> bool
        is_type_enum(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_enum(self, *args)

    def is_sue(self, *args):
        r"""
        is_sue(self) -> bool
        is_type_sue(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_sue(self, *args)

    def is_bitfield(self, *args):
        r"""
        is_bitfield(self) -> bool
        is_type_bitfld(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_bitfield(self, *args)

    def is_int128(self, *args):
        r"""
        is_int128(self) -> bool
        is_type_int128(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_int128(self, *args)

    def is_int64(self, *args):
        r"""
        is_int64(self) -> bool
        is_type_int64(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_int64(self, *args)

    def is_int32(self, *args):
        r"""
        is_int32(self) -> bool
        is_type_int32(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_int32(self, *args)

    def is_int16(self, *args):
        r"""
        is_int16(self) -> bool
        is_type_int16(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_int16(self, *args)

    def is_int(self, *args):
        r"""
        is_int(self) -> bool
        is_type_int(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_int(self, *args)

    def is_char(self, *args):
        r"""
        is_char(self) -> bool
        is_type_char(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_char(self, *args)

    def is_uint(self, *args):
        r"""
        is_uint(self) -> bool
        is_type_uint(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uint(self, *args)

    def is_uchar(self, *args):
        r"""
        is_uchar(self) -> bool
        is_type_uchar(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uchar(self, *args)

    def is_uint16(self, *args):
        r"""
        is_uint16(self) -> bool
        is_type_uint16(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uint16(self, *args)

    def is_uint32(self, *args):
        r"""
        is_uint32(self) -> bool
        is_type_uint32(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uint32(self, *args)

    def is_uint64(self, *args):
        r"""
        is_uint64(self) -> bool
        is_type_uint64(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uint64(self, *args)

    def is_uint128(self, *args):
        r"""
        is_uint128(self) -> bool
        is_type_uint128(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_uint128(self, *args)

    def is_ldouble(self, *args):
        r"""
        is_ldouble(self) -> bool
        is_type_ldouble(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_ldouble(self, *args)

    def is_double(self, *args):
        r"""
        is_double(self) -> bool
        is_type_double(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_double(self, *args)

    def is_float(self, *args):
        r"""
        is_float(self) -> bool
        is_type_float(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_float(self, *args)

    def is_tbyte(self, *args):
        r"""
        is_tbyte(self) -> bool
        is_type_tbyte(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_tbyte(self, *args)

    def is_bool(self, *args):
        r"""
        is_bool(self) -> bool
        is_type_bool(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_bool(self, *args)

    def is_paf(self, *args):
        r"""
        is_paf(self) -> bool
        is_type_paf(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_paf(self, *args)

    def is_ptr_or_array(self, *args):
        r"""
        is_ptr_or_array(self) -> bool
        is_type_ptr_or_array(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_ptr_or_array(self, *args)

    def is_integral(self, *args):
        r"""
        is_integral(self) -> bool
        is_type_integral(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_integral(self, *args)

    def is_ext_integral(self, *args):
        r"""
        is_ext_integral(self) -> bool
        is_type_ext_integral(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_ext_integral(self, *args)

    def is_floating(self, *args):
        r"""
        is_floating(self) -> bool
        is_type_floating(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_floating(self, *args)

    def is_arithmetic(self, *args):
        r"""
        is_arithmetic(self) -> bool
        is_type_arithmetic(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_arithmetic(self, *args)

    def is_ext_arithmetic(self, *args):
        r"""
        is_ext_arithmetic(self) -> bool
        is_type_ext_arithmetic(get_realtype())
        """
        return _ida_typeinf.tinfo_t_is_ext_arithmetic(self, *args)

    def is_scalar(self, *args):
        r"""
        is_scalar(self) -> bool
        Does the type represent a single number?
        """
        return _ida_typeinf.tinfo_t_is_scalar(self, *args)

    def get_ptr_details(self, *args):
        r"""
        get_ptr_details(self, pi) -> bool
        Get the pointer info.

        @param pi: (C++: ptr_type_data_t *)
        """
        return _ida_typeinf.tinfo_t_get_ptr_details(self, *args)

    def get_array_details(self, *args):
        r"""
        get_array_details(self, ai) -> bool
        Get the array specific info.

        @param ai: (C++: array_type_data_t *)
        """
        return _ida_typeinf.tinfo_t_get_array_details(self, *args)

    def get_enum_details(self, *args):
        r"""
        get_enum_details(self, ei) -> bool
        Get the enum specific info.

        @param ei: (C++: enum_type_data_t *)
        """
        return _ida_typeinf.tinfo_t_get_enum_details(self, *args)

    def get_bitfield_details(self, *args):
        r"""
        get_bitfield_details(self, bi) -> bool
        Get the bitfield specific info.

        @param bi: (C++: bitfield_type_data_t *)
        """
        return _ida_typeinf.tinfo_t_get_bitfield_details(self, *args)

    def get_udt_details(self, *args):
        r"""
        get_udt_details(self, udt, gtd=GTD_CALC_LAYOUT) -> bool
        Get the udt specific info.

        @param udt: (C++: udt_type_data_t *)
        @param gtd: (C++: gtd_udt_t) enum gtd_udt_t
        """
        return _ida_typeinf.tinfo_t_get_udt_details(self, *args)

    def get_func_details(self, *args):
        r"""
        get_func_details(self, fi, gtd=GTD_CALC_ARGLOCS) -> bool
        Get only the function specific info for this tinfo_t.

        @param fi: (C++: func_type_data_t *)
        @param gtd: (C++: gtd_func_t) enum gtd_func_t
        """
        return _ida_typeinf.tinfo_t_get_func_details(self, *args)

    def is_funcptr(self, *args):
        r"""
        is_funcptr(self) -> bool
        Is this pointer to a function?
        """
        return _ida_typeinf.tinfo_t_is_funcptr(self, *args)

    def is_shifted_ptr(self, *args):
        r"""
        is_shifted_ptr(self) -> bool
        Is a shifted pointer?
        """
        return _ida_typeinf.tinfo_t_is_shifted_ptr(self, *args)

    def is_varstruct(self, *args):
        r"""
        is_varstruct(self) -> bool
        Is a variable-size structure?
        """
        return _ida_typeinf.tinfo_t_is_varstruct(self, *args)

    def get_ptrarr_objsize(self, *args):
        r"""
        get_ptrarr_objsize(self) -> int
        BT_PTR & BT_ARRAY: get size of pointed object or array element. On error returns
        -1
        """
        return _ida_typeinf.tinfo_t_get_ptrarr_objsize(self, *args)

    def get_ptrarr_object(self, *args):
        r"""
        get_ptrarr_object(self) -> tinfo_t
        BT_PTR & BT_ARRAY: get the pointed object or array element. If the current type
        is not a pointer or array, return empty type info.
        """
        return _ida_typeinf.tinfo_t_get_ptrarr_object(self, *args)

    def get_pointed_object(self, *args):
        r"""
        get_pointed_object(self) -> tinfo_t
        """
        return _ida_typeinf.tinfo_t_get_pointed_object(self, *args)

    def is_pvoid(self, *args):
        r"""
        is_pvoid(self) -> bool
        Is "void *"?. This function does not check the pointer attributes and type
        modifiers.
        """
        return _ida_typeinf.tinfo_t_is_pvoid(self, *args)

    def get_array_element(self, *args):
        r"""
        get_array_element(self) -> tinfo_t
        """
        return _ida_typeinf.tinfo_t_get_array_element(self, *args)

    def get_array_nelems(self, *args):
        r"""
        get_array_nelems(self) -> int
        """
        return _ida_typeinf.tinfo_t_get_array_nelems(self, *args)

    def get_nth_arg(self, *args):
        r"""
        get_nth_arg(self, n) -> tinfo_t
        BT_FUNC or BT_PTR BT_FUNC: Get type of n-th arg (-1 means return type, see
        get_rettype())

        @param n: (C++: int)
        """
        return _ida_typeinf.tinfo_t_get_nth_arg(self, *args)

    def get_rettype(self, *args):
        r"""
        get_rettype(self) -> tinfo_t
        BT_FUNC or BT_PTR BT_FUNC: Get the function's return type
        """
        return _ida_typeinf.tinfo_t_get_rettype(self, *args)

    def get_nargs(self, *args):
        r"""
        get_nargs(self) -> int
        BT_FUNC or BT_PTR BT_FUNC: Calculate number of arguments (-1 - error)
        """
        return _ida_typeinf.tinfo_t_get_nargs(self, *args)

    def is_user_cc(self, *args):
        r"""
        is_user_cc(self) -> bool
        is_user_cc(get_cc())
        """
        return _ida_typeinf.tinfo_t_is_user_cc(self, *args)

    def is_vararg_cc(self, *args):
        r"""
        is_vararg_cc(self) -> bool
        is_vararg_cc(get_cc())
        """
        return _ida_typeinf.tinfo_t_is_vararg_cc(self, *args)

    def is_purging_cc(self, *args):
        r"""
        is_purging_cc(self) -> bool
        is_purging_cc(get_cc())
        """
        return _ida_typeinf.tinfo_t_is_purging_cc(self, *args)

    def calc_purged_bytes(self, *args):
        r"""
        calc_purged_bytes(self) -> int
        """
        return _ida_typeinf.tinfo_t_calc_purged_bytes(self, *args)

    def is_high_func(self, *args):
        r"""
        is_high_func(self) -> bool
        """
        return _ida_typeinf.tinfo_t_is_high_func(self, *args)

    def get_methods(self, *args):
        r"""
        get_methods(self, methods) -> bool

        @param BT_COMPLEX: get a list of member functions declared in this udt.
        @return: false if no member functions exist
        """
        return _ida_typeinf.tinfo_t_get_methods(self, *args)

    def set_methods(self, *args):
        r"""
        set_methods(self, methods) -> bool

        @param BT_COMPLEX: set the list of member functions. This function consumes 'methods'
        (makes it empty).
        @return: false if this type is not a udt, or if the given list is empty
        """
        return _ida_typeinf.tinfo_t_set_methods(self, *args)

    def find_udt_member(self, *args):
        r"""
        find_udt_member(self, udm, strmem_flags) -> int
        BTF_STRUCT,BTF_UNION: Find a udt member.
        * at the specified offset (STRMEM_OFFSET)
        * with the specified index (STRMEM_INDEX)
        * with the specified type (STRMEM_TYPE)
        * with the specified name (STRMEM_NAME)

        @param udm: (C++: struct udt_member_t *) udt_member_t *
        @param strmem_flags: (C++: int)
        @return: the index of the found member or -1
        """
        return _ida_typeinf.tinfo_t_find_udt_member(self, *args)

    def get_udt_nmembers(self, *args):
        r"""
        get_udt_nmembers(self) -> int
        Get number of udt members. -1-error.
        """
        return _ida_typeinf.tinfo_t_get_udt_nmembers(self, *args)

    def is_empty_udt(self, *args):
        r"""
        is_empty_udt(self) -> bool
        Is an empty struct/union? (has no fields)
        """
        return _ida_typeinf.tinfo_t_is_empty_udt(self, *args)

    def is_small_udt(self, *args):
        r"""
        is_small_udt(self) -> bool
        Is a small udt? (can fit a register or a pair of registers)
        """
        return _ida_typeinf.tinfo_t_is_small_udt(self, *args)

    def requires_qualifier(self, *args):
        r"""
        requires_qualifier(self, name, offset) -> bool
        Requires full qualifier? (name is not unique)

        @param name: (C++: const char *) field name
        @param offset: (C++: uint64)
        @return: if the name is not unique, returns true
        """
        return _ida_typeinf.tinfo_t_requires_qualifier(self, *args)

    def append_covered(self, *args):
        r"""
        append_covered(self, out, offset=0) -> bool
        Calculate set of covered bytes for the type

        @param out: (C++: rangeset_t *) pointer to the output buffer. covered bytes will be appended to it.
        @param offset: (C++: uint64)
        """
        return _ida_typeinf.tinfo_t_append_covered(self, *args)

    def calc_gaps(self, *args):
        r"""
        calc_gaps(self, out) -> bool
        Calculate set of padding bytes for the type

        @param out: (C++: rangeset_t *) pointer to the output buffer; old buffer contents will be lost.
        """
        return _ida_typeinf.tinfo_t_calc_gaps(self, *args)

    def is_one_fpval(self, *args):
        r"""
        is_one_fpval(self) -> bool
        Floating value or an object consisting of one floating member entirely.
        """
        return _ida_typeinf.tinfo_t_is_one_fpval(self, *args)

    def is_sse_type(self, *args):
        r"""
        is_sse_type(self) -> bool
        Is a SSE vector type?
        """
        return _ida_typeinf.tinfo_t_is_sse_type(self, *args)

    def is_anonymous_udt(self, *args):
        r"""
        is_anonymous_udt(self) -> bool
        Is an anonymous struct/union? We assume that types with names are anonymous if
        the name starts with $
        """
        return _ida_typeinf.tinfo_t_is_anonymous_udt(self, *args)

    def is_vftable(self, *args):
        r"""
        is_vftable(self) -> bool
        Is a vftable type?
        """
        return _ida_typeinf.tinfo_t_is_vftable(self, *args)

    def has_vftable(self, *args):
        r"""
        has_vftable(self) -> bool
        Has a vftable?
        """
        return _ida_typeinf.tinfo_t_has_vftable(self, *args)

    def get_enum_base_type(self, *args):
        r"""
        get_enum_base_type(self) -> type_t
        Get enum base type (convert enum to integer type) Returns BT_UNK if failed to
        convert
        """
        return _ida_typeinf.tinfo_t_get_enum_base_type(self, *args)

    def get_onemember_type(self, *args):
        r"""
        get_onemember_type(self) -> tinfo_t
        For objects consisting of one member entirely: return type of the member.
        """
        return _ida_typeinf.tinfo_t_get_onemember_type(self, *args)

    def calc_score(self, *args):
        r"""
        calc_score(self) -> uint32
        Calculate the type score (the higher - the nicer is the type)
        """
        return _ida_typeinf.tinfo_t_calc_score(self, *args)

    def _print(self, *args):
        r"""
        _print(self, name=None, prtype_flags=0, indent=0, cmtindent=0, prefix=None, cmt=None) -> bool

        Parameters
        ----------
        name: char const *
        prtype_flags: int
        indent: int
        cmtindent: int
        prefix: char const *
        cmt: char const *

        """
        return _ida_typeinf.tinfo_t__print(self, *args)

    def dstr(self, *args):
        r"""
        dstr(self) -> char const *
        Function to facilitate debugging.
        """
        return _ida_typeinf.tinfo_t_dstr(self, *args)

    def get_attrs(self, *args):
        r"""
        get_attrs(self, tav, all_attrs=False) -> bool
        Get type attributes (all_attrs: include attributes of referenced types, if any)

        @param tav: (C++: type_attrs_t *)
        @param all_attrs: (C++: bool)
        """
        return _ida_typeinf.tinfo_t_get_attrs(self, *args)

    def set_attrs(self, *args):
        r"""
        set_attrs(self, tav) -> bool
        Set type attributes. If necessary, a new typid will be created. this function
        modifies tav! (returns old attributes, if any)

        @param tav: (C++: type_attrs_t *)
        @return: false: bad attributes
        """
        return _ida_typeinf.tinfo_t_set_attrs(self, *args)

    def set_attr(self, *args):
        r"""
        set_attr(self, ta, may_overwrite=True) -> bool
        Set a type attribute. If necessary, a new typid will be created.

        @param ta: (C++: const type_attr_t &) type_attr_t const &
        @param may_overwrite: (C++: bool)
        """
        return _ida_typeinf.tinfo_t_set_attr(self, *args)

    def del_attrs(self, *args):
        r"""
        del_attrs(self)
        Del all type attributes. typerefs cannot be modified by this function.
        """
        return _ida_typeinf.tinfo_t_del_attrs(self, *args)

    def del_attr(self, *args):
        r"""
        del_attr(self, key, make_copy=True) -> bool
        Del a type attribute. typerefs cannot be modified by this function.

        @param key: (C++: const qstring &) qstring const &
        @param make_copy: (C++: bool)
        """
        return _ida_typeinf.tinfo_t_del_attr(self, *args)

    def create_simple_type(self, *args):
        r"""
        create_simple_type(self, decl_type) -> bool

        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_simple_type(self, *args)

    def create_ptr(self, *args):
        r"""
        create_ptr(self, p, decl_type=BT_PTR) -> bool

        @param p: ptr_type_data_t const &
        @param decl_type: type_t

        create_ptr(self, tif, bps=0, decl_type=BT_PTR) -> bool

        @param tif: tinfo_t const &
        @param bps: uchar
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_ptr(self, *args)

    def create_array(self, *args):
        r"""
        create_array(self, p, decl_type=BT_ARRAY) -> bool

        @param p: array_type_data_t const &
        @param decl_type: type_t

        create_array(self, tif, nelems=0, base=0, decl_type=BT_ARRAY) -> bool

        @param tif: tinfo_t const &
        @param nelems: uint32
        @param base: uint32
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_array(self, *args)

    def create_typedef(self, *args):
        r"""
        create_typedef(self, p, decl_type=BTF_TYPEDEF, try_ordinal=True) -> bool

        @param p: typedef_type_data_t const &
        @param decl_type: type_t
        @param try_ordinal: bool

        create_typedef(self, til, name, decl_type=BTF_TYPEDEF, try_ordinal=True)

        @param til: til_t const *
        @param name: char const *
        @param decl_type: type_t
        @param try_ordinal: bool

        create_typedef(self, til, ord, decl_type=BTF_TYPEDEF)

        @param til: til_t const *
        @param ord: uint
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_typedef(self, *args)

    def create_bitfield(self, *args):
        r"""
        create_bitfield(self, p, decl_type=BT_BITFIELD) -> bool

        @param p: bitfield_type_data_t const &
        @param decl_type: type_t

        create_bitfield(self, nbytes, width, is_unsigned=False, decl_type=BT_BITFIELD) -> bool

        @param nbytes: uchar
        @param width: uchar
        @param is_unsigned: bool
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_bitfield(self, *args)

    def create_udt(self, *args):
        r"""
        create_udt(self, p, decl_type) -> bool

        @param p: udt_type_data_t &
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_udt(self, *args)

    def create_enum(self, *args):
        r"""
        create_enum(self, p, decl_type=BTF_ENUM) -> bool

        @param p: enum_type_data_t &
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_enum(self, *args)

    def create_func(self, *args):
        r"""
        create_func(self, p, decl_type=BT_FUNC) -> bool

        @param p: func_type_data_t &
        @param decl_type: type_t
        """
        return _ida_typeinf.tinfo_t_create_func(self, *args)

    def set_named_type(self, *args):
        r"""
        set_named_type(self, til, name, ntf_flags=0) -> tinfo_code_t

        @param til: til_t *
        @param name: char const *
        @param ntf_flags: int
        """
        return _ida_typeinf.tinfo_t_set_named_type(self, *args)

    def set_symbol_type(self, *args):
        r"""
        set_symbol_type(self, til, name, ntf_flags=0) -> tinfo_code_t

        @param til: til_t *
        @param name: char const *
        @param ntf_flags: int
        """
        return _ida_typeinf.tinfo_t_set_symbol_type(self, *args)

    def set_numbered_type(self, *args):
        r"""
        set_numbered_type(self, til, ord, ntf_flags=0, name=None) -> tinfo_code_t

        @param til: til_t *
        @param ord: uint32
        @param ntf_flags: int
        @param name: char const *
        """
        return _ida_typeinf.tinfo_t_set_numbered_type(self, *args)

    def create_forward_decl(self, *args):
        r"""
        create_forward_decl(self, til, decl_type, name, ntf_flags=0) -> tinfo_code_t
        Create a forward declaration. decl_type: BTF_STRUCT, BTF_UNION, or BTF_ENUM

        @param til: (C++: til_t *)
        @param decl_type: (C++: type_t)
        @param name: (C++: const char *) char const *
        @param ntf_flags: (C++: int)
        """
        return _ida_typeinf.tinfo_t_create_forward_decl(self, *args)

    @staticmethod
    def get_stock(*args):
        r"""
        get_stock(id) -> tinfo_t
        Get stock type information. This function can be used to get tinfo_t for some
        common types. The same tinfo_t will be returned for the same id, thus saving
        memory and increasing the speed Please note that retrieving the STI_SIZE_T or
        STI_SSIZE_T stock type, will also have the side-effect of adding that type to
        the 'idati' TIL, under the well-known name 'size_t' or 'ssize_t' (respectively).
        The same is valid for STI_COMPLEX64 and STI_COMPLEX64 stock types with names
        'complex64_t' and 'complex128_t' (respectively).

        @param id: (C++: stock_type_id_t) enum stock_type_id_t
        """
        return _ida_typeinf.tinfo_t_get_stock(*args)

    def convert_array_to_ptr(self, *args):
        r"""
        convert_array_to_ptr(self) -> bool
        Convert an array into a pointer. type[] => type *
        """
        return _ida_typeinf.tinfo_t_convert_array_to_ptr(self, *args)

    def remove_ptr_or_array(self, *args):
        r"""
        remove_ptr_or_array(self) -> bool
        Replace the current type with the ptr obj or array element. This function
        performs one of the following conversions:
        * type[] => type
        * type* => type If the conversion is performed successfully, return true
        """
        return _ida_typeinf.tinfo_t_remove_ptr_or_array(self, *args)

    def change_sign(self, *args):
        r"""
        change_sign(self, sign) -> bool
        Change the type sign. Works only for the types that may have sign.

        @param sign: (C++: type_sign_t)
        """
        return _ida_typeinf.tinfo_t_change_sign(self, *args)

    def calc_udt_aligns(self, *args):
        r"""
        calc_udt_aligns(self, sudt_flags=0x0004) -> bool
        Calculate the udt alignments using the field offsets/sizes and the total udt
        size This function does not work on typerefs

        @param sudt_flags: (C++: int)
        """
        return _ida_typeinf.tinfo_t_calc_udt_aligns(self, *args)

    def read_bitfield_value(self, *args):
        r"""
        read_bitfield_value(self, v, bitoff) -> uint64

        @param v: uint64
        @param bitoff: int
        """
        return _ida_typeinf.tinfo_t_read_bitfield_value(self, *args)

    def write_bitfield_value(self, *args):
        r"""
        write_bitfield_value(self, dst, v, bitoff) -> uint64

        @param dst: uint64
        @param v: uint64
        @param bitoff: int
        """
        return _ida_typeinf.tinfo_t_write_bitfield_value(self, *args)

    def get_modifiers(self, *args):
        r"""
        get_modifiers(self) -> type_t
        """
        return _ida_typeinf.tinfo_t_get_modifiers(self, *args)

    def set_modifiers(self, *args):
        r"""
        set_modifiers(self, mod)

        @param mod: type_t
        """
        return _ida_typeinf.tinfo_t_set_modifiers(self, *args)

    def set_const(self, *args):
        r"""
        set_const(self)
        """
        return _ida_typeinf.tinfo_t_set_const(self, *args)

    def set_volatile(self, *args):
        r"""
        set_volatile(self)
        """
        return _ida_typeinf.tinfo_t_set_volatile(self, *args)

    def clr_const(self, *args):
        r"""
        clr_const(self)
        """
        return _ida_typeinf.tinfo_t_clr_const(self, *args)

    def clr_volatile(self, *args):
        r"""
        clr_volatile(self)
        """
        return _ida_typeinf.tinfo_t_clr_volatile(self, *args)

    def clr_const_volatile(self, *args):
        r"""
        clr_const_volatile(self)
        """
        return _ida_typeinf.tinfo_t_clr_const_volatile(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t_compare(self, *args)

    def compare_with(self, *args):
        r"""
        compare_with(self, r, tcflags=0) -> bool
        Compare two types, based on given flags (see tinfo_t comparison flags)

        @param r: (C++: const tinfo_t &) tinfo_t const &
        @param tcflags: (C++: int)
        """
        return _ida_typeinf.tinfo_t_compare_with(self, *args)

    def equals_to(self, *args):
        r"""
        equals_to(self, r) -> bool

        @param r: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t_equals_to(self, *args)

    def is_castable_to(self, *args):
        r"""
        is_castable_to(self, target) -> bool

        @param target: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t_is_castable_to(self, *args)

    def is_manually_castable_to(self, *args):
        r"""
        is_manually_castable_to(self, target) -> bool

        @param target: tinfo_t const &
        """
        return _ida_typeinf.tinfo_t_is_manually_castable_to(self, *args)

    def serialize(self, *args):
        r"""
        serialize(self, sudt_flags=SUDT_FAST|SUDT_TRUNC) -> (bytes, NoneType, NoneType), (bytes, bytes, NoneType)
        Serialize tinfo_t object into a type string.

        @param sudt_flags: (C++: int)
        """
        return _ida_typeinf.tinfo_t_serialize(self, *args)

    def deserialize(self, *args):
        r"""
        deserialize(self, til, ptype, pfields=None, pfldcmts=None) -> bool
        Deserialize a type string into a tinfo_t object.

        @param til: (C++: const til_t *) til_t const *
        @param ptype: (C++: const qtype *) type_t const **
        @param pfields: (C++: const qtype *) p_list const **
        @param pfldcmts: (C++: const qtype *) p_list const **

        deserialize(self, til, type, fields, cmts=None) -> bool

        @param til: til_t const *
        @param type: type_t const *
        @param fields: p_list const *
        @param cmts: p_list const *
        """
        return _ida_typeinf.tinfo_t_deserialize(self, *args)

    def copy(self, *args):
        r"""
        copy(self) -> tinfo_t
        """
        return _ida_typeinf.tinfo_t_copy(self, *args)

    def __str__(self, *args):
        r"""
        __str__(self) -> qstring
        """
        return _ida_typeinf.tinfo_t___str__(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_tinfo_t

    def get_attr(self, *args):
        r"""
        get_attr(self, key, all_attrs=True) -> str or None
        Get a type attribute.

        @param key: (C++: const qstring &) qstring const &
        @param all_attrs: (C++: bool)
        """
        return _ida_typeinf.tinfo_t_get_attr(self, *args)

# Register tinfo_t in _ida_typeinf:
_ida_typeinf.tinfo_t_swigregister(tinfo_t)
COMP_MASK = cvar.COMP_MASK
COMP_UNK = cvar.COMP_UNK
r"""
Unknown.
"""
COMP_MS = cvar.COMP_MS
r"""
Visual C++.
"""
COMP_BC = cvar.COMP_BC
r"""
Borland C++.
"""
COMP_WATCOM = cvar.COMP_WATCOM
r"""
Watcom C++.
"""
COMP_GNU = cvar.COMP_GNU
r"""
GNU C++.
"""
COMP_VISAGE = cvar.COMP_VISAGE
r"""
Visual Age C++.
"""
COMP_BP = cvar.COMP_BP
r"""
Delphi.
"""
COMP_UNSURE = cvar.COMP_UNSURE
r"""
uncertain compiler id
"""
BADSIZE = cvar.BADSIZE
r"""
bad type size
"""
BADORD = cvar.BADORD
r"""
invalid type ordinal
"""
FIRST_NONTRIVIAL_TYPID = cvar.FIRST_NONTRIVIAL_TYPID
r"""
Denotes the first bit describing a nontrivial type.
"""
TYPID_ISREF = cvar.TYPID_ISREF
r"""
Identifies that a type that is a typeref.
"""
TYPID_SHIFT = cvar.TYPID_SHIFT
r"""
First type detail bit.
"""

def remove_pointer(*args):
    r"""
    remove_pointer(tif) -> tinfo_t

    @param BT_PTR: If the current type is a pointer, return the pointed object. If the
    current type is not a pointer, return the current type. See also
    get_ptrarr_object() and get_pointed_object()
    """
    return _ida_typeinf.remove_pointer(*args)
STRMEM_MASK = _ida_typeinf.STRMEM_MASK

STRMEM_OFFSET = _ida_typeinf.STRMEM_OFFSET
r"""
get member by offset
* in: udm->offset - is a member offset in bits
"""

STRMEM_INDEX = _ida_typeinf.STRMEM_INDEX
r"""
get member by number
* in: udm->offset - is a member number
"""

STRMEM_AUTO = _ida_typeinf.STRMEM_AUTO
r"""
get member by offset if struct, or get member by index if union
* nb: union: index is stored in the udm->offset field!
* nb: struct: offset is in bytes (not in bits)!
"""

STRMEM_NAME = _ida_typeinf.STRMEM_NAME
r"""
get member by name
* in: udm->name - the desired member name.
"""

STRMEM_TYPE = _ida_typeinf.STRMEM_TYPE
r"""
get member by type.
* in: udm->type - the desired member type. member types are compared with
tinfo_t::equals_to()
"""

STRMEM_SIZE = _ida_typeinf.STRMEM_SIZE
r"""
get member by size.
* in: udm->size - the desired member size.
"""

STRMEM_MINS = _ida_typeinf.STRMEM_MINS
r"""
get smallest member by size.
"""

STRMEM_MAXS = _ida_typeinf.STRMEM_MAXS
r"""
get biggest member by size.
"""

STRMEM_VFTABLE = _ida_typeinf.STRMEM_VFTABLE
r"""
can be combined with STRMEM_OFFSET, STRMEM_AUTO get vftable instead of the base
class
"""

STRMEM_SKIP_EMPTY = _ida_typeinf.STRMEM_SKIP_EMPTY
r"""
can be combined with STRMEM_OFFSET, STRMEM_AUTO skip empty members (i.e. having
zero size) only last empty member can be returned
"""

STRMEM_CASTABLE_TO = _ida_typeinf.STRMEM_CASTABLE_TO
r"""
can be combined with STRMEM_TYPE: member type must be castable to the specified
type
"""

STRMEM_ANON = _ida_typeinf.STRMEM_ANON
r"""
can be combined with STRMEM_NAME: look inside anonymous members too.
"""


def tinfo_t_get_stock(*args):
    r"""
    tinfo_t_get_stock(id) -> tinfo_t

    @param id: enum stock_type_id_t
    """
    return _ida_typeinf.tinfo_t_get_stock(*args)
TCMP_EQUAL = _ida_typeinf.TCMP_EQUAL
r"""
are types equal?
"""

TCMP_IGNMODS = _ida_typeinf.TCMP_IGNMODS
r"""
ignore const/volatile modifiers
"""

TCMP_AUTOCAST = _ida_typeinf.TCMP_AUTOCAST
r"""
can t1 be cast into t2 automatically?
"""

TCMP_MANCAST = _ida_typeinf.TCMP_MANCAST
r"""
can t1 be cast into t2 manually?
"""

TCMP_CALL = _ida_typeinf.TCMP_CALL
r"""
can t1 be called with t2 type?
"""

TCMP_DELPTR = _ida_typeinf.TCMP_DELPTR
r"""
remove pointer from types before comparing
"""

TCMP_DECL = _ida_typeinf.TCMP_DECL
r"""
compare declarations without resolving them
"""

TCMP_ANYBASE = _ida_typeinf.TCMP_ANYBASE
r"""
accept any base class when casting
"""

TCMP_SKIPTHIS = _ida_typeinf.TCMP_SKIPTHIS
r"""
skip the first function argument in comparison
"""


class simd_info_t(object):
    r"""
    Proxy of C++ simd_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = property(_ida_typeinf.simd_info_t_name_get, _ida_typeinf.simd_info_t_name_set, doc=r"""name""")
    r"""
    name of SIMD type (nullptr-undefined)
    """
    tif = property(_ida_typeinf.simd_info_t_tif_get, _ida_typeinf.simd_info_t_tif_set, doc=r"""tif""")
    r"""
    SIMD type (empty-undefined)
    """
    size = property(_ida_typeinf.simd_info_t_size_get, _ida_typeinf.simd_info_t_size_set, doc=r"""size""")
    r"""
    SIMD type size in bytes (0-undefined)
    """
    memtype = property(_ida_typeinf.simd_info_t_memtype_get, _ida_typeinf.simd_info_t_memtype_set, doc=r"""memtype""")
    r"""
    member type BTF_INT8/16/32/64/128, BTF_UINT8/16/32/64/128 BTF_INT - integrals of
    any size/sign BTF_FLOAT, BTF_DOUBLE BTF_TBYTE - floatings of any size BTF_UNION
    - union of integral and floating types BTF_UNK - undefined
    """

    def __init__(self, *args):
        r"""
        __init__(self, nm=None, sz=0, memt=BTF_UNK) -> simd_info_t

        @param nm: char const *
        @param sz: uint16
        @param memt: type_t
        """
        _ida_typeinf.simd_info_t_swiginit(self, _ida_typeinf.new_simd_info_t(*args))

    def match_pattern(self, *args):
        r"""
        match_pattern(self, pattern) -> bool

        @param pattern: simd_info_t const *
        """
        return _ida_typeinf.simd_info_t_match_pattern(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_simd_info_t

# Register simd_info_t in _ida_typeinf:
_ida_typeinf.simd_info_t_swigregister(simd_info_t)


def guess_func_cc(*args):
    r"""
    guess_func_cc(fti, npurged, cc_flags) -> cm_t
    Use func_type_data_t::guess_cc()

    @param fti: (C++: const func_type_data_t &) func_type_data_t const &
    @param npurged: (C++: int)
    @param cc_flags: (C++: int)
    """
    return _ida_typeinf.guess_func_cc(*args)

def dump_func_type_data(*args):
    r"""
    dump_func_type_data(fti, praloc_bits) -> str
    Use func_type_data_t::dump()

    @param fti: (C++: const func_type_data_t &) func_type_data_t const &
    @param praloc_bits: (C++: int)
    """
    return _ida_typeinf.dump_func_type_data(*args)
class ptr_type_data_t(object):
    r"""
    Proxy of C++ ptr_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    obj_type = property(_ida_typeinf.ptr_type_data_t_obj_type_get, _ida_typeinf.ptr_type_data_t_obj_type_set, doc=r"""obj_type""")
    r"""
    pointed object type
    """
    closure = property(_ida_typeinf.ptr_type_data_t_closure_get, _ida_typeinf.ptr_type_data_t_closure_set, doc=r"""closure""")
    r"""
    cannot have both closure and based_ptr_size
    """
    based_ptr_size = property(_ida_typeinf.ptr_type_data_t_based_ptr_size_get, _ida_typeinf.ptr_type_data_t_based_ptr_size_set, doc=r"""based_ptr_size""")
    taptr_bits = property(_ida_typeinf.ptr_type_data_t_taptr_bits_get, _ida_typeinf.ptr_type_data_t_taptr_bits_set, doc=r"""taptr_bits""")
    r"""
    TAH bits.
    """
    parent = property(_ida_typeinf.ptr_type_data_t_parent_get, _ida_typeinf.ptr_type_data_t_parent_set, doc=r"""parent""")
    r"""
    Parent struct.
    """
    delta = property(_ida_typeinf.ptr_type_data_t_delta_get, _ida_typeinf.ptr_type_data_t_delta_set, doc=r"""delta""")
    r"""
    Offset from the beginning of the parent struct.
    """

    def __init__(self, *args):
        r"""
        __init__(self, c=tinfo_t(), bps=0, p=tinfo_t(), d=0) -> ptr_type_data_t

        @param c: tinfo_t
        @param bps: uchar
        @param p: tinfo_t
        @param d: int32
        """
        _ida_typeinf.ptr_type_data_t_swiginit(self, _ida_typeinf.new_ptr_type_data_t(*args))

    def swap(self, *args):
        r"""
        swap(self, r)
        Set this = r and r = this.

        @param r: (C++: ptr_type_data_t &)
        """
        return _ida_typeinf.ptr_type_data_t_swap(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: ptr_type_data_t const &
        """
        return _ida_typeinf.ptr_type_data_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: ptr_type_data_t const &
        """
        return _ida_typeinf.ptr_type_data_t___ne__(self, *args)

    def is_code_ptr(self, *args):
        r"""
        is_code_ptr(self) -> bool
        Are we pointing to code?
        """
        return _ida_typeinf.ptr_type_data_t_is_code_ptr(self, *args)

    def is_shifted(self, *args):
        r"""
        is_shifted(self) -> bool
        """
        return _ida_typeinf.ptr_type_data_t_is_shifted(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_ptr_type_data_t

# Register ptr_type_data_t in _ida_typeinf:
_ida_typeinf.ptr_type_data_t_swigregister(ptr_type_data_t)

class array_type_data_t(object):
    r"""
    Proxy of C++ array_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    elem_type = property(_ida_typeinf.array_type_data_t_elem_type_get, _ida_typeinf.array_type_data_t_elem_type_set, doc=r"""elem_type""")
    r"""
    element type
    """
    base = property(_ida_typeinf.array_type_data_t_base_get, _ida_typeinf.array_type_data_t_base_set, doc=r"""base""")
    r"""
    array base
    """
    nelems = property(_ida_typeinf.array_type_data_t_nelems_get, _ida_typeinf.array_type_data_t_nelems_set, doc=r"""nelems""")
    r"""
    number of elements
    """

    def __init__(self, *args):
        r"""
        __init__(self, b=0, n=0) -> array_type_data_t

        @param b: size_t
        @param n: size_t
        """
        _ida_typeinf.array_type_data_t_swiginit(self, _ida_typeinf.new_array_type_data_t(*args))

    def swap(self, *args):
        r"""
        swap(self, r)
        set this = r and r = this

        @param r: (C++: array_type_data_t &)
        """
        return _ida_typeinf.array_type_data_t_swap(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_array_type_data_t

# Register array_type_data_t in _ida_typeinf:
_ida_typeinf.array_type_data_t_swigregister(array_type_data_t)

class funcarg_t(object):
    r"""
    Proxy of C++ funcarg_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    argloc = property(_ida_typeinf.funcarg_t_argloc_get, _ida_typeinf.funcarg_t_argloc_set, doc=r"""argloc""")
    r"""
    argument location
    """
    name = property(_ida_typeinf.funcarg_t_name_get, _ida_typeinf.funcarg_t_name_set, doc=r"""name""")
    r"""
    argument name (may be empty)
    """
    cmt = property(_ida_typeinf.funcarg_t_cmt_get, _ida_typeinf.funcarg_t_cmt_set, doc=r"""cmt""")
    r"""
    argument comment (may be empty)
    """
    type = property(_ida_typeinf.funcarg_t_type_get, _ida_typeinf.funcarg_t_type_set, doc=r"""type""")
    r"""
    argument type
    """
    flags = property(_ida_typeinf.funcarg_t_flags_get, _ida_typeinf.funcarg_t_flags_set, doc=r"""flags""")
    r"""
    Function argument property bits
    """

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: funcarg_t const &
        """
        return _ida_typeinf.funcarg_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: funcarg_t const &
        """
        return _ida_typeinf.funcarg_t___ne__(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> funcarg_t
        """
        _ida_typeinf.funcarg_t_swiginit(self, _ida_typeinf.new_funcarg_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_funcarg_t

# Register funcarg_t in _ida_typeinf:
_ida_typeinf.funcarg_t_swigregister(funcarg_t)
FAI_HIDDEN = _ida_typeinf.FAI_HIDDEN
r"""
hidden argument
"""

FAI_RETPTR = _ida_typeinf.FAI_RETPTR
r"""
pointer to return value. implies hidden
"""

FAI_STRUCT = _ida_typeinf.FAI_STRUCT
r"""
was initially a structure
"""

FAI_ARRAY = _ida_typeinf.FAI_ARRAY
r"""
was initially an array; see "__org_typedef" or "__org_arrdim" type attributes to
determine the original type
"""

FAI_UNUSED = _ida_typeinf.FAI_UNUSED
r"""
argument is not used by the function
"""

TA_ORG_TYPEDEF = _ida_typeinf.TA_ORG_TYPEDEF
r"""
the original typedef name (simple string)
"""

TA_ORG_ARRDIM = _ida_typeinf.TA_ORG_ARRDIM
r"""
the original array dimension (pack_dd)
"""

TA_FORMAT = _ida_typeinf.TA_FORMAT
r"""
info about the 'format' argument. 3 times pack_dd: format_functype_t, argument
number of 'format', argument number of '...'
"""


class func_type_data_t(funcargvec_t):
    r"""
    Proxy of C++ func_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    flags = property(_ida_typeinf.func_type_data_t_flags_get, _ida_typeinf.func_type_data_t_flags_set, doc=r"""flags""")
    r"""
    Function type data property bits
    """
    rettype = property(_ida_typeinf.func_type_data_t_rettype_get, _ida_typeinf.func_type_data_t_rettype_set, doc=r"""rettype""")
    r"""
    return type
    """
    retloc = property(_ida_typeinf.func_type_data_t_retloc_get, _ida_typeinf.func_type_data_t_retloc_set, doc=r"""retloc""")
    r"""
    return location
    """
    stkargs = property(_ida_typeinf.func_type_data_t_stkargs_get, _ida_typeinf.func_type_data_t_stkargs_set, doc=r"""stkargs""")
    r"""
    size of stack arguments (not used in build_func_type)
    """
    spoiled = property(_ida_typeinf.func_type_data_t_spoiled_get, _ida_typeinf.func_type_data_t_spoiled_set, doc=r"""spoiled""")
    r"""
    spoiled register information. if spoiled register info is present, it overrides
    the standard spoil info (eax, edx, ecx for x86)
    """
    cc = property(_ida_typeinf.func_type_data_t_cc_get, _ida_typeinf.func_type_data_t_cc_set, doc=r"""cc""")
    r"""
    calling convention
    """

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: func_type_data_t &
        """
        return _ida_typeinf.func_type_data_t_swap(self, *args)

    def is_high(self, *args):
        r"""
        is_high(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_high(self, *args)

    def is_noret(self, *args):
        r"""
        is_noret(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_noret(self, *args)

    def is_pure(self, *args):
        r"""
        is_pure(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_pure(self, *args)

    def is_static(self, *args):
        r"""
        is_static(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_static(self, *args)

    def is_virtual(self, *args):
        r"""
        is_virtual(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_virtual(self, *args)

    def is_const(self, *args):
        r"""
        is_const(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_const(self, *args)

    def is_ctor(self, *args):
        r"""
        is_ctor(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_ctor(self, *args)

    def is_dtor(self, *args):
        r"""
        is_dtor(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_dtor(self, *args)

    def get_call_method(self, *args):
        r"""
        get_call_method(self) -> int
        """
        return _ida_typeinf.func_type_data_t_get_call_method(self, *args)

    def is_vararg_cc(self, *args):
        r"""
        is_vararg_cc(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_vararg_cc(self, *args)

    def is_golang_cc(self, *args):
        r"""
        is_golang_cc(self) -> bool
        """
        return _ida_typeinf.func_type_data_t_is_golang_cc(self, *args)

    def guess_cc(self, *args):
        r"""
        guess_cc(self, purged, cc_flags) -> cm_t
        Guess function calling convention use the following info: argument locations and
        'stkargs'

        @param purged: (C++: int)
        @param cc_flags: (C++: int)
        """
        return _ida_typeinf.func_type_data_t_guess_cc(self, *args)

    def dump(self, *args):
        r"""
        dump(self, praloc_bits=0x02) -> bool
        Dump information that is not always visible in the function prototype. (argument
        locations, return location, total stkarg size)

        @param praloc_bits: (C++: int)
        """
        return _ida_typeinf.func_type_data_t_dump(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_func_type_data_t

    def __init__(self, *args):
        r"""
        __init__(self) -> func_type_data_t
        """
        _ida_typeinf.func_type_data_t_swiginit(self, _ida_typeinf.new_func_type_data_t(*args))

# Register func_type_data_t in _ida_typeinf:
_ida_typeinf.func_type_data_t_swigregister(func_type_data_t)
FTI_SPOILED = _ida_typeinf.FTI_SPOILED
r"""
information about spoiled registers is present
"""

FTI_NORET = _ida_typeinf.FTI_NORET
r"""
noreturn
"""

FTI_PURE = _ida_typeinf.FTI_PURE
r"""
__pure
"""

FTI_HIGH = _ida_typeinf.FTI_HIGH
r"""
high level prototype (with possibly hidden args)
"""

FTI_STATIC = _ida_typeinf.FTI_STATIC
r"""
static
"""

FTI_VIRTUAL = _ida_typeinf.FTI_VIRTUAL
r"""
virtual
"""

FTI_CALLTYPE = _ida_typeinf.FTI_CALLTYPE
r"""
mask for FTI_*CALL
"""

FTI_DEFCALL = _ida_typeinf.FTI_DEFCALL
r"""
default call
"""

FTI_NEARCALL = _ida_typeinf.FTI_NEARCALL
r"""
near call
"""

FTI_FARCALL = _ida_typeinf.FTI_FARCALL
r"""
far call
"""

FTI_INTCALL = _ida_typeinf.FTI_INTCALL
r"""
interrupt call
"""

FTI_ARGLOCS = _ida_typeinf.FTI_ARGLOCS
r"""
info about argument locations has been calculated (stkargs and retloc too)
"""

FTI_EXPLOCS = _ida_typeinf.FTI_EXPLOCS
r"""
all arglocs are specified explicitly
"""

FTI_CONST = _ida_typeinf.FTI_CONST
r"""
const member function
"""

FTI_CTOR = _ida_typeinf.FTI_CTOR
r"""
constructor
"""

FTI_DTOR = _ida_typeinf.FTI_DTOR
r"""
destructor
"""

FTI_ALL = _ida_typeinf.FTI_ALL
r"""
all defined bits
"""

CC_CDECL_OK = _ida_typeinf.CC_CDECL_OK
r"""
can use __cdecl calling convention?
"""

CC_ALLOW_ARGPERM = _ida_typeinf.CC_ALLOW_ARGPERM
r"""
disregard argument order?
"""

CC_ALLOW_REGHOLES = _ida_typeinf.CC_ALLOW_REGHOLES
r"""
allow holes in register argument list?
"""

CC_HAS_ELLIPSIS = _ida_typeinf.CC_HAS_ELLIPSIS
r"""
function has a variable list of arguments?
"""

CC_GOLANG_OK = _ida_typeinf.CC_GOLANG_OK
r"""
can use __golang calling convention
"""


FMTFUNC_PRINTF = _ida_typeinf.FMTFUNC_PRINTF

FMTFUNC_SCANF = _ida_typeinf.FMTFUNC_SCANF

FMTFUNC_STRFTIME = _ida_typeinf.FMTFUNC_STRFTIME

FMTFUNC_STRFMON = _ida_typeinf.FMTFUNC_STRFMON

class stkarg_area_info_t(object):
    r"""
    Proxy of C++ stkarg_area_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    cb = property(_ida_typeinf.stkarg_area_info_t_cb_get, _ida_typeinf.stkarg_area_info_t_cb_set, doc=r"""cb""")
    stkarg_offset = property(_ida_typeinf.stkarg_area_info_t_stkarg_offset_get, _ida_typeinf.stkarg_area_info_t_stkarg_offset_set, doc=r"""stkarg_offset""")
    r"""
    Offset from the SP to the first stack argument (can include linkage area)
    examples: pc: 0, hppa: -0x34, ppc aix: 0x18
    """
    shadow_size = property(_ida_typeinf.stkarg_area_info_t_shadow_size_get, _ida_typeinf.stkarg_area_info_t_shadow_size_set, doc=r"""shadow_size""")
    r"""
    Size of the shadow area. explanations at:
    \link{https://stackoverflow.com/questions/30190132/what-is-the-shadow-space-
    in-x64-assembly} examples: x64 Visual Studio C++: 0x20, x64 gcc: 0, ppc aix:
    0x20
    """
    linkage_area = property(_ida_typeinf.stkarg_area_info_t_linkage_area_get, _ida_typeinf.stkarg_area_info_t_linkage_area_set, doc=r"""linkage_area""")
    r"""
    Size of the linkage area. explanations at: \link{https://www.ibm.com/docs/en/xl-
    fortran-aix/16.1.0?topic=conventions-linkage-area} examples: pc: 0, hppa: 0, ppc
    aix: 0x18 (equal to stkarg_offset)
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> stkarg_area_info_t
        """
        _ida_typeinf.stkarg_area_info_t_swiginit(self, _ida_typeinf.new_stkarg_area_info_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_stkarg_area_info_t

# Register stkarg_area_info_t in _ida_typeinf:
_ida_typeinf.stkarg_area_info_t_swigregister(stkarg_area_info_t)

class enum_member_t(object):
    r"""
    Proxy of C++ enum_member_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = property(_ida_typeinf.enum_member_t_name_get, _ida_typeinf.enum_member_t_name_set, doc=r"""name""")
    cmt = property(_ida_typeinf.enum_member_t_cmt_get, _ida_typeinf.enum_member_t_cmt_set, doc=r"""cmt""")
    value = property(_ida_typeinf.enum_member_t_value_get, _ida_typeinf.enum_member_t_value_set, doc=r"""value""")

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: enum_member_t const &
        """
        return _ida_typeinf.enum_member_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: enum_member_t const &
        """
        return _ida_typeinf.enum_member_t___ne__(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: enum_member_t &
        """
        return _ida_typeinf.enum_member_t_swap(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> enum_member_t
        """
        _ida_typeinf.enum_member_t_swiginit(self, _ida_typeinf.new_enum_member_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_enum_member_t

# Register enum_member_t in _ida_typeinf:
_ida_typeinf.enum_member_t_swigregister(enum_member_t)

class enum_type_data_t(enum_member_vec_t):
    r"""
    Proxy of C++ enum_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    group_sizes = property(_ida_typeinf.enum_type_data_t_group_sizes_get, _ida_typeinf.enum_type_data_t_group_sizes_set, doc=r"""group_sizes""")
    r"""
    if present, specifies bitfield group sizes each group starts with a mask member
    """
    taenum_bits = property(_ida_typeinf.enum_type_data_t_taenum_bits_get, _ida_typeinf.enum_type_data_t_taenum_bits_set, doc=r"""taenum_bits""")
    r"""
    Type attributes for enums
    """
    bte = property(_ida_typeinf.enum_type_data_t_bte_get, _ida_typeinf.enum_type_data_t_bte_set, doc=r"""bte""")
    r"""
    enum member sizes (shift amount) and style
    """

    def __init__(self, *args):
        r"""
        __init__(self, _bte=BTE_ALWAYS|BTE_HEX) -> enum_type_data_t

        @param _bte: bte_t
        """
        _ida_typeinf.enum_type_data_t_swiginit(self, _ida_typeinf.new_enum_type_data_t(*args))

    def is_64bit(self, *args):
        r"""
        is_64bit(self) -> bool
        """
        return _ida_typeinf.enum_type_data_t_is_64bit(self, *args)

    def is_hex(self, *args):
        r"""
        is_hex(self) -> bool
        """
        return _ida_typeinf.enum_type_data_t_is_hex(self, *args)

    def is_char(self, *args):
        r"""
        is_char(self) -> bool
        """
        return _ida_typeinf.enum_type_data_t_is_char(self, *args)

    def is_sdec(self, *args):
        r"""
        is_sdec(self) -> bool
        """
        return _ida_typeinf.enum_type_data_t_is_sdec(self, *args)

    def is_udec(self, *args):
        r"""
        is_udec(self) -> bool
        """
        return _ida_typeinf.enum_type_data_t_is_udec(self, *args)

    def calc_nbytes(self, *args):
        r"""
        calc_nbytes(self) -> int
        """
        return _ida_typeinf.enum_type_data_t_calc_nbytes(self, *args)

    def calc_mask(self, *args):
        r"""
        calc_mask(self) -> uint64
        """
        return _ida_typeinf.enum_type_data_t_calc_mask(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)
        swap two instances

        @param r: (C++: enum_type_data_t &)
        """
        return _ida_typeinf.enum_type_data_t_swap(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_enum_type_data_t

# Register enum_type_data_t in _ida_typeinf:
_ida_typeinf.enum_type_data_t_swigregister(enum_type_data_t)

class typedef_type_data_t(object):
    r"""
    Proxy of C++ typedef_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    til = property(_ida_typeinf.typedef_type_data_t_til_get, _ida_typeinf.typedef_type_data_t_til_set, doc=r"""til""")
    r"""
    type library to use when resolving
    """
    name = property(_ida_typeinf.typedef_type_data_t_name_get, _ida_typeinf.typedef_type_data_t_name_set, doc=r"""name""")
    r"""
    is_ordref=false: target type name. we do not own this pointer!
    """
    ordinal = property(_ida_typeinf.typedef_type_data_t_ordinal_get, _ida_typeinf.typedef_type_data_t_ordinal_set, doc=r"""ordinal""")
    r"""
    is_ordref=true: type ordinal number
    """
    is_ordref = property(_ida_typeinf.typedef_type_data_t_is_ordref_get, _ida_typeinf.typedef_type_data_t_is_ordref_set, doc=r"""is_ordref""")
    r"""
    is reference by ordinal?
    """
    resolve = property(_ida_typeinf.typedef_type_data_t_resolve_get, _ida_typeinf.typedef_type_data_t_resolve_set, doc=r"""resolve""")
    r"""
    should resolve immediately?
    """

    def __init__(self, *args):
        r"""
        __init__(self, _til, _name, _resolve=False) -> typedef_type_data_t

        @param _til: til_t const *
        @param _name: char const *
        @param _resolve: bool

        __init__(self, _til, ord, _resolve=False) -> typedef_type_data_t

        @param _til: til_t const *
        @param ord: uint32
        @param _resolve: bool
        """
        _ida_typeinf.typedef_type_data_t_swiginit(self, _ida_typeinf.new_typedef_type_data_t(*args))

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: typedef_type_data_t &
        """
        return _ida_typeinf.typedef_type_data_t_swap(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_typedef_type_data_t

# Register typedef_type_data_t in _ida_typeinf:
_ida_typeinf.typedef_type_data_t_swigregister(typedef_type_data_t)

class udt_member_t(object):
    r"""
    Proxy of C++ udt_member_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    offset = property(_ida_typeinf.udt_member_t_offset_get, _ida_typeinf.udt_member_t_offset_set, doc=r"""offset""")
    r"""
    member offset in bits
    """
    size = property(_ida_typeinf.udt_member_t_size_get, _ida_typeinf.udt_member_t_size_set, doc=r"""size""")
    r"""
    size in bits
    """
    name = property(_ida_typeinf.udt_member_t_name_get, _ida_typeinf.udt_member_t_name_set, doc=r"""name""")
    r"""
    member name
    """
    cmt = property(_ida_typeinf.udt_member_t_cmt_get, _ida_typeinf.udt_member_t_cmt_set, doc=r"""cmt""")
    r"""
    member comment
    """
    type = property(_ida_typeinf.udt_member_t_type_get, _ida_typeinf.udt_member_t_type_set, doc=r"""type""")
    r"""
    member type
    """
    effalign = property(_ida_typeinf.udt_member_t_effalign_get, _ida_typeinf.udt_member_t_effalign_set, doc=r"""effalign""")
    r"""
    effective field alignment (in bytes)
    """
    tafld_bits = property(_ida_typeinf.udt_member_t_tafld_bits_get, _ida_typeinf.udt_member_t_tafld_bits_set, doc=r"""tafld_bits""")
    r"""
    TAH bits.
    """
    fda = property(_ida_typeinf.udt_member_t_fda_get, _ida_typeinf.udt_member_t_fda_set, doc=r"""fda""")
    r"""
    field alignment (shift amount)
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> udt_member_t
        """
        _ida_typeinf.udt_member_t_swiginit(self, _ida_typeinf.new_udt_member_t(*args))

    def is_bitfield(self, *args):
        r"""
        is_bitfield(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_bitfield(self, *args)

    def is_zero_bitfield(self, *args):
        r"""
        is_zero_bitfield(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_zero_bitfield(self, *args)

    def is_unaligned(self, *args):
        r"""
        is_unaligned(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_unaligned(self, *args)

    def is_baseclass(self, *args):
        r"""
        is_baseclass(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_baseclass(self, *args)

    def is_virtbase(self, *args):
        r"""
        is_virtbase(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_virtbase(self, *args)

    def is_vftable(self, *args):
        r"""
        is_vftable(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_vftable(self, *args)

    def is_method(self, *args):
        r"""
        is_method(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_method(self, *args)

    def set_unaligned(self, *args):
        r"""
        set_unaligned(self)
        """
        return _ida_typeinf.udt_member_t_set_unaligned(self, *args)

    def set_baseclass(self, *args):
        r"""
        set_baseclass(self)
        """
        return _ida_typeinf.udt_member_t_set_baseclass(self, *args)

    def set_virtbase(self, *args):
        r"""
        set_virtbase(self)
        """
        return _ida_typeinf.udt_member_t_set_virtbase(self, *args)

    def set_vftable(self, *args):
        r"""
        set_vftable(self)
        """
        return _ida_typeinf.udt_member_t_set_vftable(self, *args)

    def set_method(self, *args):
        r"""
        set_method(self)
        """
        return _ida_typeinf.udt_member_t_set_method(self, *args)

    def clr_unaligned(self, *args):
        r"""
        clr_unaligned(self)
        """
        return _ida_typeinf.udt_member_t_clr_unaligned(self, *args)

    def clr_baseclass(self, *args):
        r"""
        clr_baseclass(self)
        """
        return _ida_typeinf.udt_member_t_clr_baseclass(self, *args)

    def clr_virtbase(self, *args):
        r"""
        clr_virtbase(self)
        """
        return _ida_typeinf.udt_member_t_clr_virtbase(self, *args)

    def clr_vftable(self, *args):
        r"""
        clr_vftable(self)
        """
        return _ida_typeinf.udt_member_t_clr_vftable(self, *args)

    def clr_method(self, *args):
        r"""
        clr_method(self)
        """
        return _ida_typeinf.udt_member_t_clr_method(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> uint64
        """
        return _ida_typeinf.udt_member_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> uint64
        """
        return _ida_typeinf.udt_member_t_end(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: udt_member_t const &
        """
        return _ida_typeinf.udt_member_t___lt__(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: udt_member_t const &
        """
        return _ida_typeinf.udt_member_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: udt_member_t const &
        """
        return _ida_typeinf.udt_member_t___ne__(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: udt_member_t &
        """
        return _ida_typeinf.udt_member_t_swap(self, *args)

    def is_anonymous_udm(self, *args):
        r"""
        is_anonymous_udm(self) -> bool
        """
        return _ida_typeinf.udt_member_t_is_anonymous_udm(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_udt_member_t

# Register udt_member_t in _ida_typeinf:
_ida_typeinf.udt_member_t_swigregister(udt_member_t)

class udtmembervec_t(udtmembervec_template_t):
    r"""
    Proxy of C++ udtmembervec_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> udtmembervec_t
        """
        _ida_typeinf.udtmembervec_t_swiginit(self, _ida_typeinf.new_udtmembervec_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_udtmembervec_t

# Register udtmembervec_t in _ida_typeinf:
_ida_typeinf.udtmembervec_t_swigregister(udtmembervec_t)

class udt_type_data_t(udtmembervec_t):
    r"""
    Proxy of C++ udt_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    total_size = property(_ida_typeinf.udt_type_data_t_total_size_get, _ida_typeinf.udt_type_data_t_total_size_set, doc=r"""total_size""")
    r"""
    total structure size in bytes
    """
    unpadded_size = property(_ida_typeinf.udt_type_data_t_unpadded_size_get, _ida_typeinf.udt_type_data_t_unpadded_size_set, doc=r"""unpadded_size""")
    r"""
    unpadded structure size in bytes
    """
    effalign = property(_ida_typeinf.udt_type_data_t_effalign_get, _ida_typeinf.udt_type_data_t_effalign_set, doc=r"""effalign""")
    r"""
    effective structure alignment (in bytes)
    """
    taudt_bits = property(_ida_typeinf.udt_type_data_t_taudt_bits_get, _ida_typeinf.udt_type_data_t_taudt_bits_set, doc=r"""taudt_bits""")
    r"""
    TA... and TAUDT... bits.
    """
    sda = property(_ida_typeinf.udt_type_data_t_sda_get, _ida_typeinf.udt_type_data_t_sda_set, doc=r"""sda""")
    r"""
    declared structure alignment (shift amount+1). 0 - unspecified
    """
    pack = property(_ida_typeinf.udt_type_data_t_pack_get, _ida_typeinf.udt_type_data_t_pack_set, doc=r"""pack""")
    r"""
    #pragma pack() alignment (shift amount)
    """
    is_union = property(_ida_typeinf.udt_type_data_t_is_union_get, _ida_typeinf.udt_type_data_t_is_union_set, doc=r"""is_union""")
    r"""
    is union or struct?
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> udt_type_data_t
        """
        _ida_typeinf.udt_type_data_t_swiginit(self, _ida_typeinf.new_udt_type_data_t(*args))

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: udt_type_data_t &
        """
        return _ida_typeinf.udt_type_data_t_swap(self, *args)

    def is_unaligned(self, *args):
        r"""
        is_unaligned(self) -> bool
        """
        return _ida_typeinf.udt_type_data_t_is_unaligned(self, *args)

    def is_msstruct(self, *args):
        r"""
        is_msstruct(self) -> bool
        """
        return _ida_typeinf.udt_type_data_t_is_msstruct(self, *args)

    def is_cppobj(self, *args):
        r"""
        is_cppobj(self) -> bool
        """
        return _ida_typeinf.udt_type_data_t_is_cppobj(self, *args)

    def is_vftable(self, *args):
        r"""
        is_vftable(self) -> bool
        """
        return _ida_typeinf.udt_type_data_t_is_vftable(self, *args)

    def set_vftable(self, *args):
        r"""
        set_vftable(self)
        """
        return _ida_typeinf.udt_type_data_t_set_vftable(self, *args)

    def is_last_baseclass(self, *args):
        r"""
        is_last_baseclass(self, idx) -> bool

        @param idx: size_t
        """
        return _ida_typeinf.udt_type_data_t_is_last_baseclass(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_udt_type_data_t

# Register udt_type_data_t in _ida_typeinf:
_ida_typeinf.udt_type_data_t_swigregister(udt_type_data_t)

VTBL_SUFFIX = _ida_typeinf.VTBL_SUFFIX

VTBL_MEMNAME = _ida_typeinf.VTBL_MEMNAME

class bitfield_type_data_t(object):
    r"""
    Proxy of C++ bitfield_type_data_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    nbytes = property(_ida_typeinf.bitfield_type_data_t_nbytes_get, _ida_typeinf.bitfield_type_data_t_nbytes_set, doc=r"""nbytes""")
    r"""
    enclosing type size (1,2,4,8 bytes)
    """
    width = property(_ida_typeinf.bitfield_type_data_t_width_get, _ida_typeinf.bitfield_type_data_t_width_set, doc=r"""width""")
    r"""
    number of bits
    """
    is_unsigned = property(_ida_typeinf.bitfield_type_data_t_is_unsigned_get, _ida_typeinf.bitfield_type_data_t_is_unsigned_set, doc=r"""is_unsigned""")
    r"""
    is bitfield unsigned?
    """

    def __init__(self, *args):
        r"""
        __init__(self, _nbytes=0, _width=0, _is_unsigned=False) -> bitfield_type_data_t

        @param _nbytes: uchar
        @param _width: uchar
        @param _is_unsigned: bool
        """
        _ida_typeinf.bitfield_type_data_t_swiginit(self, _ida_typeinf.new_bitfield_type_data_t(*args))

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: bitfield_type_data_t const &
        """
        return _ida_typeinf.bitfield_type_data_t_compare(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: bitfield_type_data_t &
        """
        return _ida_typeinf.bitfield_type_data_t_swap(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_bitfield_type_data_t

# Register bitfield_type_data_t in _ida_typeinf:
_ida_typeinf.bitfield_type_data_t_swigregister(bitfield_type_data_t)

TPOS_LNNUM = _ida_typeinf.TPOS_LNNUM


def inf_pack_stkargs(*args):
    r"""
    inf_pack_stkargs() -> bool
    inf_pack_stkargs(cc) -> bool

    @param cc: cm_t
    """
    return _ida_typeinf.inf_pack_stkargs(*args)

def inf_big_arg_align(*args):
    r"""
    inf_big_arg_align() -> bool
    inf_big_arg_align(cc) -> bool

    @param cc: cm_t
    """
    return _ida_typeinf.inf_big_arg_align(*args)
class type_mods_t(object):
    r"""
    Proxy of C++ type_mods_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    type = property(_ida_typeinf.type_mods_t_type_get, _ida_typeinf.type_mods_t_type_set, doc=r"""type""")
    r"""
    current type
    """
    name = property(_ida_typeinf.type_mods_t_name_get, _ida_typeinf.type_mods_t_name_set, doc=r"""name""")
    r"""
    current type name
    """
    cmt = property(_ida_typeinf.type_mods_t_cmt_get, _ida_typeinf.type_mods_t_cmt_set, doc=r"""cmt""")
    r"""
    comment for current type
    """
    flags = property(_ida_typeinf.type_mods_t_flags_get, _ida_typeinf.type_mods_t_flags_set, doc=r"""flags""")
    r"""
    Type modification bits
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> type_mods_t
        """
        _ida_typeinf.type_mods_t_swiginit(self, _ida_typeinf.new_type_mods_t(*args))

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_typeinf.type_mods_t_clear(self, *args)

    def set_new_type(self, *args):
        r"""
        set_new_type(self, t)
        The visit_type() function may optionally save the modified type info. Use the
        following functions for that. The new name and comment will be applied only if
        the current tinfo element has storage for them.

        @param t: (C++: const tinfo_t &) tinfo_t const &
        """
        return _ida_typeinf.type_mods_t_set_new_type(self, *args)

    def set_new_name(self, *args):
        r"""
        set_new_name(self, n)

        @param n: qstring const &
        """
        return _ida_typeinf.type_mods_t_set_new_name(self, *args)

    def set_new_cmt(self, *args):
        r"""
        set_new_cmt(self, c)

        @param c: qstring const &
        """
        return _ida_typeinf.type_mods_t_set_new_cmt(self, *args)

    def has_type(self, *args):
        r"""
        has_type(self) -> bool
        """
        return _ida_typeinf.type_mods_t_has_type(self, *args)

    def has_name(self, *args):
        r"""
        has_name(self) -> bool
        """
        return _ida_typeinf.type_mods_t_has_name(self, *args)

    def has_cmt(self, *args):
        r"""
        has_cmt(self) -> bool
        """
        return _ida_typeinf.type_mods_t_has_cmt(self, *args)

    def has_info(self, *args):
        r"""
        has_info(self) -> bool
        """
        return _ida_typeinf.type_mods_t_has_info(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_type_mods_t

# Register type_mods_t in _ida_typeinf:
_ida_typeinf.type_mods_t_swigregister(type_mods_t)
TVIS_TYPE = _ida_typeinf.TVIS_TYPE
r"""
new type info is present
"""

TVIS_NAME = _ida_typeinf.TVIS_NAME
r"""
new name is present
"""

TVIS_CMT = _ida_typeinf.TVIS_CMT
r"""
new comment is present
"""


class tinfo_visitor_t(object):
    r"""
    Proxy of C++ tinfo_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    state = property(_ida_typeinf.tinfo_visitor_t_state_get, _ida_typeinf.tinfo_visitor_t_state_set, doc=r"""state""")
    r"""
    tinfo visitor states
    """

    def __init__(self, *args):
        r"""
        __init__(self, s=0) -> tinfo_visitor_t

        @param s: int
        """
        if self.__class__ == tinfo_visitor_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.tinfo_visitor_t_swiginit(self, _ida_typeinf.new_tinfo_visitor_t(_self, *args))
    __swig_destroy__ = _ida_typeinf.delete_tinfo_visitor_t

    def visit_type(self, *args):
        r"""
        visit_type(self, out, tif, name, cmt) -> int
        Visit a subtype. this function must be implemented in the derived class. it may
        optionally fill out with the new type info. this can be used to modify types (in
        this case the 'out' argument of apply_to() may not be nullptr) return 0 to
        continue the traversal. return !=0 to stop the traversal.

        @param out: (C++: type_mods_t *)
        @param tif: (C++: const tinfo_t &) tinfo_t const &
        @param name: (C++: const char *) char const *
        @param cmt: (C++: const char *) char const *
        """
        return _ida_typeinf.tinfo_visitor_t_visit_type(self, *args)

    def prune_now(self, *args):
        r"""
        prune_now(self)
        To refuse to visit children of the current type, use this:
        """
        return _ida_typeinf.tinfo_visitor_t_prune_now(self, *args)

    def apply_to(self, *args):
        r"""
        apply_to(self, tif, out=None, name=None, cmt=None) -> int
        Call this function to initiate the traversal.

        @param tif: (C++: const tinfo_t &) tinfo_t const &
        @param out: (C++: type_mods_t *)
        @param name: (C++: const char *) char const *
        @param cmt: (C++: const char *) char const *
        """
        return _ida_typeinf.tinfo_visitor_t_apply_to(self, *args)
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_tinfo_visitor_t(self)
        return weakref.proxy(self)

# Register tinfo_visitor_t in _ida_typeinf:
_ida_typeinf.tinfo_visitor_t_swigregister(tinfo_visitor_t)
TVST_PRUNE = _ida_typeinf.TVST_PRUNE
r"""
don't visit children of current type
"""

TVST_DEF = _ida_typeinf.TVST_DEF
r"""
visit type definition (meaningful for typerefs)
"""

TVST_LEVEL = _ida_typeinf.TVST_LEVEL


class regobj_t(object):
    r"""
    Proxy of C++ regobj_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    regidx = property(_ida_typeinf.regobj_t_regidx_get, _ida_typeinf.regobj_t_regidx_set, doc=r"""regidx""")
    r"""
    index into dbg->registers
    """
    relocate = property(_ida_typeinf.regobj_t_relocate_get, _ida_typeinf.regobj_t_relocate_set, doc=r"""relocate""")
    r"""
    0-plain num, 1-must relocate
    """
    value = property(_ida_typeinf.regobj_t_value_get, _ida_typeinf.regobj_t_value_set, doc=r"""value""")

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_typeinf.regobj_t_size(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> regobj_t
        """
        _ida_typeinf.regobj_t_swiginit(self, _ida_typeinf.new_regobj_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_regobj_t

# Register regobj_t in _ida_typeinf:
_ida_typeinf.regobj_t_swigregister(regobj_t)

class regobjs_t(regobjvec_t):
    r"""
    Proxy of C++ regobjs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> regobjs_t
        """
        _ida_typeinf.regobjs_t_swiginit(self, _ida_typeinf.new_regobjs_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_regobjs_t

# Register regobjs_t in _ida_typeinf:
_ida_typeinf.regobjs_t_swigregister(regobjs_t)


def unpack_idcobj_from_idb(*args):
    r"""
    unpack_idcobj_from_idb(obj, tif, ea, off0, pio_flags=0) -> error_t
    Collection of register objects.

    Read a typed idc object from the database

    @param obj: (C++: idc_value_t *)
    @param tif: (C++: const tinfo_t &) tinfo_t const &
    @param ea: (C++: ea_t)
    @param off0: (C++: const bytevec_t *) bytevec_t const *
    @param pio_flags: (C++: int)
    """
    return _ida_typeinf.unpack_idcobj_from_idb(*args)
PIO_NOATTR_FAIL = _ida_typeinf.PIO_NOATTR_FAIL
r"""
missing attributes are not ok
"""

PIO_IGNORE_PTRS = _ida_typeinf.PIO_IGNORE_PTRS
r"""
do not follow pointers
"""


def unpack_idcobj_from_bv(*args):
    r"""
    unpack_idcobj_from_bv(obj, tif, bytes, pio_flags=0) -> error_t
    Read a typed idc object from the byte vector.

    @param obj: (C++: idc_value_t *)
    @param tif: (C++: const tinfo_t &) tinfo_t const &
    @param bytes: (C++: const bytevec_t &) bytevec_t const &
    @param pio_flags: (C++: int)
    """
    return _ida_typeinf.unpack_idcobj_from_bv(*args)

def pack_idcobj_to_idb(*args):
    r"""
    pack_idcobj_to_idb(obj, tif, ea, pio_flags=0) -> error_t
    Write a typed idc object to the database.

    @param obj: (C++: const idc_value_t *) idc_value_t const *
    @param tif: (C++: const tinfo_t &) tinfo_t const &
    @param ea: (C++: ea_t)
    @param pio_flags: (C++: int)
    """
    return _ida_typeinf.pack_idcobj_to_idb(*args)

def pack_idcobj_to_bv(*args):
    r"""
    pack_idcobj_to_bv(obj, tif, bytes, objoff, pio_flags=0) -> error_t
    Write a typed idc object to the byte vector. Byte vector may be non-empty, this
    function will append data to it

    @param obj: (C++: const idc_value_t *) idc_value_t const *
    @param tif: (C++: const tinfo_t &) tinfo_t const &
    @param bytes: (C++: relobj_t *)
    @param objoff: (C++: void *)
    @param pio_flags: (C++: int)
    """
    return _ida_typeinf.pack_idcobj_to_bv(*args)

def apply_tinfo_to_stkarg(*args):
    r"""
    apply_tinfo_to_stkarg(insn, x, v, tif, name) -> bool
    Helper function for the processor modules. to be called from
    processor_t::use_stkarg_type

    @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param x: (C++: const op_t &) op_t const &
    @param v: (C++: uval_t)
    @param tif: (C++: const tinfo_t &) tinfo_t const &
    @param name: (C++: const char *) char const *
    """
    return _ida_typeinf.apply_tinfo_to_stkarg(*args)
class argtinfo_helper_t(object):
    r"""
    Proxy of C++ argtinfo_helper_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    reserved = property(_ida_typeinf.argtinfo_helper_t_reserved_get, _ida_typeinf.argtinfo_helper_t_reserved_set, doc=r"""reserved""")
    __swig_destroy__ = _ida_typeinf.delete_argtinfo_helper_t

    def set_op_tinfo(self, *args):
        r"""
        set_op_tinfo(self, insn, x, tif, name) -> bool
        Set the operand type as specified.

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        @param x: (C++: const op_t &) op_t const &
        @param tif: (C++: const tinfo_t &) tinfo_t const &
        @param name: (C++: const char *) char const *
        """
        return _ida_typeinf.argtinfo_helper_t_set_op_tinfo(self, *args)

    def is_stkarg_load(self, *args):
        r"""
        is_stkarg_load(self, insn, src, dst) -> bool
        Is the current insn a stkarg load?. if yes:
        * src: index of the source operand in insn_t::ops
        * dst: index of the destination operand in insn_t::ops insn_t::ops[dst].addr is
        expected to have the stack offset

        @param insn: (C++: const insn_t &) an ida_ua.insn_t, or an address (C++: const insn_t &)
        @param src: (C++: int *)
        @param dst: (C++: int *)
        """
        return _ida_typeinf.argtinfo_helper_t_is_stkarg_load(self, *args)

    def has_delay_slot(self, *args):
        r"""
        has_delay_slot(self, arg0) -> bool
        The call instruction with a delay slot?.

        @param arg0: ea_t
        """
        return _ida_typeinf.argtinfo_helper_t_has_delay_slot(self, *args)

    def use_arg_tinfos(self, *args):
        r"""
        use_arg_tinfos(self, caller, fti, rargs)
        This function is to be called by the processor module in response to
        ev_use_arg_types.

        @param caller: (C++: ea_t)
        @param fti: (C++: func_type_data_t *)
        @param rargs: (C++: funcargvec_t *)
        """
        return _ida_typeinf.argtinfo_helper_t_use_arg_tinfos(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> argtinfo_helper_t

        @param self: PyObject *
        """
        if self.__class__ == argtinfo_helper_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.argtinfo_helper_t_swiginit(self, _ida_typeinf.new_argtinfo_helper_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_argtinfo_helper_t(self)
        return weakref.proxy(self)

# Register argtinfo_helper_t in _ida_typeinf:
_ida_typeinf.argtinfo_helper_t_swigregister(argtinfo_helper_t)


def gen_use_arg_tinfos2(*args):
    r"""
    gen_use_arg_tinfos2(_this, caller, fti, rargs)
    Do not call this function directly, use argtinfo_helper_t.

    @param _this: (C++: struct argtinfo_helper_t *) argtinfo_helper_t *
    @param caller: (C++: ea_t)
    @param fti: (C++: func_type_data_t *)
    @param rargs: (C++: funcargvec_t *)
    """
    return _ida_typeinf.gen_use_arg_tinfos2(*args)

def func_has_stkframe_hole(*args):
    r"""
    func_has_stkframe_hole(ea, fti) -> bool
    Looks for a hole at the beginning of the stack arguments. Will make use of the
    IDB's func_t function at that place (if present) to help determine the presence
    of such a hole.

    @param ea: (C++: ea_t)
    @param fti: (C++: const func_type_data_t &) func_type_data_t const &
    """
    return _ida_typeinf.func_has_stkframe_hole(*args)
class lowertype_helper_t(object):
    r"""
    Proxy of C++ lowertype_helper_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def func_has_stkframe_hole(self, *args):
        r"""
        func_has_stkframe_hole(self, candidate, candidate_data) -> bool

        @param candidate: tinfo_t const &
        @param candidate_data: func_type_data_t const &
        """
        return _ida_typeinf.lowertype_helper_t_func_has_stkframe_hole(self, *args)

    def get_func_purged_bytes(self, *args):
        r"""
        get_func_purged_bytes(self, candidate, candidate_data) -> int

        @param candidate: tinfo_t const &
        @param candidate_data: func_type_data_t const &
        """
        return _ida_typeinf.lowertype_helper_t_get_func_purged_bytes(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_lowertype_helper_t

# Register lowertype_helper_t in _ida_typeinf:
_ida_typeinf.lowertype_helper_t_swigregister(lowertype_helper_t)

class ida_lowertype_helper_t(lowertype_helper_t):
    r"""
    Proxy of C++ ida_lowertype_helper_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _tif, _ea, _pb) -> ida_lowertype_helper_t

        @param _tif: tinfo_t const &
        @param _ea: ea_t
        @param _pb: int
        """
        _ida_typeinf.ida_lowertype_helper_t_swiginit(self, _ida_typeinf.new_ida_lowertype_helper_t(*args))

    def func_has_stkframe_hole(self, *args):
        r"""
        func_has_stkframe_hole(self, candidate, candidate_data) -> bool

        @param candidate: tinfo_t const &
        @param candidate_data: func_type_data_t const &
        """
        return _ida_typeinf.ida_lowertype_helper_t_func_has_stkframe_hole(self, *args)

    def get_func_purged_bytes(self, *args):
        r"""
        get_func_purged_bytes(self, candidate, arg3) -> int

        @param candidate: tinfo_t const &
        @param arg3: func_type_data_t const &
        """
        return _ida_typeinf.ida_lowertype_helper_t_get_func_purged_bytes(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_ida_lowertype_helper_t

# Register ida_lowertype_helper_t in _ida_typeinf:
_ida_typeinf.ida_lowertype_helper_t_swigregister(ida_lowertype_helper_t)


def lower_type(*args):
    r"""
    lower_type(til, tif, name=None, _helper=None) -> int
    Lower type. Inspect the type and lower all function subtypes using
    lower_func_type().
    We call the prototypes usually encountered in source files "high level"
    They may have implicit arguments, array arguments, big structure retvals, etc
    We introduce explicit arguments (i.e. 'this' pointer) and call the result
    "low level prototype". See FTI_HIGH.

    In order to improve heuristics for recognition of big structure retvals,
    it is recommended to pass a helper that will be used to make decisions.
    That helper will be used only for lowering 'tif', and not for the children
    types walked through by recursion.
    @retval 1: removed FTI_HIGH,
    @retval 2: made substantial changes
    @retval -1: failure

    @param til: (C++: til_t *)
    @param tif: (C++: tinfo_t *)
    @param name: (C++: const char *) char const *
    @param _helper: (C++: lowertype_helper_t *)
    """
    return _ida_typeinf.lower_type(*args)

def replace_ordinal_typerefs(*args):
    r"""
    replace_ordinal_typerefs(til, tif) -> int
    Replace references to ordinal types by name references. This function 'unties'
    the type from the current local type library and makes it easier to export it.

    @param til: (C++: til_t *) type library to use. may be nullptr.
    @param tif: (C++: tinfo_t *) type to modify (in/out)
    @retval number: of replaced subtypes, -1 on failure
    """
    return _ida_typeinf.replace_ordinal_typerefs(*args)
UTP_ENUM = _ida_typeinf.UTP_ENUM

UTP_STRUCT = _ida_typeinf.UTP_STRUCT


def begin_type_updating(*args):
    r"""
    begin_type_updating(utp)
    Mark the beginning of a large update operation on the types. Can be used with
    add_enum_member(), add_struc_member, etc... Also see end_type_updating()

    @param utp: (C++: update_type_t) enum update_type_t
    """
    return _ida_typeinf.begin_type_updating(*args)

def end_type_updating(*args):
    r"""
    end_type_updating(utp)
    Mark the end of a large update operation on the types (see
    begin_type_updating())

    @param utp: (C++: update_type_t) enum update_type_t
    """
    return _ida_typeinf.end_type_updating(*args)
class valstr_t(object):
    r"""
    Proxy of C++ valstr_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    oneline = property(_ida_typeinf.valstr_t_oneline_get, _ida_typeinf.valstr_t_oneline_set, doc=r"""oneline""")
    r"""
    result if printed on one line in UTF-8 encoding
    """
    length = property(_ida_typeinf.valstr_t_length_get, _ida_typeinf.valstr_t_length_set, doc=r"""length""")
    r"""
    length if printed on one line
    """
    members = property(_ida_typeinf.valstr_t_members_get, _ida_typeinf.valstr_t_members_set, doc=r"""members""")
    r"""
    strings for members, each member separately
    """
    info = property(_ida_typeinf.valstr_t_info_get, _ida_typeinf.valstr_t_info_set, doc=r"""info""")
    r"""
    additional info
    """
    props = property(_ida_typeinf.valstr_t_props_get, _ida_typeinf.valstr_t_props_set, doc=r"""props""")
    r"""
    temporary properties, used internally
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> valstr_t
        """
        _ida_typeinf.valstr_t_swiginit(self, _ida_typeinf.new_valstr_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_valstr_t

# Register valstr_t in _ida_typeinf:
_ida_typeinf.valstr_t_swigregister(valstr_t)
VALSTR_OPEN = _ida_typeinf.VALSTR_OPEN
r"""
printed opening curly brace '{'
"""


class valstrs_t(valstrvec_t):
    r"""
    Proxy of C++ valstrs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> valstrs_t
        """
        _ida_typeinf.valstrs_t_swiginit(self, _ida_typeinf.new_valstrs_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_valstrs_t

# Register valstrs_t in _ida_typeinf:
_ida_typeinf.valstrs_t_swigregister(valstrs_t)

class text_sink_t(object):
    r"""
    Proxy of C++ text_sink_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def _print(self, *args):
        r"""
        _print(self, str) -> int

        Parameters
        ----------
        str: char const *

        """
        return _ida_typeinf.text_sink_t__print(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> text_sink_t

        @param self: PyObject *
        """
        if self.__class__ == text_sink_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.text_sink_t_swiginit(self, _ida_typeinf.new_text_sink_t(_self, *args))
    __swig_destroy__ = _ida_typeinf.delete_text_sink_t
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_text_sink_t(self)
        return weakref.proxy(self)

# Register text_sink_t in _ida_typeinf:
_ida_typeinf.text_sink_t_swigregister(text_sink_t)

PDF_INCL_DEPS = _ida_typeinf.PDF_INCL_DEPS
r"""
Include all type dependencies.
"""

PDF_DEF_FWD = _ida_typeinf.PDF_DEF_FWD
r"""
Allow forward declarations.
"""

PDF_DEF_BASE = _ida_typeinf.PDF_DEF_BASE
r"""
Include base types: __int8, __int16, etc..
"""

PDF_HEADER_CMT = _ida_typeinf.PDF_HEADER_CMT
r"""
Prepend output with a descriptive comment.
"""


def calc_number_of_children(*args):
    r"""
    calc_number_of_children(loc, tif, dont_deref_ptr=False) -> int
    Calculate max number of lines of a formatted c data, when expanded (PTV_EXPAND).

    @param loc: (C++: const argloc_t &) location of the data (ALOC_STATIC or ALOC_CUSTOM)
    @param tif: (C++: const tinfo_t &) type info
    @param dont_deref_ptr: (C++: bool) consider 'ea' as the ptr value
    @retval 0: data is not expandable
    @retval -1: error, see qerrno
    @retval else: the max number of lines
    """
    return _ida_typeinf.calc_number_of_children(*args)
PCN_RADIX = _ida_typeinf.PCN_RADIX
r"""
number base to use
"""

PCN_DEC = _ida_typeinf.PCN_DEC
r"""
decimal
"""

PCN_HEX = _ida_typeinf.PCN_HEX
r"""
hexadecimal
"""

PCN_OCT = _ida_typeinf.PCN_OCT
r"""
octal
"""

PCN_CHR = _ida_typeinf.PCN_CHR
r"""
character
"""

PCN_UNSIGNED = _ida_typeinf.PCN_UNSIGNED
r"""
add 'u' suffix
"""

PCN_LZHEX = _ida_typeinf.PCN_LZHEX
r"""
print leading zeroes for hexdecimal number
"""

PCN_NEGSIGN = _ida_typeinf.PCN_NEGSIGN
r"""
print negated value (-N) for negative numbers
"""

PCN_DECSEXT = _ida_typeinf.PCN_DECSEXT
r"""
automatically extend sign of signed decimal numbers
"""


def get_enum_member_expr(*args):
    r"""
    get_enum_member_expr(tif, serial, value) -> str
    Return a C expression that can be used to represent an enum member. If the value
    does not correspond to any single enum member, this function tries to find a
    bitwise combination of enum members that correspond to it. If more than half of
    value bits do not match any enum members, it fails.

    @param tif: (C++: const tinfo_t &) enumeration type
    @param serial: (C++: int) which enumeration member to use (0 means the first with the given
                   value)
    @param value: (C++: uint64) value to search in the enumeration type. only 32-bit number can be
                  handled yet
    @return: success
    """
    return _ida_typeinf.get_enum_member_expr(*args)
class til_symbol_t(object):
    r"""
    Proxy of C++ til_symbol_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = property(_ida_typeinf.til_symbol_t_name_get, _ida_typeinf.til_symbol_t_name_set, doc=r"""name""")
    r"""
    symbol name
    """
    til = property(_ida_typeinf.til_symbol_t_til_get, _ida_typeinf.til_symbol_t_til_set, doc=r"""til""")
    r"""
    pointer to til
    """

    def __init__(self, *args):
        r"""
        __init__(self, n=None, t=None) -> til_symbol_t

        @param n: char const *
        @param t: til_t const *
        """
        _ida_typeinf.til_symbol_t_swiginit(self, _ida_typeinf.new_til_symbol_t(*args))
    __swig_destroy__ = _ida_typeinf.delete_til_symbol_t

# Register til_symbol_t in _ida_typeinf:
_ida_typeinf.til_symbol_t_swigregister(til_symbol_t)

class predicate_t(object):
    r"""
    Proxy of C++ predicate_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def should_display(self, *args):
        r"""
        should_display(self, til, name, type, fields) -> bool

        @param til: til_t const *
        @param name: char const *
        @param type: type_t const *
        @param fields: p_list const *
        """
        return _ida_typeinf.predicate_t_should_display(self, *args)
    __swig_destroy__ = _ida_typeinf.delete_predicate_t

    def __init__(self, *args):
        r"""
        __init__(self) -> predicate_t

        @param self: PyObject *
        """
        if self.__class__ == predicate_t:
            _self = None
        else:
            _self = self
        _ida_typeinf.predicate_t_swiginit(self, _ida_typeinf.new_predicate_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_typeinf.disown_predicate_t(self)
        return weakref.proxy(self)

# Register predicate_t in _ida_typeinf:
_ida_typeinf.predicate_t_swigregister(predicate_t)


def choose_named_type(*args):
    r"""
    choose_named_type(out_sym, root_til, title, ntf_flags, predicate=None) -> bool
    Choose a type from a type library.

    @param out_sym: (C++: til_symbol_t *) pointer to be filled with the chosen type
    @param root_til: (C++: const til_t *) pointer to starting til (the function will inspect the base
                     tils if allowed by flags)
    @param title: (C++: const char *) title of listbox to display
    @param ntf_flags: (C++: int) combination of Flags for named types
    @param predicate: (C++: predicate_t *) predicate to select types to display (maybe nullptr)
    @return: false if nothing is chosen, otherwise true
    """
    return _ida_typeinf.choose_named_type(*args)

def choose_local_tinfo(*args):
    r"""
    choose_local_tinfo(ti, title, func=None, def_ord=0, ud=None) -> uint32
    Choose a type from the local type library.

    @param ti: (C++: const til_t *) pointer to til
    @param title: (C++: const char *) title of listbox to display
    @param func: (C++: local_tinfo_predicate_t *) predicate to select types to display (maybe nullptr)
    @param def_ord: (C++: uint32) ordinal to position cursor before choose
    @param ud: (C++: void *) user data
    @return: == 0 means nothing is chosen, otherwise an ordinal number
    """
    return _ida_typeinf.choose_local_tinfo(*args)

def choose_local_tinfo_and_delta(*args):
    r"""
    choose_local_tinfo_and_delta(delta, ti, title, func=None, def_ord=0, ud=None) -> uint32
    Choose a type from the local type library and specify the pointer shift value.

    @param delta: (C++: int32 *) pointer shift value
    @param ti: (C++: const til_t *) pointer to til
    @param title: (C++: const char *) title of listbox to display
    @param func: (C++: local_tinfo_predicate_t *) predicate to select types to display (maybe nullptr)
    @param def_ord: (C++: uint32) ordinal to position cursor before choose
    @param ud: (C++: void *) user data
    @return: == 0 means nothing is chosen, otherwise an ordinal number
    """
    return _ida_typeinf.choose_local_tinfo_and_delta(*args)

def gen_use_arg_tinfos(*args):
    r"""
    gen_use_arg_tinfos(caller, fti, rargs, set_optype, is_stkarg_load, has_delay_slot)

    @param caller: ea_t
    @param fti: func_type_data_t *
    @param rargs: funcargvec_t *
    @param set_optype: set_op_tinfo_t *
    @param is_stkarg_load: is_stkarg_load_t *
    @param has_delay_slot: has_delay_slot_t *
    """
    return _ida_typeinf.gen_use_arg_tinfos(*args)

def idc_parse_decl(*args):
    r"""
    idc_parse_decl(ti, decl, flags) -> (str, bytes, bytes) or None

    @param ti: til_t *
    @param decl: char const *
    @param flags: int
    """
    return _ida_typeinf.idc_parse_decl(*args)

def calc_type_size(*args):
    r"""
    calc_type_size(ti, tp) -> PyObject *
    Returns the size of a type

    @param ti: Type info. 'None' can be passed.
    @param tp: type string
    @return:     - None on failure
        - The size of the type
    """
    return _ida_typeinf.calc_type_size(*args)

def apply_type(*args):
    r"""
    apply_type(ti, type, fields, ea, flags) -> bool
    Apply the specified type to the address

    @param ti: Type info library. 'None' can be used.
    @param type: type_t const *
    @param fields: p_list const *
    @param ea: the address of the object
    @param flags: combination of TINFO_... constants or 0
    @return: Boolean
    """
    return _ida_typeinf.apply_type(*args)

def get_arg_addrs(*args):
    r"""
    get_arg_addrs(caller) -> PyObject *
    Retrieve addresses of argument initialization instructions

    @param caller: the address of the call instruction
    @return: list of instruction addresses
    """
    return _ida_typeinf.get_arg_addrs(*args)

def unpack_object_from_idb(*args):
    r"""
    unpack_object_from_idb(ti, type, fields, ea, pio_flags=0) -> PyObject *

    @param ti: til_t *
    @param type: type_t const *
    @param fields: p_list const *
    @param ea: ea_t
    @param pio_flags: int
    """
    return _ida_typeinf.unpack_object_from_idb(*args)

def unpack_object_from_bv(*args):
    r"""
    unpack_object_from_bv(ti, type, fields, bytes, pio_flags=0) -> PyObject *
    Unpacks a buffer into an object.
    Returns the error_t returned by idaapi.pack_object_to_idb

    @param ti: Type info. 'None' can be passed.
    @param type: type_t const *
    @param fields: fields string (may be empty or None)
    @param bytes: the bytes to unpack
    @param pio_flags: flags used while unpacking
    @return:     - tuple(0, err) on failure
        - tuple(1, obj) on success
    """
    return _ida_typeinf.unpack_object_from_bv(*args)

def pack_object_to_idb(*args):
    r"""
    pack_object_to_idb(py_obj, ti, type, fields, ea, pio_flags=0) -> PyObject *
    Write a typed object to the database.
    Raises an exception if wrong parameters were passed or conversion fails
    Returns the error_t returned by idaapi.pack_object_to_idb

    @param py_obj: PyObject *
    @param ti: Type info. 'None' can be passed.
    @param type: type_t const *
    @param fields: fields string (may be empty or None)
    @param ea: ea to be used while packing
    @param pio_flags: flags used while unpacking
    """
    return _ida_typeinf.pack_object_to_idb(*args)

def pack_object_to_bv(*args):
    r"""
    pack_object_to_bv(py_obj, ti, type, fields, base_ea, pio_flags=0) -> PyObject *
    Packs a typed object to a string

    @param py_obj: PyObject *
    @param ti: Type info. 'None' can be passed.
    @param type: type_t const *
    @param fields: fields string (may be empty or None)
    @param base_ea: base ea used to relocate the pointers in the packed object
    @param pio_flags: flags used while unpacking
    @return:     tuple(0, err_code) on failure
        tuple(1, packed_buf) on success
    """
    return _ida_typeinf.pack_object_to_bv(*args)
PT_FILE = _ida_typeinf.PT_FILE


def idc_parse_types(*args):
    r"""
    idc_parse_types(input, flags) -> int

    @param input: char const *
    @param flags: int
    """
    return _ida_typeinf.idc_parse_types(*args)

def idc_get_type_raw(*args):
    r"""
    idc_get_type_raw(ea) -> PyObject *

    @param ea: ea_t
    """
    return _ida_typeinf.idc_get_type_raw(*args)

def idc_get_local_type_raw(*args):
    r"""
    idc_get_local_type_raw(ordinal) -> (bytes, bytes)

    @param ordinal: int
    """
    return _ida_typeinf.idc_get_local_type_raw(*args)

def idc_guess_type(*args):
    r"""
    idc_guess_type(ea) -> str

    @param ea: ea_t
    """
    return _ida_typeinf.idc_guess_type(*args)

def idc_get_type(*args):
    r"""
    idc_get_type(ea) -> str

    @param ea: ea_t
    """
    return _ida_typeinf.idc_get_type(*args)

def idc_set_local_type(*args):
    r"""
    idc_set_local_type(ordinal, dcl, flags) -> int

    @param ordinal: int
    @param dcl: char const *
    @param flags: int
    """
    return _ida_typeinf.idc_set_local_type(*args)

def idc_get_local_type(*args):
    r"""
    idc_get_local_type(ordinal, flags, buf, maxsize) -> int

    @param ordinal: int
    @param flags: int
    @param buf: char *
    @param maxsize: size_t
    """
    return _ida_typeinf.idc_get_local_type(*args)

def idc_print_type(*args):
    r"""
    idc_print_type(type, fields, name, flags) -> str

    @param type: type_t const *
    @param fields: p_list const *
    @param name: char const *
    @param flags: int
    """
    return _ida_typeinf.idc_print_type(*args)

def idc_get_local_type_name(*args):
    r"""
    idc_get_local_type_name(ordinal) -> str

    @param ordinal: int
    """
    return _ida_typeinf.idc_get_local_type_name(*args)

def get_named_type(*args):
    r"""
    get_named_type(til, name, ntf_flags) -> (int, bytes, bytes, NoneType, NoneType, int, int)
    Get a type data by its name.

    @param til: the type library
    @param name: the type name
    @param ntf_flags: a combination of NTF_* constants
    @return:     None on failure
        tuple(code, type_str, fields_str, cmt, field_cmts, sclass, value) on success
    """
    return _ida_typeinf.get_named_type(*args)

def get_named_type64(*args):
    r"""
    get_named_type64(til, name, ntf_flags) -> (int, bytes, NoneType, NoneType, NoneType, int, int)
    See get_named_type() above.
    @note: If the value in the 'ti' library is 32-bit, it will be sign-extended
           before being stored in the 'value' pointer.

    @param til: til_t const *
    @param name: (C++: const char *) char const *
    @param ntf_flags: (C++: int)
    """
    return _ida_typeinf.get_named_type64(*args)

def print_decls(*args):
    r"""
    print_decls(printer, til, py_ordinals, flags) -> int
    Print types (and possibly their dependencies) in a format suitable for use in a
    header file. This is the reverse parse_decls().

    @param printer: (C++: text_sink_t &) a handler for printing text
    @param til: (C++: til_t *) the type library holding the ordinals
    @param py_ordinals: ordinals of types to export. nullptr means: all ordinals in til
    @param flags: (C++: uint32) flags for the algorithm. A combination of PDF_* constants
    @retval >0: the number of types exported
    @retval 0: an error occurred
    @retval <0: the negated number of types exported. There were minor errors and
                the resulting output might not be compilable.
    """
    return _ida_typeinf.print_decls(*args)

def remove_tinfo_pointer(*args):
    r"""
    remove_tinfo_pointer(tif, name, til) -> (bool, NoneType), (bool, str)
    Remove pointer of a type. (i.e. convert "char *" into "char"). Optionally remove
    the "lp" (or similar) prefix of the input name. If the input type is not a
    pointer, then fail.

    @param tif: (C++: tinfo_t *)
    @param name: char const *
    @param til: (C++: const til_t *) til_t const *
    """
    return _ida_typeinf.remove_tinfo_pointer(*args)

def get_numbered_type(*args):
    r"""
    get_numbered_type(til, ordinal) -> (bytes, NoneType, NoneType, NoneType, int), (bytes, bytes, NoneType, NoneType, int)
    Retrieve a type by its ordinal number.

    @param til: til_t const *
    @param ordinal: (C++: uint32)
    """
    return _ida_typeinf.get_numbered_type(*args)

#<pycode(py_typeinf)>

import ida_idaapi
ida_idaapi._listify_types(
    reginfovec_t)

#
# When turning off BC695, 'idati' would still remain available
#
_real_cvar = cvar
_notify_idati = ida_idaapi._make_one_time_warning_message("idati", "get_idati()")

class _wrap_cvar(object):
    def __getattr__(self, attr):
        if attr == "idati":
            _notify_idati()
            return get_idati()
        return getattr(_real_cvar, attr)

    def __setattr__(self, attr, value):
        if attr != "idati":
            setattr(_real_cvar, attr, value)

cvar = _wrap_cvar()

#</pycode(py_typeinf)>




