"""
"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_moves
else:
    import _ida_moves

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

SWIG_PYTHON_LEGACY_BOOL = _ida_moves.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class segm_move_info_vec_t(object):
    r"""
    Proxy of C++ qvector< segm_move_info_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> segm_move_info_vec_t
        __init__(self, x) -> segm_move_info_vec_t

        @param x: qvector< segm_move_info_t > const &
        """
        _ida_moves.segm_move_info_vec_t_swiginit(self, _ida_moves.new_segm_move_info_vec_t(*args))
    __swig_destroy__ = _ida_moves.delete_segm_move_info_vec_t

    def push_back(self, *args) -> "segm_move_info_t &":
        r"""
        push_back(self, x)

        @param x: segm_move_info_t const &

        push_back(self) -> segm_move_info_t
        """
        return _ida_moves.segm_move_info_vec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_moves.segm_move_info_vec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_moves.segm_move_info_vec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_moves.segm_move_info_vec_t_empty(self, *args)

    def at(self, *args) -> "segm_move_info_t const &":
        r"""
        at(self, _idx) -> segm_move_info_t

        @param _idx: size_t
        """
        return _ida_moves.segm_move_info_vec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_moves.segm_move_info_vec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_moves.segm_move_info_vec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: segm_move_info_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_moves.segm_move_info_vec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=segm_move_info_t())

        @param x: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_vec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_moves.segm_move_info_vec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_moves.segm_move_info_vec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_moves.segm_move_info_vec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< segm_move_info_t > &
        """
        return _ida_moves.segm_move_info_vec_t_swap(self, *args)

    def extract(self, *args) -> "segm_move_info_t *":
        r"""
        extract(self) -> segm_move_info_t
        """
        return _ida_moves.segm_move_info_vec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: segm_move_info_t *
        @param len: size_t
        """
        return _ida_moves.segm_move_info_vec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< segm_move_info_t > const &
        """
        return _ida_moves.segm_move_info_vec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< segm_move_info_t > const &
        """
        return _ida_moves.segm_move_info_vec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< segm_move_info_t >::const_iterator":
        r"""
        begin(self) -> segm_move_info_t
        """
        return _ida_moves.segm_move_info_vec_t_begin(self, *args)

    def end(self, *args) -> "qvector< segm_move_info_t >::const_iterator":
        r"""
        end(self) -> segm_move_info_t
        """
        return _ida_moves.segm_move_info_vec_t_end(self, *args)

    def insert(self, *args) -> "qvector< segm_move_info_t >::iterator":
        r"""
        insert(self, it, x) -> segm_move_info_t

        @param it: qvector< segm_move_info_t >::iterator
        @param x: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_vec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< segm_move_info_t >::iterator":
        r"""
        erase(self, it) -> segm_move_info_t

        @param it: qvector< segm_move_info_t >::iterator

        erase(self, first, last) -> segm_move_info_t

        @param first: qvector< segm_move_info_t >::iterator
        @param last: qvector< segm_move_info_t >::iterator
        """
        return _ida_moves.segm_move_info_vec_t_erase(self, *args)

    def find(self, *args) -> "qvector< segm_move_info_t >::const_iterator":
        r"""
        find(self, x) -> segm_move_info_t

        @param x: segm_move_info_t const &

        """
        return _ida_moves.segm_move_info_vec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_vec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_vec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: segm_move_info_t const &

        """
        return _ida_moves.segm_move_info_vec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_moves.segm_move_info_vec_t___len__(self, *args)

    def __getitem__(self, *args) -> "segm_move_info_t const &":
        r"""
        __getitem__(self, i) -> segm_move_info_t

        @param i: size_t
        """
        return _ida_moves.segm_move_info_vec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register segm_move_info_vec_t in _ida_moves:
_ida_moves.segm_move_info_vec_t_swigregister(segm_move_info_vec_t)

class graph_location_info_t(object):
    r"""
    Proxy of C++ graph_location_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    zoom = property(_ida_moves.graph_location_info_t_zoom_get, _ida_moves.graph_location_info_t_zoom_set, doc=r"""zoom""")
    orgx = property(_ida_moves.graph_location_info_t_orgx_get, _ida_moves.graph_location_info_t_orgx_set, doc=r"""orgx""")
    orgy = property(_ida_moves.graph_location_info_t_orgy_get, _ida_moves.graph_location_info_t_orgy_set, doc=r"""orgy""")

    def __init__(self, *args):
        r"""
        __init__(self) -> graph_location_info_t
        """
        _ida_moves.graph_location_info_t_swiginit(self, _ida_moves.new_graph_location_info_t(*args))

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: graph_location_info_t const &
        """
        return _ida_moves.graph_location_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: graph_location_info_t const &
        """
        return _ida_moves.graph_location_info_t___ne__(self, *args)
    __swig_destroy__ = _ida_moves.delete_graph_location_info_t

# Register graph_location_info_t in _ida_moves:
_ida_moves.graph_location_info_t_swigregister(graph_location_info_t)

class segm_move_info_t(object):
    r"""
    Proxy of C++ segm_move_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _from=0, _to=0, _sz=0) -> segm_move_info_t

        @param _from: ea_t
        @param _to: ea_t
        @param _sz: size_t
        """
        _ida_moves.segm_move_info_t_swiginit(self, _ida_moves.new_segm_move_info_t(*args))
    _from = property(_ida_moves.segm_move_info_t__from_get, _ida_moves.segm_move_info_t__from_set, doc=r"""_from""")
    to = property(_ida_moves.segm_move_info_t_to_get, _ida_moves.segm_move_info_t_to_set, doc=r"""to""")
    size = property(_ida_moves.segm_move_info_t_size_get, _ida_moves.segm_move_info_t_size_set, doc=r"""size""")

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: segm_move_info_t const &
        """
        return _ida_moves.segm_move_info_t___ne__(self, *args)
    __swig_destroy__ = _ida_moves.delete_segm_move_info_t

# Register segm_move_info_t in _ida_moves:
_ida_moves.segm_move_info_t_swigregister(segm_move_info_t)

class segm_move_infos_t(segm_move_info_vec_t):
    r"""
    Proxy of C++ segm_move_infos_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def find(self, *args) -> "segm_move_info_t const *":
        r"""
        find(self, ea) -> segm_move_info_t

        @param ea: ea_t
        """
        return _ida_moves.segm_move_infos_t_find(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> segm_move_infos_t
        """
        _ida_moves.segm_move_infos_t_swiginit(self, _ida_moves.new_segm_move_infos_t(*args))
    __swig_destroy__ = _ida_moves.delete_segm_move_infos_t

# Register segm_move_infos_t in _ida_moves:
_ida_moves.segm_move_infos_t_swigregister(segm_move_infos_t)

class renderer_info_pos_t(object):
    r"""
    Proxy of C++ renderer_info_pos_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    node = property(_ida_moves.renderer_info_pos_t_node_get, _ida_moves.renderer_info_pos_t_node_set, doc=r"""node""")
    cx = property(_ida_moves.renderer_info_pos_t_cx_get, _ida_moves.renderer_info_pos_t_cx_set, doc=r"""cx""")
    cy = property(_ida_moves.renderer_info_pos_t_cy_get, _ida_moves.renderer_info_pos_t_cy_set, doc=r"""cy""")

    def __init__(self, *args):
        r"""
        __init__(self) -> renderer_info_pos_t
        """
        _ida_moves.renderer_info_pos_t_swiginit(self, _ida_moves.new_renderer_info_pos_t(*args))

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: renderer_info_pos_t const &
        """
        return _ida_moves.renderer_info_pos_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: renderer_info_pos_t const &
        """
        return _ida_moves.renderer_info_pos_t___ne__(self, *args)
    __swig_destroy__ = _ida_moves.delete_renderer_info_pos_t

# Register renderer_info_pos_t in _ida_moves:
_ida_moves.renderer_info_pos_t_swigregister(renderer_info_pos_t)

class renderer_info_t(object):
    r"""
    Proxy of C++ renderer_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    gli = property(_ida_moves.renderer_info_t_gli_get, _ida_moves.renderer_info_t_gli_set, doc=r"""gli""")
    pos = property(_ida_moves.renderer_info_t_pos_get, _ida_moves.renderer_info_t_pos_set, doc=r"""pos""")
    rtype = property(_ida_moves.renderer_info_t_rtype_get, _ida_moves.renderer_info_t_rtype_set, doc=r"""rtype""")

    def __init__(self, *args):
        r"""
        __init__(self) -> renderer_info_t
        __init__(self, _rtype, cx, cy) -> renderer_info_t

        @param _rtype: enum tcc_renderer_type_t
        @param cx: short
        @param cy: short
        """
        _ida_moves.renderer_info_t_swiginit(self, _ida_moves.new_renderer_info_t(*args))

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: renderer_info_t const &
        """
        return _ida_moves.renderer_info_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: renderer_info_t const &
        """
        return _ida_moves.renderer_info_t___ne__(self, *args)
    __swig_destroy__ = _ida_moves.delete_renderer_info_t

# Register renderer_info_t in _ida_moves:
_ida_moves.renderer_info_t_swigregister(renderer_info_t)

LSEF_PLACE = _ida_moves.LSEF_PLACE

LSEF_RINFO = _ida_moves.LSEF_RINFO

LSEF_PTYPE = _ida_moves.LSEF_PTYPE

LSEF_ALL = _ida_moves.LSEF_ALL

class lochist_entry_t(object):
    r"""
    Proxy of C++ lochist_entry_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    rinfo = property(_ida_moves.lochist_entry_t_rinfo_get, _ida_moves.lochist_entry_t_rinfo_set, doc=r"""rinfo""")
    plce = property(_ida_moves.lochist_entry_t_plce_get, _ida_moves.lochist_entry_t_plce_set, doc=r"""plce""")

    def __init__(self, *args):
        r"""
        __init__(self) -> lochist_entry_t
        __init__(self, p, r) -> lochist_entry_t

        @param p: place_t const *
        @param r: renderer_info_t const &

        __init__(self, other) -> lochist_entry_t

        @param other: lochist_entry_t const &
        """
        _ida_moves.lochist_entry_t_swiginit(self, _ida_moves.new_lochist_entry_t(*args))
    __swig_destroy__ = _ida_moves.delete_lochist_entry_t

    def renderer_info(self, *args) -> "renderer_info_t &":
        r"""
        renderer_info(self) -> renderer_info_t
        """
        return _ida_moves.lochist_entry_t_renderer_info(self, *args)

    def place(self, *args) -> "place_t *":
        r"""
        place(self) -> place_t
        """
        return _ida_moves.lochist_entry_t_place(self, *args)

    def set_place(self, *args) -> "void":
        r"""
        set_place(self, p)

        @param p: place_t const *
        """
        return _ida_moves.lochist_entry_t_set_place(self, *args)

    def is_valid(self, *args) -> "bool":
        r"""
        is_valid(self) -> bool
        """
        return _ida_moves.lochist_entry_t_is_valid(self, *args)

    def acquire_place(self, *args) -> "void":
        r"""
        acquire_place(self, in_p)

        @param in_p: place_t *
        """
        return _ida_moves.lochist_entry_t_acquire_place(self, *args)

# Register lochist_entry_t in _ida_moves:
_ida_moves.lochist_entry_t_swigregister(lochist_entry_t)

UNHID_SEGM = _ida_moves.UNHID_SEGM

UNHID_FUNC = _ida_moves.UNHID_FUNC

UNHID_RANGE = _ida_moves.UNHID_RANGE

DEFAULT_CURSOR_Y = _ida_moves.DEFAULT_CURSOR_Y

DEFAULT_LNNUM = _ida_moves.DEFAULT_LNNUM

CURLOC_LIST = _ida_moves.CURLOC_LIST

MAX_MARK_SLOT = _ida_moves.MAX_MARK_SLOT

class lochist_t(object):
    r"""
    Proxy of C++ lochist_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> lochist_t
        """
        _ida_moves.lochist_t_swiginit(self, _ida_moves.new_lochist_t(*args))
    __swig_destroy__ = _ida_moves.delete_lochist_t

    def is_history_enabled(self, *args) -> "bool":
        r"""
        is_history_enabled(self) -> bool
        """
        return _ida_moves.lochist_t_is_history_enabled(self, *args)

    def get_place_id(self, *args) -> "int":
        r"""
        get_place_id(self) -> int
        """
        return _ida_moves.lochist_t_get_place_id(self, *args)

    def init(self, *args) -> "bool":
        r"""
        init(self, stream_name, _defpos, _ud, _flags) -> bool

        @param stream_name: char const *
        @param _defpos: place_t const *
        @param _ud: void *
        @param _flags: uint32
        """
        return _ida_moves.lochist_t_init(self, *args)

    def netcode(self, *args) -> "nodeidx_t":
        r"""
        netcode(self) -> nodeidx_t
        """
        return _ida_moves.lochist_t_netcode(self, *args)

    def jump(self, *args) -> "void":
        r"""
        jump(self, try_to_unhide, e)

        @param try_to_unhide: bool
        @param e: lochist_entry_t const &
        """
        return _ida_moves.lochist_t_jump(self, *args)

    def current_index(self, *args) -> "uint32":
        r"""
        current_index(self) -> uint32
        """
        return _ida_moves.lochist_t_current_index(self, *args)

    def seek(self, *args) -> "bool":
        r"""
        seek(self, index, try_to_unhide) -> bool

        @param index: uint32
        @param try_to_unhide: bool
        """
        return _ida_moves.lochist_t_seek(self, *args)

    def fwd(self, *args) -> "bool":
        r"""
        fwd(self, cnt, try_to_unhide) -> bool

        @param cnt: uint32
        @param try_to_unhide: bool
        """
        return _ida_moves.lochist_t_fwd(self, *args)

    def back(self, *args) -> "bool":
        r"""
        back(self, cnt, try_to_unhide) -> bool

        @param cnt: uint32
        @param try_to_unhide: bool
        """
        return _ida_moves.lochist_t_back(self, *args)

    def save(self, *args) -> "void":
        r"""
        save(self)
        """
        return _ida_moves.lochist_t_save(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_moves.lochist_t_clear(self, *args)

    def get_current(self, *args) -> "lochist_entry_t const &":
        r"""
        get_current(self) -> lochist_entry_t
        """
        return _ida_moves.lochist_t_get_current(self, *args)

    def set_current(self, *args) -> "void":
        r"""
        set_current(self, e)

        @param e: lochist_entry_t const &
        """
        return _ida_moves.lochist_t_set_current(self, *args)

    def set(self, *args) -> "void":
        r"""
        set(self, index, e)

        @param index: uint32
        @param e: lochist_entry_t const &
        """
        return _ida_moves.lochist_t_set(self, *args)

    def get(self, *args) -> "bool":
        r"""
        get(self, out, index) -> bool

        @param out: lochist_entry_t *
        @param index: uint32
        """
        return _ida_moves.lochist_t_get(self, *args)

    def size(self, *args) -> "uint32":
        r"""
        size(self) -> uint32
        """
        return _ida_moves.lochist_t_size(self, *args)

    def get_template_place(self, *args) -> "place_t const *":
        r"""
        get_template_place(self) -> place_t
        """
        return _ida_moves.lochist_t_get_template_place(self, *args)

# Register lochist_t in _ida_moves:
_ida_moves.lochist_t_swigregister(lochist_t)

class bookmarks_t(object):
    r"""
    Proxy of C++ bookmarks_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    @staticmethod
    def mark(*args) -> "uint32":
        r"""
        mark(e, index, title, desc, ud) -> uint32

        @param e: lochist_entry_t const &
        @param index: uint32
        @param title: char const *
        @param desc: char const *
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_mark(*args)

    @staticmethod
    def get(*args) -> "bool":
        r"""
        get(out_entry, out_desc, index, ud) -> bool

        @param out_entry: lochist_entry_t *
        @param out_desc: qstring *
        @param index: uint32 *
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_get(*args)

    @staticmethod
    def get_desc(*args) -> "qstring *":
        r"""
        get_desc(e, index, ud) -> bool

        @param e: lochist_entry_t const &
        @param index: uint32
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_get_desc(*args)

    @staticmethod
    def find_index(*args) -> "uint32":
        r"""
        find_index(e, ud) -> uint32

        @param e: lochist_entry_t const &
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_find_index(*args)

    @staticmethod
    def size(*args) -> "uint32":
        r"""
        size(e, ud) -> uint32

        @param e: lochist_entry_t const &
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_size(*args)

    @staticmethod
    def erase(*args) -> "bool":
        r"""
        erase(e, index, ud) -> bool

        @param e: lochist_entry_t const &
        @param index: uint32
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_erase(*args)

    @staticmethod
    def get_dirtree_id(*args) -> "dirtree_id_t":
        r"""
        get_dirtree_id(e, ud) -> dirtree_id_t

        @param e: lochist_entry_t const &
        @param ud: void *
        """
        return _ida_moves.bookmarks_t_get_dirtree_id(*args)

# Register bookmarks_t in _ida_moves:
_ida_moves.bookmarks_t_swigregister(bookmarks_t)
BOOKMARKS_PROMPT_WITH_HINT_PREFIX = _ida_moves.BOOKMARKS_PROMPT_WITH_HINT_PREFIX


def bookmarks_t_mark(*args) -> "uint32":
    r"""
    bookmarks_t_mark(e, index, title, desc, ud) -> uint32

    @param e: lochist_entry_t const &
    @param index: uint32
    @param title: char const *
    @param desc: char const *
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_mark(*args)

def bookmarks_t_get(*args) -> "bool":
    r"""
    bookmarks_t_get(out_entry, out_desc, index, ud) -> bool

    @param out_entry: lochist_entry_t *
    @param out_desc: qstring *
    @param index: uint32 *
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_get(*args)

def bookmarks_t_get_desc(*args) -> "qstring *":
    r"""
    bookmarks_t_get_desc(e, index, ud) -> str

    @param e: lochist_entry_t const &
    @param index: uint32
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_get_desc(*args)

def bookmarks_t_find_index(*args) -> "uint32":
    r"""
    bookmarks_t_find_index(e, ud) -> uint32

    @param e: lochist_entry_t const &
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_find_index(*args)

def bookmarks_t_size(*args) -> "uint32":
    r"""
    bookmarks_t_size(e, ud) -> uint32

    @param e: lochist_entry_t const &
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_size(*args)

def bookmarks_t_erase(*args) -> "bool":
    r"""
    bookmarks_t_erase(e, index, ud) -> bool

    @param e: lochist_entry_t const &
    @param index: uint32
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_erase(*args)

def bookmarks_t_get_dirtree_id(*args) -> "dirtree_id_t":
    r"""
    bookmarks_t_get_dirtree_id(e, ud) -> dirtree_id_t

    @param e: lochist_entry_t const &
    @param ud: void *
    """
    return _ida_moves.bookmarks_t_get_dirtree_id(*args)




