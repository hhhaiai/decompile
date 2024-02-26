"""
System independent counterparts of FILE* related functions from Clib.

You should not use C standard I/O functions in your modules. The reason: Each
module compiled with Borland (and statically linked to Borland's library) will
host a copy of the FILE * information.

So, if you open a file in the plugin and pass the handle to the kernel, the
kernel will not be able to use it.

If you really need to use the standard functions, define
USE_STANDARD_FILE_FUNCTIONS. In this case do not mix them with q... functions."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_fpro
else:
    import _ida_fpro

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

SWIG_PYTHON_LEGACY_BOOL = _ida_fpro.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class qfile_t(object):
    r"""
    A helper class to work with FILE related functions.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __idc_cvt_id__ = property(_ida_fpro.qfile_t___idc_cvt_id___get, _ida_fpro.qfile_t___idc_cvt_id___set, doc=r"""__idc_cvt_id__""")

    def __init__(self, *args):
        r"""
        __init__(self, rhs) -> qfile_t

        @param rhs: qfile_t const &

        __init__(self, pycapsule=None) -> qfile_t

        @param pycapsule: PyObject *
        """
        _ida_fpro.qfile_t_swiginit(self, _ida_fpro.new_qfile_t(*args))

    def opened(self, *args) -> "bool":
        r"""
        opened(self) -> bool
        Checks if the file is opened or not
        """
        return _ida_fpro.qfile_t_opened(self, *args)

    def close(self, *args) -> "void":
        r"""
        close(self)
        Closes the file
        """
        return _ida_fpro.qfile_t_close(self, *args)
    __swig_destroy__ = _ida_fpro.delete_qfile_t

    def open(self, *args) -> "bool":
        r"""
        open(self, filename, mode) -> bool
        Opens a file

        @param filename: the file name
        @param mode: The mode string, ala fopen() style
        @return: Boolean
        """
        return _ida_fpro.qfile_t_open(self, *args)

    @staticmethod
    def from_fp(*args) -> "qfile_t *":
        r"""
        from_fp(fp) -> qfile_t

        @param fp: FILE *
        """
        return _ida_fpro.qfile_t_from_fp(*args)

    @staticmethod
    def from_capsule(*args) -> "qfile_t *":
        r"""
        from_capsule(pycapsule) -> qfile_t

        @param pycapsule: PyObject *
        """
        return _ida_fpro.qfile_t_from_capsule(*args)

    @staticmethod
    def tmpfile(*args) -> "qfile_t *":
        r"""
        tmpfile() -> qfile_t
        A static method to construct an instance using a temporary file
        """
        return _ida_fpro.qfile_t_tmpfile(*args)

    def get_fp(self, *args) -> "FILE *":
        r"""
        get_fp(self) -> FILE *
        """
        return _ida_fpro.qfile_t_get_fp(self, *args)

    def seek(self, *args) -> "int":
        r"""
        seek(self, offset, whence=SEEK_SET) -> int
        Set input source position

        @param offset: int64
        @param whence: int
        @return: the new position (not 0 as fseek!)
        """
        return _ida_fpro.qfile_t_seek(self, *args)

    def tell(self, *args) -> "int64":
        r"""
        tell(self) -> int64
        Returns the current position
        """
        return _ida_fpro.qfile_t_tell(self, *args)

    def readbytes(self, *args) -> "PyObject *":
        r"""
        readbytes(self, size, big_endian) -> PyObject *
        Similar to read() but it respect the endianness

        @param size: int
        @param big_endian: bool
        """
        return _ida_fpro.qfile_t_readbytes(self, *args)

    def read(self, *args) -> "PyObject *":
        r"""
        read(self, size) -> PyObject *
        Reads from the file. Returns the buffer or None

        @param size: int
        """
        return _ida_fpro.qfile_t_read(self, *args)

    def gets(self, *args) -> "PyObject *":
        r"""
        gets(self, size) -> PyObject *
        Reads a line from the input file. Returns the read line or None

        @param size: int
        """
        return _ida_fpro.qfile_t_gets(self, *args)

    def writebytes(self, *args) -> "int":
        r"""
        writebytes(self, py_buf, big_endian) -> int
        Similar to write() but it respect the endianness

        @param py_buf: PyObject *
        @param big_endian: bool
        """
        return _ida_fpro.qfile_t_writebytes(self, *args)

    def write(self, *args) -> "int":
        r"""
        write(self, py_buf) -> int
        Writes to the file. Returns 0 or the number of bytes written

        @param py_buf: PyObject *
        """
        return _ida_fpro.qfile_t_write(self, *args)

    def puts(self, *args) -> "int":
        r"""
        puts(self, str) -> int

        @param str: char const *
        """
        return _ida_fpro.qfile_t_puts(self, *args)

    def size(self, *args) -> "int64":
        r"""
        size(self) -> int64
        """
        return _ida_fpro.qfile_t_size(self, *args)

    def flush(self, *args) -> "int":
        r"""
        flush(self) -> int
        """
        return _ida_fpro.qfile_t_flush(self, *args)

    def filename(self, *args) -> "PyObject *":
        r"""
        filename(self) -> PyObject *
        """
        return _ida_fpro.qfile_t_filename(self, *args)

    def get_byte(self, *args) -> "PyObject *":
        r"""
        get_byte(self) -> PyObject *
        Reads a single byte from the file. Returns None if EOF or the read byte
        """
        return _ida_fpro.qfile_t_get_byte(self, *args)

    def put_byte(self, *args) -> "int":
        r"""
        put_byte(self, chr) -> int
        Writes a single byte to the file

        @param chr: int
        """
        return _ida_fpro.qfile_t_put_byte(self, *args)

# Register qfile_t in _ida_fpro:
_ida_fpro.qfile_t_swigregister(qfile_t)

def qfile_t_from_fp(*args) -> "qfile_t *":
    r"""
    qfile_t_from_fp(fp) -> qfile_t

    @param fp: FILE *
    """
    return _ida_fpro.qfile_t_from_fp(*args)

def qfile_t_from_capsule(*args) -> "qfile_t *":
    r"""
    qfile_t_from_capsule(pycapsule) -> qfile_t

    @param pycapsule: PyObject *
    """
    return _ida_fpro.qfile_t_from_capsule(*args)

def qfile_t_tmpfile(*args) -> "qfile_t *":
    r"""
    qfile_t_tmpfile() -> qfile_t
    """
    return _ida_fpro.qfile_t_tmpfile(*args)




