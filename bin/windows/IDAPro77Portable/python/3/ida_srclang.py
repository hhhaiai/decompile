"""
Third-party compiler support."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_srclang
else:
    import _ida_srclang

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

SWIG_PYTHON_LEGACY_BOOL = _ida_srclang.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

SRCLANG_C = _ida_srclang.SRCLANG_C
r"""
C.
"""

SRCLANG_CPP = _ida_srclang.SRCLANG_CPP
r"""
C++.
"""

SRCLANG_OBJC = _ida_srclang.SRCLANG_OBJC
r"""
Objective-C.
"""

SRCLANG_SWIFT = _ida_srclang.SRCLANG_SWIFT
r"""
Swift (not supported yet)
"""

SRCLANG_GO = _ida_srclang.SRCLANG_GO
r"""
Golang (not supported yet)
"""


def select_parser_by_name(*args) -> "bool":
    r"""
    select_parser_by_name(name) -> bool
    Set the parser with the given name as the current parser. Pass nullptr or an
    empty string to select the default parser.

    @param name: (C++: const char *) char const *
    @return: false if no parser was found with the given name
    """
    return _ida_srclang.select_parser_by_name(*args)

def select_parser_by_srclang(*args) -> "bool":
    r"""
    select_parser_by_srclang(lang) -> bool
    Set the parser that supports the given language(s) as the current parser. The
    selected parser must support all languages specified by the given srclang_t.

    @param lang: (C++: srclang_t)
    @return: false if no such parser was found
    """
    return _ida_srclang.select_parser_by_srclang(*args)

def set_parser_argv(*args) -> "int":
    r"""
    set_parser_argv(parser_name, argv) -> int
    Set the command-line args to use for invocations of the parser with the given
    name

    @param parser_name: (C++: const char *) name of the target parser
    @param argv: (C++: const char *) argument list
    @retval -1: no parser was found with the given name
    @retval -2: the operation is not supported by the given parser
    @retval 0: success
    """
    return _ida_srclang.set_parser_argv(*args)

def parse_decls_for_srclang(*args) -> "int":
    r"""
    parse_decls_for_srclang(lang, til, input, is_path) -> int
    Parse type declarations in the specified language

    @param lang: (C++: srclang_t) the source language(s) expected in the input
    @param til: (C++: til_t *) type library to store the types
    @param input: (C++: const char *) input source. can be a file path or decl string
    @param is_path: (C++: bool) true if input parameter is a path to a source file, false if the
                    input is an in-memory source snippet
    @retval -1: no parser was found that supports the given source language(s)
    @retval else: the number of errors encountered in the input source
    """
    return _ida_srclang.parse_decls_for_srclang(*args)

def parse_decls_with_parser(*args) -> "int":
    r"""
    parse_decls_with_parser(parser_name, til, input, is_path) -> int
    Parse type declarations using the parser with the specified name

    @param parser_name: (C++: const char *) name of the target parser
    @param til: (C++: til_t *) type library to store the types
    @param input: (C++: const char *) input source. can be a file path or decl string
    @param is_path: (C++: bool) true if input parameter is a path to a source file, false if the
                    input is an in-memory source snippet
    @retval -1: no parser was found with the given name
    @retval else: the number of errors encountered in the input source
    """
    return _ida_srclang.parse_decls_with_parser(*args)



