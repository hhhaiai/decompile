"""
This is the first header included in the IDA project.

It defines the most common types, functions and data. Also, it tries to make
system dependent definitions.

The following preprocessor macros are used in the project (the list may be
incomplete)

Platform must be specified as one of:

__NT__ - MS Windows (all platforms)
__LINUX__ - Linux
__MAC__ - MAC OS X

__EA64__ - 64-bit address size (sizeof(ea_t)==8)
__X86__ - 32-bit debug servers (sizeof(void*)==4)
__X64__ - x64 processor (sizeof(void*)==8) default
__PPC__ - PowerPC
__ARM__ - ARM"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_pro
else:
    import _ida_pro

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

SWIG_PYTHON_LEGACY_BOOL = _ida_pro.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

BADDIFF = _ida_pro.BADDIFF

IDA_SDK_VERSION = _ida_pro.IDA_SDK_VERSION
r"""
IDA SDK v7.7.
"""

BADMEMSIZE = _ida_pro.BADMEMSIZE

MAXSTR = _ida_pro.MAXSTR
r"""
maximum string size
"""

__MF__ = _ida_pro.__MF__
r"""
byte sex of our platform (Most significant byte First). 0: little endian (Intel
80x86). 1: big endian (PowerPC).
"""


def qatoll(*args):
    r"""
    qatoll(nptr) -> int64

    @param nptr: char const *
    """
    return _ida_pro.qatoll(*args)
FMT_64 = _ida_pro.FMT_64

FMT_Z = _ida_pro.FMT_Z

FMT_ZX = _ida_pro.FMT_ZX

FMT_ZS = _ida_pro.FMT_ZS

FMT_EA = _ida_pro.FMT_EA


def qexit(*args):
    r"""
    qexit(code)
    Call qatexit functions, shut down UI and kernel, and exit.

    @param code: (C++: int) exit code
    """
    return _ida_pro.qexit(*args)

def set_bits(*args):
    r"""
    set_bits(bitmap, low, high)
    Set bits between [low, high) in 'bitmap'.

    @param bitmap: (C++: uchar *)
    @param low: (C++: size_t)
    @param high: (C++: size_t)
    """
    return _ida_pro.set_bits(*args)

def clear_bits(*args):
    r"""
    clear_bits(bitmap, low, high)
    Clear bits between [low, high) in 'bitmap'.

    @param bitmap: (C++: uchar *)
    @param low: (C++: size_t)
    @param high: (C++: size_t)
    """
    return _ida_pro.clear_bits(*args)

def log2ceil(*args):
    r"""
    log2ceil(d64) -> int
    calculate ceil(log2(d64)) or floor(log2(d64)), it returns 0 if d64 == 0

    @param d64: (C++: uint64)
    """
    return _ida_pro.log2ceil(*args)

def log2floor(*args):
    r"""
    log2floor(d64) -> int

    @param d64: uint64
    """
    return _ida_pro.log2floor(*args)

def extend_sign(*args):
    r"""
    extend_sign(v, nbytes, sign_extend) -> uint64
    Sign-, or zero-extend the value 'v' to occupy 64 bits. The value 'v' is
    considered to be of size 'nbytes'.

    @param v: (C++: uint64)
    @param nbytes: (C++: int)
    @param sign_extend: (C++: bool)
    """
    return _ida_pro.extend_sign(*args)

def readbytes(*args):
    r"""
    readbytes(h, res, size, mf) -> int
    Read at most 4 bytes from file.

    @param h: (C++: int) file handle
    @param res: (C++: uint32 *) value read from file
    @param size: (C++: int) size of value in bytes (1,2,4)
    @param mf: (C++: bool) is MSB first?
    @return: 0 on success, nonzero otherwise
    """
    return _ida_pro.readbytes(*args)

def writebytes(*args):
    r"""
    writebytes(h, l, size, mf) -> int
    Write at most 4 bytes to file.

    @param h: (C++: int) file handle
    @param l: (C++: uint32) value to write
    @param size: (C++: int) size of value in bytes (1,2,4)
    @param mf: (C++: bool) is MSB first?
    @return: 0 on success, nonzero otherwise
    """
    return _ida_pro.writebytes(*args)

def reloc_value(*args):
    r"""
    reloc_value(value, size, delta, mf)

    @param value: void *
    @param size: int
    @param delta: adiff_t
    @param mf: bool
    """
    return _ida_pro.reloc_value(*args)

def qvector_reserve(*args):
    r"""
    qvector_reserve(vec, old, cnt, elsize) -> void *
    Change capacity of given qvector.

    @param vec: (C++: void *) a pointer to a qvector
    @param old: (C++: void *) a pointer to the qvector's array
    @param cnt: (C++: size_t) number of elements to reserve
    @param elsize: (C++: size_t) size of each element
    @return: a pointer to the newly allocated array
    """
    return _ida_pro.qvector_reserve(*args)
class qrefcnt_obj_t(object):
    r"""
    Proxy of C++ qrefcnt_obj_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    refcnt = property(_ida_pro.qrefcnt_obj_t_refcnt_get, _ida_pro.qrefcnt_obj_t_refcnt_set, doc=r"""refcnt""")
    r"""
    counter
    """

    def release(self, *args):
        r"""
        release(self)
        Call destructor. We use release() instead of operator delete() to maintain
        binary compatibility with all compilers (vc and gcc use different vtable layouts
        for operator delete)
        """
        return _ida_pro.qrefcnt_obj_t_release(self, *args)
    __swig_destroy__ = _ida_pro.delete_qrefcnt_obj_t

# Register qrefcnt_obj_t in _ida_pro:
_ida_pro.qrefcnt_obj_t_swigregister(qrefcnt_obj_t)


def relocate_relobj(*args):
    r"""
    relocate_relobj(_relobj, ea, mf) -> bool

    @param _relobj: relobj_t *
    @param ea: ea_t
    @param mf: bool
    """
    return _ida_pro.relocate_relobj(*args)
IDBDEC_ESCAPE = _ida_pro.IDBDEC_ESCAPE
r"""
convert non-printable characters to C escapes (
, \xNN, \uNNNN)
"""

CP_ACP = _ida_pro.CP_ACP

CP_OEM = _ida_pro.CP_OEM

CP_UTF8 = _ida_pro.CP_UTF8

CP_BOM = _ida_pro.CP_BOM

UTF8_BOM = _ida_pro.UTF8_BOM

UTF16LE_BOM = _ida_pro.UTF16LE_BOM

UTF16BE_BOM = _ida_pro.UTF16BE_BOM

UTF32LE_BOM = _ida_pro.UTF32LE_BOM

UTF32BE_BOM = _ida_pro.UTF32BE_BOM

CP_ELLIPSIS = _ida_pro.CP_ELLIPSIS

UTF8_ELLIPSIS = _ida_pro.UTF8_ELLIPSIS

CP_REPLCHAR = _ida_pro.CP_REPLCHAR

UTF8_REPLCHAR = _ida_pro.UTF8_REPLCHAR

MAX_UTF8_SEQ_LEN = _ida_pro.MAX_UTF8_SEQ_LEN

CEF_RETERR = _ida_pro.CEF_RETERR

ENC_WIN1252 = _ida_pro.ENC_WIN1252

ENC_UTF8 = _ida_pro.ENC_UTF8

ENC_MUTF8 = _ida_pro.ENC_MUTF8

ENC_UTF16 = _ida_pro.ENC_UTF16

ENC_UTF16LE = _ida_pro.ENC_UTF16LE

ENC_UTF16BE = _ida_pro.ENC_UTF16BE

ENC_UTF32 = _ida_pro.ENC_UTF32

ENC_UTF32LE = _ida_pro.ENC_UTF32LE

ENC_UTF32BE = _ida_pro.ENC_UTF32BE

CP_UTF16 = _ida_pro.CP_UTF16
r"""
UTF-16 codepage.
"""

SUBSTCHAR = _ida_pro.SUBSTCHAR
r"""
default char, used if a char cannot be represented in a codepage
"""

class channel_redir_t(object):
    r"""
    Proxy of C++ channel_redir_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    fd = property(_ida_pro.channel_redir_t_fd_get, _ida_pro.channel_redir_t_fd_set, doc=r"""fd""")
    r"""
    channel number
    """
    file = property(_ida_pro.channel_redir_t_file_get, _ida_pro.channel_redir_t_file_set, doc=r"""file""")
    r"""
    file name to redirect to/from. if empty, the channel must be closed.
    """
    flags = property(_ida_pro.channel_redir_t_flags_get, _ida_pro.channel_redir_t_flags_set, doc=r"""flags""")
    r"""
    i/o redirection flags
    """

    def is_input(self, *args):
        r"""
        is_input(self) -> bool
        """
        return _ida_pro.channel_redir_t_is_input(self, *args)

    def is_output(self, *args):
        r"""
        is_output(self) -> bool
        """
        return _ida_pro.channel_redir_t_is_output(self, *args)

    def is_append(self, *args):
        r"""
        is_append(self) -> bool
        """
        return _ida_pro.channel_redir_t_is_append(self, *args)

    def is_quoted(self, *args):
        r"""
        is_quoted(self) -> bool
        """
        return _ida_pro.channel_redir_t_is_quoted(self, *args)
    start = property(_ida_pro.channel_redir_t_start_get, _ida_pro.channel_redir_t_start_set, doc=r"""start""")
    r"""
    begin of the redirection string in the command line
    """
    length = property(_ida_pro.channel_redir_t_length_get, _ida_pro.channel_redir_t_length_set, doc=r"""length""")
    r"""
    length of the redirection string in the command line
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> channel_redir_t
        """
        _ida_pro.channel_redir_t_swiginit(self, _ida_pro.new_channel_redir_t(*args))
    __swig_destroy__ = _ida_pro.delete_channel_redir_t

# Register channel_redir_t in _ida_pro:
_ida_pro.channel_redir_t_swigregister(channel_redir_t)
IOREDIR_INPUT = _ida_pro.IOREDIR_INPUT
r"""
input redirection
"""

IOREDIR_OUTPUT = _ida_pro.IOREDIR_OUTPUT
r"""
output redirection
"""

IOREDIR_APPEND = _ida_pro.IOREDIR_APPEND
r"""
append, do not overwrite the output file
"""

IOREDIR_QUOTED = _ida_pro.IOREDIR_QUOTED
r"""
the file name was quoted
"""



def quote_cmdline_arg(*args):
    r"""
    quote_cmdline_arg(arg) -> bool
    Quote a command line argument if it contains escape characters. For example, *.c
    will be converted into "*.c" because * may be inadvertently expanded by the
    shell

    @param arg: (C++: qstring *)
    @return: true: modified 'arg'
    """
    return _ida_pro.quote_cmdline_arg(*args)
class instant_dbgopts_t(object):
    r"""
    Proxy of C++ instant_dbgopts_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    debmod = property(_ida_pro.instant_dbgopts_t_debmod_get, _ida_pro.instant_dbgopts_t_debmod_set, doc=r"""debmod""")
    r"""
    name of debugger module
    """
    env = property(_ida_pro.instant_dbgopts_t_env_get, _ida_pro.instant_dbgopts_t_env_set, doc=r"""env""")
    r"""
    config variables for debmod. example: DEFAULT_CPU=13;MAXPACKETSIZE=-1
    """
    host = property(_ida_pro.instant_dbgopts_t_host_get, _ida_pro.instant_dbgopts_t_host_set, doc=r"""host""")
    r"""
    remote hostname (if remote debugging)
    """
    _pass = property(_ida_pro.instant_dbgopts_t__pass_get, _ida_pro.instant_dbgopts_t__pass_set, doc=r"""_pass""")
    port = property(_ida_pro.instant_dbgopts_t_port_get, _ida_pro.instant_dbgopts_t_port_set, doc=r"""port""")
    r"""
    port number for the remote debugger server
    """
    pid = property(_ida_pro.instant_dbgopts_t_pid_get, _ida_pro.instant_dbgopts_t_pid_set, doc=r"""pid""")
    r"""
    process to attach to (-1: ask the user)
    """
    event_id = property(_ida_pro.instant_dbgopts_t_event_id_get, _ida_pro.instant_dbgopts_t_event_id_set, doc=r"""event_id""")
    r"""
    event to trigger upon attaching
    """
    attach = property(_ida_pro.instant_dbgopts_t_attach_get, _ida_pro.instant_dbgopts_t_attach_set, doc=r"""attach""")
    r"""
    should attach to a process?
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> instant_dbgopts_t
        """
        _ida_pro.instant_dbgopts_t_swiginit(self, _ida_pro.new_instant_dbgopts_t(*args))
    __swig_destroy__ = _ida_pro.delete_instant_dbgopts_t

# Register instant_dbgopts_t in _ida_pro:
_ida_pro.instant_dbgopts_t_swigregister(instant_dbgopts_t)


def parse_dbgopts(*args):
    r"""
    parse_dbgopts(ido, r_switch) -> bool
    Parse the -r command line switch (for instant debugging). r_switch points to the
    value of the -r switch. Example: win32@localhost+

    @param ido: (C++: struct instant_dbgopts_t *) instant_dbgopts_t *
    @param r_switch: (C++: const char *) char const *
    @return: true-ok, false-parse error
    """
    return _ida_pro.parse_dbgopts(*args)

def check_process_exit(*args):
    r"""
    check_process_exit(handle, exit_code, msecs=-1) -> int
    Check whether process has terminated or not.

    @param handle: (C++: void *) process handle to wait for
    @param exit_code: (C++: int *) pointer to the buffer for the exit code
    @param msecs: how long to wait. special values:
    * 0: do not wait
    * 1 or -1: wait infinitely
    * other values: timeout in milliseconds
    @retval 0: process has exited, and the exit code is available. if *exit_code <
               0: the process was killed with a signal -*exit_code
    @retval 1: process has not exited yet
    @retval -1: error happened, see error code for winerr() in *exit_code
    """
    return _ida_pro.check_process_exit(*args)
TCT_UNKNOWN = _ida_pro.TCT_UNKNOWN

TCT_OWNER = _ida_pro.TCT_OWNER

TCT_NOT_OWNER = _ida_pro.TCT_NOT_OWNER


def is_control_tty(*args):
    r"""
    is_control_tty(fd) -> enum tty_control_t
    Check if the current process is the owner of the TTY specified by 'fd'
    (typically an opened descriptor to /dev/tty).

    @param fd: (C++: int)
    """
    return _ida_pro.is_control_tty(*args)

def qdetach_tty(*args):
    r"""
    qdetach_tty()
    If the current terminal is the controlling terminal of the calling process, give
    up this controlling terminal.
    @note: The current terminal is supposed to be /dev/tty
    """
    return _ida_pro.qdetach_tty(*args)

def qcontrol_tty(*args):
    r"""
    qcontrol_tty()
    Make the current terminal the controlling terminal of the calling process.
    @note: The current terminal is supposed to be /dev/tty
    """
    return _ida_pro.qcontrol_tty(*args)
class __qthread_t(object):
    r"""
    Proxy of C++ __qthread_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> __qthread_t
        """
        _ida_pro.__qthread_t_swiginit(self, _ida_pro.new___qthread_t(*args))
    __swig_destroy__ = _ida_pro.delete___qthread_t

# Register __qthread_t in _ida_pro:
_ida_pro.__qthread_t_swigregister(__qthread_t)


def qthread_equal(*args):
    r"""
    qthread_equal(q1, q2) -> bool
    Are two threads equal?

    @param q1: (C++: qthread_t)
    @param q2: (C++: qthread_t)
    """
    return _ida_pro.qthread_equal(*args)

def is_main_thread(*args):
    r"""
    is_main_thread() -> bool
    Are we running in the main thread?
    """
    return _ida_pro.is_main_thread(*args)
class __qsemaphore_t(object):
    r"""
    Proxy of C++ __qsemaphore_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> __qsemaphore_t
        """
        _ida_pro.__qsemaphore_t_swiginit(self, _ida_pro.new___qsemaphore_t(*args))
    __swig_destroy__ = _ida_pro.delete___qsemaphore_t

# Register __qsemaphore_t in _ida_pro:
_ida_pro.__qsemaphore_t_swigregister(__qsemaphore_t)

class __qmutex_t(object):
    r"""
    Proxy of C++ __qmutex_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> __qmutex_t
        """
        _ida_pro.__qmutex_t_swiginit(self, _ida_pro.new___qmutex_t(*args))
    __swig_destroy__ = _ida_pro.delete___qmutex_t

# Register __qmutex_t in _ida_pro:
_ida_pro.__qmutex_t_swigregister(__qmutex_t)

class qmutex_locker_t(object):
    r"""
    Proxy of C++ qmutex_locker_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, _lock) -> qmutex_locker_t

        @param _lock: qmutex_t
        """
        _ida_pro.qmutex_locker_t_swiginit(self, _ida_pro.new_qmutex_locker_t(*args))
    __swig_destroy__ = _ida_pro.delete_qmutex_locker_t

# Register qmutex_locker_t in _ida_pro:
_ida_pro.qmutex_locker_t_swigregister(qmutex_locker_t)

class intvec_t(object):
    r"""
    Proxy of C++ qvector< int > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> intvec_t
        __init__(self, x) -> intvec_t

        @param x: qvector< int > const &
        """
        _ida_pro.intvec_t_swiginit(self, _ida_pro.new_intvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_intvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: int const &

        push_back(self) -> int &
        """
        return _ida_pro.intvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.intvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.intvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.intvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> int const &

        @param _idx: size_t
        """
        return _ida_pro.intvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.intvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.intvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: int const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.intvec_t_resize(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.intvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.intvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.intvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< int > &
        """
        return _ida_pro.intvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> int *
        """
        return _ida_pro.intvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: int *
        @param len: size_t
        """
        return _ida_pro.intvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< int > const &
        """
        return _ida_pro.intvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< int > const &
        """
        return _ida_pro.intvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< int >::iterator
        begin(self) -> qvector< int >::const_iterator
        """
        return _ida_pro.intvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< int >::iterator
        end(self) -> qvector< int >::const_iterator
        """
        return _ida_pro.intvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< int >::iterator

        @param it: qvector< int >::iterator
        @param x: int const &
        """
        return _ida_pro.intvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< int >::iterator

        @param it: qvector< int >::iterator

        erase(self, first, last) -> qvector< int >::iterator

        @param first: qvector< int >::iterator
        @param last: qvector< int >::iterator
        """
        return _ida_pro.intvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< int >::iterator

        @param x: int const &

        find(self, x) -> qvector< int >::const_iterator

        @param x: int const &
        """
        return _ida_pro.intvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: int const &
        """
        return _ida_pro.intvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: int const &
        """
        return _ida_pro.intvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: int const &

        """
        return _ida_pro.intvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.intvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> int const &

        @param i: size_t
        """
        return _ida_pro.intvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: int const &
        """
        return _ida_pro.intvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register intvec_t in _ida_pro:
_ida_pro.intvec_t_swigregister(intvec_t)
cvar = _ida_pro.cvar
NULL_PIPE_HANDLE = cvar.NULL_PIPE_HANDLE

class uintvec_t(object):
    r"""
    Proxy of C++ qvector< unsigned int > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> uintvec_t
        __init__(self, x) -> uintvec_t

        @param x: qvector< unsigned int > const &
        """
        _ida_pro.uintvec_t_swiginit(self, _ida_pro.new_uintvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_uintvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: unsigned int const &

        push_back(self) -> unsigned int &
        """
        return _ida_pro.uintvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.uintvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.uintvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.uintvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> unsigned int const &

        @param _idx: size_t
        """
        return _ida_pro.uintvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.uintvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.uintvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: unsigned int const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.uintvec_t_resize(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.uintvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.uintvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.uintvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< unsigned int > &
        """
        return _ida_pro.uintvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> unsigned int *
        """
        return _ida_pro.uintvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: unsigned int *
        @param len: size_t
        """
        return _ida_pro.uintvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< unsigned int > const &
        """
        return _ida_pro.uintvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< unsigned int > const &
        """
        return _ida_pro.uintvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< unsigned int >::iterator
        begin(self) -> qvector< unsigned int >::const_iterator
        """
        return _ida_pro.uintvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< unsigned int >::iterator
        end(self) -> qvector< unsigned int >::const_iterator
        """
        return _ida_pro.uintvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< unsigned int >::iterator

        @param it: qvector< unsigned int >::iterator
        @param x: unsigned int const &
        """
        return _ida_pro.uintvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< unsigned int >::iterator

        @param it: qvector< unsigned int >::iterator

        erase(self, first, last) -> qvector< unsigned int >::iterator

        @param first: qvector< unsigned int >::iterator
        @param last: qvector< unsigned int >::iterator
        """
        return _ida_pro.uintvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< unsigned int >::iterator

        @param x: unsigned int const &

        find(self, x) -> qvector< unsigned int >::const_iterator

        @param x: unsigned int const &
        """
        return _ida_pro.uintvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: unsigned int const &
        """
        return _ida_pro.uintvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: unsigned int const &
        """
        return _ida_pro.uintvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: unsigned int const &

        """
        return _ida_pro.uintvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.uintvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> unsigned int const &

        @param i: size_t
        """
        return _ida_pro.uintvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: unsigned int const &
        """
        return _ida_pro.uintvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register uintvec_t in _ida_pro:
_ida_pro.uintvec_t_swigregister(uintvec_t)

class longlongvec_t(object):
    r"""
    Proxy of C++ qvector< long long > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> longlongvec_t
        __init__(self, x) -> longlongvec_t

        @param x: qvector< long long > const &
        """
        _ida_pro.longlongvec_t_swiginit(self, _ida_pro.new_longlongvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_longlongvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: long long const &

        push_back(self) -> long long &
        """
        return _ida_pro.longlongvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.longlongvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.longlongvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.longlongvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> long long const &

        @param _idx: size_t
        """
        return _ida_pro.longlongvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.longlongvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.longlongvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: long long const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.longlongvec_t_resize(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.longlongvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.longlongvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.longlongvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< long long > &
        """
        return _ida_pro.longlongvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> long long *
        """
        return _ida_pro.longlongvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: long long *
        @param len: size_t
        """
        return _ida_pro.longlongvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< long long > const &
        """
        return _ida_pro.longlongvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< long long > const &
        """
        return _ida_pro.longlongvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< long long >::iterator
        begin(self) -> qvector< long long >::const_iterator
        """
        return _ida_pro.longlongvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< long long >::iterator
        end(self) -> qvector< long long >::const_iterator
        """
        return _ida_pro.longlongvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< long long >::iterator

        @param it: qvector< long long >::iterator
        @param x: long long const &
        """
        return _ida_pro.longlongvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< long long >::iterator

        @param it: qvector< long long >::iterator

        erase(self, first, last) -> qvector< long long >::iterator

        @param first: qvector< long long >::iterator
        @param last: qvector< long long >::iterator
        """
        return _ida_pro.longlongvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< long long >::iterator

        @param x: long long const &

        find(self, x) -> qvector< long long >::const_iterator

        @param x: long long const &
        """
        return _ida_pro.longlongvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: long long const &
        """
        return _ida_pro.longlongvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: long long const &
        """
        return _ida_pro.longlongvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: long long const &

        """
        return _ida_pro.longlongvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.longlongvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> long long const &

        @param i: size_t
        """
        return _ida_pro.longlongvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: long long const &
        """
        return _ida_pro.longlongvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register longlongvec_t in _ida_pro:
_ida_pro.longlongvec_t_swigregister(longlongvec_t)

class ulonglongvec_t(object):
    r"""
    Proxy of C++ qvector< unsigned long long > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> ulonglongvec_t
        __init__(self, x) -> ulonglongvec_t

        @param x: qvector< unsigned long long > const &
        """
        _ida_pro.ulonglongvec_t_swiginit(self, _ida_pro.new_ulonglongvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_ulonglongvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: unsigned long long const &

        push_back(self) -> unsigned long long &
        """
        return _ida_pro.ulonglongvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.ulonglongvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.ulonglongvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.ulonglongvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> unsigned long long const &

        @param _idx: size_t
        """
        return _ida_pro.ulonglongvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.ulonglongvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.ulonglongvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: unsigned long long const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.ulonglongvec_t_resize(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.ulonglongvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.ulonglongvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.ulonglongvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< unsigned long long > &
        """
        return _ida_pro.ulonglongvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> unsigned long long *
        """
        return _ida_pro.ulonglongvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: unsigned long long *
        @param len: size_t
        """
        return _ida_pro.ulonglongvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< unsigned long long > const &
        """
        return _ida_pro.ulonglongvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< unsigned long long > const &
        """
        return _ida_pro.ulonglongvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< unsigned long long >::iterator
        begin(self) -> qvector< unsigned long long >::const_iterator
        """
        return _ida_pro.ulonglongvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< unsigned long long >::iterator
        end(self) -> qvector< unsigned long long >::const_iterator
        """
        return _ida_pro.ulonglongvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< unsigned long long >::iterator

        @param it: qvector< unsigned long long >::iterator
        @param x: unsigned long long const &
        """
        return _ida_pro.ulonglongvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< unsigned long long >::iterator

        @param it: qvector< unsigned long long >::iterator

        erase(self, first, last) -> qvector< unsigned long long >::iterator

        @param first: qvector< unsigned long long >::iterator
        @param last: qvector< unsigned long long >::iterator
        """
        return _ida_pro.ulonglongvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< unsigned long long >::iterator

        @param x: unsigned long long const &

        find(self, x) -> qvector< unsigned long long >::const_iterator

        @param x: unsigned long long const &
        """
        return _ida_pro.ulonglongvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: unsigned long long const &
        """
        return _ida_pro.ulonglongvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: unsigned long long const &
        """
        return _ida_pro.ulonglongvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: unsigned long long const &

        """
        return _ida_pro.ulonglongvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.ulonglongvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> unsigned long long const &

        @param i: size_t
        """
        return _ida_pro.ulonglongvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: unsigned long long const &
        """
        return _ida_pro.ulonglongvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register ulonglongvec_t in _ida_pro:
_ida_pro.ulonglongvec_t_swigregister(ulonglongvec_t)

class boolvec_t(object):
    r"""
    Proxy of C++ qvector< bool > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> boolvec_t
        __init__(self, x) -> boolvec_t

        @param x: qvector< bool > const &
        """
        _ida_pro.boolvec_t_swiginit(self, _ida_pro.new_boolvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_boolvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: bool const &

        push_back(self) -> bool &
        """
        return _ida_pro.boolvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.boolvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.boolvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.boolvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> bool const &

        @param _idx: size_t
        """
        return _ida_pro.boolvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.boolvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.boolvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: bool const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.boolvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=bool())

        @param x: bool const &
        """
        return _ida_pro.boolvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.boolvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.boolvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.boolvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< bool > &
        """
        return _ida_pro.boolvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> bool *
        """
        return _ida_pro.boolvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: bool *
        @param len: size_t
        """
        return _ida_pro.boolvec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< bool > const &
        """
        return _ida_pro.boolvec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< bool > const &
        """
        return _ida_pro.boolvec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< bool >::iterator
        begin(self) -> qvector< bool >::const_iterator
        """
        return _ida_pro.boolvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< bool >::iterator
        end(self) -> qvector< bool >::const_iterator
        """
        return _ida_pro.boolvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< bool >::iterator

        @param it: qvector< bool >::iterator
        @param x: bool const &
        """
        return _ida_pro.boolvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< bool >::iterator

        @param it: qvector< bool >::iterator

        erase(self, first, last) -> qvector< bool >::iterator

        @param first: qvector< bool >::iterator
        @param last: qvector< bool >::iterator
        """
        return _ida_pro.boolvec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< bool >::iterator

        @param x: bool const &

        find(self, x) -> qvector< bool >::const_iterator

        @param x: bool const &
        """
        return _ida_pro.boolvec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: bool const &
        """
        return _ida_pro.boolvec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: bool const &
        """
        return _ida_pro.boolvec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: bool const &

        """
        return _ida_pro.boolvec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.boolvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> bool const &

        @param i: size_t
        """
        return _ida_pro.boolvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: bool const &
        """
        return _ida_pro.boolvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register boolvec_t in _ida_pro:
_ida_pro.boolvec_t_swigregister(boolvec_t)

class strvec_t(object):
    r"""
    Proxy of C++ qvector< simpleline_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> strvec_t
        __init__(self, x) -> strvec_t

        @param x: qvector< simpleline_t > const &
        """
        _ida_pro.strvec_t_swiginit(self, _ida_pro.new_strvec_t(*args))
    __swig_destroy__ = _ida_pro.delete_strvec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: simpleline_t const &

        push_back(self) -> simpleline_t &
        """
        return _ida_pro.strvec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.strvec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.strvec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.strvec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> simpleline_t const &

        @param _idx: size_t
        """
        return _ida_pro.strvec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.strvec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.strvec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: simpleline_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.strvec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=simpleline_t())

        @param x: simpleline_t const &
        """
        return _ida_pro.strvec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.strvec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.strvec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.strvec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< simpleline_t > &
        """
        return _ida_pro.strvec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> simpleline_t *
        """
        return _ida_pro.strvec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: simpleline_t *
        @param len: size_t
        """
        return _ida_pro.strvec_t_inject(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< simpleline_t >::iterator
        begin(self) -> qvector< simpleline_t >::const_iterator
        """
        return _ida_pro.strvec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< simpleline_t >::iterator
        end(self) -> qvector< simpleline_t >::const_iterator
        """
        return _ida_pro.strvec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< simpleline_t >::iterator

        @param it: qvector< simpleline_t >::iterator
        @param x: simpleline_t const &
        """
        return _ida_pro.strvec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< simpleline_t >::iterator

        @param it: qvector< simpleline_t >::iterator

        erase(self, first, last) -> qvector< simpleline_t >::iterator

        @param first: qvector< simpleline_t >::iterator
        @param last: qvector< simpleline_t >::iterator
        """
        return _ida_pro.strvec_t_erase(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.strvec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> simpleline_t const &

        @param i: size_t
        """
        return _ida_pro.strvec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: simpleline_t const &
        """
        return _ida_pro.strvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register strvec_t in _ida_pro:
_ida_pro.strvec_t_swigregister(strvec_t)

class sizevec_t(object):
    r"""
    Proxy of C++ qvector< size_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> sizevec_t
        __init__(self, x) -> sizevec_t

        @param x: qvector< size_t > const &
        """
        _ida_pro.sizevec_t_swiginit(self, _ida_pro.new_sizevec_t(*args))
    __swig_destroy__ = _ida_pro.delete_sizevec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: size_t const &

        push_back(self) -> size_t &
        """
        return _ida_pro.sizevec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_pro.sizevec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_pro.sizevec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_pro.sizevec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> size_t const &

        @param _idx: size_t
        """
        return _ida_pro.sizevec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_pro.sizevec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_pro.sizevec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: size_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_pro.sizevec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=size_t())

        @param x: size_t const &
        """
        return _ida_pro.sizevec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_pro.sizevec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_pro.sizevec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_pro.sizevec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< size_t > &
        """
        return _ida_pro.sizevec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> size_t *
        """
        return _ida_pro.sizevec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: size_t *
        @param len: size_t
        """
        return _ida_pro.sizevec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< size_t > const &
        """
        return _ida_pro.sizevec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< size_t > const &
        """
        return _ida_pro.sizevec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> qvector< size_t >::iterator
        begin(self) -> qvector< size_t >::const_iterator
        """
        return _ida_pro.sizevec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> qvector< size_t >::iterator
        end(self) -> qvector< size_t >::const_iterator
        """
        return _ida_pro.sizevec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> qvector< size_t >::iterator

        @param it: qvector< size_t >::iterator
        @param x: size_t const &
        """
        return _ida_pro.sizevec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> qvector< size_t >::iterator

        @param it: qvector< size_t >::iterator

        erase(self, first, last) -> qvector< size_t >::iterator

        @param first: qvector< size_t >::iterator
        @param last: qvector< size_t >::iterator
        """
        return _ida_pro.sizevec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> qvector< size_t >::iterator

        @param x: size_t const &

        find(self, x) -> qvector< size_t >::const_iterator

        @param x: size_t const &
        """
        return _ida_pro.sizevec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: size_t const &
        """
        return _ida_pro.sizevec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: size_t const &
        """
        return _ida_pro.sizevec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: size_t const &

        """
        return _ida_pro.sizevec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_pro.sizevec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> size_t const &

        @param i: size_t
        """
        return _ida_pro.sizevec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: size_t const &
        """
        return _ida_pro.sizevec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register sizevec_t in _ida_pro:
_ida_pro.sizevec_t_swigregister(sizevec_t)


def qstrvec_t_create(*args):
    r"""
    qstrvec_t_create() -> PyObject *
    """
    return _ida_pro.qstrvec_t_create(*args)

def qstrvec_t_destroy(*args):
    r"""
    qstrvec_t_destroy(py_obj) -> bool

    @param py_obj: PyObject *
    """
    return _ida_pro.qstrvec_t_destroy(*args)

def qstrvec_t_get_clink(*args):
    r"""
    qstrvec_t_get_clink(_self) -> qstrvec_t *

    @param self: PyObject *
    """
    return _ida_pro.qstrvec_t_get_clink(*args)

def qstrvec_t_get_clink_ptr(*args):
    r"""
    qstrvec_t_get_clink_ptr(_self) -> PyObject *

    @param self: PyObject *
    """
    return _ida_pro.qstrvec_t_get_clink_ptr(*args)

def qstrvec_t_assign(*args):
    r"""
    qstrvec_t_assign(_self, other) -> bool

    @param self: PyObject *
    @param other: PyObject *
    """
    return _ida_pro.qstrvec_t_assign(*args)

def qstrvec_t_addressof(*args):
    r"""
    qstrvec_t_addressof(_self, idx) -> PyObject *

    @param self: PyObject *
    @param idx: size_t
    """
    return _ida_pro.qstrvec_t_addressof(*args)

def qstrvec_t_set(*args):
    r"""
    qstrvec_t_set(_self, idx, s) -> bool

    @param self: PyObject *
    @param idx: size_t
    @param s: char const *
    """
    return _ida_pro.qstrvec_t_set(*args)

def qstrvec_t_from_list(*args):
    r"""
    qstrvec_t_from_list(_self, py_list) -> bool

    @param self: PyObject *
    @param py_list: PyObject *
    """
    return _ida_pro.qstrvec_t_from_list(*args)

def qstrvec_t_size(*args):
    r"""
    qstrvec_t_size(_self) -> size_t

    @param self: PyObject *
    """
    return _ida_pro.qstrvec_t_size(*args)

def qstrvec_t_get(*args):
    r"""
    qstrvec_t_get(_self, idx) -> PyObject *

    @param self: PyObject *
    @param idx: size_t
    """
    return _ida_pro.qstrvec_t_get(*args)

def qstrvec_t_add(*args):
    r"""
    qstrvec_t_add(_self, s) -> bool

    @param self: PyObject *
    @param s: char const *
    """
    return _ida_pro.qstrvec_t_add(*args)

def qstrvec_t_clear(*args):
    r"""
    qstrvec_t_clear(_self, qclear) -> bool

    @param self: PyObject *
    @param qclear: bool
    """
    return _ida_pro.qstrvec_t_clear(*args)

def qstrvec_t_insert(*args):
    r"""
    qstrvec_t_insert(_self, idx, s) -> bool

    @param self: PyObject *
    @param idx: size_t
    @param s: char const *
    """
    return _ida_pro.qstrvec_t_insert(*args)

def qstrvec_t_remove(*args):
    r"""
    qstrvec_t_remove(_self, idx) -> bool

    @param self: PyObject *
    @param idx: size_t
    """
    return _ida_pro.qstrvec_t_remove(*args)

def str2user(*args):
    r"""
    str2user(str) -> str or None
    Insert C-style escape characters to string

    @param str: char const *
    @return: new string with escape characters inserted
    """
    return _ida_pro.str2user(*args)
class uchar_array(object):
    r"""
    Proxy of C++ uchar_array class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, nelements) -> uchar_array

        @param nelements: size_t
        """
        _ida_pro.uchar_array_swiginit(self, _ida_pro.new_uchar_array(*args))
    __swig_destroy__ = _ida_pro.delete_uchar_array

    def __getitem__(self, *args):
        r"""
        __getitem__(self, index) -> uchar

        @param index: size_t
        """
        return _ida_pro.uchar_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, index, value)

        @param index: size_t
        @param value: uchar
        """
        return _ida_pro.uchar_array___setitem__(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> uchar *
        """
        return _ida_pro.uchar_array_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> uchar_array

        @param t: uchar *
        """
        return _ida_pro.uchar_array_frompointer(*args)

# Register uchar_array in _ida_pro:
_ida_pro.uchar_array_swigregister(uchar_array)

def uchar_array_frompointer(*args):
    r"""
    uchar_array_frompointer(t) -> uchar_array

    @param t: uchar *
    """
    return _ida_pro.uchar_array_frompointer(*args)

class tid_array(object):
    r"""
    Proxy of C++ tid_array class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, nelements) -> tid_array

        @param nelements: size_t
        """
        _ida_pro.tid_array_swiginit(self, _ida_pro.new_tid_array(*args))
    __swig_destroy__ = _ida_pro.delete_tid_array

    def __getitem__(self, *args):
        r"""
        __getitem__(self, index) -> tid_t

        @param index: size_t
        """
        return _ida_pro.tid_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, index, value)

        @param index: size_t
        @param value: tid_t
        """
        return _ida_pro.tid_array___setitem__(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> tid_t *
        """
        return _ida_pro.tid_array_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> tid_array

        @param t: tid_t *
        """
        return _ida_pro.tid_array_frompointer(*args)

# Register tid_array in _ida_pro:
_ida_pro.tid_array_swigregister(tid_array)

def tid_array_frompointer(*args):
    r"""
    tid_array_frompointer(t) -> tid_array

    @param t: tid_t *
    """
    return _ida_pro.tid_array_frompointer(*args)

class ea_array(object):
    r"""
    Proxy of C++ ea_array class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, nelements) -> ea_array

        @param nelements: size_t
        """
        _ida_pro.ea_array_swiginit(self, _ida_pro.new_ea_array(*args))
    __swig_destroy__ = _ida_pro.delete_ea_array

    def __getitem__(self, *args):
        r"""
        __getitem__(self, index) -> ea_t

        @param index: size_t
        """
        return _ida_pro.ea_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, index, value)

        @param index: size_t
        @param value: ea_t
        """
        return _ida_pro.ea_array___setitem__(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> ea_t *
        """
        return _ida_pro.ea_array_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> ea_array

        @param t: ea_t *
        """
        return _ida_pro.ea_array_frompointer(*args)

# Register ea_array in _ida_pro:
_ida_pro.ea_array_swigregister(ea_array)

def ea_array_frompointer(*args):
    r"""
    ea_array_frompointer(t) -> ea_array

    @param t: ea_t *
    """
    return _ida_pro.ea_array_frompointer(*args)

class sel_array(object):
    r"""
    Proxy of C++ sel_array class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, nelements) -> sel_array

        @param nelements: size_t
        """
        _ida_pro.sel_array_swiginit(self, _ida_pro.new_sel_array(*args))
    __swig_destroy__ = _ida_pro.delete_sel_array

    def __getitem__(self, *args):
        r"""
        __getitem__(self, index) -> sel_t

        @param index: size_t
        """
        return _ida_pro.sel_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, index, value)

        @param index: size_t
        @param value: sel_t
        """
        return _ida_pro.sel_array___setitem__(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> sel_t *
        """
        return _ida_pro.sel_array_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> sel_array

        @param t: sel_t *
        """
        return _ida_pro.sel_array_frompointer(*args)

# Register sel_array in _ida_pro:
_ida_pro.sel_array_swigregister(sel_array)

def sel_array_frompointer(*args):
    r"""
    sel_array_frompointer(t) -> sel_array

    @param t: sel_t *
    """
    return _ida_pro.sel_array_frompointer(*args)

class uval_array(object):
    r"""
    Proxy of C++ uval_array class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, nelements) -> uval_array

        @param nelements: size_t
        """
        _ida_pro.uval_array_swiginit(self, _ida_pro.new_uval_array(*args))
    __swig_destroy__ = _ida_pro.delete_uval_array

    def __getitem__(self, *args):
        r"""
        __getitem__(self, index) -> uval_t

        @param index: size_t
        """
        return _ida_pro.uval_array___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, index, value)

        @param index: size_t
        @param value: uval_t
        """
        return _ida_pro.uval_array___setitem__(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> uval_t *
        """
        return _ida_pro.uval_array_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> uval_array

        @param t: uval_t *
        """
        return _ida_pro.uval_array_frompointer(*args)

# Register uval_array in _ida_pro:
_ida_pro.uval_array_swigregister(uval_array)

def uval_array_frompointer(*args):
    r"""
    uval_array_frompointer(t) -> uval_array

    @param t: uval_t *
    """
    return _ida_pro.uval_array_frompointer(*args)

class int_pointer(object):
    r"""
    Proxy of C++ int_pointer class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> int_pointer
        """
        _ida_pro.int_pointer_swiginit(self, _ida_pro.new_int_pointer(*args))
    __swig_destroy__ = _ida_pro.delete_int_pointer

    def assign(self, *args):
        r"""
        assign(self, value)

        @param value: int
        """
        return _ida_pro.int_pointer_assign(self, *args)

    def value(self, *args):
        r"""
        value(self) -> int
        """
        return _ida_pro.int_pointer_value(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> int *
        """
        return _ida_pro.int_pointer_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> int_pointer

        @param t: int *
        """
        return _ida_pro.int_pointer_frompointer(*args)

# Register int_pointer in _ida_pro:
_ida_pro.int_pointer_swigregister(int_pointer)

def int_pointer_frompointer(*args):
    r"""
    int_pointer_frompointer(t) -> int_pointer

    @param t: int *
    """
    return _ida_pro.int_pointer_frompointer(*args)

class ea_pointer(object):
    r"""
    Proxy of C++ ea_pointer class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> ea_pointer
        """
        _ida_pro.ea_pointer_swiginit(self, _ida_pro.new_ea_pointer(*args))
    __swig_destroy__ = _ida_pro.delete_ea_pointer

    def assign(self, *args):
        r"""
        assign(self, value)

        @param value: ea_t
        """
        return _ida_pro.ea_pointer_assign(self, *args)

    def value(self, *args):
        r"""
        value(self) -> ea_t
        """
        return _ida_pro.ea_pointer_value(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> ea_t *
        """
        return _ida_pro.ea_pointer_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> ea_pointer

        @param t: ea_t *
        """
        return _ida_pro.ea_pointer_frompointer(*args)

# Register ea_pointer in _ida_pro:
_ida_pro.ea_pointer_swigregister(ea_pointer)

def ea_pointer_frompointer(*args):
    r"""
    ea_pointer_frompointer(t) -> ea_pointer

    @param t: ea_t *
    """
    return _ida_pro.ea_pointer_frompointer(*args)

class sval_pointer(object):
    r"""
    Proxy of C++ sval_pointer class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> sval_pointer
        """
        _ida_pro.sval_pointer_swiginit(self, _ida_pro.new_sval_pointer(*args))
    __swig_destroy__ = _ida_pro.delete_sval_pointer

    def assign(self, *args):
        r"""
        assign(self, value)

        @param value: sval_t
        """
        return _ida_pro.sval_pointer_assign(self, *args)

    def value(self, *args):
        r"""
        value(self) -> sval_t
        """
        return _ida_pro.sval_pointer_value(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> sval_t *
        """
        return _ida_pro.sval_pointer_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> sval_pointer

        @param t: sval_t *
        """
        return _ida_pro.sval_pointer_frompointer(*args)

# Register sval_pointer in _ida_pro:
_ida_pro.sval_pointer_swigregister(sval_pointer)

def sval_pointer_frompointer(*args):
    r"""
    sval_pointer_frompointer(t) -> sval_pointer

    @param t: sval_t *
    """
    return _ida_pro.sval_pointer_frompointer(*args)

class sel_pointer(object):
    r"""
    Proxy of C++ sel_pointer class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> sel_pointer
        """
        _ida_pro.sel_pointer_swiginit(self, _ida_pro.new_sel_pointer(*args))
    __swig_destroy__ = _ida_pro.delete_sel_pointer

    def assign(self, *args):
        r"""
        assign(self, value)

        @param value: sel_t
        """
        return _ida_pro.sel_pointer_assign(self, *args)

    def value(self, *args):
        r"""
        value(self) -> sel_t
        """
        return _ida_pro.sel_pointer_value(self, *args)

    def cast(self, *args):
        r"""
        cast(self) -> sel_t *
        """
        return _ida_pro.sel_pointer_cast(self, *args)

    @staticmethod
    def frompointer(*args):
        r"""
        frompointer(t) -> sel_pointer

        @param t: sel_t *
        """
        return _ida_pro.sel_pointer_frompointer(*args)

# Register sel_pointer in _ida_pro:
_ida_pro.sel_pointer_swigregister(sel_pointer)

def sel_pointer_frompointer(*args):
    r"""
    sel_pointer_frompointer(t) -> sel_pointer

    @param t: sel_t *
    """
    return _ida_pro.sel_pointer_frompointer(*args)


#<pycode(py_pro)>
import ida_idaapi

int64vec_t = longlongvec_t
uint64vec_t = ulonglongvec_t
if ida_idaapi.__EA64__:
    svalvec_t = longlongvec_t
    uvalvec_t = ulonglongvec_t
else:
    svalvec_t = intvec_t
    uvalvec_t = uintvec_t
eavec_t = uvalvec_t

ida_idaapi._listify_types(
        intvec_t,
        uintvec_t,
        longlongvec_t,
        ulonglongvec_t,
        boolvec_t,
        strvec_t)

# -----------------------------------------------------------------------
# qstrvec_t clinked object
class _qstrvec_t(ida_idaapi.py_clinked_object_t):
    """
    WARNING: It is very unlikely an IDAPython user should ever, ever
    have to use this type. It should only be used for IDAPython internals.

    For example, in py_askusingform.py, we ctypes-expose to the IDA
    kernel & UI a qstrvec instance, in case a DropdownListControl is
    constructed.
    That's because that's what ask_form expects, and we have no
    choice but to make a DropdownListControl hold a qstrvec_t.
    This is, afaict, the only situation where a Python
    _qstrvec_t is required.
    """

    def __init__(self, items=None):
        ida_idaapi.py_clinked_object_t.__init__(self)
# Populate the list if needed
        if items:
            self.from_list(items)

    def _create_clink(self):
        return _ida_pro.qstrvec_t_create()

    def _del_clink(self, lnk):
        return _ida_pro.qstrvec_t_destroy(lnk)

    def _get_clink_ptr(self):
        return _ida_pro.qstrvec_t_get_clink_ptr(self)

    def assign(self, other):
        """Copies the contents of 'other' to 'self'"""
        return _ida_pro.qstrvec_t_assign(self, other)

    def __setitem__(self, idx, s):
        """Sets string at the given index"""
        return _ida_pro.qstrvec_t_set(self, idx, s)

    def __getitem__(self, idx):
        """Gets the string at the given index"""
        return _ida_pro.qstrvec_t_get(self, idx)

    def __get_size(self):
        return _ida_pro.qstrvec_t_size(self)

    size = property(__get_size)
    """Returns the count of elements"""

    def addressof(self, idx):
        """Returns the address (as number) of the qstring at the given index"""
        return _ida_pro.qstrvec_t_addressof(self, idx)

    def add(self, s):
        """Add a string to the vector"""
        return _ida_pro.qstrvec_t_add(self, s)

    def from_list(self, lst):
        """Populates the vector from a Python string list"""
        return _ida_pro.qstrvec_t_from_list(self, lst)

    def clear(self, qclear=False):
        """
        Clears all strings from the vector.
        @param qclear: Just reset the size but do not actually free the memory
        """
        return _ida_pro.qstrvec_t_clear(self, qclear)

    def insert(self, idx, s):
        """Insert a string into the vector"""
        return _ida_pro.qstrvec_t_insert(self, idx, s)

    def remove(self, idx):
        """Removes a string from the vector"""
        return _ida_pro.qstrvec_t_remove(self, idx)

#</pycode(py_pro)>




