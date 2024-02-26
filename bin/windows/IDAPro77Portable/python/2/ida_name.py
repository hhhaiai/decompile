"""
Functions that deal with names.

A non-tail address of the program may have a name. Tail addresses (i.e. the
addresses in the middle of an instruction or data item) cannot have names."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_name
else:
    import _ida_name

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

SWIG_PYTHON_LEGACY_BOOL = _ida_name.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class ea_name_vec_t(object):
    r"""
    Proxy of C++ qvector< ea_name_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> ea_name_vec_t
        __init__(self, x) -> ea_name_vec_t

        @param x: qvector< ea_name_t > const &
        """
        _ida_name.ea_name_vec_t_swiginit(self, _ida_name.new_ea_name_vec_t(*args))
    __swig_destroy__ = _ida_name.delete_ea_name_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: ea_name_t const &

        push_back(self) -> ea_name_t
        """
        return _ida_name.ea_name_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_name.ea_name_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_name.ea_name_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_name.ea_name_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> ea_name_t

        @param _idx: size_t
        """
        return _ida_name.ea_name_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_name.ea_name_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_name.ea_name_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: ea_name_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_name.ea_name_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=ea_name_t())

        @param x: ea_name_t const &
        """
        return _ida_name.ea_name_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_name.ea_name_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_name.ea_name_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_name.ea_name_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< ea_name_t > &
        """
        return _ida_name.ea_name_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> ea_name_t
        """
        return _ida_name.ea_name_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: ea_name_t *
        @param len: size_t
        """
        return _ida_name.ea_name_vec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> ea_name_t
        """
        return _ida_name.ea_name_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> ea_name_t
        """
        return _ida_name.ea_name_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> ea_name_t

        @param it: qvector< ea_name_t >::iterator
        @param x: ea_name_t const &
        """
        return _ida_name.ea_name_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> ea_name_t

        @param it: qvector< ea_name_t >::iterator

        erase(self, first, last) -> ea_name_t

        @param first: qvector< ea_name_t >::iterator
        @param last: qvector< ea_name_t >::iterator
        """
        return _ida_name.ea_name_vec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_name.ea_name_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> ea_name_t

        @param i: size_t
        """
        return _ida_name.ea_name_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: ea_name_t const &
        """
        return _ida_name.ea_name_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register ea_name_vec_t in _ida_name:
_ida_name.ea_name_vec_t_swigregister(ea_name_vec_t)


def get_name(*args):
    r"""
    get_name(ea) -> qstring

    @param ea: ea_t
    """
    return _ida_name.get_name(*args)

def get_colored_name(*args):
    r"""
    get_colored_name(ea) -> qstring

    @param ea: ea_t
    """
    return _ida_name.get_colored_name(*args)
MAXNAMELEN = _ida_name.MAXNAMELEN
r"""
Maximum length of a name in IDA (with the trailing zero)
"""

FUNC_IMPORT_PREFIX = _ida_name.FUNC_IMPORT_PREFIX
r"""
Name prefix used by IDA for the imported functions.
"""


def set_name(*args):
    r"""
    set_name(ea, name, flags=0) -> bool
    Set or delete name of an item at the specified address. An item can be anything:
    instruction, function, data byte, word, string, structure, etc... Include name
    into the list of names.

    @param ea: (C++: ea_t) linear address. do nothing if ea is not valid (return 0). tail bytes
               can't have names.
    @param name: (C++: const char *) new name.
    * nullptr: do nothing (return 0).
    * "" : delete name.
    * otherwise this is a new name.
    @param flags: (C++: int) Set name flags. If a bit is not specified, then the corresponding
                  action is not performed and the name will retain the same bits as
                  before calling this function. For new names, default is: non-
                  public, non-weak, non-auto.
    @retval 1: ok, name is changed
    @retval 0: failure, a warning is displayed
    """
    return _ida_name.set_name(*args)
SN_CHECK = _ida_name.SN_CHECK

SN_NOCHECK = _ida_name.SN_NOCHECK
r"""
Don't fail if the name contains invalid characters. If this bit is clear, all
invalid chars (those !is_ident_cp()) will be replaced by SUBSTCHAR List of valid
characters is defined in ida.cfg
"""

SN_PUBLIC = _ida_name.SN_PUBLIC
r"""
if set, make name public
"""

SN_NON_PUBLIC = _ida_name.SN_NON_PUBLIC
r"""
if set, make name non-public
"""

SN_WEAK = _ida_name.SN_WEAK
r"""
if set, make name weak
"""

SN_NON_WEAK = _ida_name.SN_NON_WEAK
r"""
if set, make name non-weak
"""

SN_AUTO = _ida_name.SN_AUTO
r"""
if set, make name autogenerated
"""

SN_NON_AUTO = _ida_name.SN_NON_AUTO
r"""
if set, make name non-autogenerated
"""

SN_NOLIST = _ida_name.SN_NOLIST
r"""
if set, exclude name from the list. if not set, then include the name into the
list (however, if other bits are set, the name might be immediately excluded
from the list).
"""

SN_NOWARN = _ida_name.SN_NOWARN
r"""
don't display a warning if failed
"""

SN_LOCAL = _ida_name.SN_LOCAL
r"""
create local name. a function should exist. local names can't be public or weak.
also they are not included into the list of names they can't have dummy
prefixes.
"""

SN_IDBENC = _ida_name.SN_IDBENC
r"""
the name is given in the IDB encoding; non-ASCII bytes will be decoded
accordingly. Specifying SN_IDBENC also implies SN_NODUMMY
"""

SN_FORCE = _ida_name.SN_FORCE
r"""
if the specified name is already present in the database, try variations with a
numerical suffix like "_123"
"""

SN_NODUMMY = _ida_name.SN_NODUMMY
r"""
automatically prepend the name with '_' if it begins with a dummy suffix such as
'sub_'. See also SN_IDBENC
"""

SN_DELTAIL = _ida_name.SN_DELTAIL
r"""
if name cannot be set because of a tail byte, delete the hindering item
"""


def force_name(*args):
    r"""
    force_name(ea, name, flags=0) -> bool

    @param ea: ea_t
    @param name: char const *
    @param flags: int
    """
    return _ida_name.force_name(*args)

def del_global_name(*args):
    r"""
    del_global_name(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.del_global_name(*args)

def del_local_name(*args):
    r"""
    del_local_name(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.del_local_name(*args)

def set_dummy_name(*args):
    r"""
    set_dummy_name(_from, ea) -> bool
    Give an autogenerated (dummy) name. Autogenerated names have special prefixes
    (loc_...).

    @param from: (C++: ea_t) linear address of the operand which references to the address
    @param ea: (C++: ea_t) linear address
    @retval 1: ok, dummy name is generated or the byte already had a name
    @retval 0: failure, invalid address or tail byte
    """
    return _ida_name.set_dummy_name(*args)

def make_name_auto(*args):
    r"""
    make_name_auto(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.make_name_auto(*args)

def make_name_user(*args):
    r"""
    make_name_user(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.make_name_user(*args)
UCDR_STRLIT = _ida_name.UCDR_STRLIT

UCDR_NAME = _ida_name.UCDR_NAME

UCDR_MANGLED = _ida_name.UCDR_MANGLED

UCDR_TYPE = _ida_name.UCDR_TYPE

VNT_IDENT = _ida_name.VNT_IDENT

VNT_TYPE = _ida_name.VNT_TYPE

VNT_UDTMEM = _ida_name.VNT_UDTMEM

VNT_STRLIT = _ida_name.VNT_STRLIT

VNT_VISIBLE = _ida_name.VNT_VISIBLE


def is_valid_cp(*args):
    r"""
    is_valid_cp(cp, kind, data=None) -> bool
    Is the given codepoint acceptable in the given context?

    @param cp: (C++: wchar32_t)
    @param kind: (C++: nametype_t) enum nametype_t
    @param data: (C++: void *)
    """
    return _ida_name.is_valid_cp(*args)

def set_cp_validity(*args):
    r"""
    set_cp_validity(kind, cp, endcp=wchar32_t(-1), valid=True)
    Mark the given codepoint (or range) as acceptable or unacceptable in the given
    context If 'endcp' is not BADCP, it is considered to be the end of the range:
    [cp, endcp), and is not included in the range

    @param kind: (C++: ucdr_kind_t) enum ucdr_kind_t
    @param cp: (C++: wchar32_t)
    @param endcp: (C++: wchar32_t)
    """
    return _ida_name.set_cp_validity(*args)

def get_cp_validity(*args):
    r"""
    get_cp_validity(kind, cp, endcp=wchar32_t(-1)) -> bool
    Is the given codepoint (or range) acceptable in the given context? If 'endcp' is
    not BADCP, it is considered to be the end of the range: [cp, endcp), and is not
    included in the range

    @param kind: (C++: ucdr_kind_t) enum ucdr_kind_t
    @param cp: (C++: wchar32_t)
    @param endcp: (C++: wchar32_t)
    """
    return _ida_name.get_cp_validity(*args)

def is_ident_cp(*args):
    r"""
    is_ident_cp(cp) -> bool
    Can a character appear in a name? (present in ::NameChars or ::MangleChars)

    @param cp: (C++: wchar32_t)
    """
    return _ida_name.is_ident_cp(*args)

def is_strlit_cp(*args):
    r"""
    is_strlit_cp(cp, specific_ranges=None) -> bool
    Can a character appear in a string literal (present in ::StrlitChars) If
    'specific_ranges' are specified, those will be used instead of the ones
    corresponding to the current culture (only if ::StrlitChars is configured to use
    the current culture)

    @param cp: (C++: wchar32_t)
    @param specific_ranges: (C++: const rangeset_crefvec_t *) rangeset_crefvec_t const *
    """
    return _ida_name.is_strlit_cp(*args)

def is_visible_cp(*args):
    r"""
    is_visible_cp(cp) -> bool
    Can a character be displayed in a name? (present in ::NameChars)

    @param cp: (C++: wchar32_t)
    """
    return _ida_name.is_visible_cp(*args)

def is_ident(*args):
    r"""
    is_ident(name) -> bool
    Is a valid name? (including ::MangleChars)

    @param name: (C++: const char *) char const *
    """
    return _ida_name.is_ident(*args)

def is_uname(*args):
    r"""
    is_uname(name) -> bool
    Is valid user-specified name? (valid name & !dummy prefix).

    @param name: (C++: const char *) name to test. may be nullptr.
    @retval 1: yes
    @retval 0: no
    """
    return _ida_name.is_uname(*args)

def is_valid_typename(*args):
    r"""
    is_valid_typename(name) -> bool
    Is valid type name?

    @param name: (C++: const char *) name to test. may be nullptr.
    @retval 1: yes
    @retval 0: no
    """
    return _ida_name.is_valid_typename(*args)

def extract_name(*args):
    r"""
    extract_name(line, x) -> str
    Extract a name or address from the specified string.

    @param line: (C++: const char *) input string
    @param x: (C++: int) x coordinate of cursor
    @return: -1 if cannot extract. otherwise length of the name
    """
    return _ida_name.extract_name(*args)

def hide_name(*args):
    r"""
    hide_name(ea)
    Remove name from the list of names

    @param ea: (C++: ea_t) address of the name
    """
    return _ida_name.hide_name(*args)

def show_name(*args):
    r"""
    show_name(ea)
    Insert name to the list of names.

    @param ea: (C++: ea_t)
    """
    return _ida_name.show_name(*args)

def get_name_ea(*args):
    r"""
    get_name_ea(_from, name) -> ea_t
    Get address of the name. Dummy names (like byte_xxxx where xxxx are hex digits)
    are parsed by this function to obtain the address. The database is not consulted
    for them. This function works only with regular names.

    @param from: (C++: ea_t) linear address where the name is used. if not applicable, then
                 should be BADADDR.
    @param name: (C++: const char *) any name in the program or nullptr
    @return: address of the name or BADADDR
    """
    return _ida_name.get_name_ea(*args)

def get_name_base_ea(*args):
    r"""
    get_name_base_ea(_from, to) -> ea_t
    Get address of the name used in the expression for the address

    @param from: (C++: ea_t) address of the operand which references to the address
    @param to: (C++: ea_t) the referenced address
    @return: address of the name used to represent the operand
    """
    return _ida_name.get_name_base_ea(*args)

def get_name_value(*args):
    r"""
    get_name_value(_from, name) -> int
    Get value of the name. This function knows about: regular names, enums, special
    segments, etc.

    @param from: (C++: ea_t) linear address where the name is used if not applicable, then
                 should be BADADDR
    @param name: (C++: const char *) any name in the program or nullptr
    @return: Name value result codes
    """
    return _ida_name.get_name_value(*args)
NT_NONE = _ida_name.NT_NONE
r"""
name doesn't exist or has no value
"""

NT_BYTE = _ida_name.NT_BYTE
r"""
name is byte name (regular name)
"""

NT_LOCAL = _ida_name.NT_LOCAL
r"""
name is local label
"""

NT_STKVAR = _ida_name.NT_STKVAR
r"""
name is stack variable name
"""

NT_ENUM = _ida_name.NT_ENUM
r"""
name is symbolic constant
"""

NT_ABS = _ida_name.NT_ABS
r"""
name is absolute symbol (SEG_ABSSYM)
"""

NT_SEG = _ida_name.NT_SEG
r"""
name is segment or segment register name
"""

NT_STROFF = _ida_name.NT_STROFF
r"""
name is structure member
"""

NT_BMASK = _ida_name.NT_BMASK
r"""
name is a bit group mask name
"""

NT_REGVAR = _ida_name.NT_REGVAR
r"""
name is a renamed register (*value is idx into pfn->regvars)
"""

GN_VISIBLE = _ida_name.GN_VISIBLE
r"""
replace forbidden characters by SUBSTCHAR
"""

GN_COLORED = _ida_name.GN_COLORED
r"""
return colored name
"""

GN_DEMANGLED = _ida_name.GN_DEMANGLED
r"""
return demangled name
"""

GN_STRICT = _ida_name.GN_STRICT
r"""
fail if cannot demangle
"""

GN_SHORT = _ida_name.GN_SHORT
r"""
use short form of demangled name
"""

GN_LONG = _ida_name.GN_LONG
r"""
use long form of demangled name
"""

GN_LOCAL = _ida_name.GN_LOCAL
r"""
try to get local name first; if failed, get global
"""

GN_ISRET = _ida_name.GN_ISRET
r"""
for dummy names: use retloc
"""

GN_NOT_ISRET = _ida_name.GN_NOT_ISRET
r"""
for dummy names: do not use retloc
"""

GN_NOT_DUMMY = _ida_name.GN_NOT_DUMMY
r"""
do not return a dummy name
"""


def get_visible_name(*args):
    r"""
    get_visible_name(ea, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param gtn_flags: int
    """
    return _ida_name.get_visible_name(*args)

def get_short_name(*args):
    r"""
    get_short_name(ea, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param gtn_flags: int
    """
    return _ida_name.get_short_name(*args)

def get_long_name(*args):
    r"""
    get_long_name(ea, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param gtn_flags: int
    """
    return _ida_name.get_long_name(*args)

def get_colored_short_name(*args):
    r"""
    get_colored_short_name(ea, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param gtn_flags: int
    """
    return _ida_name.get_colored_short_name(*args)

def get_colored_long_name(*args):
    r"""
    get_colored_long_name(ea, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param gtn_flags: int
    """
    return _ida_name.get_colored_long_name(*args)

def get_demangled_name(*args):
    r"""
    get_demangled_name(ea, inhibitor, demform, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param inhibitor: int32
    @param demform: int
    @param gtn_flags: int
    """
    return _ida_name.get_demangled_name(*args)

def get_colored_demangled_name(*args):
    r"""
    get_colored_demangled_name(ea, inhibitor, demform, gtn_flags=0) -> qstring

    @param ea: ea_t
    @param inhibitor: int32
    @param demform: int
    @param gtn_flags: int
    """
    return _ida_name.get_colored_demangled_name(*args)

def get_name_color(*args):
    r"""
    get_name_color(_from, ea) -> color_t
    Calculate flags for get_ea_name() function.

    Get name color.

    @param from: (C++: ea_t) linear address where the name is used. if not applicable, then
                 should be BADADDR. The kernel returns a local name color if the
                 reference is within a function, i.e. 'from' and 'ea' belong to the
                 same function.
    @param ea: (C++: ea_t) linear address
    """
    return _ida_name.get_name_color(*args)
GETN_APPZERO = _ida_name.GETN_APPZERO
r"""
meaningful only if the name refers to a structure. append a struct field name if
the field offset is zero?
"""

GETN_NOFIXUP = _ida_name.GETN_NOFIXUP
r"""
ignore the fixup information when producing the name
"""

GETN_NODUMMY = _ida_name.GETN_NODUMMY
r"""
do not create a new dummy name but pretend it exists
"""


def get_name_expr(*args):
    r"""
    get_name_expr(_from, n, ea, off, flags=0x0001) -> str
    Convert address to name expression (name with a displacement). This function
    takes into account fixup information and returns a colored name expression (in
    the form <name> +/- <offset>). It also knows about structure members and arrays.
    If the specified address doesn't have a name, a dummy name is generated.

    @param from: (C++: ea_t) linear address of instruction operand or data referring to the
                 name. This address will be used to get fixup information, so it
                 should point to exact position of the operand in the instruction.
    @param n: (C++: int) number of referencing operand. for data items specify 0
    @param ea: (C++: ea_t) address to convert to name expression
    @param off: (C++: uval_t) the value of name expression. this parameter is used only to check
                that the name expression will have the wanted value. 'off' may be
                equal to BADADDR but this is discouraged because it prohibits
                checks.
    @param flags: (C++: int) Name expression flags
    @return: < 0 if address is not valid, no segment or other failure. otherwise the
             length of the name expression in characters.
    """
    return _ida_name.get_name_expr(*args)

def get_nice_colored_name(*args):
    r"""
    get_nice_colored_name(ea, flags=0) -> str
    Get a nice colored name at the specified address. Ex:
    * segment:sub+offset
    * segment:sub:local_label
    * segment:label
    * segment:address
    * segment:address+offset

    @param ea: (C++: ea_t) linear address
    @param flags: (C++: int) Nice colored name flags
    @return: the length of the generated name in bytes.
    """
    return _ida_name.get_nice_colored_name(*args)
GNCN_NOSEG = _ida_name.GNCN_NOSEG
r"""
ignore the segment prefix when producing the name
"""

GNCN_NOCOLOR = _ida_name.GNCN_NOCOLOR
r"""
generate an uncolored name
"""

GNCN_NOLABEL = _ida_name.GNCN_NOLABEL
r"""
don't generate labels
"""

GNCN_NOFUNC = _ida_name.GNCN_NOFUNC
r"""
don't generate funcname+... expressions
"""

GNCN_SEG_FUNC = _ida_name.GNCN_SEG_FUNC
r"""
generate both segment and function names (default is to omit segment name if a
function name is present)
"""

GNCN_SEGNUM = _ida_name.GNCN_SEGNUM
r"""
segment part is displayed as a hex number
"""

GNCN_REQFUNC = _ida_name.GNCN_REQFUNC
r"""
return 0 if the address does not belong to a function
"""

GNCN_REQNAME = _ida_name.GNCN_REQNAME
r"""
return 0 if the address can only be represented as a hex number
"""

GNCN_NODBGNM = _ida_name.GNCN_NODBGNM
r"""
don't use debug names
"""

GNCN_PREFDBG = _ida_name.GNCN_PREFDBG
r"""
if using debug names, prefer debug names over function names
"""


def append_struct_fields(*args):
    r"""
    append_struct_fields(disp, n, path, flags, delta, appzero) -> str
    Append names of struct fields to a name if the name is a struct name.

    @param disp: (C++: adiff_t *) displacement from the name
    @param n: (C++: int) number of operand n which the name appears
    @param path: (C++: const tid_t *) path in the struct. path is an array of id's. maximal length of
                 array is MAXSTRUCPATH. the first element of the array is the
                 structure id. consecutive elements are id's of used union members
                 (if any).
    @param flags: (C++: flags_t) the input flags. they will be returned if the struct cannot be
                  found.
    @param delta: (C++: adiff_t) delta to add to displacement
    @param appzero: (C++: bool) should append a struct field name if the displacement is zero?
    @return: flags of the innermost struct member or the input flags
    """
    return _ida_name.append_struct_fields(*args)

def is_public_name(*args):
    r"""
    is_public_name(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.is_public_name(*args)

def make_name_public(*args):
    r"""
    make_name_public(ea)

    @param ea: ea_t
    """
    return _ida_name.make_name_public(*args)

def make_name_non_public(*args):
    r"""
    make_name_non_public(ea)

    @param ea: ea_t
    """
    return _ida_name.make_name_non_public(*args)

def is_weak_name(*args):
    r"""
    is_weak_name(ea) -> bool

    @param ea: ea_t
    """
    return _ida_name.is_weak_name(*args)

def make_name_weak(*args):
    r"""
    make_name_weak(ea)

    @param ea: ea_t
    """
    return _ida_name.make_name_weak(*args)

def make_name_non_weak(*args):
    r"""
    make_name_non_weak(ea)

    @param ea: ea_t
    """
    return _ida_name.make_name_non_weak(*args)

def get_nlist_size(*args):
    r"""
    get_nlist_size() -> size_t
    Get number of names in the list.
    """
    return _ida_name.get_nlist_size(*args)

def get_nlist_idx(*args):
    r"""
    get_nlist_idx(ea) -> size_t
    Get index of the name in the list
    @warning: returns the closest match. may return idx >= size.

    @param ea: (C++: ea_t)
    """
    return _ida_name.get_nlist_idx(*args)

def is_in_nlist(*args):
    r"""
    is_in_nlist(ea) -> bool
    Is the name included into the name list?

    @param ea: (C++: ea_t)
    """
    return _ida_name.is_in_nlist(*args)

def get_nlist_ea(*args):
    r"""
    get_nlist_ea(idx) -> ea_t
    Get address from the list at 'idx'.

    @param idx: (C++: size_t)
    """
    return _ida_name.get_nlist_ea(*args)

def get_nlist_name(*args):
    r"""
    get_nlist_name(idx) -> char const *
    Get name using idx.

    @param idx: (C++: size_t)
    """
    return _ida_name.get_nlist_name(*args)

def rebuild_nlist(*args):
    r"""
    rebuild_nlist()
    Rebuild the name list.
    """
    return _ida_name.rebuild_nlist(*args)

def reorder_dummy_names(*args):
    r"""
    reorder_dummy_names()
    Renumber dummy names.
    """
    return _ida_name.reorder_dummy_names(*args)
DEBNAME_EXACT = _ida_name.DEBNAME_EXACT
r"""
find a name at exactly the specified address
"""

DEBNAME_LOWER = _ida_name.DEBNAME_LOWER
r"""
find a name with the address >= the specified address
"""

DEBNAME_UPPER = _ida_name.DEBNAME_UPPER
r"""
find a name with the address > the specified address
"""

DEBNAME_NICE = _ida_name.DEBNAME_NICE
r"""
find a name with the address <= the specified address
"""

class ea_name_t(object):
    r"""
    Proxy of C++ ea_name_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = property(_ida_name.ea_name_t_ea_get, _ida_name.ea_name_t_ea_set, doc=r"""ea""")
    name = property(_ida_name.ea_name_t_name_get, _ida_name.ea_name_t_name_set, doc=r"""name""")

    def __init__(self, *args):
        r"""
        __init__(self) -> ea_name_t
        __init__(self, _ea, _name) -> ea_name_t

        @param _ea: ea_t
        @param _name: qstring const &
        """
        _ida_name.ea_name_t_swiginit(self, _ida_name.new_ea_name_t(*args))
    __swig_destroy__ = _ida_name.delete_ea_name_t

# Register ea_name_t in _ida_name:
_ida_name.ea_name_t_swigregister(ea_name_t)


def set_debug_name(*args):
    r"""
    set_debug_name(ea, name) -> bool

    @param ea: ea_t
    @param name: char const *
    """
    return _ida_name.set_debug_name(*args)

def get_debug_name(*args):
    r"""
    get_debug_name(ea_ptr, how) -> str

    @param ea_ptr: ea_t *
    @param how: enum debug_name_how_t
    """
    return _ida_name.get_debug_name(*args)

def del_debug_names(*args):
    r"""
    del_debug_names(ea1, ea2)

    @param ea1: ea_t
    @param ea2: ea_t
    """
    return _ida_name.del_debug_names(*args)

def get_debug_name_ea(*args):
    r"""
    get_debug_name_ea(name) -> ea_t

    @param name: char const *
    """
    return _ida_name.get_debug_name_ea(*args)
DQT_NPURGED_8 = _ida_name.DQT_NPURGED_8

DQT_NPURGED_4 = _ida_name.DQT_NPURGED_4

DQT_NPURGED_2 = _ida_name.DQT_NPURGED_2

DQT_COMPILER = _ida_name.DQT_COMPILER

DQT_NAME_TYPE = _ida_name.DQT_NAME_TYPE

DQT_FULL = _ida_name.DQT_FULL


def demangle_name(*args):
    r"""
    demangle_name(name, disable_mask, demreq=DQT_FULL) -> str
    Demangle a name.

    @param name: (C++: const char *) char const *
    @param disable_mask: (C++: uint32)
    @param demreq: (C++: demreq_type_t) enum demreq_type_t
    """
    return _ida_name.demangle_name(*args)

def is_name_defined_locally(*args):
    r"""
    is_name_defined_locally(pfn, name, ignore_name_def, ea1=BADADDR, ea2=BADADDR) -> bool
    Is the name defined locally in the specified function?

    @param pfn: (C++: func_t *) pointer to function
    @param name: (C++: const char *) name to check
    @param ignore_name_def: (C++: ignore_name_def_t) which names to ignore when checking
    @param ea1: (C++: ea_t) the starting address of the range inside the function (optional)
    @param ea2: (C++: ea_t) the ending address of the range inside the function (optional)
    @return: true if the name has been defined
    """
    return _ida_name.is_name_defined_locally(*args)

def cleanup_name(*args):
    r"""
    cleanup_name(ea, name, flags=0) -> str

    @param ea: ea_t
    @param name: char const *
    @param flags: uint32
    """
    return _ida_name.cleanup_name(*args)
CN_KEEP_TRAILING__DIGITS = _ida_name.CN_KEEP_TRAILING__DIGITS

ME_INTERR = _ida_name.ME_INTERR

ME_PARAMERR = _ida_name.ME_PARAMERR

ME_ILLSTR = _ida_name.ME_ILLSTR

ME_SMALLANS = _ida_name.ME_SMALLANS

ME_FRAME = _ida_name.ME_FRAME

ME_NOCOMP = _ida_name.ME_NOCOMP

ME_ERRAUTO = _ida_name.ME_ERRAUTO

ME_NOHASHMEM = _ida_name.ME_NOHASHMEM

ME_NOSTRMEM = _ida_name.ME_NOSTRMEM

ME_NOERROR_LIMIT = _ida_name.ME_NOERROR_LIMIT

M_PRCMSK = _ida_name.M_PRCMSK

MT_DEFAULT = _ida_name.MT_DEFAULT

MT_CDECL = _ida_name.MT_CDECL

MT_PASCAL = _ida_name.MT_PASCAL

MT_STDCALL = _ida_name.MT_STDCALL

MT_FASTCALL = _ida_name.MT_FASTCALL

MT_THISCALL = _ida_name.MT_THISCALL

MT_FORTRAN = _ida_name.MT_FORTRAN

MT_SYSCALL = _ida_name.MT_SYSCALL

MT_INTERRUPT = _ida_name.MT_INTERRUPT

MT_MSFASTCALL = _ida_name.MT_MSFASTCALL

MT_CLRCALL = _ida_name.MT_CLRCALL

MT_DMDCALL = _ida_name.MT_DMDCALL

MT_VECTORCALL = _ida_name.MT_VECTORCALL

MT_REGCALL = _ida_name.MT_REGCALL

MT_LOCALNAME = _ida_name.MT_LOCALNAME

M_SAVEREGS = _ida_name.M_SAVEREGS

M_CLASS = _ida_name.M_CLASS

MT_PUBLIC = _ida_name.MT_PUBLIC

MT_PRIVATE = _ida_name.MT_PRIVATE

MT_PROTECT = _ida_name.MT_PROTECT

MT_MEMBER = _ida_name.MT_MEMBER

MT_VTABLE = _ida_name.MT_VTABLE

MT_RTTI = _ida_name.MT_RTTI

M_PARMSK = _ida_name.M_PARMSK

MT_PARSHF = _ida_name.MT_PARSHF

MT_PARMAX = _ida_name.MT_PARMAX

M_ELLIPSIS = _ida_name.M_ELLIPSIS

MT_VOIDARG = _ida_name.MT_VOIDARG

M_STATIC = _ida_name.M_STATIC

M_VIRTUAL = _ida_name.M_VIRTUAL

M_AUTOCRT = _ida_name.M_AUTOCRT

M_TYPMASK = _ida_name.M_TYPMASK

MT_OPERAT = _ida_name.MT_OPERAT

MT_CONSTR = _ida_name.MT_CONSTR

MT_DESTR = _ida_name.MT_DESTR

MT_CASTING = _ida_name.MT_CASTING

MT_CLRCDTOR = _ida_name.MT_CLRCDTOR

M_TRUNCATE = _ida_name.M_TRUNCATE

M_THUNK = _ida_name.M_THUNK

M_ANONNSP = _ida_name.M_ANONNSP

M_TMPLNAM = _ida_name.M_TMPLNAM

M_DBGNAME = _ida_name.M_DBGNAME

M_COMPILER = _ida_name.M_COMPILER

MT_MSCOMP = _ida_name.MT_MSCOMP

MT_BORLAN = _ida_name.MT_BORLAN

MT_WATCOM = _ida_name.MT_WATCOM

MT_OTHER = _ida_name.MT_OTHER

MT_GNU = _ida_name.MT_GNU

MT_GCC3 = _ida_name.MT_GCC3

MT_VISAGE = _ida_name.MT_VISAGE

MNG_PTRMSK = _ida_name.MNG_PTRMSK

MNG_DEFNEAR = _ida_name.MNG_DEFNEAR

MNG_DEFNEARANY = _ida_name.MNG_DEFNEARANY

MNG_DEFFAR = _ida_name.MNG_DEFFAR

MNG_NOPTRTYP16 = _ida_name.MNG_NOPTRTYP16

MNG_DEFHUGE = _ida_name.MNG_DEFHUGE

MNG_DEFPTR64 = _ida_name.MNG_DEFPTR64

MNG_DEFNONE = _ida_name.MNG_DEFNONE

MNG_NOPTRTYP = _ida_name.MNG_NOPTRTYP

MNG_NODEFINIT = _ida_name.MNG_NODEFINIT

MNG_NOUNDERSCORE = _ida_name.MNG_NOUNDERSCORE

MNG_NOTYPE = _ida_name.MNG_NOTYPE

MNG_NORETTYPE = _ida_name.MNG_NORETTYPE

MNG_NOBASEDT = _ida_name.MNG_NOBASEDT

MNG_NOCALLC = _ida_name.MNG_NOCALLC

MNG_NOPOSTFC = _ida_name.MNG_NOPOSTFC

MNG_NOSCTYP = _ida_name.MNG_NOSCTYP

MNG_NOTHROW = _ida_name.MNG_NOTHROW

MNG_NOSTVIR = _ida_name.MNG_NOSTVIR

MNG_NOECSU = _ida_name.MNG_NOECSU

MNG_NOCSVOL = _ida_name.MNG_NOCSVOL

MNG_NOCLOSUR = _ida_name.MNG_NOCLOSUR

MNG_NOUNALG = _ida_name.MNG_NOUNALG

MNG_NOMANAGE = _ida_name.MNG_NOMANAGE

MNG_NOMODULE = _ida_name.MNG_NOMODULE

MNG_SHORT_S = _ida_name.MNG_SHORT_S

MNG_SHORT_U = _ida_name.MNG_SHORT_U

MNG_ZPT_SPACE = _ida_name.MNG_ZPT_SPACE

MNG_DROP_IMP = _ida_name.MNG_DROP_IMP

MNG_IGN_ANYWAY = _ida_name.MNG_IGN_ANYWAY

MNG_IGN_JMP = _ida_name.MNG_IGN_JMP

MNG_MOVE_JMP = _ida_name.MNG_MOVE_JMP

MNG_COMPILER_MSK = _ida_name.MNG_COMPILER_MSK

MNG_SHORT_FORM = _ida_name.MNG_SHORT_FORM

MNG_LONG_FORM = _ida_name.MNG_LONG_FORM

MNG_CALC_VALID = _ida_name.MNG_CALC_VALID


def get_mangled_name_type(*args):
    r"""
    get_mangled_name_type(name) -> mangled_name_type_t

    @param name: char const *
    """
    return _ida_name.get_mangled_name_type(*args)

def get_debug_names(*args):
    r"""
    get_debug_names(names, ea1, ea2)

    @param names: ea_name_vec_t *
    @param ea1: ea_t
    @param ea2: ea_t

    get_debug_names(ea1, ea2, return_list=False) -> dict or None

    @param ea1: ea_t
    @param ea2: ea_t
    @param return_list: bool
    """
    return _ida_name.get_debug_names(*args)

def get_ea_name(*args):
    r"""
    get_ea_name(ea, gtn_flags=0) -> qstring
    Get name at the specified address.

    @param ea: (C++: ea_t) linear address
    @param gtn_flags: (C++: int) how exactly the name should be retrieved. combination of bits
                      for get_ea_name() function. There is a convenience bits
    @return: success
    """
    return _ida_name.get_ea_name(*args)

def validate_name(*args):
    r"""
    validate_name(name, type, flags=0) -> PyObject *
    Validate a name. This function replaces all invalid characters in the name with
    SUBSTCHAR. However, it will return false if name is valid but not allowed to be
    an identifier (is a register name).

    @param name: (C++: qstring *) ptr to name. the name will be modified
    @param type: (C++: nametype_t) the type of name we want to validate
    @param flags: (C++: int) see SN_* . Only SN_IDBENC is currently considered
    @return: success
    """
    return _ida_name.validate_name(*args)

#<pycode(py_name)>
import _ida_idaapi
import _ida_funcs
import bisect


class NearestName(object):
    r"""
    Utility class to help find the nearest name in a given ea/name dictionary
    """
    def __init__(self, ea_names):
        self.update(ea_names)


    def update(self, ea_names):
        r"""
        Updates the ea/names map
        """
        self._names = ea_names
        self._addrs = list(ea_names.keys())
        self._addrs.sort()


    def find(self, ea):
        r"""
        Returns a tupple (ea, name, pos) that is the nearest to the passed ea
        If no name is matched then None is returned
        """
        pos = bisect.bisect_left(self._addrs, ea)
# no match
        if pos >= len(self._addrs):
            return None
# exact match?
        if self._addrs[pos] != ea:
            pos -= 1 # go to previous element
        if pos < 0:
            return None
        return self[pos]


    def _get_item(self, index):
        ea = self._addrs[index]
        return (ea, self._names[ea], index)


    def __iter__(self):
        return (self._get_item(index) for index in range(0, len(self._addrs)))


    def __getitem__(self, index):
        r"""
        Returns the tupple (ea, name, index)
        """
        if index > len(self._addrs):
            raise StopIteration
        return self._get_item(index)

def calc_gtn_flags(fromaddr, ea):
    r"""
    Calculate flags for get_ea_name() function

    @param fromaddr: the referring address. May be BADADDR.
    @param ea: linear address

    @return: flags
    """
    gtn_flags = 0
    if fromaddr != _ida_idaapi.BADADDR:
        pfn = _ida_funcs.get_func(fromaddr)
        if _ida_funcs.func_contains(pfn, ea):
            gtn_flags = GN_LOCAL
    return gtn_flags

#</pycode(py_name)>


cvar = _ida_name.cvar
ignore_none = cvar.ignore_none
ignore_regvar = cvar.ignore_regvar
ignore_llabel = cvar.ignore_llabel
ignore_stkvar = cvar.ignore_stkvar
ignore_glabel = cvar.ignore_glabel
MANGLED_CODE = cvar.MANGLED_CODE
MANGLED_DATA = cvar.MANGLED_DATA
MANGLED_UNKNOWN = cvar.MANGLED_UNKNOWN


