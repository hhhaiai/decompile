"""
Functions that provide the lowest level public interface to the database.

(Namely, Btree). To learn more about Balanced Trees:
\link{http://www.bluerwhite.org/btree/}

We don't use Btree directly. Instead, we have another layer built on the top of
Btree. Here is a brief explanation of this layer.

An object called "netnode" is modeled on the top of Btree. Each netnode has a
unique id: a 32-bit value (64-bit for ida64). Usually there is a trivial mapping
of the linear addresses used in the program to netnodes. If we have additional
information about an address (a comment is attached to it, for example), this
information is stored in the corresponding netnode. See nalt.hpp to see how the
kernel uses netnodes. Also, some netnodes have no corresponding linear address
(however, they still have an id). They are used to store information not related
to a particular address.

Each netnode _may_ have the following attributes:

* a name: an arbitrary non-empty string, up to 255KB-1 bytes
* a value: arbitrary sized object, max size is MAXSPECSIZE
* altvals: a sparse array of 32-bit values. indexes in this array may be 8-bit
or 32-bit values
* supvals: an array of arbitrary sized objects. (size of each object is limited
by MAXSPECSIZE) indexes in this array may be 8-bit or 32-bit values
* charvals: a sparse array of 8-bit values. indexes in this array may be 8-bit
or 32-bit values
* hashvals: a hash (an associative array). indexes in this array are strings
values are arbitrary sized (max size is MAXSPECSIZE)

Initially a new netnode contains no information at all so no disk space is used
for it. As you add new information, the netnode grows.

All arrays that are attached to the netnode behave in the same manner.
Initially:
* all members of altvals/charvals array are zeroes
* all members of supvals/hashvals array are undefined

If you need to store objects bigger that MAXSPECSIZE, please note that there are
high-level functions to store arbitrary sized objects in supvals. See
setblog/getblob and other blob-related functions.

You may use netnodes to store additional information about the program.
Limitations on the use of netnodes are the following:

* use netnodes only if you could not find a kernel service to store your type of
information
* do not create netnodes with valid identifier names. Use the "$ " prefix (or
any other prefix with characters not allowed in the identifiers for the names of
your netnodes. Although you will probably not destroy anything by accident,
using already defined names for the names of your netnodes is still discouraged.
* you may create as many netnodes as you want (creation of an unnamed netnode
does not increase the size of the database). however, since each netnode has a
number, creating too many netnodes could lead to the exhaustion of the netnode
numbers (the numbering starts at 0xFF000000)
* remember that netnodes are automatically saved to the disk by the kernel.

Advanced info:

In fact a netnode may contain up to 256 arrays of arbitrary sized objects (not
only the 4 listed above). Each array has an 8-bit tag. Usually tags are
represented by character constants. For example, altvals and supvals are simply
2 of 256 arrays, with the tags 'A' and 'S' respectively."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_netnode
else:
    import _ida_netnode

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

SWIG_PYTHON_LEGACY_BOOL = _ida_netnode.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

BADNODE = _ida_netnode.BADNODE
r"""
A number to represent a bad netnode reference.
"""

class netnode(object):
    r"""
    Proxy of C++ netnode class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, num=nodeidx_t(-1)) -> netnode

        @param num: nodeidx_t

        __init__(self, _name, namlen=0, do_create=False) -> netnode

        @param _name: char const *
        @param namlen: size_t
        @param do_create: bool
        """
        _ida_netnode.netnode_swiginit(self, _ida_netnode.new_netnode(*args))

    @staticmethod
    def exist(*args):
        r"""
        exist(_name) -> bool
        Does the netnode with the specified name exist?

        @param _name: (C++: const char *) char const *
        """
        return _ida_netnode.netnode_exist(*args)

    def create(self, *args):
        r"""
        create(self, _name, namlen=0) -> bool
        Create unnamed netnode.
        @retval 1: ok
        @retval 0: should not happen, indicates internal error

        @param _name: char const *
        @param namlen: size_t

        create(self) -> bool
        """
        return _ida_netnode.netnode_create(self, *args)

    def kill(self, *args):
        r"""
        kill(self)
        Delete a netnode with all information attached to it.
        """
        return _ida_netnode.netnode_kill(self, *args)

    def get_name(self, *args):
        r"""
        get_name(self) -> ssize_t
        Get the netnode name.

        @return: -1 if netnode is unnamed (buf is untouched in this case), otherwise the
                 name length
        """
        return _ida_netnode.netnode_get_name(self, *args)

    def rename(self, *args):
        r"""
        rename(self, newname, namlen=0) -> bool
        Rename a netnode.

        @param newname: (C++: const char *) new name of netnode. nullptr or "" means to delete name. names
                        of user-defined netnodes must have the "$ " prefix in order to
                        avoid clashes with program byte names.
        @param namlen: (C++: size_t) length of new name. if not specified, it will be calculated using
                       strlen()
        @retval 1: ok
        @retval 0: failed, newname is already used
        """
        return _ida_netnode.netnode_rename(self, *args)

    def valobj(self, *args):
        r"""
        valobj(self) -> ssize_t
        Get value of netnode. Netnode values are arbitrary sized objects with max size
        is MAXSPECSIZE. NB: do not use this function for strings - see valstr().

        @return: length of value, -1 if no value present
        """
        return _ida_netnode.netnode_valobj(self, *args)

    def valstr(self, *args):
        r"""
        valstr(self) -> ssize_t
        @see: valstr(qstring *buf) const
        """
        return _ida_netnode.netnode_valstr(self, *args)

    def set(self, *args):
        r"""
        set(self, value) -> bool
        Set value of netnode.

        @param value: (C++: const void *) pointer to value
        @return: 1 - ok
        """
        return _ida_netnode.netnode_set(self, *args)

    def delvalue(self, *args):
        r"""
        delvalue(self) -> bool
        Delete value of netnode.
        @retval 1: ok
        @retval 0: failed, netnode is bad or other error
        """
        return _ida_netnode.netnode_delvalue(self, *args)

    def set_long(self, *args):
        r"""
        set_long(self, x) -> bool
        Value of netnode as a long number:

        @param x: (C++: nodeidx_t)
        """
        return _ida_netnode.netnode_set_long(self, *args)

    def value_exists(self, *args):
        r"""
        value_exists(self) -> bool
        """
        return _ida_netnode.netnode_value_exists(self, *args)

    def long_value(self, *args):
        r"""
        long_value(self) -> nodeidx_t
        """
        return _ida_netnode.netnode_long_value(self, *args)

    def altval(self, *args):
        r"""
        altval(self, alt, tag=atag) -> nodeidx_t
        Get altval element of the specified array.

        @param alt: (C++: nodeidx_t) index into array of altvals
        @param tag: (C++: uchar) tag of array. may be omitted
        @return: value of altval element. nonexistent altval members are returned as
                 zeroes
        """
        return _ida_netnode.netnode_altval(self, *args)

    def altval_ea(self, *args):
        r"""
        altval_ea(self, ea, tag=atag) -> nodeidx_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_altval_ea(self, *args)

    def altset(self, *args):
        r"""
        altset(self, alt, value, tag=atag) -> bool
        Set value of altval array.

        @param alt: (C++: nodeidx_t) index into array of altvals
        @param value: (C++: nodeidx_t) new value of altval element
        @param tag: (C++: uchar) tag of array
        @retval 1: ok
        @retval 0: failed, normally should not occur
        """
        return _ida_netnode.netnode_altset(self, *args)

    def altset_ea(self, *args):
        r"""
        altset_ea(self, ea, value, tag=atag) -> bool

        @param ea: ea_t
        @param value: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_altset_ea(self, *args)

    def altdel_ea(self, *args):
        r"""
        altdel_ea(self, ea, tag=atag) -> bool

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_altdel_ea(self, *args)

    def easet(self, *args):
        r"""
        easet(self, ea, addr, tag) -> bool
        Store/retrieve/delete an address value in the netnode that corresponds to an
        address.

        @param ea: (C++: ea_t)
        @param addr: (C++: ea_t)
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_easet(self, *args)

    def eaget(self, *args):
        r"""
        eaget(self, ea, tag) -> ea_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_eaget(self, *args)

    def eadel(self, *args):
        r"""
        eadel(self, ea, tag) -> bool

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_eadel(self, *args)

    def easet_idx(self, *args):
        r"""
        easet_idx(self, idx, addr, tag) -> bool

        @param idx: nodeidx_t
        @param addr: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_easet_idx(self, *args)

    def eaget_idx(self, *args):
        r"""
        eaget_idx(self, idx, tag) -> ea_t

        @param idx: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_eaget_idx(self, *args)

    def easet_idx8(self, *args):
        r"""
        easet_idx8(self, idx, addr, tag) -> bool

        @param idx: uchar
        @param addr: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_easet_idx8(self, *args)

    def eaget_idx8(self, *args):
        r"""
        eaget_idx8(self, idx, tag) -> ea_t

        @param idx: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_eaget_idx8(self, *args)

    def eadel_idx8(self, *args):
        r"""
        eadel_idx8(self, idx, tag) -> bool

        @param idx: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_eadel_idx8(self, *args)

    def altfirst(self, *args):
        r"""
        altfirst(self, tag=atag) -> nodeidx_t
        Get first existing element of altval array.

        @param tag: (C++: uchar) tag of array
        @return: index of first existing element of altval array, BADNODE if altval
                 array is empty
        """
        return _ida_netnode.netnode_altfirst(self, *args)

    def altnext(self, *args):
        r"""
        altnext(self, cur, tag=atag) -> nodeidx_t
        Get next existing element of altval array.

        @param cur: (C++: nodeidx_t) current index
        @param tag: (C++: uchar) tag of array
        @return: index of the next existing element of altval array, BADNODE if no more
                 altval array elements exist
        """
        return _ida_netnode.netnode_altnext(self, *args)

    def altlast(self, *args):
        r"""
        altlast(self, tag=atag) -> nodeidx_t
        Get last element of altval array.

        @param tag: (C++: uchar) tag of array
        @return: index of last existing element of altval array, BADNODE if altval array
                 is empty
        """
        return _ida_netnode.netnode_altlast(self, *args)

    def altprev(self, *args):
        r"""
        altprev(self, cur, tag=atag) -> nodeidx_t
        Get previous existing element of altval array.

        @param cur: (C++: nodeidx_t) current index
        @param tag: (C++: uchar) tag of array
        @return: index of the previous existing element of altval array, BADNODE if no
                 more altval array elements exist
        """
        return _ida_netnode.netnode_altprev(self, *args)

    def altshift(self, *args):
        r"""
        altshift(self, _from, to, size, tag=atag) -> size_t
        Shift the altval array elements. Moves the array elements at (from..from+size)
        to (to..to+size)

        @param from: (C++: nodeidx_t)
        @param to: (C++: nodeidx_t)
        @param size: (C++: nodeidx_t)
        @param tag: (C++: uchar)
        @return: number of shifted elements
        """
        return _ida_netnode.netnode_altshift(self, *args)

    def charval(self, *args):
        r"""
        charval(self, alt, tag) -> uchar

        @param alt: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_charval(self, *args)

    def charset(self, *args):
        r"""
        charset(self, alt, val, tag) -> bool

        @param alt: nodeidx_t
        @param val: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charset(self, *args)

    def chardel(self, *args):
        r"""
        chardel(self, alt, tag) -> bool

        @param alt: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_chardel(self, *args)

    def charval_ea(self, *args):
        r"""
        charval_ea(self, ea, tag) -> uchar

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_charval_ea(self, *args)

    def charset_ea(self, *args):
        r"""
        charset_ea(self, ea, val, tag) -> bool

        @param ea: ea_t
        @param val: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charset_ea(self, *args)

    def chardel_ea(self, *args):
        r"""
        chardel_ea(self, ea, tag) -> bool

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_chardel_ea(self, *args)

    def charfirst(self, *args):
        r"""
        charfirst(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_charfirst(self, *args)

    def charnext(self, *args):
        r"""
        charnext(self, cur, tag) -> nodeidx_t

        @param cur: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_charnext(self, *args)

    def charlast(self, *args):
        r"""
        charlast(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_charlast(self, *args)

    def charprev(self, *args):
        r"""
        charprev(self, cur, tag) -> nodeidx_t

        @param cur: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_charprev(self, *args)

    def charshift(self, *args):
        r"""
        charshift(self, _from, to, size, tag) -> size_t

        @param from: nodeidx_t
        @param to: nodeidx_t
        @param size: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_charshift(self, *args)

    def altval_idx8(self, *args):
        r"""
        altval_idx8(self, alt, tag) -> nodeidx_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_altval_idx8(self, *args)

    def altset_idx8(self, *args):
        r"""
        altset_idx8(self, alt, val, tag) -> bool

        @param alt: uchar
        @param val: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_altset_idx8(self, *args)

    def altdel_idx8(self, *args):
        r"""
        altdel_idx8(self, alt, tag) -> bool

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_altdel_idx8(self, *args)

    def altfirst_idx8(self, *args):
        r"""
        altfirst_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_altfirst_idx8(self, *args)

    def altnext_idx8(self, *args):
        r"""
        altnext_idx8(self, cur, tag) -> nodeidx_t

        @param cur: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_altnext_idx8(self, *args)

    def altlast_idx8(self, *args):
        r"""
        altlast_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_altlast_idx8(self, *args)

    def altprev_idx8(self, *args):
        r"""
        altprev_idx8(self, cur, tag) -> nodeidx_t

        @param cur: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_altprev_idx8(self, *args)

    def charval_idx8(self, *args):
        r"""
        charval_idx8(self, alt, tag) -> uchar

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charval_idx8(self, *args)

    def charset_idx8(self, *args):
        r"""
        charset_idx8(self, alt, val, tag) -> bool

        @param alt: uchar
        @param val: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charset_idx8(self, *args)

    def chardel_idx8(self, *args):
        r"""
        chardel_idx8(self, alt, tag) -> bool

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_chardel_idx8(self, *args)

    def charfirst_idx8(self, *args):
        r"""
        charfirst_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_charfirst_idx8(self, *args)

    def charnext_idx8(self, *args):
        r"""
        charnext_idx8(self, cur, tag) -> nodeidx_t

        @param cur: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charnext_idx8(self, *args)

    def charlast_idx8(self, *args):
        r"""
        charlast_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_charlast_idx8(self, *args)

    def charprev_idx8(self, *args):
        r"""
        charprev_idx8(self, cur, tag) -> nodeidx_t

        @param cur: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_charprev_idx8(self, *args)

    def altdel(self, *args):
        r"""
        altdel(self, alt, tag=atag) -> bool
        Delete all elements of altval array. This function may be applied to 32-bit and
        8-bit altval arrays. This function deletes the whole altval array.

        @param alt: nodeidx_t
        @param tag: uchar

        @return: success
        altdel(self) -> bool
        """
        return _ida_netnode.netnode_altdel(self, *args)

    def altdel_all(self, *args):
        r"""
        altdel_all(self, tag=atag) -> bool
        Delete all elements of the specified altval array. This function may be applied
        to 32-bit and 8-bit altval arrays. This function deletes the whole altval array.

        @param tag: (C++: uchar) tag of array
        @return: success
        """
        return _ida_netnode.netnode_altdel_all(self, *args)

    def supval(self, *args):
        r"""
        supval(self, alt, tag=stag) -> ssize_t
        Get value of the specified supval array element. NB: do not use this function to
        retrieve strings, see supstr()!

        @param alt: (C++: nodeidx_t) index into array of supvals
        @param tag: (C++: uchar) tag of array. Default: stag
        @return: size of value, -1 if element doesn't exist
        """
        return _ida_netnode.netnode_supval(self, *args)

    def supval_ea(self, *args):
        r"""
        supval_ea(self, ea, tag=stag) -> ssize_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_supval_ea(self, *args)

    def supstr(self, *args):
        r"""
        supstr(self, alt, tag=stag) -> ssize_t
        @see: supstr(qstring *buf, nodeidx_t alt, uchar tag=stag) const

        @param alt: (C++: nodeidx_t)
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_supstr(self, *args)

    def supstr_ea(self, *args):
        r"""
        supstr_ea(self, ea, tag=stag) -> ssize_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_supstr_ea(self, *args)

    def supset(self, *args):
        r"""
        supset(self, alt, value, tag=stag) -> bool
        Set value of supval array element.

        @param alt: (C++: nodeidx_t) index into array of supvals
        @param value: (C++: const void *) pointer to supval value
        @param tag: (C++: uchar) tag of array
        @retval 1: ok
        @retval 0: should not occur - indicates internal error
        """
        return _ida_netnode.netnode_supset(self, *args)

    def supset_ea(self, *args):
        r"""
        supset_ea(self, ea, value, tag=stag) -> bool

        @param ea: ea_t
        @param value: void const *
        @param tag: uchar
        """
        return _ida_netnode.netnode_supset_ea(self, *args)

    def supdel_ea(self, *args):
        r"""
        supdel_ea(self, ea, tag=stag) -> bool

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_supdel_ea(self, *args)

    def lower_bound(self, *args):
        r"""
        lower_bound(self, cur, tag=stag) -> nodeidx_t
        Get lower bound of existing elements of supval array.

        @param cur: (C++: nodeidx_t) current index
        @param tag: (C++: uchar) tag of array
        @return: index of first existing element of supval array >= cur BADNODE if
                 supval array is empty
        """
        return _ida_netnode.netnode_lower_bound(self, *args)

    def lower_bound_ea(self, *args):
        r"""
        lower_bound_ea(self, ea, tag=stag) -> nodeidx_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_lower_bound_ea(self, *args)

    def supfirst(self, *args):
        r"""
        supfirst(self, tag=stag) -> nodeidx_t
        Get first existing element of supval array.

        @param tag: (C++: uchar) tag of array
        @return: index of first existing element of supval array, BADNODE if supval
                 array is empty
        """
        return _ida_netnode.netnode_supfirst(self, *args)

    def supnext(self, *args):
        r"""
        supnext(self, cur, tag=stag) -> nodeidx_t
        Get next existing element of supval array.

        @param cur: (C++: nodeidx_t) current index
        @param tag: (C++: uchar) tag of array
        @return: index of the next existing element of supval array, BADNODE if no more
                 supval array elements exist
        """
        return _ida_netnode.netnode_supnext(self, *args)

    def suplast(self, *args):
        r"""
        suplast(self, tag=stag) -> nodeidx_t
        Get last existing element of supval array.

        @param tag: (C++: uchar) tag of array
        @return: index of last existing element of supval array, BADNODE if supval array
                 is empty
        """
        return _ida_netnode.netnode_suplast(self, *args)

    def supprev(self, *args):
        r"""
        supprev(self, cur, tag=stag) -> nodeidx_t
        Get previous existing element of supval array.

        @param cur: (C++: nodeidx_t) current index
        @param tag: (C++: uchar) tag of array
        @return: index of the previous existing element of supval array BADNODE if no
                 more supval array elements exist
        """
        return _ida_netnode.netnode_supprev(self, *args)

    def supshift(self, *args):
        r"""
        supshift(self, _from, to, size, tag=stag) -> size_t
        Shift the supval array elements. Moves the array elements at (from..from+size)
        to (to..to+size)

        @param from: (C++: nodeidx_t)
        @param to: (C++: nodeidx_t)
        @param size: (C++: nodeidx_t)
        @param tag: (C++: uchar)
        @return: number of shifted elements
        """
        return _ida_netnode.netnode_supshift(self, *args)

    def supval_idx8(self, *args):
        r"""
        supval_idx8(self, alt, tag) -> ssize_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_supval_idx8(self, *args)

    def supstr_idx8(self, *args):
        r"""
        supstr_idx8(self, alt, tag) -> ssize_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_supstr_idx8(self, *args)

    def supset_idx8(self, *args):
        r"""
        supset_idx8(self, alt, value, tag) -> bool

        @param alt: uchar
        @param value: void const *
        @param tag: uchar
        """
        return _ida_netnode.netnode_supset_idx8(self, *args)

    def supdel_idx8(self, *args):
        r"""
        supdel_idx8(self, alt, tag) -> bool

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_supdel_idx8(self, *args)

    def lower_bound_idx8(self, *args):
        r"""
        lower_bound_idx8(self, alt, tag) -> nodeidx_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_lower_bound_idx8(self, *args)

    def supfirst_idx8(self, *args):
        r"""
        supfirst_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_supfirst_idx8(self, *args)

    def supnext_idx8(self, *args):
        r"""
        supnext_idx8(self, alt, tag) -> nodeidx_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_supnext_idx8(self, *args)

    def suplast_idx8(self, *args):
        r"""
        suplast_idx8(self, tag) -> nodeidx_t

        @param tag: uchar
        """
        return _ida_netnode.netnode_suplast_idx8(self, *args)

    def supprev_idx8(self, *args):
        r"""
        supprev_idx8(self, alt, tag) -> nodeidx_t

        @param alt: uchar
        @param tag: uchar
        """
        return _ida_netnode.netnode_supprev_idx8(self, *args)

    def supdel(self, *args):
        r"""
        supdel(self, alt, tag=stag) -> bool
        Delete all elements of supval array. This function may be applied to 32-bit and
        8-bit supval arrays. This function deletes the whole supval array.

        @param alt: nodeidx_t
        @param tag: uchar

        @return: success
        supdel(self) -> bool
        """
        return _ida_netnode.netnode_supdel(self, *args)

    def supdel_all(self, *args):
        r"""
        supdel_all(self, tag) -> bool
        Delete all elements of the specified supval array. This function may be applied
        to 32-bit and 8-bit supval arrays. This function deletes the whole supval array.

        @param tag: (C++: uchar)
        @return: success
        """
        return _ida_netnode.netnode_supdel_all(self, *args)

    def supdel_range(self, *args):
        r"""
        supdel_range(self, idx1, idx2, tag) -> int
        Delete range of elements in the specified supval array. Elements in range [idx1,
        idx2) will be deleted.
        @note: This function can also be used to delete a range of altval elements

        @param idx1: (C++: nodeidx_t) first element to delete
        @param idx2: (C++: nodeidx_t) last element to delete + 1
        @param tag: (C++: uchar) tag of array
        @return: number of deleted elements
        """
        return _ida_netnode.netnode_supdel_range(self, *args)

    def supdel_range_idx8(self, *args):
        r"""
        supdel_range_idx8(self, idx1, idx2, tag) -> int
        Same as above, but accepts 8-bit indexes.

        @param idx1: (C++: uchar)
        @param idx2: (C++: uchar)
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_supdel_range_idx8(self, *args)

    def hashval(self, *args):
        r"""
        hashval(self, idx, tag=htag) -> ssize_t
        Get value of the specified hash element.

        @param idx: (C++: const char *) index into hash
        @param tag: (C++: uchar) tag of hash. Default: htag
        @return: -1 if element doesn't exist or idx is nullptr. otherwise returns the
                 value size in bytes
        """
        return _ida_netnode.netnode_hashval(self, *args)

    def hashstr(self, *args):
        r"""
        hashstr(self, idx, tag=htag) -> ssize_t
        @see: hashstr(qstring *buf, const char *idx, uchar tag=htag) const

        @param idx: (C++: const char *) char const *
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_hashstr(self, *args)

    def hashval_long(self, *args):
        r"""
        hashval_long(self, idx, tag=htag) -> nodeidx_t
        Get value of the specified hash element.

        @param idx: (C++: const char *) index into hash
        @param tag: (C++: uchar) tag of hash. Default: htag
        @return: value of hash element (it should be set using hashset(nodeidx_t)), 0 if
                 the element does not exist
        """
        return _ida_netnode.netnode_hashval_long(self, *args)

    def hashset(self, *args):
        r"""
        hashset(self, idx, value, tag=htag) -> bool
        Set value of hash element to long value.

        @param idx: (C++: const char *) index into hash
        @param value: (C++: nodeidx_t) new value of hash element
        @param tag: (C++: uchar) tag of hash. Default: htag
        @retval 1: ok
        @retval 0: should not occur - indicates internal error
        """
        return _ida_netnode.netnode_hashset(self, *args)

    def hashset_idx(self, *args):
        r"""
        hashset_idx(self, idx, value, tag=htag) -> bool

        @param idx: char const *
        @param value: nodeidx_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_hashset_idx(self, *args)

    def hashdel(self, *args):
        r"""
        hashdel(self, idx, tag=htag) -> bool
        Delete hash element.

        @param idx: (C++: const char *) index into hash
        @param tag: (C++: uchar) tag of hash. Default: htag
        @retval true: deleted
        @retval false: element does not exist
        """
        return _ida_netnode.netnode_hashdel(self, *args)

    def hashfirst(self, *args):
        r"""
        hashfirst(self, tag=htag) -> ssize_t
        @see: hashfirst(qstring *buf, uchar tag=htag) const

        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_hashfirst(self, *args)

    def hashnext(self, *args):
        r"""
        hashnext(self, idx, tag=htag) -> ssize_t
        @see: hashnext(qstring *buf, const char *idx, uchar tag=htag) const

        @param idx: (C++: const char *) char const *
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_hashnext(self, *args)

    def hashlast(self, *args):
        r"""
        hashlast(self, tag=htag) -> ssize_t
        @see: hashlast(qstring *buf, uchar tag=htag) const

        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_hashlast(self, *args)

    def hashprev(self, *args):
        r"""
        hashprev(self, idx, tag=htag) -> ssize_t
        @see: hashprev(qstring *buf, const char *idx, uchar tag=htag) const

        @param idx: (C++: const char *) char const *
        @param tag: (C++: uchar)
        """
        return _ida_netnode.netnode_hashprev(self, *args)

    def hashdel_all(self, *args):
        r"""
        hashdel_all(self, tag=htag) -> bool
        Delete all elements of hash. This function deletes the whole hash.

        @param tag: (C++: uchar) tag of hash. Default: htag
        @return: success
        """
        return _ida_netnode.netnode_hashdel_all(self, *args)

    def blobsize(self, *args):
        r"""
        blobsize(self, _start, tag) -> size_t
        Get size of blob.

        @param _start: (C++: nodeidx_t) index of the first supval element used to store blob
        @param tag: (C++: uchar) tag of supval array
        @return: number of bytes required to store a blob
        """
        return _ida_netnode.netnode_blobsize(self, *args)

    def blobsize_ea(self, *args):
        r"""
        blobsize_ea(self, ea, tag) -> size_t

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_blobsize_ea(self, *args)

    def setblob(self, *args):
        r"""
        setblob(self, buf, _start, tag) -> bool
        Store a blob in a netnode.

        @param buf: (C++: const void *) pointer to blob to save
        @param _start: (C++: nodeidx_t)
        @param tag: (C++: uchar) tag of supval array
        @return: success
        """
        return _ida_netnode.netnode_setblob(self, *args)

    def setblob_ea(self, *args):
        r"""
        setblob_ea(self, buf, ea, tag) -> bool

        @param buf: void const *
        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_setblob_ea(self, *args)

    def delblob(self, *args):
        r"""
        delblob(self, _start, tag) -> int
        Delete a blob.

        @param _start: (C++: nodeidx_t) index of the first supval element used to store blob
        @param tag: (C++: uchar) tag of supval array
        @return: number of deleted supvals
        """
        return _ida_netnode.netnode_delblob(self, *args)

    def delblob_ea(self, *args):
        r"""
        delblob_ea(self, ea, tag) -> int

        @param ea: ea_t
        @param tag: uchar
        """
        return _ida_netnode.netnode_delblob_ea(self, *args)

    def start(self, *args):
        r"""
        start(self) -> bool
        Get first netnode in the graph. Sets netnodenumber to the lowest existing
        number.
        @retval true: ok
        @retval false: graph is empty
        """
        return _ida_netnode.netnode_start(self, *args)

    def end(self, *args):
        r"""
        end(self) -> bool
        Get last netnode in the graph. Sets netnodenumber to the highest existing
        number.
        @retval true: ok
        @retval false: graph is empty
        """
        return _ida_netnode.netnode_end(self, *args)

    def next(self, *args):
        r"""
        next(self) -> bool
        Get next netnode in the graph. Sets netnodenumber to the next existing number
        @retval true: ok
        @retval false: no more netnodes
        """
        return _ida_netnode.netnode_next(self, *args)

    def prev(self, *args):
        r"""
        prev(self) -> bool
        Get prev netnode in the graph. Sets netnodenumber to the previous existing
        number
        @retval true: ok
        @retval false: no more netnodes
        """
        return _ida_netnode.netnode_prev(self, *args)

    def copyto(self, *args):
        r"""
        copyto(self, destnode, count=1) -> size_t

        @param destnode: netnode
        @param count: nodeidx_t
        """
        return _ida_netnode.netnode_copyto(self, *args)

    def moveto(self, *args):
        r"""
        moveto(self, destnode, count=1) -> size_t

        @param destnode: netnode
        @param count: nodeidx_t
        """
        return _ida_netnode.netnode_moveto(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, n) -> bool

        @param n: netnode &

        __eq__(self, x) -> bool

        @param x: nodeidx_t
        """
        return _ida_netnode.netnode___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, n) -> bool

        @param n: netnode &

        __ne__(self, x) -> bool

        @param x: nodeidx_t
        """
        return _ida_netnode.netnode___ne__(self, *args)

    def index(self, *args):
        r"""
        index(self) -> nodeidx_t
        """
        return _ida_netnode.netnode_index(self, *args)

    def getblob(self, *args):
        r"""
        getblob(self, start, tag) -> bytes or None
        Get blob from a netnode into a qstring* and make sure the string is null-
        terminated.

        @param start: nodeidx_t
        @param tag: (C++: uchar) tag of supval array
        @return: -1 if blob doesn't exist size of string (including terminating null)
                 otherwise
        """
        return _ida_netnode.netnode_getblob(self, *args)

    def getclob(self, *args):
        r"""
        getclob(self, start, tag) -> str

        @param start: nodeidx_t
        @param tag: char
        """
        return _ida_netnode.netnode_getclob(self, *args)

    def getblob_ea(self, *args):
        r"""
        getblob_ea(self, ea, tag) -> PyObject *

        @param ea: ea_t
        @param tag: char
        """
        return _ida_netnode.netnode_getblob_ea(self, *args)

    def hashstr_buf(self, *args):
        r"""
        hashstr_buf(self, idx, tag=htag) -> PyObject *

        @param idx: char const *
        @param tag: char
        """
        return _ida_netnode.netnode_hashstr_buf(self, *args)

    def hashset_buf(self, *args):
        r"""
        hashset_buf(self, idx, py_str, tag=htag) -> bool

        @param idx: char const *
        @param py_str: PyObject *
        @param tag: char
        """
        return _ida_netnode.netnode_hashset_buf(self, *args)
    __swig_destroy__ = _ida_netnode.delete_netnode

# Register netnode in _ida_netnode:
_ida_netnode.netnode_swigregister(netnode)
cvar = _ida_netnode.cvar
MAXNAMESIZE = cvar.MAXNAMESIZE
r"""
Maximum length of a netnode name. WILL BE REMOVED IN THE FUTURE.
"""
MAX_NODENAME_SIZE = cvar.MAX_NODENAME_SIZE
r"""
Maximum length of a name. We permit names up to 32KB-1 bytes.
"""
MAXSPECSIZE = cvar.MAXSPECSIZE
r"""
Maximum length of strings or objects stored in a supval array element.
"""
atag = cvar.atag
r"""
Array of altvals.
"""
stag = cvar.stag
r"""
Array of supvals.
"""
htag = cvar.htag
r"""
Array of hashvals.
"""
vtag = cvar.vtag
r"""
Value of netnode.
"""
ntag = cvar.ntag
r"""
Name of netnode.
"""
ltag = cvar.ltag
r"""
Links between netnodes.
"""
NETMAP_IDX = cvar.NETMAP_IDX
NETMAP_VAL = cvar.NETMAP_VAL
NETMAP_STR = cvar.NETMAP_STR
NETMAP_X8 = cvar.NETMAP_X8
NETMAP_V8 = cvar.NETMAP_V8

def exist(*args):
    r"""
    exist(n) -> bool

    @param n: netnode const &
    """
    return _ida_netnode.exist(*args)

def netnode_exist(*args):
    r"""
    netnode_exist(_name) -> bool

    @param _name: char const *
    """
    return _ida_netnode.netnode_exist(*args)




