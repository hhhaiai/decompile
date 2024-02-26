"""
Routines to manipulate function stack frames, stack variables, register
variables and local labels.

The frame is represented as a structure:
+------------------------------------------------+
  | function arguments                             |
  +------------------------------------------------+
  | return address (isn't stored in func_t)        |
  +------------------------------------------------+
  | saved registers (SI, DI, etc - func_t::frregs) |
  +------------------------------------------------+ <- typical BP
  |                                                |  |
  |                                                |  | func_t::fpd
  |                                                |  |
  |                                                | <- real BP
  | local variables (func_t::frsize)               |
  |                                                |
  |                                                |
  +------------------------------------------------+ <- SP

To access the structure of a function frame, use:
* get_struc() (use func_t::frame as structure ID)
* get_frame(const func_t *pfn)
* get_frame(ea_t ea)"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_frame
else:
    import _ida_frame

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

SWIG_PYTHON_LEGACY_BOOL = _ida_frame.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
class xreflist_t(object):
    r"""
    Proxy of C++ qvector< xreflist_entry_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> xreflist_t
        __init__(self, x) -> xreflist_t

        @param x: qvector< xreflist_entry_t > const &
        """
        _ida_frame.xreflist_t_swiginit(self, _ida_frame.new_xreflist_t(*args))
    __swig_destroy__ = _ida_frame.delete_xreflist_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: xreflist_entry_t const &

        push_back(self) -> xreflist_entry_t
        """
        return _ida_frame.xreflist_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_frame.xreflist_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_frame.xreflist_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_frame.xreflist_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> xreflist_entry_t

        @param _idx: size_t
        """
        return _ida_frame.xreflist_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_frame.xreflist_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_frame.xreflist_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: xreflist_entry_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_frame.xreflist_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=xreflist_entry_t())

        @param x: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_frame.xreflist_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_frame.xreflist_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_frame.xreflist_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< xreflist_entry_t > &
        """
        return _ida_frame.xreflist_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> xreflist_entry_t
        """
        return _ida_frame.xreflist_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: xreflist_entry_t *
        @param len: size_t
        """
        return _ida_frame.xreflist_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< xreflist_entry_t > const &
        """
        return _ida_frame.xreflist_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< xreflist_entry_t > const &
        """
        return _ida_frame.xreflist_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> xreflist_entry_t
        """
        return _ida_frame.xreflist_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> xreflist_entry_t
        """
        return _ida_frame.xreflist_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> xreflist_entry_t

        @param it: qvector< xreflist_entry_t >::iterator
        @param x: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> xreflist_entry_t

        @param it: qvector< xreflist_entry_t >::iterator

        erase(self, first, last) -> xreflist_entry_t

        @param first: qvector< xreflist_entry_t >::iterator
        @param last: qvector< xreflist_entry_t >::iterator
        """
        return _ida_frame.xreflist_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> xreflist_entry_t

        @param x: xreflist_entry_t const &

        """
        return _ida_frame.xreflist_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: xreflist_entry_t const &

        """
        return _ida_frame.xreflist_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_frame.xreflist_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> xreflist_entry_t

        @param i: size_t
        """
        return _ida_frame.xreflist_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register xreflist_t in _ida_frame:
_ida_frame.xreflist_t_swigregister(xreflist_t)


def get_stkvar(*args):
    r"""
    get_stkvar(insn, op, v) -> (member_t, int) or None
    Get pointer to stack variable

    @param insn: an ida_ua.insn_t, or an address (C++: const insn_t &)
    @param op: reference to instruction operand
    @param v: immediate value in the operand (usually op.addr)
    @return:     - None on failure
        - tuple(member_t, actval)
          where actval: actual value used to fetch stack variable
    """
    return _ida_frame.get_stkvar(*args)

def is_funcarg_off(*args):
    r"""
    is_funcarg_off(pfn, frameoff) -> bool

    @param pfn: func_t const *
    @param frameoff: uval_t
    """
    return _ida_frame.is_funcarg_off(*args)

def lvar_off(*args):
    r"""
    lvar_off(pfn, frameoff) -> sval_t

    @param pfn: func_t const *
    @param frameoff: uval_t
    """
    return _ida_frame.lvar_off(*args)
class stkpnt_t(object):
    r"""
    Proxy of C++ stkpnt_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = property(_ida_frame.stkpnt_t_ea_get, _ida_frame.stkpnt_t_ea_set, doc=r"""ea""")
    spd = property(_ida_frame.stkpnt_t_spd_get, _ida_frame.stkpnt_t_spd_set, doc=r"""spd""")

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: stkpnt_t const &
        """
        return _ida_frame.stkpnt_t_compare(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> stkpnt_t
        """
        _ida_frame.stkpnt_t_swiginit(self, _ida_frame.new_stkpnt_t(*args))
    __swig_destroy__ = _ida_frame.delete_stkpnt_t

# Register stkpnt_t in _ida_frame:
_ida_frame.stkpnt_t_swigregister(stkpnt_t)

class stkpnts_t(object):
    r"""
    Proxy of C++ stkpnts_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: stkpnts_t const &
        """
        return _ida_frame.stkpnts_t_compare(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> stkpnts_t
        """
        _ida_frame.stkpnts_t_swiginit(self, _ida_frame.new_stkpnts_t(*args))
    __swig_destroy__ = _ida_frame.delete_stkpnts_t

# Register stkpnts_t in _ida_frame:
_ida_frame.stkpnts_t_swigregister(stkpnts_t)


def add_frame(*args):
    r"""
    add_frame(pfn, frsize, frregs, argsize) -> bool
    Add function frame.

    @param pfn: (C++: func_t *) pointer to function structure
    @param frsize: (C++: sval_t) size of function local variables
    @param frregs: (C++: ushort) size of saved registers
    @param argsize: (C++: asize_t) size of function arguments range which will be purged upon
                    return. this parameter is used for __stdcall and __pascal
                    calling conventions. for other calling conventions please pass
                    0.
    @retval 1: ok
    @retval 0: failed (no function, frame already exists)
    """
    return _ida_frame.add_frame(*args)

def del_frame(*args):
    r"""
    del_frame(pfn) -> bool
    Delete a function frame.

    @param pfn: (C++: func_t *) pointer to function structure
    @return: success
    """
    return _ida_frame.del_frame(*args)

def set_frame_size(*args):
    r"""
    set_frame_size(pfn, frsize, frregs, argsize) -> bool
    Set size of function frame. Note: The returned size may not include all stack
    arguments. It does so only for __stdcall and __fastcall calling conventions. To
    get the entire frame size for all cases use get_struc_size(get_frame(pfn)).

    @param pfn: (C++: func_t *) pointer to function structure
    @param frsize: (C++: asize_t) size of function local variables
    @param frregs: (C++: ushort) size of saved registers
    @param argsize: (C++: asize_t) size of function arguments that will be purged from the stack
                    upon return
    @return: success
    """
    return _ida_frame.set_frame_size(*args)

def get_frame_size(*args):
    r"""
    get_frame_size(pfn) -> asize_t
    Get full size of a function frame. This function takes into account size of
    local variables + size of saved registers + size of return address + number of
    purged bytes. The purged bytes correspond to the arguments of the functions with
    __stdcall and __fastcall calling conventions.

    @param pfn: (C++: const func_t *) pointer to function structure, may be nullptr
    @return: size of frame in bytes or zero
    """
    return _ida_frame.get_frame_size(*args)

def get_frame_retsize(*args):
    r"""
    get_frame_retsize(pfn) -> int
    Get size of function return address.

    @param pfn: (C++: const func_t *) pointer to function structure, can't be nullptr
    """
    return _ida_frame.get_frame_retsize(*args)
FPC_ARGS = _ida_frame.FPC_ARGS

FPC_RETADDR = _ida_frame.FPC_RETADDR

FPC_SAVREGS = _ida_frame.FPC_SAVREGS

FPC_LVARS = _ida_frame.FPC_LVARS


def get_frame_part(*args):
    r"""
    get_frame_part(range, pfn, part)
    Get offsets of the frame part in the frame.

    @param range: (C++: range_t *) pointer to the output buffer with the frame part
                  start/end(exclusive) offsets, can't be nullptr
    @param pfn: (C++: const func_t *) pointer to function structure, can't be nullptr
    @param part: (C++: frame_part_t) frame part
    """
    return _ida_frame.get_frame_part(*args)

def frame_off_args(*args):
    r"""
    frame_off_args(pfn) -> ea_t
    Get starting address of arguments section.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_frame.frame_off_args(*args)

def frame_off_retaddr(*args):
    r"""
    frame_off_retaddr(pfn) -> ea_t
    Get starting address of return address section.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_frame.frame_off_retaddr(*args)

def frame_off_savregs(*args):
    r"""
    frame_off_savregs(pfn) -> ea_t
    Get starting address of saved registers section.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_frame.frame_off_savregs(*args)

def frame_off_lvars(*args):
    r"""
    frame_off_lvars(pfn) -> ea_t
    Get start address of local variables section.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_frame.frame_off_lvars(*args)

def get_frame(*args):
    r"""
    get_frame(pfn) -> struc_t
    Get pointer to function frame.

    @param pfn: func_t const *

    get_frame(ea) -> struc_t *

    @param ea: ea_t
    """
    return _ida_frame.get_frame(*args)

def soff_to_fpoff(*args):
    r"""
    soff_to_fpoff(pfn, soff) -> sval_t
    Convert struct offsets into fp-relative offsets. This function converts the
    offsets inside the struc_t object into the frame pointer offsets (for example,
    EBP-relative).

    @param pfn: (C++: func_t *)
    @param soff: (C++: uval_t)
    """
    return _ida_frame.soff_to_fpoff(*args)

def update_fpd(*args):
    r"""
    update_fpd(pfn, fpd) -> bool
    Update frame pointer delta.

    @param pfn: (C++: func_t *) pointer to function structure
    @param fpd: (C++: asize_t) new fpd value. cannot be bigger than the local variable range size.
    @return: success
    """
    return _ida_frame.update_fpd(*args)

def set_purged(*args):
    r"""
    set_purged(ea, nbytes, override_old_value) -> bool
    Set the number of purged bytes for a function or data item (funcptr). This
    function will update the database and plan to reanalyze items referencing the
    specified address. It works only for processors with PR_PURGING bit in 16 and 32
    bit modes.

    @param ea: (C++: ea_t) address of the function of item
    @param nbytes: (C++: int) number of purged bytes
    @param override_old_value: (C++: bool) may overwrite old information about purged bytes
    @return: success
    """
    return _ida_frame.set_purged(*args)

def get_func_by_frame(*args):
    r"""
    get_func_by_frame(frame_id) -> ea_t
    Get function by its frame id.
    @warning: this function works only with databases created by IDA > 5.6

    @param frame_id: (C++: tid_t) id of the function frame
    @return: start address of the function or BADADDR
    """
    return _ida_frame.get_func_by_frame(*args)
STKVAR_VALID_SIZE = _ida_frame.STKVAR_VALID_SIZE
r"""
x.dtyp contains correct variable type (for insns like 'lea' this bit must be
off). In general, dr_O references do not allow to determine the variable size
"""


def define_stkvar(*args):
    r"""
    define_stkvar(pfn, name, off, flags, ti, nbytes) -> bool
    Define/redefine a stack variable.

    @param pfn: (C++: func_t *) pointer to function
    @param name: (C++: const char *) variable name, nullptr means autogenerate a name
    @param off: (C++: sval_t) offset of the stack variable in the frame. negative values denote
                local variables, positive - function arguments.
    @param flags: (C++: flags_t) variable type flags (byte_flag() for a byte variable, for example)
    @param ti: (C++: const opinfo_t *) additional type information (like offsets, structs, etc)
    @param nbytes: (C++: asize_t) number of bytes occupied by the variable
    @return: success
    """
    return _ida_frame.define_stkvar(*args)

def build_stkvar_name(*args):
    r"""
    build_stkvar_name(pfn, v) -> str
    Build automatic stack variable name.

    @param pfn: (C++: const func_t *) pointer to function (can't be nullptr!)
    @param v: (C++: sval_t) value of variable offset
    @return: length of stack variable name or -1
    """
    return _ida_frame.build_stkvar_name(*args)

def calc_stkvar_struc_offset(*args):
    r"""
    calc_stkvar_struc_offset(pfn, insn, n) -> ea_t
    Calculate offset of stack variable in the frame structure.

    @param pfn: (C++: func_t *) pointer to function (can't be nullptr!)
    @param insn: (C++: const insn_t &) the instruction
    @param n: (C++: int) number of operand: (0..UA_MAXOP-1) -1 if error, return BADADDR
    @return: BADADDR if some error (issue a warning if stack frame is bad)
    """
    return _ida_frame.calc_stkvar_struc_offset(*args)

def free_regvar(*args):
    r"""
    free_regvar(v)

    @param v: regvar_t *
    """
    return _ida_frame.free_regvar(*args)
class regvar_t(ida_range.range_t):
    r"""
    Proxy of C++ regvar_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    canon = property(_ida_frame.regvar_t_canon_get, _ida_frame.regvar_t_canon_set, doc=r"""canon""")
    r"""
    canonical register name (case-insensitive)
    """
    user = property(_ida_frame.regvar_t_user_get, _ida_frame.regvar_t_user_set, doc=r"""user""")
    r"""
    user-defined register name
    """
    cmt = property(_ida_frame.regvar_t_cmt_get, _ida_frame.regvar_t_cmt_set, doc=r"""cmt""")
    r"""
    comment to appear near definition
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> regvar_t
        __init__(self, r) -> regvar_t

        @param r: regvar_t const &
        """
        _ida_frame.regvar_t_swiginit(self, _ida_frame.new_regvar_t(*args))
    __swig_destroy__ = _ida_frame.delete_regvar_t

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: regvar_t &
        """
        return _ida_frame.regvar_t_swap(self, *args)

# Register regvar_t in _ida_frame:
_ida_frame.regvar_t_swigregister(regvar_t)


def add_regvar(*args):
    r"""
    add_regvar(pfn, ea1, ea2, canon, user, cmt) -> int
    Define a register variable.

    @param pfn: (C++: func_t *) function in which the definition will be created
    @param ea1: (C++: ea_t) ,ea2: range of addresses within the function where the definition will
                    be used
    @param canon: (C++: const char *) name of a general register
    @param canon: (C++: const char *) name of a general register
    @param user: (C++: const char *) user-defined name for the register
    @param cmt: (C++: const char *) comment for the definition
    @return: Register variable error codes
    """
    return _ida_frame.add_regvar(*args)
REGVAR_ERROR_OK = _ida_frame.REGVAR_ERROR_OK
r"""
all ok
"""

REGVAR_ERROR_ARG = _ida_frame.REGVAR_ERROR_ARG
r"""
function arguments are bad
"""

REGVAR_ERROR_RANGE = _ida_frame.REGVAR_ERROR_RANGE
r"""
the definition range is bad
"""

REGVAR_ERROR_NAME = _ida_frame.REGVAR_ERROR_NAME
r"""
the provided name(s) can't be accepted
"""


def find_regvar(*args):
    r"""
    find_regvar(pfn, ea1, ea2, canon, user) -> regvar_t
    Find a register variable definition.

    @param pfn: (C++: func_t *) function in question
    @param ea1: ea_t
    @param canon: (C++: const char *) name of a general register
    @param canon: (C++: const char *) name of a general register
    @param user: char const *

    @return: nullptr-not found, otherwise ptr to regvar_t
    find_regvar(pfn, ea, canon) -> regvar_t

    @param pfn: func_t *
    @param ea: ea_t
    @param canon: char const *
    """
    return _ida_frame.find_regvar(*args)

def has_regvar(*args):
    r"""
    has_regvar(pfn, ea) -> bool
    Is there a register variable definition?

    @param pfn: (C++: func_t *) function in question
    @param ea: (C++: ea_t) current address
    """
    return _ida_frame.has_regvar(*args)

def rename_regvar(*args):
    r"""
    rename_regvar(pfn, v, user) -> int
    Rename a register variable.

    @param pfn: (C++: func_t *) function in question
    @param v: (C++: regvar_t *) variable to rename
    @param user: (C++: const char *) new user-defined name for the register
    @return: Register variable error codes
    """
    return _ida_frame.rename_regvar(*args)

def set_regvar_cmt(*args):
    r"""
    set_regvar_cmt(pfn, v, cmt) -> int
    Set comment for a register variable.

    @param pfn: (C++: func_t *) function in question
    @param v: (C++: regvar_t *) variable to rename
    @param cmt: (C++: const char *) new comment
    @return: Register variable error codes
    """
    return _ida_frame.set_regvar_cmt(*args)

def del_regvar(*args):
    r"""
    del_regvar(pfn, ea1, ea2, canon) -> int
    Delete a register variable definition.

    @param pfn: (C++: func_t *) function in question
    @param ea1: (C++: ea_t) ,ea2: range of addresses within the function where the definition
                    holds
    @param canon: (C++: const char *) name of a general register
    @param canon: (C++: const char *) name of a general register
    @return: Register variable error codes
    """
    return _ida_frame.del_regvar(*args)

def add_auto_stkpnt(*args):
    r"""
    add_auto_stkpnt(pfn, ea, delta) -> bool
    Add automatic SP register change point.

    @param pfn: (C++: func_t *) pointer to function. may be nullptr.
    @param ea: (C++: ea_t) linear address where SP changes. usually this is the end of the
               instruction which modifies the stack pointer ( insn_t::ea+
               insn_t::size)
    @param delta: (C++: sval_t) difference between old and new values of SP
    @return: success
    """
    return _ida_frame.add_auto_stkpnt(*args)

def add_user_stkpnt(*args):
    r"""
    add_user_stkpnt(ea, delta) -> bool
    Add user-defined SP register change point.

    @param ea: (C++: ea_t) linear address where SP changes
    @param delta: (C++: sval_t) difference between old and new values of SP
    @return: success
    """
    return _ida_frame.add_user_stkpnt(*args)

def del_stkpnt(*args):
    r"""
    del_stkpnt(pfn, ea) -> bool
    Delete SP register change point.

    @param pfn: (C++: func_t *) pointer to function. may be nullptr.
    @param ea: (C++: ea_t) linear address
    @return: success
    """
    return _ida_frame.del_stkpnt(*args)

def get_spd(*args):
    r"""
    get_spd(pfn, ea) -> sval_t
    Get difference between the initial and current values of ESP.

    @param pfn: (C++: func_t *) pointer to function. may be nullptr.
    @param ea: (C++: ea_t) linear address of an instruction
    @return: 0 or the difference, usually a negative number. returns the sp-diff
             before executing the instruction.
    """
    return _ida_frame.get_spd(*args)

def get_effective_spd(*args):
    r"""
    get_effective_spd(pfn, ea) -> sval_t
    Get effective difference between the initial and current values of ESP. This
    function returns the sp-diff used by the instruction. The difference between
    get_spd() and get_effective_spd() is present only for instructions like "pop
    [esp+N]": they modify sp and use the modified value.

    @param pfn: (C++: func_t *) pointer to function. may be nullptr.
    @param ea: (C++: ea_t) linear address
    @return: 0 or the difference, usually a negative number
    """
    return _ida_frame.get_effective_spd(*args)

def get_sp_delta(*args):
    r"""
    get_sp_delta(pfn, ea) -> sval_t
    Get modification of SP made at the specified location

    @param pfn: (C++: func_t *) pointer to function. may be nullptr.
    @param ea: (C++: ea_t) linear address
    @return: 0 if the specified location doesn't contain a SP change point.
             otherwise return delta of SP modification.
    """
    return _ida_frame.get_sp_delta(*args)

def recalc_spd(*args):
    r"""
    recalc_spd(cur_ea) -> bool
    Recalculate SP delta for an instruction that stops execution. The next
    instruction is not reached from the current instruction. We need to recalculate
    SP for the next instruction.

    This function will create a new automatic SP register change point if necessary.
    It should be called from the emulator (emu.cpp) when auto_state == AU_USED if
    the current instruction doesn't pass the execution flow to the next instruction.

    @param cur_ea: (C++: ea_t) linear address of the current instruction
    @retval 1: new stkpnt is added
    @retval 0: nothing is changed
    """
    return _ida_frame.recalc_spd(*args)
class xreflist_entry_t(object):
    r"""
    Proxy of C++ xreflist_entry_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ea = property(_ida_frame.xreflist_entry_t_ea_get, _ida_frame.xreflist_entry_t_ea_set, doc=r"""ea""")
    r"""
    Location of the insn referencing the stack frame member.
    """
    opnum = property(_ida_frame.xreflist_entry_t_opnum_get, _ida_frame.xreflist_entry_t_opnum_set, doc=r"""opnum""")
    r"""
    Number of the operand of that instruction.
    """
    type = property(_ida_frame.xreflist_entry_t_type_get, _ida_frame.xreflist_entry_t_type_set, doc=r"""type""")
    r"""
    The type of xref (cref_t & dref_t)
    """

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___ne__(self, *args)

    def __lt__(self, *args):
        r"""
        __lt__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___lt__(self, *args)

    def __gt__(self, *args):
        r"""
        __gt__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___gt__(self, *args)

    def __le__(self, *args):
        r"""
        __le__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___le__(self, *args)

    def __ge__(self, *args):
        r"""
        __ge__(self, r) -> bool

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t___ge__(self, *args)

    def compare(self, *args):
        r"""
        compare(self, r) -> int

        @param r: xreflist_entry_t const &
        """
        return _ida_frame.xreflist_entry_t_compare(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> xreflist_entry_t
        """
        _ida_frame.xreflist_entry_t_swiginit(self, _ida_frame.new_xreflist_entry_t(*args))
    __swig_destroy__ = _ida_frame.delete_xreflist_entry_t

# Register xreflist_entry_t in _ida_frame:
_ida_frame.xreflist_entry_t_swigregister(xreflist_entry_t)


def build_stkvar_xrefs(*args):
    r"""
    build_stkvar_xrefs(out, pfn, mptr)
    Fill 'out' with a list of all the xrefs made from function 'pfn', to the
    argument or variable 'mptr' in 'pfn's stack frame.

    @param out: (C++: xreflist_t *) the list of xrefs to fill.
    @param pfn: (C++: func_t *) the function to scan.
    @param mptr: (C++: const member_t *) the argument/variable in pfn's stack frame.
    """
    return _ida_frame.build_stkvar_xrefs(*args)

def get_min_spd_ea(*args):
    r"""
    get_min_spd_ea(pfn) -> ea_t

    @param pfn: func_t *
    """
    return _ida_frame.get_min_spd_ea(*args)

def delete_unreferenced_stkvars(*args):
    r"""
    delete_unreferenced_stkvars(pfn) -> int

    @param pfn: func_t *
    """
    return _ida_frame.delete_unreferenced_stkvars(*args)

def delete_wrong_stkvar_ops(*args):
    r"""
    delete_wrong_stkvar_ops(pfn) -> int

    @param pfn: func_t *
    """
    return _ida_frame.delete_wrong_stkvar_ops(*args)



