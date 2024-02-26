
from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_idc
else:
    import _ida_idc

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

SWIG_PYTHON_LEGACY_BOOL = _ida_idc.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


def mark_position(*args) -> "void":
    r"""
    mark_position(ea, lnnum, x, y, slot, comment)

    @param ea: ea_t
    @param lnnum: int
    @param x: short
    @param y: short
    @param slot: int32
    @param comment: char const *
    """
    return _ida_idc.mark_position(*args)

def get_marked_pos(*args) -> "ea_t":
    r"""
    get_marked_pos(slot) -> ea_t

    @param slot: int32
    """
    return _ida_idc.get_marked_pos(*args)

def get_mark_comment(*args) -> "PyObject *":
    r"""
    get_mark_comment(slot) -> PyObject *

    @param slot: int32
    """
    return _ida_idc.get_mark_comment(*args)

#<pycode(py_idc)>
#</pycode(py_idc)>




