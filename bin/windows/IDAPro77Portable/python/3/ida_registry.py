"""
Registry related functions.

IDA uses the registry to store global configuration options that must persist
after IDA has been closed.

On Windows, IDA uses the Windows registry directly. On Unix systems, the
registry is stored in a file (typically ~/.idapro/ida.reg).

The root key for accessing IDA settings in the registry is defined by
ROOT_KEY_NAME."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_registry
else:
    import _ida_registry

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

SWIG_PYTHON_LEGACY_BOOL = _ida_registry.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


def reg_read_string(*args) -> "PyObject *":
    r"""
    reg_read_string(name, subkey=None, _def=None) -> str
    Read a string from the registry.

    @param name: (C++: const char *) value name
    @param subkey: (C++: const char *) key name
    @param def: char const *
    @return: success
    """
    return _ida_registry.reg_read_string(*args)

def reg_data_type(*args) -> "regval_type_t":
    r"""
    reg_data_type(name, subkey=None) -> regval_type_t
    Get data type of a given value.

    @param name: (C++: const char *) value name
    @param subkey: (C++: const char *) key name
    @return: false if the [key+]value doesn't exist
    """
    return _ida_registry.reg_data_type(*args)

def reg_read_binary(*args) -> "PyObject *":
    r"""
    reg_read_binary(name, subkey=None) -> bytes or None
    Read binary data from the registry.

    @param name: (C++: const char *) value name
    @param subkey: (C++: const char *) key name
    @return: success
    """
    return _ida_registry.reg_read_binary(*args)

def reg_write_binary(*args) -> "PyObject *":
    r"""
    reg_write_binary(name, py_bytes, subkey=None) -> PyObject *
    Write binary data to the registry.

    @param name: (C++: const char *) value name
    @param py_bytes: PyObject *
    @param subkey: (C++: const char *) key name
    """
    return _ida_registry.reg_write_binary(*args)

def reg_subkey_subkeys(*args) -> "PyObject *":
    r"""
    reg_subkey_subkeys(name) -> [str, ...]
    Get all subkey names of given key.

    @param name: (C++: const char *) char const *
    """
    return _ida_registry.reg_subkey_subkeys(*args)

def reg_subkey_values(*args) -> "PyObject *":
    r"""
    reg_subkey_values(name) -> [str, ...]
    Get all value names under given key.

    @param name: (C++: const char *) char const *
    """
    return _ida_registry.reg_subkey_values(*args)
ROOT_KEY_NAME = _ida_registry.ROOT_KEY_NAME
r"""
Key used to store IDA settings in registry (Windows version).
@note: this name is automatically prepended to all key names passed to functions
       in this file.
"""

reg_unknown = _ida_registry.reg_unknown
r"""
unknown
"""

reg_sz = _ida_registry.reg_sz
r"""
utf8 string
"""

reg_binary = _ida_registry.reg_binary
r"""
binary data
"""

reg_dword = _ida_registry.reg_dword
r"""
32-bit number
"""


def reg_delete_subkey(*args) -> "bool":
    r"""
    reg_delete_subkey(name) -> bool
    Delete a key from the registry.

    @param name: (C++: const char *) char const *
    """
    return _ida_registry.reg_delete_subkey(*args)

def reg_delete_tree(*args) -> "bool":
    r"""
    reg_delete_tree(name) -> bool
    Delete a subtree from the registry.

    @param name: (C++: const char *) char const *
    """
    return _ida_registry.reg_delete_tree(*args)

def reg_delete(*args) -> "bool":
    r"""
    reg_delete(name, subkey=None) -> bool
    Delete a value from the registry.

    @param name: (C++: const char *) value name
    @param subkey: (C++: const char *) parent key
    @return: success
    """
    return _ida_registry.reg_delete(*args)

def reg_subkey_exists(*args) -> "bool":
    r"""
    reg_subkey_exists(name) -> bool
    Is there already a key with the given name?

    @param name: (C++: const char *) char const *
    """
    return _ida_registry.reg_subkey_exists(*args)

def reg_exists(*args) -> "bool":
    r"""
    reg_exists(name, subkey=None) -> bool
    Is there already a value with the given name?

    @param name: (C++: const char *) value name
    @param subkey: (C++: const char *) parent key
    """
    return _ida_registry.reg_exists(*args)

def reg_read_strlist(*args) -> "qstrvec_t *":
    r"""
    reg_read_strlist(subkey)
    Retrieve all string values associated with the given key. Also see
    reg_update_strlist().

    @param subkey: (C++: const char *) char const *
    """
    return _ida_registry.reg_read_strlist(*args)

def reg_update_strlist(*args) -> "void":
    r"""
    reg_update_strlist(subkey, add, maxrecs, rem=None, ignorecase=False)
    Update list of strings associated with given key.

    @param subkey: (C++: const char *) key name
    @param add: (C++: const char *) string to be added to list, can be nullptr
    @param maxrecs: (C++: size_t) limit list to this size
    @param rem: (C++: const char *) string to be removed from list, can be nullptr
    @param ignorecase: (C++: bool) ignore case for 'add' and 'rem'
    """
    return _ida_registry.reg_update_strlist(*args)

def reg_write_string(*args) -> "void":
    r"""
    reg_write_string(name, utf8, subkey=None)
    Write a string to the registry.

    @param name: (C++: const char *) value name
    @param utf8: (C++: const char *) utf8-encoded string
    @param subkey: (C++: const char *) key name
    """
    return _ida_registry.reg_write_string(*args)

def reg_read_int(*args) -> "int":
    r"""
    reg_read_int(name, defval, subkey=None) -> int
    Read integer value from the registry.

    @param name: (C++: const char *) value name
    @param defval: (C++: int) default value
    @param subkey: (C++: const char *) key name
    @return: the value read from the registry, or 'defval' if the read failed
    """
    return _ida_registry.reg_read_int(*args)

def reg_write_int(*args) -> "void":
    r"""
    reg_write_int(name, value, subkey=None)
    Write integer value to the registry.

    @param name: (C++: const char *) value name
    @param value: (C++: int) value to write
    @param subkey: (C++: const char *) key name
    """
    return _ida_registry.reg_write_int(*args)

def reg_read_bool(*args) -> "bool":
    r"""
    reg_read_bool(name, defval, subkey=None) -> bool
    Read boolean value from the registry.

    @param name: (C++: const char *) value name
    @param defval: (C++: bool) default value
    @param subkey: (C++: const char *) key name
    @return: boolean read from registry, or 'defval' if the read failed
    """
    return _ida_registry.reg_read_bool(*args)

def reg_write_bool(*args) -> "void":
    r"""
    reg_write_bool(name, value, subkey=None)
    Write boolean value to the registry.

    @param name: (C++: const char *) value name
    @param value: (C++: int) boolean to write (nonzero = true)
    @param subkey: (C++: const char *) key name
    """
    return _ida_registry.reg_write_bool(*args)

def reg_update_filestrlist(*args) -> "void":
    r"""
    reg_update_filestrlist(subkey, add, maxrecs, rem=None)
    Update registry with a file list. Case sensitivity will vary depending on the
    target OS.
    @note: 'add' and 'rem' must be UTF-8, just like for regular string operations.

    @param subkey: (C++: const char *) char const *
    @param add: (C++: const char *) char const *
    @param maxrecs: (C++: size_t)
    @param rem: (C++: const char *) char const *
    """
    return _ida_registry.reg_update_filestrlist(*args)

def reg_load(*args) -> "void":
    r"""
    reg_load()
    """
    return _ida_registry.reg_load(*args)

def reg_flush(*args) -> "void":
    r"""
    reg_flush()
    """
    return _ida_registry.reg_flush(*args)



