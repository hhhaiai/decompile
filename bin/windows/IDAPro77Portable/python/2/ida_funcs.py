"""
Routines for working with functions within the disassembled program.

This file also contains routines for working with library signatures (e.g.
FLIRT).

Each function consists of function chunks. At least one function chunk must be
present in the function definition - the function entry chunk. Other chunks are
called function tails. There may be several of them for a function.

A function tail is a continuous range of addresses. It can be used in the
definition of one or more functions. One function using the tail is singled out
and called the tail owner. This function is considered as 'possessing' the tail.
get_func() on a tail address will return the function possessing the tail. You
can enumerate the functions using the tail by using func_parent_iterator_t.

Each function chunk in the disassembly is represented as an "range" (a range of
addresses, see range.hpp for details) with characteristics.

A function entry must start with an instruction (code) byte."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_funcs
else:
    import _ida_funcs

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

SWIG_PYTHON_LEGACY_BOOL = _ida_funcs.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
class dyn_stkpnt_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< stkpnt_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = property(_ida_funcs.dyn_stkpnt_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.dyn_stkpnt_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_stkpnt_array

        @param _data: stkpnt_t *
        @param _count: size_t
        """
        _ida_funcs.dyn_stkpnt_array_swiginit(self, _ida_funcs.new_dyn_stkpnt_array(*args))

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_funcs.dyn_stkpnt_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> stkpnt_t const &

        @param i: size_t
        """
        return _ida_funcs.dyn_stkpnt_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: stkpnt_t const &
        """
        return _ida_funcs.dyn_stkpnt_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_dyn_stkpnt_array

# Register dyn_stkpnt_array in _ida_funcs:
_ida_funcs.dyn_stkpnt_array_swigregister(dyn_stkpnt_array)

class dyn_regvar_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< regvar_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = property(_ida_funcs.dyn_regvar_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.dyn_regvar_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_regvar_array

        @param _data: regvar_t *
        @param _count: size_t
        """
        _ida_funcs.dyn_regvar_array_swiginit(self, _ida_funcs.new_dyn_regvar_array(*args))

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_funcs.dyn_regvar_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> regvar_t const &

        @param i: size_t
        """
        return _ida_funcs.dyn_regvar_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: regvar_t const &
        """
        return _ida_funcs.dyn_regvar_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_dyn_regvar_array

# Register dyn_regvar_array in _ida_funcs:
_ida_funcs.dyn_regvar_array_swigregister(dyn_regvar_array)

class dyn_range_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< range_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = property(_ida_funcs.dyn_range_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.dyn_range_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_range_array

        @param _data: range_t *
        @param _count: size_t
        """
        _ida_funcs.dyn_range_array_swiginit(self, _ida_funcs.new_dyn_range_array(*args))

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_funcs.dyn_range_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> range_t

        @param i: size_t
        """
        return _ida_funcs.dyn_range_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: range_t const &
        """
        return _ida_funcs.dyn_range_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_dyn_range_array

# Register dyn_range_array in _ida_funcs:
_ida_funcs.dyn_range_array_swigregister(dyn_range_array)

class dyn_ea_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< ea_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = property(_ida_funcs.dyn_ea_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.dyn_ea_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_ea_array

        @param _data: unsigned long long *
        @param _count: size_t
        """
        _ida_funcs.dyn_ea_array_swiginit(self, _ida_funcs.new_dyn_ea_array(*args))

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_funcs.dyn_ea_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> unsigned long long const &

        @param i: size_t
        """
        return _ida_funcs.dyn_ea_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: unsigned long long const &
        """
        return _ida_funcs.dyn_ea_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_dyn_ea_array

# Register dyn_ea_array in _ida_funcs:
_ida_funcs.dyn_ea_array_swigregister(dyn_ea_array)

class dyn_regarg_array(object):
    r"""
    Proxy of C++ dynamic_wrapped_array_t< regarg_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    data = property(_ida_funcs.dyn_regarg_array_data_get, doc=r"""data""")
    count = property(_ida_funcs.dyn_regarg_array_count_get, doc=r"""count""")

    def __init__(self, *args):
        r"""
        __init__(self, _data, _count) -> dyn_regarg_array

        @param _data: regarg_t *
        @param _count: size_t
        """
        _ida_funcs.dyn_regarg_array_swiginit(self, _ida_funcs.new_dyn_regarg_array(*args))

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_funcs.dyn_regarg_array___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> regarg_t

        @param i: size_t
        """
        return _ida_funcs.dyn_regarg_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: regarg_t const &
        """
        return _ida_funcs.dyn_regarg_array___setitem__(self, *args)

    __iter__ = ida_idaapi._bounded_getitem_iterator

    __swig_destroy__ = _ida_funcs.delete_dyn_regarg_array

# Register dyn_regarg_array in _ida_funcs:
_ida_funcs.dyn_regarg_array_swigregister(dyn_regarg_array)


def free_regarg(*args):
    r"""
    free_regarg(v)

    @param v: regarg_t *
    """
    return _ida_funcs.free_regarg(*args)
class regarg_t(object):
    r"""
    Proxy of C++ regarg_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    reg = property(_ida_funcs.regarg_t_reg_get, _ida_funcs.regarg_t_reg_set, doc=r"""reg""")
    type = property(_ida_funcs.regarg_t_type_get, _ida_funcs.regarg_t_type_set, doc=r"""type""")
    name = property(_ida_funcs.regarg_t_name_get, _ida_funcs.regarg_t_name_set, doc=r"""name""")

    def __init__(self, *args):
        r"""
        __init__(self) -> regarg_t
        __init__(self, r) -> regarg_t

        @param r: regarg_t const &
        """
        _ida_funcs.regarg_t_swiginit(self, _ida_funcs.new_regarg_t(*args))
    __swig_destroy__ = _ida_funcs.delete_regarg_t

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: regarg_t &
        """
        return _ida_funcs.regarg_t_swap(self, *args)

# Register regarg_t in _ida_funcs:
_ida_funcs.regarg_t_swigregister(regarg_t)

class func_t(ida_range.range_t):
    r"""
    Proxy of C++ func_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    flags = property(_ida_funcs.func_t_flags_get, _ida_funcs.func_t_flags_set, doc=r"""flags""")
    r"""
    Function flags
    """

    def is_far(self, *args):
        r"""
        is_far(self) -> bool
        Is a far function?
        """
        return _ida_funcs.func_t_is_far(self, *args)

    def does_return(self, *args):
        r"""
        does_return(self) -> bool
        Does function return?
        """
        return _ida_funcs.func_t_does_return(self, *args)

    def analyzed_sp(self, *args):
        r"""
        analyzed_sp(self) -> bool
        Has SP-analysis been performed?
        """
        return _ida_funcs.func_t_analyzed_sp(self, *args)

    def need_prolog_analysis(self, *args):
        r"""
        need_prolog_analysis(self) -> bool
        Needs prolog analysis?
        """
        return _ida_funcs.func_t_need_prolog_analysis(self, *args)
    frame = property(_ida_funcs.func_t_frame_get, _ida_funcs.func_t_frame_set, doc=r"""frame""")
    r"""
    netnode id of frame structure - see frame.hpp
    """
    frsize = property(_ida_funcs.func_t_frsize_get, _ida_funcs.func_t_frsize_set, doc=r"""frsize""")
    r"""
    size of local variables part of frame in bytes. If FUNC_FRAME is set and fpd==0,
    the frame pointer (EBP) is assumed to point to the top of the local variables
    range.
    """
    frregs = property(_ida_funcs.func_t_frregs_get, _ida_funcs.func_t_frregs_set, doc=r"""frregs""")
    r"""
    size of saved registers in frame. This range is immediately above the local
    variables range.
    """
    argsize = property(_ida_funcs.func_t_argsize_get, _ida_funcs.func_t_argsize_set, doc=r"""argsize""")
    r"""
    number of bytes purged from the stack upon returning
    """
    fpd = property(_ida_funcs.func_t_fpd_get, _ida_funcs.func_t_fpd_set, doc=r"""fpd""")
    r"""
    frame pointer delta. (usually 0, i.e. realBP==typicalBP) use update_fpd() to
    modify it.
    """
    color = property(_ida_funcs.func_t_color_get, _ida_funcs.func_t_color_set, doc=r"""color""")
    r"""
    user defined function color
    """
    pntqty = property(_ida_funcs.func_t_pntqty_get, _ida_funcs.func_t_pntqty_set, doc=r"""pntqty""")
    r"""
    number of SP change points
    """
    points = property(_ida_funcs.func_t_points_get, _ida_funcs.func_t_points_set, doc=r"""points""")
    r"""
    array of SP change points. use ...stkpnt...() functions to access this array.
    """
    regvarqty = property(_ida_funcs.func_t_regvarqty_get, _ida_funcs.func_t_regvarqty_set, doc=r"""regvarqty""")
    r"""
    number of register variables (-1-not read in yet) use find_regvar() to read
    register variables
    """
    regvars = property(_ida_funcs.func_t_regvars_get, _ida_funcs.func_t_regvars_set, doc=r"""regvars""")
    r"""
    array of register variables. this array is sorted by: start_ea. use
    ...regvar...() functions to access this array.
    """
    regargqty = property(_ida_funcs.func_t_regargqty_get, _ida_funcs.func_t_regargqty_set, doc=r"""regargqty""")
    r"""
    number of register arguments. During analysis IDA tries to guess the register
    arguments. It stores store the guessing outcome in this field. As soon as it
    determines the final function prototype, regargqty is set to zero.
    """
    regargs = property(_ida_funcs.func_t_regargs_get, _ida_funcs.func_t_regargs_set, doc=r"""regargs""")
    r"""
    unsorted array of register arguments. use ...regarg...() functions to access
    this array. regargs are destroyed when the full function type is determined.
    """
    tailqty = property(_ida_funcs.func_t_tailqty_get, _ida_funcs.func_t_tailqty_set, doc=r"""tailqty""")
    r"""
    number of function tails
    """
    tails = property(_ida_funcs.func_t_tails_get, _ida_funcs.func_t_tails_set, doc=r"""tails""")
    r"""
    array of tails, sorted by ea. use func_tail_iterator_t to access function tails.
    """
    owner = property(_ida_funcs.func_t_owner_get, _ida_funcs.func_t_owner_set, doc=r"""owner""")
    r"""
    the address of the main function possessing this tail
    """
    refqty = property(_ida_funcs.func_t_refqty_get, _ida_funcs.func_t_refqty_set, doc=r"""refqty""")
    r"""
    number of referers
    """
    referers = property(_ida_funcs.func_t_referers_get, _ida_funcs.func_t_referers_set, doc=r"""referers""")
    r"""
    array of referers (function start addresses). use func_parent_iterator_t to
    access the referers.
    """

    def __init__(self, *args):
        r"""
        __init__(self, start=0, end=0, f=0) -> func_t

        @param start: ea_t
        @param end: ea_t
        @param f: flags_t
        """
        _ida_funcs.func_t_swiginit(self, _ida_funcs.new_func_t(*args))

    def __get_points__(self, *args):
        r"""
        __get_points__(self) -> dyn_stkpnt_array
        """
        return _ida_funcs.func_t___get_points__(self, *args)

    def __get_regvars__(self, *args):
        r"""
        __get_regvars__(self) -> dyn_regvar_array
        """
        return _ida_funcs.func_t___get_regvars__(self, *args)

    def __get_tails__(self, *args):
        r"""
        __get_tails__(self) -> dyn_range_array
        """
        return _ida_funcs.func_t___get_tails__(self, *args)

    def __get_referers__(self, *args):
        r"""
        __get_referers__(self) -> dyn_ea_array
        """
        return _ida_funcs.func_t___get_referers__(self, *args)

    def __get_regargs__(self, *args):
        r"""
        __get_regargs__(self) -> dyn_regarg_array
        """
        return _ida_funcs.func_t___get_regargs__(self, *args)

    points = property(__get_points__)
    regvars = property(__get_regvars__)
    tails = property(__get_tails__)
    referers = property(__get_referers__)
    regargs = property(__get_regargs__)


    def __iter__(self):
        r"""
        Alias for func_item_iterator_t(self).__iter__()
        """
        return func_item_iterator_t(self).__iter__()

    __swig_destroy__ = _ida_funcs.delete_func_t

# Register func_t in _ida_funcs:
_ida_funcs.func_t_swigregister(func_t)
FUNC_NORET = _ida_funcs.FUNC_NORET
r"""
Function doesn't return.
"""

FUNC_FAR = _ida_funcs.FUNC_FAR
r"""
Far function.
"""

FUNC_LIB = _ida_funcs.FUNC_LIB
r"""
Library function.
"""

FUNC_STATICDEF = _ida_funcs.FUNC_STATICDEF
r"""
Static function.
"""

FUNC_FRAME = _ida_funcs.FUNC_FRAME
r"""
Function uses frame pointer (BP)
"""

FUNC_USERFAR = _ida_funcs.FUNC_USERFAR
r"""
User has specified far-ness of the function
"""

FUNC_HIDDEN = _ida_funcs.FUNC_HIDDEN
r"""
A hidden function chunk.
"""

FUNC_THUNK = _ida_funcs.FUNC_THUNK
r"""
Thunk (jump) function.
"""

FUNC_BOTTOMBP = _ida_funcs.FUNC_BOTTOMBP
r"""
BP points to the bottom of the stack frame.
"""

FUNC_NORET_PENDING = _ida_funcs.FUNC_NORET_PENDING
r"""
Function 'non-return' analysis must be performed. This flag is verified upon
func_does_return()
"""

FUNC_SP_READY = _ida_funcs.FUNC_SP_READY
r"""
SP-analysis has been performed. If this flag is on, the stack change points
should not be not modified anymore. Currently this analysis is performed only
for PC
"""

FUNC_FUZZY_SP = _ida_funcs.FUNC_FUZZY_SP
r"""
Function changes SP in untraceable way, for example: and esp, 0FFFFFFF0h
"""

FUNC_PROLOG_OK = _ida_funcs.FUNC_PROLOG_OK
r"""
Prolog analysis has been performed by last SP-analysis
"""

FUNC_PURGED_OK = _ida_funcs.FUNC_PURGED_OK
r"""
'argsize' field has been validated. If this bit is clear and 'argsize' is 0,
then we do not known the real number of bytes removed from the stack. This bit
is handled by the processor module.
"""

FUNC_TAIL = _ida_funcs.FUNC_TAIL
r"""
This is a function tail. Other bits must be clear (except FUNC_HIDDEN).
"""

FUNC_LUMINA = _ida_funcs.FUNC_LUMINA
r"""
Function info is provided by Lumina.
"""



def is_func_entry(*args):
    r"""
    is_func_entry(pfn) -> bool
    Does function describe a function entry chunk?

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.is_func_entry(*args)

def is_func_tail(*args):
    r"""
    is_func_tail(pfn) -> bool
    Does function describe a function tail chunk?

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.is_func_tail(*args)

def lock_func_range(*args):
    r"""
    lock_func_range(pfn, lock)
    Lock function pointer Locked pointers are guaranteed to remain valid until they
    are unlocked. Ranges with locked pointers cannot be deleted or moved.

    @param pfn: (C++: const func_t *) func_t const *
    @param lock: (C++: bool)
    """
    return _ida_funcs.lock_func_range(*args)
class lock_func(object):
    r"""
    Proxy of C++ lock_func class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _pfn) -> lock_func

        @param _pfn: func_t const *
        """
        _ida_funcs.lock_func_swiginit(self, _ida_funcs.new_lock_func(*args))
    __swig_destroy__ = _ida_funcs.delete_lock_func

# Register lock_func in _ida_funcs:
_ida_funcs.lock_func_swigregister(lock_func)


def is_func_locked(*args):
    r"""
    is_func_locked(pfn) -> bool
    Is the function pointer locked?

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.is_func_locked(*args)

def get_func(*args):
    r"""
    get_func(ea) -> func_t
    Get pointer to function structure by address.

    @param ea: (C++: ea_t) any address in a function
    @return: ptr to a function or nullptr. This function returns a function entry
             chunk.
    """
    return _ida_funcs.get_func(*args)

def get_func_chunknum(*args):
    r"""
    get_func_chunknum(pfn, ea) -> int
    Get the containing tail chunk of 'ea'.
    @retval -1: means 'does not contain ea'
    @retval 0: means the 'pfn' itself contains ea
    @retval >0: the number of the containing function tail chunk

    @param pfn: (C++: func_t *)
    @param ea: (C++: ea_t)
    """
    return _ida_funcs.get_func_chunknum(*args)

def func_contains(*args):
    r"""
    func_contains(pfn, ea) -> bool
    Does the given function contain the given address?

    @param pfn: (C++: func_t *)
    @param ea: (C++: ea_t)
    """
    return _ida_funcs.func_contains(*args)

def is_same_func(*args):
    r"""
    is_same_func(ea1, ea2) -> bool
    Do two addresses belong to the same function?

    @param ea1: (C++: ea_t)
    @param ea2: (C++: ea_t)
    """
    return _ida_funcs.is_same_func(*args)

def getn_func(*args):
    r"""
    getn_func(n) -> func_t
    Get pointer to function structure by number.

    @param n: (C++: size_t) number of function, is in range 0..get_func_qty()-1
    @return: ptr to a function or nullptr. This function returns a function entry
             chunk.
    """
    return _ida_funcs.getn_func(*args)

def get_func_qty(*args):
    r"""
    get_func_qty() -> size_t
    Get total number of functions in the program.
    """
    return _ida_funcs.get_func_qty(*args)

def get_func_num(*args):
    r"""
    get_func_num(ea) -> int
    Get ordinal number of a function.

    @param ea: (C++: ea_t) any address in the function
    @return: number of function (0..get_func_qty()-1). -1 means 'no function at the
             specified address'.
    """
    return _ida_funcs.get_func_num(*args)

def get_prev_func(*args):
    r"""
    get_prev_func(ea) -> func_t
    Get pointer to the previous function.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to function or nullptr if previous function doesn't exist
    """
    return _ida_funcs.get_prev_func(*args)

def get_next_func(*args):
    r"""
    get_next_func(ea) -> func_t
    Get pointer to the next function.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to function or nullptr if next function doesn't exist
    """
    return _ida_funcs.get_next_func(*args)

def get_func_ranges(*args):
    r"""
    get_func_ranges(ranges, pfn) -> ea_t
    Get function ranges.

    @param ranges: (C++: rangeset_t *) buffer to receive the range info
    @param pfn: (C++: func_t *) ptr to function structure
    @return: end address of the last function range (BADADDR-error)
    """
    return _ida_funcs.get_func_ranges(*args)

def get_func_cmt(*args):
    r"""
    get_func_cmt(pfn, repeatable) -> str
    Get function comment.

    @param pfn: (C++: const func_t *) ptr to function structure
    @param repeatable: (C++: bool) get repeatable comment?
    @return: size of comment or -1 In fact this function works with function chunks
             too.
    """
    return _ida_funcs.get_func_cmt(*args)

def set_func_cmt(*args):
    r"""
    set_func_cmt(pfn, cmt, repeatable) -> bool
    Set function comment. This function works with function chunks too.

    @param pfn: (C++: const func_t *) ptr to function structure
    @param cmt: (C++: const char *) comment string, may be multiline (with '
    '). Use empty str ("") to delete comment
    @param repeatable: (C++: bool) set repeatable comment?
    """
    return _ida_funcs.set_func_cmt(*args)

def update_func(*args):
    r"""
    update_func(pfn) -> bool
    Update information about a function in the database (func_t). You must not
    change the function start and end addresses using this function. Use
    set_func_start() and set_func_end() for it.

    @param pfn: (C++: func_t *) ptr to function structure
    @return: success
    """
    return _ida_funcs.update_func(*args)

def add_func_ex(*args):
    r"""
    add_func_ex(pfn) -> bool
    Add a new function. If the fn->end_ea is BADADDR, then IDA will try to determine
    the function bounds by calling find_func_bounds(..., FIND_FUNC_DEFINE).

    @param pfn: (C++: func_t *) ptr to filled function structure
    @return: success
    """
    return _ida_funcs.add_func_ex(*args)

def add_func(*args):
    r"""
    add_func(ea1, ea2=BADADDR) -> bool
    Add a new function. If the function end address is BADADDR, then IDA will try to
    determine the function bounds by calling find_func_bounds(...,
    FIND_FUNC_DEFINE).

    @param ea1: (C++: ea_t) start address
    @param ea2: (C++: ea_t) end address
    @return: success
    """
    return _ida_funcs.add_func(*args)

def del_func(*args):
    r"""
    del_func(ea) -> bool
    Delete a function.

    @param ea: (C++: ea_t) any address in the function entry chunk
    @return: success
    """
    return _ida_funcs.del_func(*args)

def set_func_start(*args):
    r"""
    set_func_start(ea, newstart) -> int
    Move function chunk start address.

    @param ea: (C++: ea_t) any address in the function
    @param newstart: (C++: ea_t) new end address of the function
    @return: Function move result codes
    """
    return _ida_funcs.set_func_start(*args)
MOVE_FUNC_OK = _ida_funcs.MOVE_FUNC_OK
r"""
ok
"""

MOVE_FUNC_NOCODE = _ida_funcs.MOVE_FUNC_NOCODE
r"""
no instruction at 'newstart'
"""

MOVE_FUNC_BADSTART = _ida_funcs.MOVE_FUNC_BADSTART
r"""
bad new start address
"""

MOVE_FUNC_NOFUNC = _ida_funcs.MOVE_FUNC_NOFUNC
r"""
no function at 'ea'
"""

MOVE_FUNC_REFUSED = _ida_funcs.MOVE_FUNC_REFUSED
r"""
a plugin refused the action
"""


def set_func_end(*args):
    r"""
    set_func_end(ea, newend) -> bool
    Move function chunk end address.

    @param ea: (C++: ea_t) any address in the function
    @param newend: (C++: ea_t) new end address of the function
    @return: success
    """
    return _ida_funcs.set_func_end(*args)

def reanalyze_function(*args):
    r"""
    reanalyze_function(pfn, ea1=0, ea2=BADADDR, analyze_parents=False)
    Reanalyze a function. This function plans to analyzes all chunks of the given
    function. Optional parameters (ea1, ea2) may be used to narrow the analyzed
    range.

    @param pfn: (C++: func_t *) pointer to a function
    @param ea1: (C++: ea_t) start of the range to analyze
    @param ea2: (C++: ea_t) end of range to analyze
    @param analyze_parents: (C++: bool) meaningful only if pfn points to a function tail. if
                            true, all tail parents will be reanalyzed. if false,
                            only the given tail will be reanalyzed.
    """
    return _ida_funcs.reanalyze_function(*args)

def find_func_bounds(*args):
    r"""
    find_func_bounds(nfn, flags) -> int
    Determine the boundaries of a new function. This function tries to find the
    start and end addresses of a new function. It calls the module with
    processor_t::func_bounds in order to fine tune the function boundaries.

    @param nfn: (C++: func_t *) structure to fill with information \ nfn->start_ea points to the
                start address of the new function.
    @param flags: (C++: int) Find function bounds flags
    @return: Find function bounds result codes
    """
    return _ida_funcs.find_func_bounds(*args)
FIND_FUNC_NORMAL = _ida_funcs.FIND_FUNC_NORMAL
r"""
stop processing if undefined byte is encountered
"""

FIND_FUNC_DEFINE = _ida_funcs.FIND_FUNC_DEFINE
r"""
create instruction if undefined byte is encountered
"""

FIND_FUNC_IGNOREFN = _ida_funcs.FIND_FUNC_IGNOREFN
r"""
ignore existing function boundaries. by default the function returns function
boundaries if ea belongs to a function.
"""

FIND_FUNC_KEEPBD = _ida_funcs.FIND_FUNC_KEEPBD
r"""
do not modify incoming function boundaries, just create instructions inside the
boundaries.
"""

FIND_FUNC_UNDEF = _ida_funcs.FIND_FUNC_UNDEF
r"""
function has instructions that pass execution flow to unexplored bytes.
nfn->end_ea will have the address of the unexplored byte.
"""

FIND_FUNC_OK = _ida_funcs.FIND_FUNC_OK
r"""
ok, 'nfn' is ready for add_func()
"""

FIND_FUNC_EXIST = _ida_funcs.FIND_FUNC_EXIST
r"""
function exists already. its bounds are returned in 'nfn'.
"""


def get_func_name(*args):
    r"""
    get_func_name(ea) -> str
    Get function name.

    @param ea: (C++: ea_t) any address in the function
    @return: length of the function name
    """
    return _ida_funcs.get_func_name(*args)

def calc_func_size(*args):
    r"""
    calc_func_size(pfn) -> asize_t
    Calculate function size. This function takes into account all fragments of the
    function.

    @param pfn: (C++: func_t *) ptr to function structure
    """
    return _ida_funcs.calc_func_size(*args)

def get_func_bitness(*args):
    r"""
    get_func_bitness(pfn) -> int
    Get function bitness (which is equal to the function segment bitness).
    pfn==nullptr => returns 0
    @retval 0: 16
    @retval 1: 32
    @retval 2: 64

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.get_func_bitness(*args)

def get_func_bits(*args):
    r"""
    get_func_bits(pfn) -> int
    Get number of bits in the function addressing.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.get_func_bits(*args)

def get_func_bytes(*args):
    r"""
    get_func_bytes(pfn) -> int
    Get number of bytes in the function addressing.

    @param pfn: (C++: const func_t *) func_t const *
    """
    return _ida_funcs.get_func_bytes(*args)

def is_visible_func(*args):
    r"""
    is_visible_func(pfn) -> bool
    Is the function visible (not hidden)?

    @param pfn: (C++: func_t *)
    """
    return _ida_funcs.is_visible_func(*args)

def is_finally_visible_func(*args):
    r"""
    is_finally_visible_func(pfn) -> bool
    Is the function visible (event after considering SCF_SHHID_FUNC)?

    @param pfn: (C++: func_t *)
    """
    return _ida_funcs.is_finally_visible_func(*args)

def set_visible_func(*args):
    r"""
    set_visible_func(pfn, visible)
    Set visibility of function.

    @param pfn: (C++: func_t *)
    @param visible: (C++: bool)
    """
    return _ida_funcs.set_visible_func(*args)

def set_func_name_if_jumpfunc(*args):
    r"""
    set_func_name_if_jumpfunc(pfn, oldname) -> int
    Give a meaningful name to function if it consists of only 'jump' instruction.

    @param pfn: (C++: func_t *) pointer to function (may be nullptr)
    @param oldname: (C++: const char *) old name of function. if old name was in "j_..." form, then we
                    may discard it and set a new name. if oldname is not known, you
                    may pass nullptr.
    @return: success
    """
    return _ida_funcs.set_func_name_if_jumpfunc(*args)

def calc_thunk_func_target(*args):
    r"""
    calc_thunk_func_target(pfn) -> ea_t
    Calculate target of a thunk function.

    @param pfn: (C++: func_t *) pointer to function (may not be nullptr)
    @return: the target function or BADADDR
    """
    return _ida_funcs.calc_thunk_func_target(*args)

def func_does_return(*args):
    r"""
    func_does_return(callee) -> bool
    Does the function return?. To calculate the answer, FUNC_NORET flag and
    is_noret() are consulted The latter is required for imported functions in the
    .idata section. Since in .idata we have only function pointers but not
    functions, we have to introduce a special flag for them.

    @param callee: (C++: ea_t)
    """
    return _ida_funcs.func_does_return(*args)

def reanalyze_noret_flag(*args):
    r"""
    reanalyze_noret_flag(ea) -> bool
    Plan to reanalyze noret flag. This function does not remove FUNC_NORET if it is
    already present. It just plans to reanalysis.

    @param ea: (C++: ea_t)
    """
    return _ida_funcs.reanalyze_noret_flag(*args)

def set_noret_insn(*args):
    r"""
    set_noret_insn(insn_ea, noret) -> bool
    Signal a non-returning instruction. This function can be used by the processor
    module to tell the kernel about non-returning instructions (like call exit). The
    kernel will perform the global function analysis and find out if the function
    returns at all. This analysis will be done at the first call to
    func_does_return()

    @param insn_ea: (C++: ea_t)
    @param noret: (C++: bool)
    @return: true if the instruction 'noret' flag has been changed
    """
    return _ida_funcs.set_noret_insn(*args)

def get_fchunk(*args):
    r"""
    get_fchunk(ea) -> func_t
    Get pointer to function chunk structure by address.

    @param ea: (C++: ea_t) any address in a function chunk
    @return: ptr to a function chunk or nullptr. This function may return a function
             entry as well as a function tail.
    """
    return _ida_funcs.get_fchunk(*args)

def getn_fchunk(*args):
    r"""
    getn_fchunk(n) -> func_t
    Get pointer to function chunk structure by number.

    @param n: (C++: int) number of function chunk, is in range 0..get_fchunk_qty()-1
    @return: ptr to a function chunk or nullptr. This function may return a function
             entry as well as a function tail.
    """
    return _ida_funcs.getn_fchunk(*args)

def get_fchunk_qty(*args):
    r"""
    get_fchunk_qty() -> size_t
    Get total number of function chunks in the program.
    """
    return _ida_funcs.get_fchunk_qty(*args)

def get_fchunk_num(*args):
    r"""
    get_fchunk_num(ea) -> int
    Get ordinal number of a function chunk in the global list of function chunks.

    @param ea: (C++: ea_t) any address in the function chunk
    @return: number of function chunk (0..get_fchunk_qty()-1). -1 means 'no function
             chunk at the specified address'.
    """
    return _ida_funcs.get_fchunk_num(*args)

def get_prev_fchunk(*args):
    r"""
    get_prev_fchunk(ea) -> func_t
    Get pointer to the previous function chunk in the global list.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to function chunk or nullptr if previous function chunk doesn't
             exist
    """
    return _ida_funcs.get_prev_fchunk(*args)

def get_next_fchunk(*args):
    r"""
    get_next_fchunk(ea) -> func_t
    Get pointer to the next function chunk in the global list.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to function chunk or nullptr if next function chunk doesn't exist
    """
    return _ida_funcs.get_next_fchunk(*args)

def append_func_tail(*args):
    r"""
    append_func_tail(pfn, ea1, ea2) -> bool
    Append a new tail chunk to the function definition. If the tail already exists,
    then it will simply be added to the function tail list Otherwise a new tail will
    be created and its owner will be set to be our function If a new tail cannot be
    created, then this function will fail.

    @param ea1: (C++: ea_t) start of the tail. If a tail already exists at the specified address
                it must start at 'ea1'
    @param ea1: (C++: ea_t) start of the tail. If a tail already exists at the specified address
                it must start at 'ea1'
    @param ea2: (C++: ea_t) end of the tail. If a tail already exists at the specified address
                it must end at 'ea2'. If specified as BADADDR, IDA will determine
                the end address itself.
    """
    return _ida_funcs.append_func_tail(*args)

def remove_func_tail(*args):
    r"""
    remove_func_tail(pfn, tail_ea) -> bool
    Remove a function tail. If the tail belongs only to one function, it will be
    completely removed. Otherwise if the function was the tail owner, the first
    function using this tail becomes the owner of the tail.

    @param pfn: (C++: func_t *)
    @param tail_ea: (C++: ea_t)
    """
    return _ida_funcs.remove_func_tail(*args)

def set_tail_owner(*args):
    r"""
    set_tail_owner(fnt, func_start) -> bool
    Set a function as the possessing function of a function tail. The function
    should already refer to the tail (after append_func_tail).

    @param fnt: (C++: func_t *)
    @param func_start: (C++: ea_t)
    """
    return _ida_funcs.set_tail_owner(*args)

def func_tail_iterator_set(*args):
    r"""
    func_tail_iterator_set(fti, pfn, ea) -> bool

    @param fti: func_tail_iterator_t *
    @param pfn: func_t *
    @param ea: ea_t
    """
    return _ida_funcs.func_tail_iterator_set(*args)

def func_tail_iterator_set_ea(*args):
    r"""
    func_tail_iterator_set_ea(fti, ea) -> bool

    @param fti: func_tail_iterator_t *
    @param ea: ea_t
    """
    return _ida_funcs.func_tail_iterator_set_ea(*args)

def func_parent_iterator_set(*args):
    r"""
    func_parent_iterator_set(fpi, pfn) -> bool

    @param fpi: func_parent_iterator_t *
    @param pfn: func_t *
    """
    return _ida_funcs.func_parent_iterator_set(*args)

def f_any(*args):
    r"""
    f_any(arg1, arg2) -> bool
    Helper function to accept any address.

    @param arg1: flags_t
    @param arg2: void *
    """
    return _ida_funcs.f_any(*args)
class func_tail_iterator_t(object):
    r"""
    Proxy of C++ func_tail_iterator_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_tail_iterator_t
        __init__(self, _pfn, ea=BADADDR) -> func_tail_iterator_t

        @param _pfn: func_t *
        @param ea: ea_t
        """
        _ida_funcs.func_tail_iterator_t_swiginit(self, _ida_funcs.new_func_tail_iterator_t(*args))
    __swig_destroy__ = _ida_funcs.delete_func_tail_iterator_t

    def set(self, *args):
        r"""
        set(self, _pfn, ea=BADADDR) -> bool

        @param _pfn: func_t *
        @param ea: ea_t
        """
        return _ida_funcs.func_tail_iterator_t_set(self, *args)

    def set_ea(self, *args):
        r"""
        set_ea(self, ea) -> bool

        @param ea: ea_t
        """
        return _ida_funcs.func_tail_iterator_t_set_ea(self, *args)

    def set_range(self, *args):
        r"""
        set_range(self, ea1, ea2) -> bool

        @param ea1: ea_t
        @param ea2: ea_t
        """
        return _ida_funcs.func_tail_iterator_t_set_range(self, *args)

    def chunk(self, *args):
        r"""
        chunk(self) -> range_t
        """
        return _ida_funcs.func_tail_iterator_t_chunk(self, *args)

    def first(self, *args):
        r"""
        first(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_first(self, *args)

    def last(self, *args):
        r"""
        last(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_last(self, *args)

    def __next__(self, *args):
        r"""
        __next__(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t___next__(self, *args)

    def prev(self, *args):
        r"""
        prev(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_prev(self, *args)

    def main(self, *args):
        r"""
        main(self) -> bool
        """
        return _ida_funcs.func_tail_iterator_t_main(self, *args)

    def __iter__(self):
        r"""
        Provide an iterator on function tails
        """
        ok = self.main()
        while ok:
            yield self.chunk()
            ok = self.next()


    next = __next__


# Register func_tail_iterator_t in _ida_funcs:
_ida_funcs.func_tail_iterator_t_swigregister(func_tail_iterator_t)

class func_item_iterator_t(object):
    r"""
    Proxy of C++ func_item_iterator_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_item_iterator_t
        __init__(self, pfn, _ea=BADADDR) -> func_item_iterator_t

        @param pfn: func_t *
        @param _ea: ea_t
        """
        _ida_funcs.func_item_iterator_t_swiginit(self, _ida_funcs.new_func_item_iterator_t(*args))

    def set(self, *args):
        r"""
        set(self, pfn, _ea=BADADDR) -> bool
        Set a function range. if pfn == nullptr then a segment range will be set.

        @param pfn: (C++: func_t *)
        @param _ea: (C++: ea_t)
        """
        return _ida_funcs.func_item_iterator_t_set(self, *args)

    def set_range(self, *args):
        r"""
        set_range(self, ea1, ea2) -> bool
        Set an arbitrary range.

        @param ea1: (C++: ea_t)
        @param ea2: (C++: ea_t)
        """
        return _ida_funcs.func_item_iterator_t_set_range(self, *args)

    def first(self, *args):
        r"""
        first(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_first(self, *args)

    def last(self, *args):
        r"""
        last(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_last(self, *args)

    def current(self, *args):
        r"""
        current(self) -> ea_t
        """
        return _ida_funcs.func_item_iterator_t_current(self, *args)

    def chunk(self, *args):
        r"""
        chunk(self) -> range_t
        """
        return _ida_funcs.func_item_iterator_t_chunk(self, *args)

    def __next__(self, *args):
        r"""
        __next__(self, func) -> bool

        @param func: testf_t *
        """
        return _ida_funcs.func_item_iterator_t___next__(self, *args)

    def prev(self, *args):
        r"""
        prev(self, func) -> bool

        @param func: testf_t *
        """
        return _ida_funcs.func_item_iterator_t_prev(self, *args)

    def next_addr(self, *args):
        r"""
        next_addr(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_addr(self, *args)

    def next_head(self, *args):
        r"""
        next_head(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_head(self, *args)

    def next_code(self, *args):
        r"""
        next_code(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_code(self, *args)

    def next_data(self, *args):
        r"""
        next_data(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_data(self, *args)

    def next_not_tail(self, *args):
        r"""
        next_not_tail(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_next_not_tail(self, *args)

    def prev_addr(self, *args):
        r"""
        prev_addr(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_addr(self, *args)

    def prev_head(self, *args):
        r"""
        prev_head(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_head(self, *args)

    def prev_code(self, *args):
        r"""
        prev_code(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_code(self, *args)

    def prev_data(self, *args):
        r"""
        prev_data(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_data(self, *args)

    def prev_not_tail(self, *args):
        r"""
        prev_not_tail(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_prev_not_tail(self, *args)

    def decode_prev_insn(self, *args):
        r"""
        decode_prev_insn(self, out) -> bool

        @param out: insn_t *
        """
        return _ida_funcs.func_item_iterator_t_decode_prev_insn(self, *args)

    def decode_preceding_insn(self, *args):
        r"""
        decode_preceding_insn(self, visited, p_farref, out) -> bool

        @param visited: eavec_t *
        @param p_farref: bool *
        @param out: insn_t *
        """
        return _ida_funcs.func_item_iterator_t_decode_preceding_insn(self, *args)

    def succ(self, *args):
        r"""
        succ(self, func) -> bool
        Similar to next(), but succ() iterates the chunks from low to high addresses,
        while next() iterates through chunks starting at the function entry chunk

        @param func: (C++: testf_t *)
        """
        return _ida_funcs.func_item_iterator_t_succ(self, *args)

    def succ_code(self, *args):
        r"""
        succ_code(self) -> bool
        """
        return _ida_funcs.func_item_iterator_t_succ_code(self, *args)

    def __iter__(self):
        r"""
        Provide an iterator on code items
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_code()


    next = __next__


    def addresses(self):
        r"""
        Provide an iterator on addresses contained within the function
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_addr()


    def code_items(self):
        r"""
        Provide an iterator on code items contained within the function
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_code()


    def data_items(self):
        r"""
        Provide an iterator on data items contained within the function
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_data()


    def head_items(self):
        r"""
        Provide an iterator on item heads contained within the function
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_head()


    def not_tails(self):
        r"""
        Provide an iterator on non-tail addresses contained within the function
        """
        ok = self.first()
        while ok:
            yield self.current()
            ok = self.next_not_tail()

    __swig_destroy__ = _ida_funcs.delete_func_item_iterator_t

# Register func_item_iterator_t in _ida_funcs:
_ida_funcs.func_item_iterator_t_swigregister(func_item_iterator_t)

class func_parent_iterator_t(object):
    r"""
    Proxy of C++ func_parent_iterator_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> func_parent_iterator_t
        __init__(self, _fnt) -> func_parent_iterator_t

        @param _fnt: func_t *
        """
        _ida_funcs.func_parent_iterator_t_swiginit(self, _ida_funcs.new_func_parent_iterator_t(*args))
    __swig_destroy__ = _ida_funcs.delete_func_parent_iterator_t

    def set(self, *args):
        r"""
        set(self, _fnt) -> bool

        @param _fnt: func_t *
        """
        return _ida_funcs.func_parent_iterator_t_set(self, *args)

    def parent(self, *args):
        r"""
        parent(self) -> ea_t
        """
        return _ida_funcs.func_parent_iterator_t_parent(self, *args)

    def first(self, *args):
        r"""
        first(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_first(self, *args)

    def last(self, *args):
        r"""
        last(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_last(self, *args)

    def __next__(self, *args):
        r"""
        __next__(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t___next__(self, *args)

    def prev(self, *args):
        r"""
        prev(self) -> bool
        """
        return _ida_funcs.func_parent_iterator_t_prev(self, *args)

    def reset_fnt(self, *args):
        r"""
        reset_fnt(self, _fnt)

        @param _fnt: func_t *
        """
        return _ida_funcs.func_parent_iterator_t_reset_fnt(self, *args)

    def __iter__(self):
        r"""
        Provide an iterator on function parents
        """
        ok = self.first()
        while ok:
            yield self.parent()
            ok = self.next()


    next = __next__


# Register func_parent_iterator_t in _ida_funcs:
_ida_funcs.func_parent_iterator_t_swigregister(func_parent_iterator_t)


def get_prev_func_addr(*args):
    r"""
    get_prev_func_addr(pfn, ea) -> ea_t

    @param pfn: func_t *
    @param ea: ea_t
    """
    return _ida_funcs.get_prev_func_addr(*args)

def get_next_func_addr(*args):
    r"""
    get_next_func_addr(pfn, ea) -> ea_t

    @param pfn: func_t *
    @param ea: ea_t
    """
    return _ida_funcs.get_next_func_addr(*args)

def read_regargs(*args):
    r"""
    read_regargs(pfn)

    @param pfn: func_t *
    """
    return _ida_funcs.read_regargs(*args)

def add_regarg(*args):
    r"""
    add_regarg(pfn, reg, tif, name)

    @param pfn: func_t *
    @param reg: int
    @param tif: tinfo_t const &
    @param name: char const *
    """
    return _ida_funcs.add_regarg(*args)
IDASGN_OK = _ida_funcs.IDASGN_OK
r"""
ok
"""

IDASGN_BADARG = _ida_funcs.IDASGN_BADARG
r"""
bad number of signature
"""

IDASGN_APPLIED = _ida_funcs.IDASGN_APPLIED
r"""
signature is already applied
"""

IDASGN_CURRENT = _ida_funcs.IDASGN_CURRENT
r"""
signature is currently being applied
"""

IDASGN_PLANNED = _ida_funcs.IDASGN_PLANNED
r"""
signature is planned to be applied
"""


def plan_to_apply_idasgn(*args):
    r"""
    plan_to_apply_idasgn(fname) -> int
    Add a signature file to the list of planned signature files.

    @param fname: (C++: const char *) file name. should not contain directory part.
    @return: 0 if failed, otherwise number of planned (and applied) signatures
    """
    return _ida_funcs.plan_to_apply_idasgn(*args)

def apply_idasgn_to(*args):
    r"""
    apply_idasgn_to(signame, ea, is_startup) -> int
    Apply a signature file to the specified address.

    @param signame: (C++: const char *) short name of signature file (the file name without path)
    @param ea: (C++: ea_t) address to apply the signature
    @param is_startup: (C++: bool) if set, then the signature is treated as a startup one for
                       startup signature ida doesn't rename the first function of
                       the applied module.
    @return: Library function codes
    """
    return _ida_funcs.apply_idasgn_to(*args)

def get_idasgn_qty(*args):
    r"""
    get_idasgn_qty() -> int
    Get number of signatures in the list of planned and applied signatures.

    @return: 0..n
    """
    return _ida_funcs.get_idasgn_qty(*args)

def get_current_idasgn(*args):
    r"""
    get_current_idasgn() -> int
    Get number of the the current signature.

    @return: 0..n-1
    """
    return _ida_funcs.get_current_idasgn(*args)

def calc_idasgn_state(*args):
    r"""
    calc_idasgn_state(n) -> int
    Get state of a signature in the list of planned signatures

    @param n: (C++: int) number of signature in the list (0..get_idasgn_qty()-1)
    @return: state of signature or IDASGN_BADARG
    """
    return _ida_funcs.calc_idasgn_state(*args)

def del_idasgn(*args):
    r"""
    del_idasgn(n) -> int
    Remove signature from the list of planned signatures.

    @param n: (C++: int) number of signature in the list (0..get_idasgn_qty()-1)
    @return: IDASGN_OK, IDASGN_BADARG, IDASGN_APPLIED
    """
    return _ida_funcs.del_idasgn(*args)

def get_idasgn_title(*args):
    r"""
    get_idasgn_title(name) -> str
    Get full description of the signature by its short name.

    @param name: (C++: const char *) short name of a signature
    @return: size of signature description or -1
    """
    return _ida_funcs.get_idasgn_title(*args)

def apply_startup_sig(*args):
    r"""
    apply_startup_sig(ea, startup) -> bool
    Apply a startup signature file to the specified address.

    @param ea: (C++: ea_t) address to apply the signature to; usually idainfo::start_ea
    @param startup: (C++: const char *) the name of the signature file without path and extension
    @return: true if successfully applied the signature
    """
    return _ida_funcs.apply_startup_sig(*args)

def try_to_add_libfunc(*args):
    r"""
    try_to_add_libfunc(ea) -> int
    Apply the currently loaded signature file to the specified address. If a library
    function is found, then create a function and name it accordingly.

    @param ea: (C++: ea_t) any address in the program
    @return: Library function codes
    """
    return _ida_funcs.try_to_add_libfunc(*args)
LIBFUNC_FOUND = _ida_funcs.LIBFUNC_FOUND
r"""
ok, library function is found
"""

LIBFUNC_NONE = _ida_funcs.LIBFUNC_NONE
r"""
no, this is not a library function
"""

LIBFUNC_DELAY = _ida_funcs.LIBFUNC_DELAY
r"""
no decision because of lack of information
"""


def get_fchunk_referer(*args):
    r"""
    get_fchunk_referer(ea, idx) -> ea_t

    @param ea: ea_t
    @param idx: size_t
    """
    return _ida_funcs.get_fchunk_referer(*args)

def get_idasgn_desc(*args):
    r"""
    get_idasgn_desc(n) -> (str, str)
    Get information about a signature in the list.
    It returns: (name of signature, names of optional libraries)

    See also: get_idasgn_desc_with_matches

    @param n: number of signature in the list (0..get_idasgn_qty()-1)
    @return: None on failure or tuple(signame, optlibs)
    """
    return _ida_funcs.get_idasgn_desc(*args)

def get_idasgn_desc_with_matches(*args):
    r"""
    get_idasgn_desc_with_matches(n) -> (str, str, int)
    Get information about a signature in the list.
    It returns: (name of signature, names of optional libraries, number of matches)

    @param n: number of signature in the list (0..get_idasgn_qty()-1)
    @return: None on failure or tuple(signame, optlibs, nmatches)
    """
    return _ida_funcs.get_idasgn_desc_with_matches(*args)

def func_t__from_ptrval__(*args):
    r"""
    func_t__from_ptrval__(ptrval) -> func_t

    @param ptrval: size_t
    """
    return _ida_funcs.func_t__from_ptrval__(*args)

#<pycode(py_funcs)>
import ida_idaapi
@ida_idaapi.replfun
def calc_thunk_func_target(*args):
    if len(args) == 2:
        pfn, rawptr = args
        target, fptr = calc_thunk_func_target.__dict__["orig"](pfn)
        import ida_pro
        ida_pro.ea_pointer.frompointer(rawptr).assign(fptr)
        return target
    else:
        return calc_thunk_func_target.__dict__["orig"](*args)
#</pycode(py_funcs)>




