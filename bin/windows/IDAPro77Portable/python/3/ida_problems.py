"""
Functions that deal with the list of problems.

There are several problem lists. An address may be inserted to any list. The
kernel simply maintains these lists, no additional processing is done.

The problem lists are accessible for the user from the View->Subviews->Problems
menu item.

Addresses in the lists are kept sorted. In general IDA just maintains these
lists without using them during analysis (except PR_ROLLED)."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_problems
else:
    import _ida_problems

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

SWIG_PYTHON_LEGACY_BOOL = _ida_problems.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


def get_problem_desc(*args) -> "qstring *":
    r"""
    get_problem_desc(t, ea) -> str
    Get the human-friendly description of the problem, if one was provided to
    remember_problem.

    @param t: (C++: problist_id_t) problem list type.
    @param ea: (C++: ea_t) linear address.
    @return: the message length or -1 if none
    """
    return _ida_problems.get_problem_desc(*args)

def remember_problem(*args) -> "void":
    r"""
    remember_problem(type, ea, msg=None)
    Insert an address to a list of problems. Display a message saying about the
    problem (except of PR_ATTN,PR_FINAL) PR_JUMP is temporarily ignored.

    @param type: (C++: problist_id_t) problem list type
    @param ea: (C++: ea_t) linear address
    @param msg: (C++: const char *) a user-friendly message to be displayed instead of the default more
                generic one associated with the type of problem. Defaults to
                nullptr.
    """
    return _ida_problems.remember_problem(*args)

def get_problem(*args) -> "ea_t":
    r"""
    get_problem(type, lowea) -> ea_t
    Get an address from the specified problem list. The address is not removed from
    the list.

    @param type: (C++: problist_id_t) problem list type
    @param lowea: (C++: ea_t) the returned address will be higher or equal than the specified
                  address
    @return: linear address or BADADDR
    """
    return _ida_problems.get_problem(*args)

def forget_problem(*args) -> "bool":
    r"""
    forget_problem(type, ea) -> bool
    Remove an address from a problem list

    @param type: (C++: problist_id_t) problem list type
    @param ea: (C++: ea_t) linear address
    @return: success
    """
    return _ida_problems.forget_problem(*args)

def get_problem_name(*args) -> "char const *":
    r"""
    get_problem_name(type, longname=True) -> char const *
    Get problem list description.

    @param type: (C++: problist_id_t)
    @param longname: (C++: bool)
    """
    return _ida_problems.get_problem_name(*args)

def is_problem_present(*args) -> "bool":
    r"""
    is_problem_present(t, ea) -> bool
    Check if the specified address is present in the problem list.

    @param t: (C++: problist_id_t)
    @param ea: (C++: ea_t)
    """
    return _ida_problems.is_problem_present(*args)

def was_ida_decision(*args) -> "bool":
    r"""
    was_ida_decision(ea) -> bool

    @param ea: ea_t
    """
    return _ida_problems.was_ida_decision(*args)

cvar = _ida_problems.cvar
PR_NOBASE = cvar.PR_NOBASE
r"""
Can't find offset base.
"""
PR_NONAME = cvar.PR_NONAME
r"""
Can't find name.
"""
PR_NOFOP = cvar.PR_NOFOP
r"""
Can't find forced op (not used anymore)
"""
PR_NOCMT = cvar.PR_NOCMT
r"""
Can't find comment (not used anymore)
"""
PR_NOXREFS = cvar.PR_NOXREFS
r"""
Can't find references.
"""
PR_JUMP = cvar.PR_JUMP
r"""
Jump by table !!!! ignored.
"""
PR_DISASM = cvar.PR_DISASM
r"""
Can't disasm.
"""
PR_HEAD = cvar.PR_HEAD
r"""
Already head.
"""
PR_ILLADDR = cvar.PR_ILLADDR
r"""
Exec flows beyond limits.
"""
PR_MANYLINES = cvar.PR_MANYLINES
r"""
Too many lines.
"""
PR_BADSTACK = cvar.PR_BADSTACK
r"""
Failed to trace the value of the stack pointer.
"""
PR_ATTN = cvar.PR_ATTN
r"""
Attention! Probably erroneous situation.
"""
PR_FINAL = cvar.PR_FINAL
r"""
Decision to convert to instruction/data is made by IDA.
"""
PR_ROLLED = cvar.PR_ROLLED
r"""
The decision made by IDA was wrong and rolled back.
"""
PR_COLLISION = cvar.PR_COLLISION
r"""
FLAIR collision: the function with the given name already exists.
"""
PR_DECIMP = cvar.PR_DECIMP
r"""
FLAIR match indecision: the patterns matched, but not the function(s) being
referenced.
"""
PR_END = cvar.PR_END
r"""
Number of problem types.
"""


