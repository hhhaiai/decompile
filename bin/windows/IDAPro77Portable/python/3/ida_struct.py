"""
Structure type management (assembly level types)"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_struct
else:
    import _ida_struct

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

SWIG_PYTHON_LEGACY_BOOL = _ida_struct.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class dyn_member_ref_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< member_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data = property(_ida_struct.dyn_member_ref_array_data_get, doc=r"""data""")
    count = property(_ida_struct.dyn_member_ref_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_member_ref_array

        @param _data: member_t *
        @param _count: size_t
        """
        _ida_struct.dyn_member_ref_array_swiginit(self, _ida_struct.new_dyn_member_ref_array(*args))

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_struct.dyn_member_ref_array___len__(self, *args)

    def __getitem__(self, *args) -> "member_t const &":
        r"""
        __getitem__(self, i) -> member_t

        @param i: size_t
        """
        return _ida_struct.dyn_member_ref_array___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: member_t const &
        """
        return _ida_struct.dyn_member_ref_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_struct.delete_dyn_member_ref_array

# Register dyn_member_ref_array in _ida_struct:
_ida_struct.dyn_member_ref_array_swigregister(dyn_member_ref_array)

STRUC_SEPARATOR = _ida_struct.STRUC_SEPARATOR
r"""
structname.fieldname
"""

class member_t(object):
    r"""
    Proxy of C++ member_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    id = property(_ida_struct.member_t_id_get, _ida_struct.member_t_id_set, doc=r"""id""")
    r"""
    name(), cmt, rptcmt
    """
    soff = property(_ida_struct.member_t_soff_get, _ida_struct.member_t_soff_set, doc=r"""soff""")
    r"""
    start offset (for unions - number of the member 0..n)
    """
    eoff = property(_ida_struct.member_t_eoff_get, _ida_struct.member_t_eoff_set, doc=r"""eoff""")
    r"""
    end offset
    """
    flag = property(_ida_struct.member_t_flag_get, _ida_struct.member_t_flag_set, doc=r"""flag""")
    r"""
    type+representation bits
    """
    props = property(_ida_struct.member_t_props_get, _ida_struct.member_t_props_set, doc=r"""props""")
    r"""
    Struct member properties
    """

    def unimem(self, *args) -> "bool":
        r"""
        unimem(self) -> bool
        Is a member of a union?
        """
        return _ida_struct.member_t_unimem(self, *args)

    def has_union(self, *args) -> "bool":
        r"""
        has_union(self) -> bool
        Has members of type "union"?
        """
        return _ida_struct.member_t_has_union(self, *args)

    def by_til(self, *args) -> "bool":
        r"""
        by_til(self) -> bool
        Was the member created due to the type system?
        """
        return _ida_struct.member_t_by_til(self, *args)

    def has_ti(self, *args) -> "bool":
        r"""
        has_ti(self) -> bool
        Has type information?
        """
        return _ida_struct.member_t_has_ti(self, *args)

    def is_baseclass(self, *args) -> "bool":
        r"""
        is_baseclass(self) -> bool
        Is a base class member?
        """
        return _ida_struct.member_t_is_baseclass(self, *args)

    def is_dupname(self, *args) -> "bool":
        r"""
        is_dupname(self) -> bool
        Duplicate name was resolved during import?
        """
        return _ida_struct.member_t_is_dupname(self, *args)

    def is_destructor(self, *args) -> "bool":
        r"""
        is_destructor(self) -> bool
        Is a virtual destructor?
        """
        return _ida_struct.member_t_is_destructor(self, *args)

    def get_soff(self, *args) -> "ea_t":
        r"""
        get_soff(self) -> ea_t
        Get start offset (for unions - returns 0)
        """
        return _ida_struct.member_t_get_soff(self, *args)

    def get_size(self, *args) -> "asize_t":
        r"""
        get_size(self) -> asize_t
        Get member size.
        """
        return _ida_struct.member_t_get_size(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> member_t
        """
        _ida_struct.member_t_swiginit(self, _ida_struct.new_member_t(*args))
    __swig_destroy__ = _ida_struct.delete_member_t

# Register member_t in _ida_struct:
_ida_struct.member_t_swigregister(member_t)
MF_OK = _ida_struct.MF_OK
r"""
is the member ok? (always yes)
"""

MF_UNIMEM = _ida_struct.MF_UNIMEM
r"""
is a member of a union?
"""

MF_HASUNI = _ida_struct.MF_HASUNI
r"""
has members of type "union"?
"""

MF_BYTIL = _ida_struct.MF_BYTIL
r"""
the member was created due to the type system
"""

MF_HASTI = _ida_struct.MF_HASTI
r"""
has type information?
"""

MF_BASECLASS = _ida_struct.MF_BASECLASS
r"""
a special member representing base class
"""

MF_DTOR = _ida_struct.MF_DTOR
r"""
a special member representing destructor
"""

MF_DUPNAME = _ida_struct.MF_DUPNAME
r"""
duplicate name resolved with _N suffix (N==soff)
"""


class struc_t(object):
    r"""
    Proxy of C++ struc_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    id = property(_ida_struct.struc_t_id_get, _ida_struct.struc_t_id_set, doc=r"""id""")
    r"""
    struct id
    """
    memqty = property(_ida_struct.struc_t_memqty_get, _ida_struct.struc_t_memqty_set, doc=r"""memqty""")
    r"""
    number of members
    """
    members = property(_ida_struct.struc_t_members_get, _ida_struct.struc_t_members_set, doc=r"""members""")
    r"""
    only defined members are stored here. there may be gaps between members.
    """
    age = property(_ida_struct.struc_t_age_get, _ida_struct.struc_t_age_set, doc=r"""age""")
    r"""
    not used
    """
    props = property(_ida_struct.struc_t_props_get, _ida_struct.struc_t_props_set, doc=r"""props""")
    r"""
    Structure properties
    """

    def is_varstr(self, *args) -> "bool":
        r"""
        is_varstr(self) -> bool
        Is variable size structure?
        """
        return _ida_struct.struc_t_is_varstr(self, *args)

    def is_union(self, *args) -> "bool":
        r"""
        is_union(self) -> bool
        Is a union?
        """
        return _ida_struct.struc_t_is_union(self, *args)

    def has_union(self, *args) -> "bool":
        r"""
        has_union(self) -> bool
        Has members of type "union"?
        """
        return _ida_struct.struc_t_has_union(self, *args)

    def like_union(self, *args) -> "bool":
        r"""
        like_union(self) -> bool
        Is a union or contains members of type "union"?
        """
        return _ida_struct.struc_t_like_union(self, *args)

    def is_choosable(self, *args) -> "bool":
        r"""
        is_choosable(self) -> bool
        Is included in chooser list? Use set_struc_listed to change the listed status
        """
        return _ida_struct.struc_t_is_choosable(self, *args)

    def from_til(self, *args) -> "bool":
        r"""
        from_til(self) -> bool
        Does structure come from a type library?
        """
        return _ida_struct.struc_t_from_til(self, *args)

    def is_hidden(self, *args) -> "bool":
        r"""
        is_hidden(self) -> bool
        Is the structure collapsed? Use set_struc_hidden to change the hidden status
        """
        return _ida_struct.struc_t_is_hidden(self, *args)

    def is_frame(self, *args) -> "bool":
        r"""
        is_frame(self) -> bool
        Is this structure a function frame?
        """
        return _ida_struct.struc_t_is_frame(self, *args)

    def get_alignment(self, *args) -> "int":
        r"""
        get_alignment(self) -> int
        See SF_ALIGN.
        """
        return _ida_struct.struc_t_get_alignment(self, *args)

    def is_ghost(self, *args) -> "bool":
        r"""
        is_ghost(self) -> bool
        Is a ghost copy of a local type?
        """
        return _ida_struct.struc_t_is_ghost(self, *args)

    def is_synced(self, *args) -> "bool":
        r"""
        is_synced(self) -> bool
        Is synced with a local type?
        """
        return _ida_struct.struc_t_is_synced(self, *args)

    def is_mappedto(self, *args) -> "bool":
        r"""
        is_mappedto(self) -> bool
        Is mapped to a local type?
        """
        return _ida_struct.struc_t_is_mappedto(self, *args)

    def is_copyof(self, *args) -> "bool":
        r"""
        is_copyof(self) -> bool
        Is copied from a local type?
        """
        return _ida_struct.struc_t_is_copyof(self, *args)

    def set_alignment(self, *args) -> "void":
        r"""
        set_alignment(self, shift)
        Do not use; use set_struc_align()

        @param shift: (C++: int)
        """
        return _ida_struct.struc_t_set_alignment(self, *args)

    def get_last_member(self, *args) -> "member_t const *":
        r"""
        get_last_member(self) -> member_t
        """
        return _ida_struct.struc_t_get_last_member(self, *args)

    def set_ghost(self, *args) -> "void":
        r"""
        set_ghost(self, _is_ghost)

        @param _is_ghost: bool
        """
        return _ida_struct.struc_t_set_ghost(self, *args)

    def unsync(self, *args) -> "void":
        r"""
        unsync(self)
        """
        return _ida_struct.struc_t_unsync(self, *args)
    ordinal = property(_ida_struct.struc_t_ordinal_get, _ida_struct.struc_t_ordinal_set, doc=r"""ordinal""")
    r"""
    corresponding local type ordinal number
    """

    def __get_members__(self, *args) -> "dynamic_wrapped_array_t< member_t >":
        r"""
        __get_members__(self) -> dyn_member_ref_array
        """
        return _ida_struct.struc_t___get_members__(self, *args)

    members = property(__get_members__)
    def get_member(self, index):
        return self.members[index]

    __swig_destroy__ = _ida_struct.delete_struc_t

# Register struc_t in _ida_struct:
_ida_struct.struc_t_swigregister(struc_t)
SF_VAR = _ida_struct.SF_VAR
r"""
is variable size structure (varstruct)? a variable size structure is one with
the zero size last member. if the last member is a varstruct, then the current
structure is a varstruct too.
"""

SF_UNION = _ida_struct.SF_UNION
r"""
is a union? varunions are prohibited!
"""

SF_HASUNI = _ida_struct.SF_HASUNI
r"""
has members of type "union"?
"""

SF_NOLIST = _ida_struct.SF_NOLIST
r"""
don't include in the chooser list
"""

SF_TYPLIB = _ida_struct.SF_TYPLIB
r"""
the structure comes from type library
"""

SF_HIDDEN = _ida_struct.SF_HIDDEN
r"""
the structure is collapsed
"""

SF_FRAME = _ida_struct.SF_FRAME
r"""
the structure is a function frame
"""

SF_ALIGN = _ida_struct.SF_ALIGN
r"""
alignment (shift amount: 0..31)
"""

SF_GHOST = _ida_struct.SF_GHOST
r"""
ghost copy of a local type
"""



def get_struc_qty(*args) -> "size_t":
    r"""
    get_struc_qty() -> size_t
    Get number of known structures.
    """
    return _ida_struct.get_struc_qty(*args)

def get_first_struc_idx(*args) -> "uval_t":
    r"""
    get_first_struc_idx() -> uval_t
    Get index of first structure.

    @return: BADADDR if no known structures, 0 otherwise
    """
    return _ida_struct.get_first_struc_idx(*args)

def get_last_struc_idx(*args) -> "uval_t":
    r"""
    get_last_struc_idx() -> uval_t
    Get index of last structure.

    @return: BADADDR if no known structures, get_struc_qty()-1 otherwise
    """
    return _ida_struct.get_last_struc_idx(*args)

def get_prev_struc_idx(*args) -> "uval_t":
    r"""
    get_prev_struc_idx(idx) -> uval_t
    Get previous struct index.

    @param idx: (C++: uval_t)
    @return: BADADDR if resulting index is negative, otherwise idx - 1
    """
    return _ida_struct.get_prev_struc_idx(*args)

def get_next_struc_idx(*args) -> "uval_t":
    r"""
    get_next_struc_idx(idx) -> uval_t
    Get next struct index.

    @param idx: (C++: uval_t)
    @return: BADADDR if resulting index is out of bounds, otherwise idx++
    """
    return _ida_struct.get_next_struc_idx(*args)

def get_struc_idx(*args) -> "uval_t":
    r"""
    get_struc_idx(id) -> uval_t
    Get internal number of the structure.

    @param id: (C++: tid_t)
    """
    return _ida_struct.get_struc_idx(*args)

def get_struc_by_idx(*args) -> "tid_t":
    r"""
    get_struc_by_idx(idx) -> tid_t
    Get struct id by struct number.

    @param idx: (C++: uval_t)
    """
    return _ida_struct.get_struc_by_idx(*args)

def get_struc(*args) -> "struc_t *":
    r"""
    get_struc(id) -> struc_t
    Get pointer to struct type info.

    @param id: (C++: tid_t)
    """
    return _ida_struct.get_struc(*args)

def get_struc_id(*args) -> "tid_t":
    r"""
    get_struc_id(name) -> tid_t
    Get struct id by name.

    @param name: (C++: const char *) char const *
    """
    return _ida_struct.get_struc_id(*args)

def get_struc_name(*args) -> "qstring *":
    r"""
    get_struc_name(id, flags=0) -> str

    @param id: tid_t
    @param flags: int
    """
    return _ida_struct.get_struc_name(*args)
STRNFL_REGEX = _ida_struct.STRNFL_REGEX
r"""
apply regular expressions to beautify the name
"""


def get_struc_cmt(*args) -> "qstring *":
    r"""
    get_struc_cmt(id, repeatable) -> str
    Get struct comment.

    @param id: (C++: tid_t)
    @param repeatable: (C++: bool)
    """
    return _ida_struct.get_struc_cmt(*args)

def get_struc_size(*args) -> "asize_t":
    r"""
    get_struc_size(sptr) -> asize_t
    Get struct size (also see get_struc_size(const struc_t *))

    @param sptr: struc_t const *

    get_struc_size(id) -> asize_t

    @param id: tid_t
    """
    return _ida_struct.get_struc_size(*args)

def get_struc_prev_offset(*args) -> "ea_t":
    r"""
    get_struc_prev_offset(sptr, offset) -> ea_t
    Get offset of member with largest offset less than 'offset'.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param offset: (C++: ea_t)
    @return: BADADDR if no prev offset
    """
    return _ida_struct.get_struc_prev_offset(*args)

def get_struc_next_offset(*args) -> "ea_t":
    r"""
    get_struc_next_offset(sptr, offset) -> ea_t
    Get offset of member with smallest offset larger than 'offset'.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param offset: (C++: ea_t)
    @return: BADADDR if no next offset
    """
    return _ida_struct.get_struc_next_offset(*args)

def get_struc_last_offset(*args) -> "ea_t":
    r"""
    get_struc_last_offset(sptr) -> ea_t
    Get offset of last member.

    @param sptr: (C++: const struc_t *) struc_t const *
    @return: BADADDR if memqty == 0
    """
    return _ida_struct.get_struc_last_offset(*args)

def get_struc_first_offset(*args) -> "ea_t":
    r"""
    get_struc_first_offset(sptr) -> ea_t
    Get offset of first member.

    @param sptr: (C++: const struc_t *) struc_t const *
    @return: BADADDR if memqty == 0
    """
    return _ida_struct.get_struc_first_offset(*args)

def get_max_offset(*args) -> "ea_t":
    r"""
    get_max_offset(sptr) -> ea_t
    For unions: returns number of members, for structs: returns size of structure.

    @param sptr: (C++: struc_t *)
    """
    return _ida_struct.get_max_offset(*args)

def is_varstr(*args) -> "bool":
    r"""
    is_varstr(id) -> bool
    Is variable size structure?

    @param id: (C++: tid_t)
    """
    return _ida_struct.is_varstr(*args)

def is_union(*args) -> "bool":
    r"""
    is_union(id) -> bool
    Is a union?

    @param id: (C++: tid_t)
    """
    return _ida_struct.is_union(*args)

def get_member_struc(*args) -> "struc_t *":
    r"""
    get_member_struc(fullname) -> struc_t
    Get containing structure of member by its full name "struct.field".

    @param fullname: (C++: const char *) char const *
    """
    return _ida_struct.get_member_struc(*args)

def get_sptr(*args) -> "struc_t *":
    r"""
    get_sptr(mptr) -> struc_t
    Get child struct if member is a struct.

    @param mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.get_sptr(*args)

def get_member(*args) -> "member_t *":
    r"""
    get_member(sptr, offset) -> member_t
    Get member at given offset.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param offset: (C++: asize_t)
    """
    return _ida_struct.get_member(*args)

def get_member_id(*args) -> "tid_t":
    r"""
    get_member_id(sptr, offset) -> tid_t
    Get member id at given offset.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param offset: (C++: asize_t)
    """
    return _ida_struct.get_member_id(*args)

def get_member_by_name(*args) -> "member_t *":
    r"""
    get_member_by_name(sptr, membername) -> member_t
    Get a member by its name, like "field44".

    @param sptr: (C++: const struc_t *) struc_t const *
    @param membername: (C++: const char *) char const *
    """
    return _ida_struct.get_member_by_name(*args)

def get_member_by_fullname(*args) -> "struc_t **":
    r"""
    get_member_by_fullname(fullname) -> member_t
    Get a member by its fully qualified name, "struct.field".

    @param fullname: (C++: const char *) char const *
    """
    return _ida_struct.get_member_by_fullname(*args)

def get_member_fullname(*args) -> "qstring *":
    r"""
    get_member_fullname(mid) -> str
    Get a member's fully qualified name, "struct.field".

    @param mid: (C++: tid_t)
    """
    return _ida_struct.get_member_fullname(*args)

def get_member_name(*args) -> "qstring *":
    r"""
    get_member_name(mid) -> str

    @param mid: tid_t
    """
    return _ida_struct.get_member_name(*args)

def get_member_cmt(*args) -> "qstring *":
    r"""
    get_member_cmt(mid, repeatable) -> str
    Get comment of structure member.

    @param mid: (C++: tid_t)
    @param repeatable: (C++: bool)
    """
    return _ida_struct.get_member_cmt(*args)

def get_member_size(*args) -> "asize_t":
    r"""
    get_member_size(NONNULL_mptr) -> asize_t
    Get size of structure member. May return 0 for the last member of varstruct. For
    union members, returns member_t::eoff.

    @param NONNULL_mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.get_member_size(*args)

def is_varmember(*args) -> "bool":
    r"""
    is_varmember(mptr) -> bool
    Is variable size member?

    @param mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.is_varmember(*args)

def get_best_fit_member(*args) -> "member_t *":
    r"""
    get_best_fit_member(sptr, offset) -> member_t
    Get member that is most likely referenced by the specified offset. Useful for
    offsets > sizeof(struct).

    @param sptr: (C++: const struc_t *) struc_t const *
    @param offset: (C++: asize_t)
    """
    return _ida_struct.get_best_fit_member(*args)

def get_next_member_idx(*args) -> "ssize_t":
    r"""
    get_next_member_idx(sptr, off) -> ssize_t
    Get the next member idx, if it does not exist, return -1.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param off: (C++: asize_t)
    """
    return _ida_struct.get_next_member_idx(*args)

def get_prev_member_idx(*args) -> "ssize_t":
    r"""
    get_prev_member_idx(sptr, off) -> ssize_t
    Get the prev member idx, if it does not exist, return -1.

    @param sptr: (C++: const struc_t *) struc_t const *
    @param off: (C++: asize_t)
    """
    return _ida_struct.get_prev_member_idx(*args)

def add_struc(*args) -> "tid_t":
    r"""
    add_struc(idx, name, is_union=False) -> tid_t
    Create a structure type. if idx==BADADDR then add as the last idx. if
    name==nullptr then a name will be generated "struct_%d".

    @param idx: (C++: uval_t)
    @param name: (C++: const char *) char const *
    @param is_union: (C++: bool)
    """
    return _ida_struct.add_struc(*args)

def del_struc(*args) -> "bool":
    r"""
    del_struc(sptr) -> bool
    Delete a structure type.

    @param sptr: (C++: struc_t *)
    """
    return _ida_struct.del_struc(*args)

def set_struc_idx(*args) -> "bool":
    r"""
    set_struc_idx(sptr, idx) -> bool
    Set internal number of struct. Also see get_struc_idx(), get_struc_by_idx().

    @param sptr: (C++: const struc_t *) struc_t const *
    @param idx: (C++: uval_t)
    """
    return _ida_struct.set_struc_idx(*args)

def set_struc_align(*args) -> "bool":
    r"""
    set_struc_align(sptr, shift) -> bool
    Set structure alignment (SF_ALIGN)

    @param sptr: (C++: struc_t *)
    @param shift: (C++: int)
    """
    return _ida_struct.set_struc_align(*args)

def set_struc_name(*args) -> "bool":
    r"""
    set_struc_name(id, name) -> bool
    Set structure name.

    @param id: (C++: tid_t)
    @param name: (C++: const char *) char const *
    """
    return _ida_struct.set_struc_name(*args)

def set_struc_cmt(*args) -> "bool":
    r"""
    set_struc_cmt(id, cmt, repeatable) -> bool
    Set structure comment.

    @param id: (C++: tid_t)
    @param cmt: (C++: const char *) char const *
    @param repeatable: (C++: bool)
    """
    return _ida_struct.set_struc_cmt(*args)
STRUC_ERROR_MEMBER_OK = _ida_struct.STRUC_ERROR_MEMBER_OK
r"""
success
"""

STRUC_ERROR_MEMBER_NAME = _ida_struct.STRUC_ERROR_MEMBER_NAME
r"""
already has member with this name (bad name)
"""

STRUC_ERROR_MEMBER_OFFSET = _ida_struct.STRUC_ERROR_MEMBER_OFFSET
r"""
already has member at this offset
"""

STRUC_ERROR_MEMBER_SIZE = _ida_struct.STRUC_ERROR_MEMBER_SIZE
r"""
bad number of bytes or bad sizeof(type)
"""

STRUC_ERROR_MEMBER_TINFO = _ida_struct.STRUC_ERROR_MEMBER_TINFO
r"""
bad typeid parameter
"""

STRUC_ERROR_MEMBER_STRUCT = _ida_struct.STRUC_ERROR_MEMBER_STRUCT
r"""
bad struct id (the 1st argument)
"""

STRUC_ERROR_MEMBER_UNIVAR = _ida_struct.STRUC_ERROR_MEMBER_UNIVAR
r"""
unions can't have variable sized members
"""

STRUC_ERROR_MEMBER_VARLAST = _ida_struct.STRUC_ERROR_MEMBER_VARLAST
r"""
variable sized member should be the last member in the structure
"""

STRUC_ERROR_MEMBER_NESTED = _ida_struct.STRUC_ERROR_MEMBER_NESTED
r"""
recursive structure nesting is forbidden
"""


def add_struc_member(*args) -> "struc_error_t":
    r"""
    add_struc_member(sptr, fieldname, offset, flag, mt, nbytes) -> struc_error_t
    Add member to existing structure.

    @param sptr: (C++: struc_t *) structure to modify
    @param fieldname: (C++: const char *) if nullptr, then "anonymous_#" name will be generated
    @param offset: (C++: ea_t) BADADDR means add to the end of structure
    @param flag: (C++: flags_t) type + representation bits
    @param mt: (C++: const opinfo_t *) additional info about member type. must be present for structs,
               offsets, enums, strings, struct offsets.
    @param nbytes: (C++: asize_t) if == 0 then the structure will be a varstruct. in this case the
                   member should be the last member in the structure
    """
    return _ida_struct.add_struc_member(*args)

def del_struc_member(*args) -> "bool":
    r"""
    del_struc_member(sptr, offset) -> bool
    Delete member at given offset.

    @param sptr: (C++: struc_t *)
    @param offset: (C++: ea_t)
    """
    return _ida_struct.del_struc_member(*args)

def del_struc_members(*args) -> "int":
    r"""
    del_struc_members(sptr, off1, off2) -> int
    Delete members which occupy range of offsets (off1..off2).

    @param sptr: (C++: struc_t *)
    @param off1: (C++: ea_t)
    @param off2: (C++: ea_t)
    @return: number of deleted members or -1 on error
    """
    return _ida_struct.del_struc_members(*args)

def set_member_name(*args) -> "bool":
    r"""
    set_member_name(sptr, offset, name) -> bool
    Set name of member at given offset.

    @param sptr: (C++: struc_t *)
    @param offset: (C++: ea_t)
    @param name: (C++: const char *) char const *
    """
    return _ida_struct.set_member_name(*args)

def set_member_type(*args) -> "bool":
    r"""
    set_member_type(sptr, offset, flag, mt, nbytes) -> bool
    Set type of member at given offset (also see add_struc_member())

    @param sptr: (C++: struc_t *)
    @param offset: (C++: ea_t)
    @param flag: (C++: flags_t)
    @param mt: (C++: const opinfo_t *) opinfo_t const *
    @param nbytes: (C++: asize_t)
    """
    return _ida_struct.set_member_type(*args)

def set_member_cmt(*args) -> "bool":
    r"""
    set_member_cmt(mptr, cmt, repeatable) -> bool
    Set member comment.

    @param mptr: (C++: member_t *)
    @param cmt: (C++: const char *) char const *
    @param repeatable: (C++: bool)
    """
    return _ida_struct.set_member_cmt(*args)

def expand_struc(*args) -> "bool":
    r"""
    expand_struc(sptr, offset, delta, recalc=True) -> bool
    Expand/Shrink structure type.

    @param sptr: (C++: struc_t *)
    @param offset: (C++: ea_t)
    @param delta: (C++: adiff_t)
    @param recalc: (C++: bool)
    """
    return _ida_struct.expand_struc(*args)

def save_struc(*args) -> "void":
    r"""
    save_struc(sptr, may_update_ltypes=True)
    Update struct information in the database (internal function)

    @param sptr: (C++: struc_t *)
    @param may_update_ltypes: (C++: bool)
    """
    return _ida_struct.save_struc(*args)

def set_struc_hidden(*args) -> "void":
    r"""
    set_struc_hidden(sptr, is_hidden)
    Hide/unhide a struct type.

    @param sptr: (C++: struc_t *)
    @param is_hidden: (C++: bool)
    """
    return _ida_struct.set_struc_hidden(*args)

def set_struc_listed(*args) -> "void":
    r"""
    set_struc_listed(sptr, is_listed)
    Add/remove a struct type from the struct list.

    @param sptr: (C++: struc_t *)
    @param is_listed: (C++: bool)
    """
    return _ida_struct.set_struc_listed(*args)
SMT_BADARG = _ida_struct.SMT_BADARG
r"""
bad parameters
"""

SMT_NOCOMPAT = _ida_struct.SMT_NOCOMPAT
r"""
the new type is not compatible with the old type
"""

SMT_WORSE = _ida_struct.SMT_WORSE
r"""
the new type is worse than the old type
"""

SMT_SIZE = _ida_struct.SMT_SIZE
r"""
the new type is incompatible with the member size
"""

SMT_ARRAY = _ida_struct.SMT_ARRAY
r"""
arrays are forbidden as function arguments
"""

SMT_OVERLAP = _ida_struct.SMT_OVERLAP
r"""
member would overlap with members that cannot be deleted
"""

SMT_FAILED = _ida_struct.SMT_FAILED
r"""
failed to set new member type
"""

SMT_OK = _ida_struct.SMT_OK

SMT_KEEP = _ida_struct.SMT_KEEP
r"""
no need to change the member type, the old type is better
"""


def get_member_tinfo(*args) -> "bool":
    r"""
    get_member_tinfo(tif, mptr) -> bool
    Get tinfo for given member.

    @param tif: (C++: tinfo_t *)
    @param mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.get_member_tinfo(*args)

def del_member_tinfo(*args) -> "bool":
    r"""
    del_member_tinfo(sptr, mptr) -> bool
    Delete tinfo for given member.

    @param sptr: (C++: struc_t *)
    @param mptr: (C++: member_t *)
    """
    return _ida_struct.del_member_tinfo(*args)

def set_member_tinfo(*args) -> "smt_code_t":
    r"""
    set_member_tinfo(sptr, mptr, memoff, tif, flags) -> smt_code_t
    Set tinfo for given member.

    @param sptr: (C++: struc_t *) containing struct
    @param mptr: (C++: member_t *) target member
    @param memoff: (C++: uval_t) offset within member
    @param tif: (C++: const tinfo_t &) type info
    @param flags: (C++: int) Set member tinfo flags
    """
    return _ida_struct.set_member_tinfo(*args)
SET_MEMTI_MAY_DESTROY = _ida_struct.SET_MEMTI_MAY_DESTROY
r"""
may destroy other members
"""

SET_MEMTI_COMPATIBLE = _ida_struct.SET_MEMTI_COMPATIBLE
r"""
new type must be compatible with the old
"""

SET_MEMTI_FUNCARG = _ida_struct.SET_MEMTI_FUNCARG
r"""
mptr is function argument (cannot create arrays)
"""

SET_MEMTI_BYTIL = _ida_struct.SET_MEMTI_BYTIL
r"""
new type was created by the type subsystem
"""

SET_MEMTI_USERTI = _ida_struct.SET_MEMTI_USERTI
r"""
user-specified type
"""


def get_or_guess_member_tinfo(*args) -> "bool":
    r"""
    get_or_guess_member_tinfo(tif, mptr) -> bool
    Try to get tinfo for given member - if failed, generate a tinfo using
    information about the member id from the disassembly

    @param tif: (C++: tinfo_t *)
    @param mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.get_or_guess_member_tinfo(*args)

def retrieve_member_info(*args) -> "opinfo_t *":
    r"""
    retrieve_member_info(buf, mptr) -> opinfo_t
    Get operand type info for member.

    @param buf: (C++: opinfo_t *)
    @param mptr: (C++: const member_t *) member_t const *
    """
    return _ida_struct.retrieve_member_info(*args)

def is_anonymous_member_name(*args) -> "bool":
    r"""
    is_anonymous_member_name(name) -> bool
    Is member name prefixed with "anonymous"?

    @param name: (C++: const char *) char const *
    """
    return _ida_struct.is_anonymous_member_name(*args)

def is_dummy_member_name(*args) -> "bool":
    r"""
    is_dummy_member_name(name) -> bool
    Is member name an auto-generated name?

    @param name: (C++: const char *) char const *
    """
    return _ida_struct.is_dummy_member_name(*args)

def get_member_by_id(*args) -> "qstring *, struc_t **":
    r"""
    get_member_by_id(mid) -> member_t
    Check if the specified member id points to a struct member. convenience
    function.

    @param mid: (C++: tid_t)
    """
    return _ida_struct.get_member_by_id(*args)

def is_member_id(*args) -> "bool":
    r"""
    is_member_id(mid) -> bool
    Is a member id?

    @param mid: (C++: tid_t)
    """
    return _ida_struct.is_member_id(*args)

def is_special_member(*args) -> "bool":
    r"""
    is_special_member(id) -> bool
    Is a special member with the name beginning with ' '?

    @param id: (C++: tid_t)
    """
    return _ida_struct.is_special_member(*args)
class struct_field_visitor_t(object):
    r"""
    Proxy of C++ struct_field_visitor_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def visit_field(self, *args) -> "int":
        r"""
        visit_field(self, sptr, mptr) -> int

        @param sptr: struc_t *
        @param mptr: member_t *
        """
        return _ida_struct.struct_field_visitor_t_visit_field(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> struct_field_visitor_t

        @param self: PyObject *
        """
        if self.__class__ == struct_field_visitor_t:
            _self = None
        else:
            _self = self
        _ida_struct.struct_field_visitor_t_swiginit(self, _ida_struct.new_struct_field_visitor_t(_self, *args))
    __swig_destroy__ = _ida_struct.delete_struct_field_visitor_t
    def __disown__(self):
        self.this.disown()
        _ida_struct.disown_struct_field_visitor_t(self)
        return weakref.proxy(self)

# Register struct_field_visitor_t in _ida_struct:
_ida_struct.struct_field_visitor_t_swigregister(struct_field_visitor_t)


def visit_stroff_fields(*args) -> "adiff_t *":
    r"""
    visit_stroff_fields(sfv, path, disp, appzero) -> flags_t
    Visit structure fields in a stroff expression or in a reference to a struct data
    variable. This function can be used to enumerate all components of an expression
    like 'a.b.c'.

    @param sfv: (C++: struct_field_visitor_t &) visitor object
    @param path: (C++: const tid_t *) struct path (path[0] contains the initial struct id)
    @param disp: (C++: adiff_t *) offset into structure
    @param appzero: (C++: bool) should visit field at offset zero?
    """
    return _ida_struct.visit_stroff_fields(*args)

def stroff_as_size(*args) -> "bool":
    r"""
    stroff_as_size(plen, sptr, value) -> bool
    Should display a structure offset expression as the structure size?

    @param plen: (C++: int)
    @param sptr: (C++: const struc_t *) struc_t const *
    @param value: (C++: asize_t)
    """
    return _ida_struct.stroff_as_size(*args)

def get_innermost_member(*args) -> "PyObject *":
    r"""
    get_innermost_member(sptr, offset) -> (member_t, struc_t, int)
    Get the innermost member at the given offset

    @param sptr: the starting structure
    @param offset: offset into the starting structure
    @return:     - None on failure
        - tuple(member_t, struct_t, offset)
          where member_t: a member in SPTR (it is not a structure),
                struct_t: the innermost structure,
                offset:   remaining offset into the returned member
    """
    return _ida_struct.get_innermost_member(*args)



