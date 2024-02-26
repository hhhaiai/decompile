"""
Functions that deal with cross-references.

There are 2 types of xrefs: CODE and DATA references. All xrefs are kept in the
bTree except ordinary execution flow to the next instruction. Ordinary execution
flow to the next instruction is kept in flags (see bytes.hpp)

The source address of a cross-reference must be an item head (is_head) or a
structure member id.

Cross-references are automatically sorted."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_xref
else:
    import _ida_xref

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

SWIG_PYTHON_LEGACY_BOOL = _ida_xref.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


def create_switch_xrefs(*args) -> "bool":
    r"""
    create_switch_xrefs(ea, si) -> bool
    This function creates xrefs from the indirect jump.

    Usually there is no need to call this function directly because the kernel
    will call it for switch tables

    Note: Custom switch information are not supported yet.

    @param ea: address of the 'indirect jump' instruction
    @param si: switch information

    @return: Boolean
    """
    return _ida_xref.create_switch_xrefs(*args)
class cases_and_targets_t(object):
    r"""
    Proxy of C++ cases_and_targets_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    cases = property(_ida_xref.cases_and_targets_t_cases_get, _ida_xref.cases_and_targets_t_cases_set, doc=r"""cases""")
    targets = property(_ida_xref.cases_and_targets_t_targets_get, _ida_xref.cases_and_targets_t_targets_set, doc=r"""targets""")

    def __init__(self, *args):
        r"""
        __init__(self) -> cases_and_targets_t
        """
        _ida_xref.cases_and_targets_t_swiginit(self, _ida_xref.new_cases_and_targets_t(*args))
    __swig_destroy__ = _ida_xref.delete_cases_and_targets_t

# Register cases_and_targets_t in _ida_xref:
_ida_xref.cases_and_targets_t_swigregister(cases_and_targets_t)


def calc_switch_cases(*args) -> "cases_and_targets_t *":
    r"""
    calc_switch_cases(ea, si) -> cases_and_targets_t
    Get information about a switch's cases.

    The returned information can be used as follows:

        for idx in range(len(results.cases)):
            cur_case = results.cases[idx]
            for cidx in range(len(cur_case)):
                print("case: %d" % cur_case[cidx])
            print("  goto 0x%x" % results.targets[idx])

    @param ea: address of the 'indirect jump' instruction
    @param si: switch information

    @return: a structure with 2 members: 'cases', and 'targets'.
    """
    return _ida_xref.calc_switch_cases(*args)

def create_switch_table(*args) -> "bool":
    r"""
    create_switch_table(ea, si) -> bool
    Create switch table from the switch information

    @param ea: address of the 'indirect jump' instruction
    @param si: switch information

    @return: Boolean
    """
    return _ida_xref.create_switch_table(*args)
fl_U = _ida_xref.fl_U
r"""
unknown - for compatibility with old versions. Should not be used anymore.
"""

fl_CF = _ida_xref.fl_CF
r"""
Call Far This xref creates a function at the referenced location
"""

fl_CN = _ida_xref.fl_CN
r"""
Call Near This xref creates a function at the referenced location
"""

fl_JF = _ida_xref.fl_JF
r"""
Jump Far.
"""

fl_JN = _ida_xref.fl_JN
r"""
Jump Near.
"""

fl_USobsolete = _ida_xref.fl_USobsolete
r"""
User specified (obsolete)
"""

fl_F = _ida_xref.fl_F
r"""
Ordinary flow: used to specify execution flow to the next instruction.
"""

dr_U = _ida_xref.dr_U
r"""
Unknown - for compatibility with old versions. Should not be used anymore.
"""

dr_O = _ida_xref.dr_O
r"""
Offset The reference uses 'offset' of data rather than its value OR The
reference appeared because the "OFFSET" flag of instruction is set. The meaning
of this type is IDP dependent.
"""

dr_W = _ida_xref.dr_W
r"""
Write access.
"""

dr_R = _ida_xref.dr_R
r"""
Read access.
"""

dr_T = _ida_xref.dr_T
r"""
Text (for forced operands only) Name of data is used in manual operand
"""

dr_I = _ida_xref.dr_I
r"""
Informational (a derived java class references its base class informationally)
"""

dr_S = _ida_xref.dr_S
r"""
Reference to enum member (symbolic constant)
"""

XREF_USER = _ida_xref.XREF_USER
r"""
User specified xref. This xref will not be deleted by IDA. This bit should be
combined with the existing xref types (cref_t & dref_t) Cannot be used for fl_F
xrefs
"""

XREF_TAIL = _ida_xref.XREF_TAIL
r"""
Reference to tail byte in extrn symbols.
"""

XREF_BASE = _ida_xref.XREF_BASE
r"""
Reference to the base part of an offset.
"""

XREF_MASK = _ida_xref.XREF_MASK
r"""
Mask to get xref type.
"""

XREF_PASTEND = _ida_xref.XREF_PASTEND
r"""
Reference is past item. This bit may be passed to add_dref() functions but it
won't be saved in the database. It will prevent the destruction of eventual
alignment directives.
"""


def xrefchar(*args) -> "char":
    r"""
    xrefchar(xrtype) -> char
    Get character describing the xref type.

    @param xrtype: (C++: char) combination of Cross-Reference type flags and a cref_t of dref_t
                   value
    """
    return _ida_xref.xrefchar(*args)

def add_cref(*args) -> "bool":
    r"""
    add_cref(frm, to, type) -> bool
    Create a code cross-reference.

    @param from: (C++: ea_t) linear address of referencing instruction
    @param to: (C++: ea_t) linear address of referenced instruction
    @param type: (C++: cref_t) cross-reference type
    @return: success
    """
    return _ida_xref.add_cref(*args)

def del_cref(*args) -> "bool":
    r"""
    del_cref(frm, to, expand) -> bool
    Delete a code cross-reference.

    @param from: (C++: ea_t) linear address of referencing instruction
    @param to: (C++: ea_t) linear address of referenced instruction
    @param expand: (C++: bool) policy to delete the referenced instruction
    * 1: plan to delete the referenced instruction if it has no more references.
    * 0: don't delete the referenced instruction even if no more cross-references
    point to it
    @retval true: if the referenced instruction will be deleted
    """
    return _ida_xref.del_cref(*args)

def add_dref(*args) -> "bool":
    r"""
    add_dref(frm, to, type) -> bool
    Create a data cross-reference.

    @param from: (C++: ea_t) linear address of referencing instruction or data
    @param to: (C++: ea_t) linear address of referenced data
    @param type: (C++: dref_t) cross-reference type
    @return: success (may fail if user-defined xref exists from->to)
    """
    return _ida_xref.add_dref(*args)

def del_dref(*args) -> "void":
    r"""
    del_dref(frm, to)
    Delete a data cross-reference.

    @param from: (C++: ea_t) linear address of referencing instruction or data
    @param to: (C++: ea_t) linear address of referenced data
    """
    return _ida_xref.del_dref(*args)
class xrefblk_t(object):
    r"""
    Proxy of C++ xrefblk_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    frm = property(_ida_xref.xrefblk_t_frm_get, _ida_xref.xrefblk_t_frm_set, doc=r"""frm""")
    to = property(_ida_xref.xrefblk_t_to_get, _ida_xref.xrefblk_t_to_set, doc=r"""to""")
    r"""
    the referenced address - filled by first_from(), next_from()
    """
    iscode = property(_ida_xref.xrefblk_t_iscode_get, _ida_xref.xrefblk_t_iscode_set, doc=r"""iscode""")
    r"""
    1-is code reference; 0-is data reference
    """
    type = property(_ida_xref.xrefblk_t_type_get, _ida_xref.xrefblk_t_type_set, doc=r"""type""")
    r"""
    type of the last returned reference (cref_t & dref_t)
    """
    user = property(_ida_xref.xrefblk_t_user_get, _ida_xref.xrefblk_t_user_set, doc=r"""user""")
    r"""
    1-is user defined xref, 0-defined by ida
    """

    def first_from(self, *args) -> "bool":
        r"""
        first_from(self, _from, flags) -> bool
        Get first xref from the given address (store in to)

        @param _from: (C++: ea_t)
        @param flags: (C++: int)
        """
        return _ida_xref.xrefblk_t_first_from(self, *args)

    def first_to(self, *args) -> "bool":
        r"""
        first_to(self, _to, flags) -> bool
        Get xref to given address (store in from)

        @param _to: (C++: ea_t)
        @param flags: (C++: int)
        """
        return _ida_xref.xrefblk_t_first_to(self, *args)

    def next_from(self, *args) -> "bool":
        r"""
        next_from(self) -> bool
        Get xref from '_from' that comes after '_to'.
        next_from(self, _from, _to, flags) -> bool

        @param _from: ea_t
        @param _to: ea_t
        @param flags: int
        """
        return _ida_xref.xrefblk_t_next_from(self, *args)

    def next_to(self, *args) -> "bool":
        r"""
        next_to(self) -> bool
        Get xref to '_to' that comes after '_from'.
        next_to(self, _from, _to, flags) -> bool

        @param _from: ea_t
        @param _to: ea_t
        @param flags: int
        """
        return _ida_xref.xrefblk_t_next_to(self, *args)

    def crefs_to(self, ea):
        r"""
        Provide an iterator on code references to ea including flow references
        """
        ref = get_first_cref_to(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_cref_to(ea, ref)


    def fcrefs_to(self, ea):
        r"""
        Provide an iterator on code references to ea
        """
        ref = get_first_fcref_to(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_fcref_to(ea, ref)


    def crefs_from(self, ea):
        r"""
        Provide an iterator on code references from ea including flow references
        """
        ref = get_first_cref_from(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_cref_from(ea, ref)


    def fcrefs_from(self, ea):
        r"""
        Provide an iterator on code references from ea
        """
        ref = get_first_fcref_from(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_fcref_from(ea, ref)


    def drefs_to(self, ea):
        r"""
        Provide an iterator on data references to ea
        """
        ref = get_first_dref_to(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_dref_to(ea, ref)


    def drefs_from(self, ea):
        r"""
        Provide an iterator on data references from ea
        """
        ref = get_first_dref_from(ea)
        while ref != ida_idaapi.BADADDR:
            yield ref
            ref = get_next_dref_from(ea, ref)


    def refs_from(self, ea, flag):
        r"""
        Provide an iterator on from reference represented by flag
        """
        def _copy_xref():
            """ Make a private copy of the xref class to preserve its contents """
            class _xref(object):
                pass

            xr = _xref()
            for attr in [ 'frm', 'to', 'iscode', 'type', 'user' ]:
                setattr(xr, attr, getattr(self, attr))
            return xr

        if self.first_from(ea, flag):
            yield _copy_xref()
            while self.next_from():
                yield _copy_xref()


    def refs_to(self, ea, flag):
        r"""
        Provide an iterator on to reference represented by flag
        """
        def _copy_xref():
            """ Make a private copy of the xref class to preserve its contents """
            class _xref(object):
                pass

            xr = _xref()
            for attr in [ 'frm', 'to', 'iscode', 'type', 'user' ]:
                setattr(xr, attr, getattr(self, attr))
            return xr

        if self.first_to(ea, flag):
            yield _copy_xref()
            while self.next_to():
                yield _copy_xref()


    def __init__(self, *args):
        r"""
        __init__(self) -> xrefblk_t
        """
        _ida_xref.xrefblk_t_swiginit(self, _ida_xref.new_xrefblk_t(*args))
    __swig_destroy__ = _ida_xref.delete_xrefblk_t

# Register xrefblk_t in _ida_xref:
_ida_xref.xrefblk_t_swigregister(xrefblk_t)
XREF_ALL = _ida_xref.XREF_ALL
r"""
return all references
"""

XREF_FAR = _ida_xref.XREF_FAR
r"""
don't return ordinary flow xrefs
"""

XREF_DATA = _ida_xref.XREF_DATA
r"""
return data references only
"""



def get_first_dref_from(*args) -> "ea_t":
    r"""
    get_first_dref_from(frm) -> ea_t
    Get first data referenced from the specified address.

    @param from: (C++: ea_t) linear address of referencing instruction or data
    @return: linear address of first (lowest) data referenced from the specified
             address. Return BADADDR if the specified instruction/data doesn't
             reference to anything.
    """
    return _ida_xref.get_first_dref_from(*args)

def get_next_dref_from(*args) -> "ea_t":
    r"""
    get_next_dref_from(frm, current) -> ea_t
    Get next data referenced from the specified address.

    @param from: (C++: ea_t) linear address of referencing instruction or data
    @param current: (C++: ea_t) linear address of current referenced data. This value is
                    returned by get_first_dref_from() or previous call to
                    get_next_dref_from() functions.
    @return: linear address of next data or BADADDR.
    """
    return _ida_xref.get_next_dref_from(*args)

def get_first_dref_to(*args) -> "ea_t":
    r"""
    get_first_dref_to(to) -> ea_t
    Get address of instruction/data referencing to the specified data.

    @param to: (C++: ea_t) linear address of referencing instruction or data
    @return: BADADDR if nobody refers to the specified data.
    """
    return _ida_xref.get_first_dref_to(*args)

def get_next_dref_to(*args) -> "ea_t":
    r"""
    get_next_dref_to(to, current) -> ea_t
    Get address of instruction/data referencing to the specified data

    @param to: (C++: ea_t) linear address of referencing instruction or data
    @param current: (C++: ea_t) current linear address. This value is returned by
                    get_first_dref_to() or previous call to get_next_dref_to()
                    functions.
    @return: BADADDR if nobody refers to the specified data.
    """
    return _ida_xref.get_next_dref_to(*args)

def get_first_cref_from(*args) -> "ea_t":
    r"""
    get_first_cref_from(frm) -> ea_t
    Get first instruction referenced from the specified instruction. If the
    specified instruction passes execution to the next instruction then the next
    instruction is returned. Otherwise the lowest referenced address is returned
    (remember that xrefs are kept sorted!).

    @param from: (C++: ea_t) linear address of referencing instruction
    @return: first referenced address. If the specified instruction doesn't
             reference to other instructions then returns BADADDR.
    """
    return _ida_xref.get_first_cref_from(*args)

def get_next_cref_from(*args) -> "ea_t":
    r"""
    get_next_cref_from(frm, current) -> ea_t
    Get next instruction referenced from the specified instruction.

    @param from: (C++: ea_t) linear address of referencing instruction
    @param current: (C++: ea_t) linear address of current referenced instruction This value is
                    returned by get_first_cref_from() or previous call to
                    get_next_cref_from() functions.
    @return: next referenced address or BADADDR.
    """
    return _ida_xref.get_next_cref_from(*args)

def get_first_cref_to(*args) -> "ea_t":
    r"""
    get_first_cref_to(to) -> ea_t
    Get first instruction referencing to the specified instruction. If the specified
    instruction may be executed immediately after its previous instruction then the
    previous instruction is returned. Otherwise the lowest referencing address is
    returned. (remember that xrefs are kept sorted!).

    @param to: (C++: ea_t) linear address of referenced instruction
    @return: linear address of the first referencing instruction or BADADDR.
    """
    return _ida_xref.get_first_cref_to(*args)

def get_next_cref_to(*args) -> "ea_t":
    r"""
    get_next_cref_to(to, current) -> ea_t
    Get next instruction referencing to the specified instruction.

    @param to: (C++: ea_t) linear address of referenced instruction
    @param current: (C++: ea_t) linear address of current referenced instruction This value is
                    returned by get_first_cref_to() or previous call to
                    get_next_cref_to() functions.
    @return: linear address of the next referencing instruction or BADADDR.
    """
    return _ida_xref.get_next_cref_to(*args)

def get_first_fcref_from(*args) -> "ea_t":
    r"""
    get_first_fcref_from(frm) -> ea_t

    @param from: ea_t
    """
    return _ida_xref.get_first_fcref_from(*args)

def get_next_fcref_from(*args) -> "ea_t":
    r"""
    get_next_fcref_from(frm, current) -> ea_t

    @param from: ea_t
    @param current: ea_t
    """
    return _ida_xref.get_next_fcref_from(*args)

def get_first_fcref_to(*args) -> "ea_t":
    r"""
    get_first_fcref_to(to) -> ea_t

    @param to: ea_t
    """
    return _ida_xref.get_first_fcref_to(*args)

def get_next_fcref_to(*args) -> "ea_t":
    r"""
    get_next_fcref_to(to, current) -> ea_t

    @param to: ea_t
    @param current: ea_t
    """
    return _ida_xref.get_next_fcref_to(*args)

def has_external_refs(*args) -> "bool":
    r"""
    has_external_refs(pfn, ea) -> bool
    Has a location external to the function references?

    @param pfn: (C++: func_t *)
    @param ea: (C++: ea_t)
    """
    return _ida_xref.has_external_refs(*args)

def delete_switch_table(*args) -> "void":
    r"""
    delete_switch_table(jump_ea, si)

    @param jump_ea: ea_t
    @param si: switch_info_t const &
    """
    return _ida_xref.delete_switch_table(*args)
class casevec_t(object):
    r"""
    Proxy of C++ qvector< qvector< sval_t > > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> casevec_t
        __init__(self, x) -> casevec_t

        @param x: qvector< qvector< long long > > const &
        """
        _ida_xref.casevec_t_swiginit(self, _ida_xref.new_casevec_t(*args))
    __swig_destroy__ = _ida_xref.delete_casevec_t

    def push_back(self, *args) -> "qvector< long long > &":
        r"""
        push_back(self, x)

        @param x: qvector< long long > const &

        push_back(self) -> qvector< long long > &
        """
        return _ida_xref.casevec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_xref.casevec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_xref.casevec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_xref.casevec_t_empty(self, *args)

    def at(self, *args) -> "qvector< long long > const &":
        r"""
        at(self, _idx) -> qvector< long long > const &

        @param _idx: size_t
        """
        return _ida_xref.casevec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_xref.casevec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_xref.casevec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: qvector< long long > const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_xref.casevec_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=qvector< long long >())

        @param x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_xref.casevec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_xref.casevec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_xref.casevec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< qvector< long long > > &
        """
        return _ida_xref.casevec_t_swap(self, *args)

    def extract(self, *args) -> "qvector< long long > *":
        r"""
        extract(self) -> qvector< long long > *
        """
        return _ida_xref.casevec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: qvector< long long > *
        @param len: size_t
        """
        return _ida_xref.casevec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< qvector< long long > > const &
        """
        return _ida_xref.casevec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< qvector< long long > > const &
        """
        return _ida_xref.casevec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< qvector< long long > >::const_iterator":
        r"""
        begin(self) -> qvector< qvector< long long > >::iterator
        begin(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_begin(self, *args)

    def end(self, *args) -> "qvector< qvector< long long > >::const_iterator":
        r"""
        end(self) -> qvector< qvector< long long > >::iterator
        end(self) -> qvector< qvector< long long > >::const_iterator
        """
        return _ida_xref.casevec_t_end(self, *args)

    def insert(self, *args) -> "qvector< qvector< long long > >::iterator":
        r"""
        insert(self, it, x) -> qvector< qvector< long long > >::iterator

        @param it: qvector< qvector< long long > >::iterator
        @param x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< qvector< long long > >::iterator":
        r"""
        erase(self, it) -> qvector< qvector< long long > >::iterator

        @param it: qvector< qvector< long long > >::iterator

        erase(self, first, last) -> qvector< qvector< long long > >::iterator

        @param first: qvector< qvector< long long > >::iterator
        @param last: qvector< qvector< long long > >::iterator
        """
        return _ida_xref.casevec_t_erase(self, *args)

    def find(self, *args) -> "qvector< qvector< long long > >::const_iterator":
        r"""
        find(self, x) -> qvector< qvector< long long > >::iterator

        @param x: qvector< long long > const &

        find(self, x) -> qvector< qvector< long long > >::const_iterator

        @param x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: qvector< long long > const &
        """
        return _ida_xref.casevec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: qvector< long long > const &

        """
        return _ida_xref.casevec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_xref.casevec_t___len__(self, *args)

    def __getitem__(self, *args) -> "qvector< long long > const &":
        r"""
        __getitem__(self, i) -> qvector< long long > const &

        @param i: size_t
        """
        return _ida_xref.casevec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: qvector< long long > const &
        """
        return _ida_xref.casevec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register casevec_t in _ida_xref:
_ida_xref.casevec_t_swigregister(casevec_t)


#<pycode(py_xref)>

import ida_idaapi
ida_idaapi._listify_types(
        casevec_t)

#</pycode(py_xref)>




