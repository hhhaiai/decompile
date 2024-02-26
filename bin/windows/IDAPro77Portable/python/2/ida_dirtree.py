"""
Types involved in grouping of item into folders.

The dirtree_t class is used to organize a directory tree on top of any
collection that allows for accessing its elements by an id (inode).

No requirements are imposed on the inodes apart from the forbidden value -1 (it
is used ot denote a bad inode).

The dirspec_t class is used to specialize the dirtree. It can be used to
introduce a directory structure for:
* local types
* structs
* enums
* functions
* names
* etc

@note: you should be manipulating dirtree_t (and, if implementing a new tree
       backend, dirspec_t) instances, not calling top-level functions in this
       file directly."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_dirtree
else:
    import _ida_dirtree

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

SWIG_PYTHON_LEGACY_BOOL = _ida_dirtree.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class direntry_vec_t(object):
    r"""
    Proxy of C++ qvector< direntry_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> direntry_vec_t
        __init__(self, x) -> direntry_vec_t

        @param x: qvector< direntry_t > const &
        """
        _ida_dirtree.direntry_vec_t_swiginit(self, _ida_dirtree.new_direntry_vec_t(*args))
    __swig_destroy__ = _ida_dirtree.delete_direntry_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: direntry_t const &

        push_back(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dirtree.direntry_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dirtree.direntry_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> direntry_t

        @param _idx: size_t
        """
        return _ida_dirtree.direntry_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dirtree.direntry_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dirtree.direntry_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: direntry_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dirtree.direntry_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=direntry_t())

        @param x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dirtree.direntry_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dirtree.direntry_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< direntry_t > &
        """
        return _ida_dirtree.direntry_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: direntry_t *
        @param len: size_t
        """
        return _ida_dirtree.direntry_vec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< direntry_t > const &
        """
        return _ida_dirtree.direntry_vec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< direntry_t > const &
        """
        return _ida_dirtree.direntry_vec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> direntry_t
        """
        return _ida_dirtree.direntry_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> direntry_t

        @param it: qvector< direntry_t >::iterator
        @param x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> direntry_t

        @param it: qvector< direntry_t >::iterator

        erase(self, first, last) -> direntry_t

        @param first: qvector< direntry_t >::iterator
        @param last: qvector< direntry_t >::iterator
        """
        return _ida_dirtree.direntry_vec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> direntry_t

        @param x: direntry_t const &

        """
        return _ida_dirtree.direntry_vec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: direntry_t const &

        """
        return _ida_dirtree.direntry_vec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dirtree.direntry_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> direntry_t

        @param i: size_t
        """
        return _ida_dirtree.direntry_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: direntry_t const &
        """
        return _ida_dirtree.direntry_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register direntry_vec_t in _ida_dirtree:
_ida_dirtree.direntry_vec_t_swigregister(direntry_vec_t)

class dirtree_cursor_vec_t(object):
    r"""
    Proxy of C++ qvector< dirtree_cursor_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_cursor_vec_t
        __init__(self, x) -> dirtree_cursor_vec_t

        @param x: qvector< dirtree_cursor_t > const &
        """
        _ida_dirtree.dirtree_cursor_vec_t_swiginit(self, _ida_dirtree.new_dirtree_cursor_vec_t(*args))
    __swig_destroy__ = _ida_dirtree.delete_dirtree_cursor_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: dirtree_cursor_t const &

        push_back(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> dirtree_cursor_t

        @param _idx: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: dirtree_cursor_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=dirtree_cursor_t())

        @param x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_dirtree.dirtree_cursor_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< dirtree_cursor_t > &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: dirtree_cursor_t *
        @param len: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< dirtree_cursor_t > const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< dirtree_cursor_t > const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> dirtree_cursor_t

        @param it: qvector< dirtree_cursor_t >::iterator
        @param x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> dirtree_cursor_t

        @param it: qvector< dirtree_cursor_t >::iterator

        erase(self, first, last) -> dirtree_cursor_t

        @param first: qvector< dirtree_cursor_t >::iterator
        @param last: qvector< dirtree_cursor_t >::iterator
        """
        return _ida_dirtree.dirtree_cursor_vec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> dirtree_cursor_t

        @param x: dirtree_cursor_t const &

        """
        return _ida_dirtree.dirtree_cursor_vec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: dirtree_cursor_t const &

        """
        return _ida_dirtree.dirtree_cursor_vec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> dirtree_cursor_t

        @param i: size_t
        """
        return _ida_dirtree.dirtree_cursor_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register dirtree_cursor_vec_t in _ida_dirtree:
_ida_dirtree.dirtree_cursor_vec_t_swigregister(dirtree_cursor_vec_t)

class direntry_t(object):
    r"""
    Proxy of C++ direntry_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    idx = property(_ida_dirtree.direntry_t_idx_get, _ida_dirtree.direntry_t_idx_set, doc=r"""idx""")
    r"""
    diridx_t or inode_t
    """
    isdir = property(_ida_dirtree.direntry_t_isdir_get, _ida_dirtree.direntry_t_isdir_set, doc=r"""isdir""")
    r"""
    is 'idx' a diridx_t, or an inode_t
    """
    BADIDX = _ida_dirtree.direntry_t_BADIDX
    
    ROOTIDX = _ida_dirtree.direntry_t_ROOTIDX
    

    def __init__(self, *args):
        r"""
        __init__(self, i=BADIDX, d=False) -> direntry_t

        @param i: uval_t
        @param d: bool
        """
        _ida_dirtree.direntry_t_swiginit(self, _ida_dirtree.new_direntry_t(*args))

    def valid(self, *args):
        r"""
        valid(self) -> bool
        """
        return _ida_dirtree.direntry_t_valid(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: direntry_t const &
        """
        return _ida_dirtree.direntry_t___lt__(self, *args)
    __swig_destroy__ = _ida_dirtree.delete_direntry_t

# Register direntry_t in _ida_dirtree:
_ida_dirtree.direntry_t_swigregister(direntry_t)

DTN_FULL_NAME = _ida_dirtree.DTN_FULL_NAME
r"""
use long form of the entry name. That name is unique.
"""

DTN_DISPLAY_NAME = _ida_dirtree.DTN_DISPLAY_NAME
r"""
use short, displayable form of the entry name. for example, 'std::string'
instead of 'std::basic_string<char, ...>'. Note that more than one "full name"
can have the same displayable name.
"""

class dirspec_t(object):
    r"""
    Proxy of C++ dirspec_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    flags = property(_ida_dirtree.dirspec_t_flags_get, _ida_dirtree.dirspec_t_flags_set, doc=r"""flags""")
    DSF_INODE_EA = _ida_dirtree.dirspec_t_DSF_INODE_EA
    
    DSF_PRIVRANGE = _ida_dirtree.dirspec_t_DSF_PRIVRANGE
    
    id = property(_ida_dirtree.dirspec_t_id_get, _ida_dirtree.dirspec_t_id_set, doc=r"""id""")

    def __init__(self, *args):
        r"""
        __init__(self, nm=None, f=0) -> dirspec_t

        @param nm: char const *
        @param f: uint32
        """
        if self.__class__ == dirspec_t:
            _self = None
        else:
            _self = self
        _ida_dirtree.dirspec_t_swiginit(self, _ida_dirtree.new_dirspec_t(_self, *args))
    __swig_destroy__ = _ida_dirtree.delete_dirspec_t

    def get_name(self, *args):
        r"""
        get_name(self, inode, name_flags=DTN_FULL_NAME) -> bool
        get the entry name. for example, the structure name

        @param out: (C++: qstring *) may be nullptr; in this case get_name can be used to validate an
                    inode.
        @param name_flags: (C++: uint32) how exactly the name should be retrieved. combination of bits
                           for get_...name() methods bits
        @return: false if the entry does not exist.
        """
        return _ida_dirtree.dirspec_t_get_name(self, *args)

    def get_inode(self, *args):
        r"""
        get_inode(self, dirpath, name) -> inode_t
        get the entry inode in the specified directory

        @param dirpath: (C++: const char *) the absolute directory path with trailing slash
        @param name: (C++: const char *) the entry name in the directory
        @return: the entry inode
        """
        return _ida_dirtree.dirspec_t_get_inode(self, *args)

    def get_attrs(self, *args):
        r"""
        get_attrs(self, inode) -> qstring

        @param inode: inode_t
        """
        return _ida_dirtree.dirspec_t_get_attrs(self, *args)

    def rename_inode(self, *args):
        r"""
        rename_inode(self, inode, newname) -> bool
        rename the entry

        @param inode: (C++: inode_t)
        @param newname: (C++: const char *)
        @return: success
        """
        return _ida_dirtree.dirspec_t_rename_inode(self, *args)

    def unlink_inode(self, *args):
        r"""
        unlink_inode(self, inode)

        @param inode: (C++: inode_t)
        """
        return _ida_dirtree.dirspec_t_unlink_inode(self, *args)

    nodename = id

    def __disown__(self):
        self.this.disown()
        _ida_dirtree.disown_dirspec_t(self)
        return weakref.proxy(self)

# Register dirspec_t in _ida_dirtree:
_ida_dirtree.dirspec_t_swigregister(dirspec_t)

class dirtree_cursor_t(object):
    r"""
    Proxy of C++ dirtree_cursor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    parent = property(_ida_dirtree.dirtree_cursor_t_parent_get, _ida_dirtree.dirtree_cursor_t_parent_set, doc=r"""parent""")
    r"""
    the parent directory
    """
    rank = property(_ida_dirtree.dirtree_cursor_t_rank_get, _ida_dirtree.dirtree_cursor_t_rank_set, doc=r"""rank""")
    r"""
    the index into the parent directory
    """

    def __init__(self, *args):
        r"""
        __init__(self, _parent=BADIDX, _rank=size_t(-1)) -> dirtree_cursor_t

        @param _parent: diridx_t
        @param _rank: size_t
        """
        _ida_dirtree.dirtree_cursor_t_swiginit(self, _ida_dirtree.new_dirtree_cursor_t(*args))

    def valid(self, *args):
        r"""
        valid(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_t_valid(self, *args)

    def is_root_cursor(self, *args):
        r"""
        is_root_cursor(self) -> bool
        """
        return _ida_dirtree.dirtree_cursor_t_is_root_cursor(self, *args)

    def set_root_cursor(self, *args):
        r"""
        set_root_cursor(self)
        """
        return _ida_dirtree.dirtree_cursor_t_set_root_cursor(self, *args)

    @staticmethod
    def root_cursor(*args):
        r"""
        root_cursor() -> dirtree_cursor_t
        """
        return _ida_dirtree.dirtree_cursor_t_root_cursor(*args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: dirtree_cursor_t const &
        """
        return _ida_dirtree.dirtree_cursor_t_compare(self, *args)
    __swig_destroy__ = _ida_dirtree.delete_dirtree_cursor_t

# Register dirtree_cursor_t in _ida_dirtree:
_ida_dirtree.dirtree_cursor_t_swigregister(dirtree_cursor_t)

def dirtree_cursor_t_root_cursor(*args):
    r"""
    dirtree_cursor_t_root_cursor() -> dirtree_cursor_t
    """
    return _ida_dirtree.dirtree_cursor_t_root_cursor(*args)

class dirtree_selection_t(dirtree_cursor_vec_t):
    r"""
    Proxy of C++ dirtree_selection_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_selection_t
        """
        _ida_dirtree.dirtree_selection_t_swiginit(self, _ida_dirtree.new_dirtree_selection_t(*args))
    __swig_destroy__ = _ida_dirtree.delete_dirtree_selection_t

# Register dirtree_selection_t in _ida_dirtree:
_ida_dirtree.dirtree_selection_t_swigregister(dirtree_selection_t)

class dirtree_iterator_t(object):
    r"""
    Proxy of C++ dirtree_iterator_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    pattern = property(_ida_dirtree.dirtree_iterator_t_pattern_get, _ida_dirtree.dirtree_iterator_t_pattern_set, doc=r"""pattern""")
    cursor = property(_ida_dirtree.dirtree_iterator_t_cursor_get, _ida_dirtree.dirtree_iterator_t_cursor_set, doc=r"""cursor""")

    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_iterator_t
        """
        _ida_dirtree.dirtree_iterator_t_swiginit(self, _ida_dirtree.new_dirtree_iterator_t(*args))
    __swig_destroy__ = _ida_dirtree.delete_dirtree_iterator_t

# Register dirtree_iterator_t in _ida_dirtree:
_ida_dirtree.dirtree_iterator_t_swigregister(dirtree_iterator_t)

DTE_OK = _ida_dirtree.DTE_OK

DTE_ALREADY_EXISTS = _ida_dirtree.DTE_ALREADY_EXISTS

DTE_NOT_FOUND = _ida_dirtree.DTE_NOT_FOUND

DTE_NOT_DIRECTORY = _ida_dirtree.DTE_NOT_DIRECTORY

DTE_NOT_EMPTY = _ida_dirtree.DTE_NOT_EMPTY

DTE_BAD_PATH = _ida_dirtree.DTE_BAD_PATH

DTE_CANT_RENAME = _ida_dirtree.DTE_CANT_RENAME

DTE_OWN_CHILD = _ida_dirtree.DTE_OWN_CHILD

DTE_MAX_DIR = _ida_dirtree.DTE_MAX_DIR

DTE_LAST = _ida_dirtree.DTE_LAST

class dirtree_visitor_t(object):
    r"""
    Proxy of C++ dirtree_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def visit(self, *args):
        r"""
        visit(self, c, de) -> ssize_t
        Will be called for each entry in the dirtree_t If something other than 0 is
        returned, iteration will stop.

        @param c: (C++: const dirtree_cursor_t &) the current cursor
        @param de: (C++: const direntry_t &) the current entry
        @return: 0 to keep iterating, or anything else to stop
        """
        return _ida_dirtree.dirtree_visitor_t_visit(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> dirtree_visitor_t

        @param self: PyObject *
        """
        if self.__class__ == dirtree_visitor_t:
            _self = None
        else:
            _self = self
        _ida_dirtree.dirtree_visitor_t_swiginit(self, _ida_dirtree.new_dirtree_visitor_t(_self, *args))
    __swig_destroy__ = _ida_dirtree.delete_dirtree_visitor_t
    def __disown__(self):
        self.this.disown()
        _ida_dirtree.disown_dirtree_visitor_t(self)
        return weakref.proxy(self)

# Register dirtree_visitor_t in _ida_dirtree:
_ida_dirtree.dirtree_visitor_t_swigregister(dirtree_visitor_t)

class dirtree_t(object):
    r"""
    Proxy of C++ dirtree_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, ds) -> dirtree_t

        @param ds: dirspec_t *
        """
        _ida_dirtree.dirtree_t_swiginit(self, _ida_dirtree.new_dirtree_t(*args))
    __swig_destroy__ = _ida_dirtree.delete_dirtree_t

    @staticmethod
    def errstr(*args):
        r"""
        errstr(err) -> char const *
        Get textual representation of the error code.

        @param err: (C++: dterr_t) enum dterr_t
        """
        return _ida_dirtree.dirtree_t_errstr(*args)

    def chdir(self, *args):
        r"""
        chdir(self, path) -> dterr_t
        Change current directory

        @param path: (C++: const char *) new current directory
        @return: dterr_t error code
        """
        return _ida_dirtree.dirtree_t_chdir(self, *args)

    def getcwd(self, *args):
        r"""
        getcwd(self) -> qstring
        Get current directory

        @return: the current working directory
        """
        return _ida_dirtree.dirtree_t_getcwd(self, *args)

    def get_abspath(self, *args):
        r"""
        get_abspath(self, cursor) -> qstring
        Construct an absolute path from the specified relative path. This function
        verifies the directory part of the specified path. The last component of the
        specified path is not verified.

        @param cursor: dirtree_cursor_t const &

        @return: path. empty path means wrong directory part of RELPATH
        get_abspath(self, relpath) -> qstring

        @param relpath: char const *
        """
        return _ida_dirtree.dirtree_t_get_abspath(self, *args)

    def resolve_cursor(self, *args):
        r"""
        resolve_cursor(self, cursor) -> direntry_t
        Resolve cursor

        @param cursor: (C++: const dirtree_cursor_t &) to analyze
        @return: directory entry; if the cursor is bad, the resolved entry will be
                 invalid.
        @note: see also get_abspath()
        """
        return _ida_dirtree.dirtree_t_resolve_cursor(self, *args)

    def resolve_path(self, *args):
        r"""
        resolve_path(self, path) -> direntry_t
        Resolve path

        @param path: (C++: const char *) to analyze
        @return: directory entry
        """
        return _ida_dirtree.dirtree_t_resolve_path(self, *args)

    def isdir(self, *args):
        r"""
        isdir(self, de) -> bool

        @param de: direntry_t const &

        isdir(self, path) -> bool

        @param path: char const *
        """
        return _ida_dirtree.dirtree_t_isdir(self, *args)

    def isfile(self, *args):
        r"""
        isfile(self, de) -> bool

        @param de: direntry_t const &

        isfile(self, path) -> bool

        @param path: char const *
        """
        return _ida_dirtree.dirtree_t_isfile(self, *args)

    def get_entry_name(self, *args):
        r"""
        get_entry_name(self, de, name_flags=DTN_FULL_NAME) -> qstring
        Get entry name

        @param de: (C++: const direntry_t &) directory entry
        @param name_flags: (C++: uint32) how exactly the name should be retrieved. combination of bits
                           for get_...name() methods bits
        @return: name
        """
        return _ida_dirtree.dirtree_t_get_entry_name(self, *args)

    def get_dir_size(self, *args):
        r"""
        get_dir_size(self, diridx) -> ssize_t
        Get dir size

        @param diridx: (C++: diridx_t) directory index
        @return: number of entries under this directory; if error, return -1
        """
        return _ida_dirtree.dirtree_t_get_dir_size(self, *args)

    def get_entry_attrs(self, *args):
        r"""
        get_entry_attrs(self, de) -> qstring
        Get entry attributes

        @param de: (C++: const direntry_t &) directory entry
        @return: name
        """
        return _ida_dirtree.dirtree_t_get_entry_attrs(self, *args)

    def findfirst(self, *args):
        r"""
        findfirst(self, ff, pattern) -> bool
        Start iterating over files in a directory

        @param ff: (C++: dirtree_iterator_t *) directory iterator. it will be initialized by the function
        @param pattern: (C++: const char *) pattern to search for
        @return: success
        """
        return _ida_dirtree.dirtree_t_findfirst(self, *args)

    def findnext(self, *args):
        r"""
        findnext(self, ff) -> bool
        Continue iterating over files in a directory

        @param ff: (C++: dirtree_iterator_t *) directory iterator
        @return: success
        """
        return _ida_dirtree.dirtree_t_findnext(self, *args)

    def mkdir(self, *args):
        r"""
        mkdir(self, path) -> dterr_t
        Create a directory.

        @param path: (C++: const char *) directory to create
        @return: dterr_t error code
        """
        return _ida_dirtree.dirtree_t_mkdir(self, *args)

    def rmdir(self, *args):
        r"""
        rmdir(self, path) -> dterr_t
        Remove a directory.

        @param path: (C++: const char *) directory to delete
        @return: dterr_t error code
        """
        return _ida_dirtree.dirtree_t_rmdir(self, *args)

    def link(self, *args):
        r"""
        link(self, path) -> dterr_t
        Add an inode into the current directory

        @param path: char const *

        @return: dterr_t error code
        link(self, inode) -> dterr_t

        @param inode: inode_t
        """
        return _ida_dirtree.dirtree_t_link(self, *args)

    def unlink(self, *args):
        r"""
        unlink(self, path) -> dterr_t
        Remove an inode from the current directory

        @param path: char const *

        @return: dterr_t error code
        unlink(self, inode) -> dterr_t

        @param inode: inode_t
        """
        return _ida_dirtree.dirtree_t_unlink(self, *args)

    def rename(self, *args):
        r"""
        rename(self, _from, to) -> dterr_t
        Rename a directory entry.

        @param from: (C++: const char *) source path
        @param to: (C++: const char *) destination path
        @return: dterr_t error code
        @note: This function can also rename the item
        """
        return _ida_dirtree.dirtree_t_rename(self, *args)

    def get_rank(self, *args):
        r"""
        get_rank(self, diridx, de) -> ssize_t
        Get ordering rank of an item.

        @param diridx: (C++: diridx_t) index of the parent directory
        @param de: (C++: const direntry_t &) directory entry
        @return: number in a range of [0..n) where n is the number of entries in the
                 parent directory. -1 if error
        """
        return _ida_dirtree.dirtree_t_get_rank(self, *args)

    def change_rank(self, *args):
        r"""
        change_rank(self, path, rank_delta) -> dterr_t
        Change ordering rank of an item.

        @param path: (C++: const char *) path to the item
        @param delta: the amount of the change. positive numbers mean to move down in
                      the list; negative numbers mean to move up.
        @return: dterr_t error code
        @note: All subdirectories go before all file entries.
        """
        return _ida_dirtree.dirtree_t_change_rank(self, *args)

    def get_parent_cursor(self, *args):
        r"""
        get_parent_cursor(self, cursor) -> dirtree_cursor_t
        Get parent cursor.

        @param cursor: (C++: const dirtree_cursor_t &) a valid ditree cursor
        @return: cursor's parent
        """
        return _ida_dirtree.dirtree_t_get_parent_cursor(self, *args)

    def load(self, *args):
        r"""
        load(self) -> bool
        Load the tree structure from the netnode. If dirspec_t::id is empty, the
        operation will be considered a success. In addition, calling load() more than
        once will not do anything, and will be considered a success.

        @return: success
        @see: dirspec_t::id.
        """
        return _ida_dirtree.dirtree_t_load(self, *args)

    def save(self, *args):
        r"""
        save(self) -> bool
        Save the tree structure to the netnode.

        @return: success
        @see: dirspec_t::id.
        """
        return _ida_dirtree.dirtree_t_save(self, *args)

    def get_id(self, *args):
        r"""
        get_id(self) -> char const *
        netnode name
        """
        return _ida_dirtree.dirtree_t_get_id(self, *args)

    def set_id(self, *args):
        r"""
        set_id(self, nm)

        @param nm: char const *
        """
        return _ida_dirtree.dirtree_t_set_id(self, *args)

    def notify_dirtree(self, *args):
        r"""
        notify_dirtree(self, added, inode)
        Notify dirtree about a change of an inode.

        @param add: are we adding or deleting an inode?
        @param inode: (C++: inode_t) inode in question
        """
        return _ida_dirtree.dirtree_t_notify_dirtree(self, *args)

    def traverse(self, *args):
        r"""
        traverse(self, v) -> ssize_t
        Traverse dirtree, and be notified at each entry If the the visitor returns
        anything other than 0, iteration will stop, and that value returned. The tree is
        traversed using a depth-first algorithm. It is forbidden to modify the dirtree_t
        during traversal; doing so will result in undefined behavior.

        @param v: (C++: dirtree_visitor_t &) the callback
        @return: 0, or whatever the visitor returned
        """
        return _ida_dirtree.dirtree_t_traverse(self, *args)

    def find_entry(self, *args):
        r"""
        find_entry(self, de) -> dirtree_cursor_t
        Find the cursor corresponding to an entry of a directory

        @param directory: entry
        @return: cursor corresponding to the directory entry
        """
        return _ida_dirtree.dirtree_t_find_entry(self, *args)

    get_nodename = get_id
    set_nodename = set_id


# Register dirtree_t in _ida_dirtree:
_ida_dirtree.dirtree_t_swigregister(dirtree_t)

def dirtree_t_errstr(*args):
    r"""
    dirtree_t_errstr(err) -> char const *

    @param err: enum dterr_t
    """
    return _ida_dirtree.dirtree_t_errstr(*args)

DIRTREE_LOCAL_TYPES = _ida_dirtree.DIRTREE_LOCAL_TYPES

DIRTREE_STRUCTS = _ida_dirtree.DIRTREE_STRUCTS

DIRTREE_ENUMS = _ida_dirtree.DIRTREE_ENUMS

DIRTREE_FUNCS = _ida_dirtree.DIRTREE_FUNCS

DIRTREE_NAMES = _ida_dirtree.DIRTREE_NAMES

DIRTREE_IMPORTS = _ida_dirtree.DIRTREE_IMPORTS

DIRTREE_IDAPLACE_BOOKMARKS = _ida_dirtree.DIRTREE_IDAPLACE_BOOKMARKS

DIRTREE_STRUCTS_BOOKMARKS = _ida_dirtree.DIRTREE_STRUCTS_BOOKMARKS

DIRTREE_ENUMS_BOOKMARKS = _ida_dirtree.DIRTREE_ENUMS_BOOKMARKS

DIRTREE_BPTS = _ida_dirtree.DIRTREE_BPTS

DIRTREE_END = _ida_dirtree.DIRTREE_END


def get_std_dirtree(*args):
    r"""
    get_std_dirtree(id) -> dirtree_t

    @param id: enum dirtree_id_t
    """
    return _ida_dirtree.get_std_dirtree(*args)



