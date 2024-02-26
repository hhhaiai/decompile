"""
Functions that deal with C-like expressions and built-in IDC language.

Functions marked THREAD_SAFE may be called from any thread. No simultaneous
calls should be made for the same variable. We protect only global structures,
individual variables must be protected manually."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_expr
else:
    import _ida_expr

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

SWIG_PYTHON_LEGACY_BOOL = _ida_expr.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi


def compile_idc_file(*args) -> "qstring *":
    r"""
    compile_idc_file(nonnul_line) -> str

    @param nonnul_line: char const *
    """
    return _ida_expr.compile_idc_file(*args)

def compile_idc_text(*args) -> "qstring *":
    r"""
    compile_idc_text(nonnul_line) -> str

    @param nonnul_line: char const *
    """
    return _ida_expr.compile_idc_text(*args)

def py_get_call_idc_func(*args) -> "size_t":
    r"""
    py_get_call_idc_func() -> size_t
    """
    return _ida_expr.py_get_call_idc_func(*args)

def pyw_register_idc_func(*args) -> "size_t":
    r"""
    pyw_register_idc_func(name, args, py_fp) -> size_t

    @param name: char const *
    @param args: char const *
    @param py_fp: PyObject *
    """
    return _ida_expr.pyw_register_idc_func(*args)

def pyw_unregister_idc_func(*args) -> "bool":
    r"""
    pyw_unregister_idc_func(ctxptr) -> bool

    @param ctxptr: size_t
    """
    return _ida_expr.pyw_unregister_idc_func(*args)

def pyw_convert_defvals(*args) -> "bool":
    r"""
    pyw_convert_defvals(out, py_seq) -> bool

    @param out: idc_values_t *
    @param py_seq: PyObject *
    """
    return _ida_expr.pyw_convert_defvals(*args)

def py_add_idc_func(*args) -> "bool":
    r"""
    py_add_idc_func(name, fp_ptr, args, defvals, flags) -> bool

    @param name: char const *
    @param fp_ptr: size_t
    @param args: char const *
    @param defvals: idc_values_t const &
    @param flags: int
    """
    return _ida_expr.py_add_idc_func(*args)

def eval_expr(*args) -> "qstring *":
    r"""
    eval_expr(rv, where, line) -> str
    Compile and calculate an expression.

    @param rv: (C++: idc_value_t *) pointer to the result
    @param where: (C++: ea_t) the current linear address in the addressing space of the program
                  being disassembled. If will be used to resolve names of local
                  variables etc. if not applicable, then should be BADADDR.
    @param line: (C++: const char *) the expression to evaluate
    @retval true: ok
    @retval false: error, see errbuf
    """
    return _ida_expr.eval_expr(*args)

def eval_idc_expr(*args) -> "qstring *":
    r"""
    eval_idc_expr(rv, where, line) -> str
    Same as eval_expr(), but will always use the IDC interpreter regardless of the
    currently installed extlang.

    @param rv: (C++: idc_value_t *)
    @param where: (C++: ea_t)
    @param line: char const *
    """
    return _ida_expr.eval_idc_expr(*args)
IDC_LANG_EXT = _ida_expr.IDC_LANG_EXT
r"""
IDC script extension.
"""


def idcv_long(*args) -> "error_t":
    r"""
    idcv_long(v) -> error_t
    Convert IDC variable to a long (32/64bit) number.

    @param v: (C++: idc_value_t *)
    @return: v = 0 if impossible to convert to long
    """
    return _ida_expr.idcv_long(*args)

def idcv_int64(*args) -> "error_t":
    r"""
    idcv_int64(v) -> error_t
    Convert IDC variable to a 64bit number.

    @param v: (C++: idc_value_t *)
    @return: v = 0 if impossible to convert to int64
    """
    return _ida_expr.idcv_int64(*args)

def idcv_num(*args) -> "error_t":
    r"""
    idcv_num(v) -> error_t
    Convert IDC variable to a long number.

    @param v: (C++: idc_value_t *)
    @return: * v = 0 if IDC variable = "false" string
    * v = 1 if IDC variable = "true" string
    * v = number if IDC variable is number or string containing a number
    * eTypeConflict if IDC variable = empty string
    """
    return _ida_expr.idcv_num(*args)

def idcv_string(*args) -> "error_t":
    r"""
    idcv_string(v) -> error_t
    Convert IDC variable to a text string.

    @param v: (C++: idc_value_t *)
    """
    return _ida_expr.idcv_string(*args)

def idcv_float(*args) -> "error_t":
    r"""
    idcv_float(v) -> error_t
    Convert IDC variable to a floating point.

    @param v: (C++: idc_value_t *)
    """
    return _ida_expr.idcv_float(*args)

def idcv_object(*args) -> "error_t":
    r"""
    idcv_object(v, icls=None) -> error_t
    Create an IDC object. The original value of 'v' is discarded (freed).

    @param v: (C++: idc_value_t *) variable to hold the object. any previous value will be cleaned
    @param icls: (C++: const idc_class_t *) ptr to the desired class. nullptr means "object" class this ptr
                 must be returned by add_idc_class() or find_idc_class()
    @return: always eOk
    """
    return _ida_expr.idcv_object(*args)

def move_idcv(*args) -> "error_t":
    r"""
    move_idcv(dst, src) -> error_t
    Move 'src' to 'dst'. This function is more effective than copy_idcv since it
    never copies big amounts of data.

    @param dst: (C++: idc_value_t *)
    @param src: (C++: idc_value_t *)
    """
    return _ida_expr.move_idcv(*args)

def copy_idcv(*args) -> "error_t":
    r"""
    copy_idcv(dst, src) -> error_t
    Copy 'src' to 'dst'. For idc objects only a reference is copied.

    @param dst: (C++: idc_value_t *)
    @param src: (C++: const idc_value_t &) idc_value_t const &
    """
    return _ida_expr.copy_idcv(*args)

def deep_copy_idcv(*args) -> "error_t":
    r"""
    deep_copy_idcv(dst, src) -> error_t
    Deep copy an IDC object. This function performs deep copy of idc objects. If
    'src' is not an object, copy_idcv() will be called

    @param dst: (C++: idc_value_t *)
    @param src: (C++: const idc_value_t &) idc_value_t const &
    """
    return _ida_expr.deep_copy_idcv(*args)

def free_idcv(*args) -> "void":
    r"""
    free_idcv(v)
    Free storage used by VT_STR/VT_OBJ IDC variables. After this call the variable
    has a numeric value 0

    @param v: (C++: idc_value_t *)
    """
    return _ida_expr.free_idcv(*args)

def swap_idcvs(*args) -> "void":
    r"""
    swap_idcvs(v1, v2)
    Swap 2 variables.

    @param v1: (C++: idc_value_t *)
    @param v2: (C++: idc_value_t *)
    """
    return _ida_expr.swap_idcvs(*args)

def get_idcv_class_name(*args) -> "qstring *":
    r"""
    get_idcv_class_name(obj) -> str
    Retrieves the IDC object class name.

    @param obj: (C++: const idc_value_t *) class instance variable
    @return: error code, eOk on success
    """
    return _ida_expr.get_idcv_class_name(*args)

def get_idcv_attr(*args) -> "error_t":
    r"""
    get_idcv_attr(res, obj, attr, may_use_getattr=False) -> error_t
    Get an object attribute.

    @param res: (C++: idc_value_t *) buffer for the attribute value
    @param obj: (C++: const idc_value_t *) variable that holds an object reference. if obj is nullptr it
                searches global variables, then user functions
    @param attr: (C++: const char *) attribute name
    @param may_use_getattr: (C++: bool) may call getattr functions to calculate the attribute if
                            it does not exist
    @return: error code, eOk on success
    """
    return _ida_expr.get_idcv_attr(*args)

def set_idcv_attr(*args) -> "error_t":
    r"""
    set_idcv_attr(obj, attr, value, may_use_setattr=False) -> error_t
    Set an object attribute.

    @param obj: (C++: idc_value_t *) variable that holds an object reference. if obj is nullptr then it
                tries to modify a global variable with the attribute name
    @param attr: (C++: const char *) attribute name
    @param value: (C++: const idc_value_t &) new attribute value
    @param may_use_setattr: (C++: bool) may call setattr functions for the class
    @return: error code, eOk on success
    """
    return _ida_expr.set_idcv_attr(*args)

def del_idcv_attr(*args) -> "error_t":
    r"""
    del_idcv_attr(obj, attr) -> error_t
    Delete an object attribute.

    @param obj: (C++: idc_value_t *) variable that holds an object reference
    @param attr: (C++: const char *) attribute name
    @return: error code, eOk on success
    """
    return _ida_expr.del_idcv_attr(*args)

def first_idcv_attr(*args) -> "char const *":
    r"""
    first_idcv_attr(obj) -> char const *

    @param obj: idc_value_t const *
    """
    return _ida_expr.first_idcv_attr(*args)

def last_idcv_attr(*args) -> "char const *":
    r"""
    last_idcv_attr(obj) -> char const *

    @param obj: idc_value_t const *
    """
    return _ida_expr.last_idcv_attr(*args)

def next_idcv_attr(*args) -> "char const *":
    r"""
    next_idcv_attr(obj, attr) -> char const *

    @param obj: idc_value_t const *
    @param attr: char const *
    """
    return _ida_expr.next_idcv_attr(*args)

def prev_idcv_attr(*args) -> "char const *":
    r"""
    prev_idcv_attr(obj, attr) -> char const *

    @param obj: idc_value_t const *
    @param attr: char const *
    """
    return _ida_expr.prev_idcv_attr(*args)

def print_idcv(*args) -> "qstring *":
    r"""
    print_idcv(v, name=None, indent=0) -> str
    Get text representation of idc_value_t.

    @param v: (C++: const idc_value_t &) idc_value_t const &
    @param name: (C++: const char *) char const *
    @param indent: (C++: int)
    """
    return _ida_expr.print_idcv(*args)

def get_idcv_slice(*args) -> "error_t":
    r"""
    get_idcv_slice(res, v, i1, i2, flags=0) -> error_t
    Get slice.

    @param res: (C++: idc_value_t *) output variable that will contain the slice
    @param v: (C++: const idc_value_t *) input variable (string or object)
    @param i1: (C++: uval_t) slice start index
    @param i2: (C++: uval_t) slice end index (excluded)
    @param flags: (C++: int) IDC variable slice flags or 0
    @return: eOk if success
    """
    return _ida_expr.get_idcv_slice(*args)
VARSLICE_SINGLE = _ida_expr.VARSLICE_SINGLE
r"""
return single index (i2 is ignored)
"""


def set_idcv_slice(*args) -> "error_t":
    r"""
    set_idcv_slice(v, i1, i2, _in, flags=0) -> error_t
    Set slice.

    @param v: (C++: idc_value_t *) variable to modify (string or object)
    @param i1: (C++: uval_t) slice start index
    @param i2: (C++: uval_t) slice end index (excluded)
    @param in: (C++: const idc_value_t &) new value for the slice
    @param flags: (C++: int) IDC variable slice flags or 0
    @return: eOk on success
    """
    return _ida_expr.set_idcv_slice(*args)

def add_idc_class(*args) -> "idc_class_t *":
    r"""
    add_idc_class(name, super=None) -> idc_class_t *
    Create a new IDC class.

    @param name: (C++: const char *) name of the new class
    @param super: (C++: const idc_class_t *) the base class for the new class. if the new class is not based on
                  any other class, pass nullptr
    @return: pointer to the created class. If such a class already exists, a pointer
             to it will be returned. Pointers to other existing classes may be
             invalidated by this call.
    """
    return _ida_expr.add_idc_class(*args)

def find_idc_class(*args) -> "idc_class_t *":
    r"""
    find_idc_class(name) -> idc_class_t *
    Find an existing IDC class by its name.

    @param name: (C++: const char *) name of the class
    @return: pointer to the class or nullptr. The returned pointer is valid until a
             new call to add_idc_class()
    """
    return _ida_expr.find_idc_class(*args)

def deref_idcv(*args) -> "idc_value_t *":
    r"""
    deref_idcv(v, vref_flags) -> idc_value_t
    Dereference a VT_REF variable.

    @param v: (C++: idc_value_t *) variable to dereference
    @param vref_flags: (C++: int) Dereference IDC variable flags
    @return: pointer to the dereference result or nullptr. If returns nullptr,
             qerrno is set to eExecBadRef "Illegal variable reference"
    """
    return _ida_expr.deref_idcv(*args)
VREF_LOOP = _ida_expr.VREF_LOOP
r"""
dereference until we get a non VT_REF
"""

VREF_ONCE = _ida_expr.VREF_ONCE
r"""
dereference only once, do not loop
"""

VREF_COPY = _ida_expr.VREF_COPY
r"""
copy the result to the input var (v)
"""


def create_idcv_ref(*args) -> "bool":
    r"""
    create_idcv_ref(ref, v) -> bool
    Create a variable reference. Currently only references to global variables can
    be created.

    @param ref: (C++: idc_value_t *) ptr to the result
    @param v: (C++: const idc_value_t *) variable to reference
    @return: success
    """
    return _ida_expr.create_idcv_ref(*args)

def add_idc_gvar(*args) -> "idc_value_t *":
    r"""
    add_idc_gvar(name) -> idc_value_t
    Add global IDC variable.

    @param name: (C++: const char *) name of the global variable
    @return: pointer to the created variable or existing variable. NB: the returned
             pointer is valid until a new global var is added.
    """
    return _ida_expr.add_idc_gvar(*args)

def find_idc_gvar(*args) -> "idc_value_t *":
    r"""
    find_idc_gvar(name) -> idc_value_t
    Find an existing global IDC variable by its name.

    @param name: (C++: const char *) name of the global variable
    @return: pointer to the variable or nullptr. NB: the returned pointer is valid
             until a new global var is added. FIXME: it is difficult to use this
             function in a thread safe manner
    """
    return _ida_expr.find_idc_gvar(*args)
class idc_value_t(object):
    r"""
    Proxy of C++ idc_value_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    vtype = property(_ida_expr.idc_value_t_vtype_get, _ida_expr.idc_value_t_vtype_set, doc=r"""vtype""")
    r"""
    IDC value types
    """
    num = property(_ida_expr.idc_value_t_num_get, _ida_expr.idc_value_t_num_set, doc=r"""num""")
    r"""
    VT_LONG
    """
    e = property(_ida_expr.idc_value_t_e_get, _ida_expr.idc_value_t_e_set, doc=r"""e""")
    r"""
    VT_FLOAT
    """
    obj = property(_ida_expr.idc_value_t_obj_get, _ida_expr.idc_value_t_obj_set, doc=r"""obj""")
    funcidx = property(_ida_expr.idc_value_t_funcidx_get, _ida_expr.idc_value_t_funcidx_set, doc=r"""funcidx""")
    r"""
    VT_FUNC
    """
    pvoid = property(_ida_expr.idc_value_t_pvoid_get, _ida_expr.idc_value_t_pvoid_set, doc=r"""pvoid""")
    r"""
    VT_PVOID
    """
    i64 = property(_ida_expr.idc_value_t_i64_get, _ida_expr.idc_value_t_i64_set, doc=r"""i64""")
    r"""
    VT_INT64
    """
    reserve = property(_ida_expr.idc_value_t_reserve_get, _ida_expr.idc_value_t_reserve_set, doc=r"""reserve""")
    r"""
    internal housekeeping: 64-bit qstring is bigger than 12 bytes
    """

    def __init__(self, *args):
        r"""
        __init__(self, n=0) -> idc_value_t

        @param n: sval_t

        __init__(self, r) -> idc_value_t

        @param r: idc_value_t const &

        __init__(self, _str) -> idc_value_t

        @param _str: char const *
        """
        _ida_expr.idc_value_t_swiginit(self, _ida_expr.new_idc_value_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_value_t

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        See free_idcv()
        """
        return _ida_expr.idc_value_t_clear(self, *args)

    def qstr(self, *args) -> "qstring const &":
        r"""
        qstr(self) -> qstring
        VT_STR
        qstr(self) -> qstring const &
        """
        return _ida_expr.idc_value_t_qstr(self, *args)

    def c_str(self, *args) -> "char const *":
        r"""
        c_str(self) -> char const *
        VT_STR
        """
        return _ida_expr.idc_value_t_c_str(self, *args)

    def u_str(self, *args) -> "uchar const *":
        r"""
        u_str(self) -> uchar const *
        VT_STR
        """
        return _ida_expr.idc_value_t_u_str(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, v)
        Set this = r and v = this.

        @param v: (C++: idc_value_t &)
        """
        return _ida_expr.idc_value_t_swap(self, *args)

    def is_zero(self, *args) -> "bool":
        r"""
        is_zero(self) -> bool
        Does value represent the integer 0?
        """
        return _ida_expr.idc_value_t_is_zero(self, *args)

    def is_integral(self, *args) -> "bool":
        r"""
        is_integral(self) -> bool
        Does value represent a whole number?
        """
        return _ida_expr.idc_value_t_is_integral(self, *args)

    def is_convertible(self, *args) -> "bool":
        r"""
        is_convertible(self) -> bool
        Convertible types are VT_LONG, VT_FLOAT, VT_INT64, and VT_STR.
        """
        return _ida_expr.idc_value_t_is_convertible(self, *args)

    def _create_empty_string(self, *args) -> "void":
        r"""_create_empty_string(self)"""
        return _ida_expr.idc_value_t__create_empty_string(self, *args)

    def create_empty_string(self, *args) -> "void":
        r"""
        create_empty_string(self)
        """
        return _ida_expr.idc_value_t_create_empty_string(self, *args)

    def set_string(self, *args) -> "void":
        r"""
        set_string(self, _str, len)

        @param _str: char const *
        @param len: size_t

        set_string(self, _str)

        @param _str: char const *
        """
        return _ida_expr.idc_value_t_set_string(self, *args)

    def set_long(self, *args) -> "void":
        r"""
        set_long(self, v)

        @param v: sval_t
        """
        return _ida_expr.idc_value_t_set_long(self, *args)

    def set_pvoid(self, *args) -> "void":
        r"""
        set_pvoid(self, p)

        @param p: void *
        """
        return _ida_expr.idc_value_t_set_pvoid(self, *args)

    def set_int64(self, *args) -> "void":
        r"""
        set_int64(self, v)

        @param v: int64
        """
        return _ida_expr.idc_value_t_set_int64(self, *args)

    def set_float(self, *args) -> "void":
        r"""
        set_float(self, f)

        @param f: fpvalue_t const &
        """
        return _ida_expr.idc_value_t_set_float(self, *args)

    str = property(lambda self: self.c_str(), lambda self, v: self.set_string(v))


# Register idc_value_t in _ida_expr:
_ida_expr.idc_value_t_swigregister(idc_value_t)
VT_LONG = _ida_expr.VT_LONG
r"""
Integer (see idc_value_t::num)
"""

VT_FLOAT = _ida_expr.VT_FLOAT
r"""
Floating point (see idc_value_t::e)
"""

VT_WILD = _ida_expr.VT_WILD
r"""
Function with arbitrary number of arguments. The actual number of arguments will
be passed in idc_value_t::num. This value should not be used for idc_value_t.
"""

VT_OBJ = _ida_expr.VT_OBJ
r"""
Object (see idc_value_t::obj)
"""

VT_FUNC = _ida_expr.VT_FUNC
r"""
Function (see idc_value_t::funcidx)
"""

VT_STR = _ida_expr.VT_STR
r"""
String (see qstr() and similar functions)
"""

VT_PVOID = _ida_expr.VT_PVOID
r"""
void *
"""

VT_INT64 = _ida_expr.VT_INT64
r"""
i64
"""

VT_REF = _ida_expr.VT_REF
r"""
Reference.
"""


class idc_global_t(object):
    r"""
    Proxy of C++ idc_global_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_ida_expr.idc_global_t_name_get, _ida_expr.idc_global_t_name_set, doc=r"""name""")
    value = property(_ida_expr.idc_global_t_value_get, _ida_expr.idc_global_t_value_set, doc=r"""value""")

    def __init__(self, *args):
        r"""
        __init__(self) -> idc_global_t
        __init__(self, n) -> idc_global_t

        @param n: char const *
        """
        _ida_expr.idc_global_t_swiginit(self, _ida_expr.new_idc_global_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_global_t

# Register idc_global_t in _ida_expr:
_ida_expr.idc_global_t_swigregister(idc_global_t)

eExecThrow = _ida_expr.eExecThrow
r"""
See return value of idc_func_t.
"""


def find_idc_func(*args) -> "qstring *":
    r"""
    find_idc_func(prefix, n=0) -> str

    @param prefix: char const *
    @param n: int
    """
    return _ida_expr.find_idc_func(*args)
HF_DEFAULT = _ida_expr.HF_DEFAULT

HF_KEYWORD1 = _ida_expr.HF_KEYWORD1

HF_KEYWORD2 = _ida_expr.HF_KEYWORD2

HF_KEYWORD3 = _ida_expr.HF_KEYWORD3

HF_STRING = _ida_expr.HF_STRING

HF_COMMENT = _ida_expr.HF_COMMENT

HF_PREPROC = _ida_expr.HF_PREPROC

HF_NUMBER = _ida_expr.HF_NUMBER

HF_MAX = _ida_expr.HF_MAX

class highlighter_cbs_t(object):
    r"""
    Proxy of C++ highlighter_cbs_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _ida_expr.delete_highlighter_cbs_t

    def set_style(self, *args) -> "void":
        r"""
        set_style(self, arg0, arg1, arg2)

        @param arg0: int32
        @param arg1: int32
        @param arg2: enum syntax_highlight_style
        """
        return _ida_expr.highlighter_cbs_t_set_style(self, *args)

    def prev_block_state(self, *args) -> "int32":
        r"""
        prev_block_state(self) -> int32
        """
        return _ida_expr.highlighter_cbs_t_prev_block_state(self, *args)

    def cur_block_state(self, *args) -> "int32":
        r"""
        cur_block_state(self) -> int32
        """
        return _ida_expr.highlighter_cbs_t_cur_block_state(self, *args)

    def set_block_state(self, *args) -> "void":
        r"""
        set_block_state(self, arg0)

        @param arg0: int32
        """
        return _ida_expr.highlighter_cbs_t_set_block_state(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> highlighter_cbs_t

        @param self: PyObject *
        """
        if self.__class__ == highlighter_cbs_t:
            _self = None
        else:
            _self = self
        _ida_expr.highlighter_cbs_t_swiginit(self, _ida_expr.new_highlighter_cbs_t(_self, *args))
    def __disown__(self):
        self.this.disown()
        _ida_expr.disown_highlighter_cbs_t(self)
        return weakref.proxy(self)

# Register highlighter_cbs_t in _ida_expr:
_ida_expr.highlighter_cbs_t_swigregister(highlighter_cbs_t)


def set_header_path(*args) -> "bool":
    r"""
    set_header_path(path, add) -> bool
    Set or append a header path. IDA looks for the include files in the appended
    header paths, then in the ida executable directory.

    @param path: (C++: const char *) list of directories to add (separated by ';') may be nullptr, in
                 this case nothing is added
    @param add: (C++: bool) true: append. false: remove old paths.
    @retval true: success
    @retval false: no memory
    """
    return _ida_expr.set_header_path(*args)

def get_idc_filename(*args) -> "char const *":
    r"""
    get_idc_filename(file) -> str
    Get full name of IDC file name. Search for file in list of include directories,
    IDCPATH directory and system directories.

    @param file: (C++: const char *) file name without full path
    @return: nullptr is file not found. otherwise returns pointer to buf
    """
    return _ida_expr.get_idc_filename(*args)

def exec_system_script(*args) -> "bool":
    r"""
    exec_system_script(file, complain_if_no_file=True) -> bool
    Compile and execute "main" function from system file.

    @param file: (C++: const char *) file name with IDC function(s). The file will be searched using
                 get_idc_filename().
    @param complain_if_no_file: (C++: bool) * 1: display warning if the file is not found
    * 0: don't complain if file doesn't exist
    @retval 1: ok, file is compiled and executed
    @retval 0: failure, compilation or execution error, warning is displayed
    """
    return _ida_expr.exec_system_script(*args)
CPL_DEL_MACROS = _ida_expr.CPL_DEL_MACROS
r"""
delete macros at the end of compilation
"""

CPL_USE_LABELS = _ida_expr.CPL_USE_LABELS
r"""
allow program labels in the script
"""

CPL_ONLY_SAFE = _ida_expr.CPL_ONLY_SAFE
r"""
allow calls of only thread-safe functions
"""


def compile_idc_snippet(*args) -> "qstring *":
    r"""
    compile_idc_snippet(func, text, resolver=None, only_safe_funcs=False) -> str
    Compile text with IDC statements.

    @param func: (C++: const char *) name of the function to create out of the snippet
    @param text: (C++: const char *) text to compile
    @param resolver: (C++: idc_resolver_t *) callback object to get values of undefined variables This
                     object will be called if IDC function contains references to
                     undefined variables. May be nullptr.
    @param only_safe_funcs: (C++: bool) if true, any calls to functions without EXTFUN_SAFE flag
                            will lead to a compilation error.
    @retval true: ok
    @retval false: error, see errbuf
    """
    return _ida_expr.compile_idc_snippet(*args)

def exec_idc_script(*args) -> "qstring *":
    r"""
    exec_idc_script(result, path, func, args, argsnum) -> str
    Compile and execute IDC function(s) from file.

    @param result: (C++: idc_value_t *) ptr to idc_value_t to hold result of the function. If execution
                   fails, this variable will contain the exception information. You
                   may pass nullptr if you are not interested in the returned value.
    @param path: (C++: const char *) text file containing text of IDC functions
    @param func: (C++: const char *) function name to execute
    @param args: (C++: const idc_value_t) array of parameters
    @param argsnum: (C++: size_t) number of parameters to pass to 'fname' This number should be
                    equal to number of parameters the function expects.
    @retval true: ok
    @retval false: error, see errbuf
    """
    return _ida_expr.exec_idc_script(*args)

def throw_idc_exception(*args) -> "error_t":
    r"""
    throw_idc_exception(r, desc) -> error_t
    Create an idc execution exception object. This helper function can be used to
    return an exception from C++ code to IDC. In other words this function can be
    called from idc_func_t() callbacks. Sample usage: if ( !ok ) return
    throw_idc_exception(r, "detailed error msg");

    @param r: (C++: idc_value_t *) object to hold the exception object
    @param desc: (C++: const char *) exception description
    @return: eExecThrow
    """
    return _ida_expr.throw_idc_exception(*args)
class idc_values_t(object):
    r"""
    Proxy of C++ qvector< idc_value_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> idc_values_t
        __init__(self, x) -> idc_values_t

        @param x: qvector< idc_value_t > const &
        """
        _ida_expr.idc_values_t_swiginit(self, _ida_expr.new_idc_values_t(*args))
    __swig_destroy__ = _ida_expr.delete_idc_values_t

    def push_back(self, *args) -> "idc_value_t &":
        r"""
        push_back(self, x)

        @param x: idc_value_t const &

        push_back(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_expr.idc_values_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_expr.idc_values_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_expr.idc_values_t_empty(self, *args)

    def at(self, *args) -> "idc_value_t const &":
        r"""
        at(self, _idx) -> idc_value_t

        @param _idx: size_t
        """
        return _ida_expr.idc_values_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_expr.idc_values_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_expr.idc_values_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: idc_value_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_expr.idc_values_t_resize(self, *args)

    def grow(self, *args) -> "void":
        r"""
        grow(self, x=idc_value_t())

        @param x: idc_value_t const &
        """
        return _ida_expr.idc_values_t_grow(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_expr.idc_values_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_expr.idc_values_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_expr.idc_values_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< idc_value_t > &
        """
        return _ida_expr.idc_values_t_swap(self, *args)

    def extract(self, *args) -> "idc_value_t *":
        r"""
        extract(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: idc_value_t *
        @param len: size_t
        """
        return _ida_expr.idc_values_t_inject(self, *args)

    def begin(self, *args) -> "qvector< idc_value_t >::const_iterator":
        r"""
        begin(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_begin(self, *args)

    def end(self, *args) -> "qvector< idc_value_t >::const_iterator":
        r"""
        end(self) -> idc_value_t
        """
        return _ida_expr.idc_values_t_end(self, *args)

    def insert(self, *args) -> "qvector< idc_value_t >::iterator":
        r"""
        insert(self, it, x) -> idc_value_t

        @param it: qvector< idc_value_t >::iterator
        @param x: idc_value_t const &
        """
        return _ida_expr.idc_values_t_insert(self, *args)

    def erase(self, *args) -> "qvector< idc_value_t >::iterator":
        r"""
        erase(self, it) -> idc_value_t

        @param it: qvector< idc_value_t >::iterator

        erase(self, first, last) -> idc_value_t

        @param first: qvector< idc_value_t >::iterator
        @param last: qvector< idc_value_t >::iterator
        """
        return _ida_expr.idc_values_t_erase(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_expr.idc_values_t___len__(self, *args)

    def __getitem__(self, *args) -> "idc_value_t const &":
        r"""
        __getitem__(self, i) -> idc_value_t

        @param i: size_t
        """
        return _ida_expr.idc_values_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: idc_value_t const &
        """
        return _ida_expr.idc_values_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register idc_values_t in _ida_expr:
_ida_expr.idc_values_t_swigregister(idc_values_t)


#<pycode(py_expr)>
try:
    import types
    import ctypes
# Callback for IDC func callback (On Windows, we use stdcall)
# typedef error_t idaapi idc_func_t(idc_value_t *argv,idc_value_t *r);
    try:
        _IDCFUNC_CB_T = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
    except:
        _IDCFUNC_CB_T = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

# A trampoline function that is called from idcfunc_t that will
# call the Python callback with the argv and r properly serialized to python
    call_idc_func__ = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(_ida_expr.py_get_call_idc_func())
except:
    def call_idc_func__(*args):
        warning("IDC extensions need ctypes library in order to work")
        return 0
    _IDCFUNC_CB_T = None

# --------------------------------------------------------------------------
EXTFUN_BASE  = 0x0001
r"""
requires open database.
"""
EXTFUN_NORET = 0x0002
r"""
does not return. the interpreter may clean up its state before calling it.
"""
EXTFUN_SAFE  = 0x0004
r"""
thread safe function. may be called from any thread.
"""

# --------------------------------------------------------------------------
class _IdcFunction(object):
    """
    Internal class that calls pyw_call_idc_func() with a context
    """
    def __init__(self, ctxptr):
        self.ctxptr = ctxptr
# Take a reference to the ctypes callback
# (note: this will create a circular reference)
        self.cb = _IDCFUNC_CB_T(self)

    fp_ptr = property(lambda self: ctypes.cast(self.cb, ctypes.c_void_p).value)

    def __call__(self, args, res):
        return call_idc_func__(self.ctxptr, args, res)


# --------------------------------------------------------------------------
# Dictionary to remember IDC function names along with the context pointer
# retrieved by using the internal pyw_register_idc_func()
__IDC_FUNC_CTXS = {}

def del_idc_func(name):
    r"""
    Unregisters the specified IDC function

    Delete an IDC function
    """
    global __IDC_FUNC_CTXS

# Get the context
    f = __IDC_FUNC_CTXS.get(name, None)

    if f is None:
        return False # Not registered

# Break circular reference
    del f.cb

# Delete the name from the dictionary
    del __IDC_FUNC_CTXS[name]

# Delete the context and unregister the function
    return _ida_expr.pyw_unregister_idc_func(f.ctxptr)

# --------------------------------------------------------------------------
def add_idc_func(name, fp, args, defvals=(), flags=0):
    r"""
    Extends the IDC language by exposing a new IDC function that is backed up by a Python function

    Add an IDC function. This function does not modify the predefined kernel
    functions. Example:
    static error_t idaapi myfunc5(idc_value_t *argv, idc_value_t *res)
    {
    msg("myfunc is called with arg0=%a and arg1=%s\n", argv[0].num, argv[1].str);
    res->num = 5;     // let's return 5
    return eOk;
    }
    static const char myfunc5_args[] = { VT_LONG, VT_STR, 0 };
    static const ext_idcfunc_t myfunc_desc = { "MyFunc5", myfunc5, myfunc5_args,
    nullptr, 0, EXTFUN_BASE };
    // after this:
    add_idc_func(myfunc_desc);
    // there is a new IDC function which can be called like this:
    MyFunc5(0x123, "test");

    @note: If the function already exists, it will be replaced by the new function
    @return: success
    """
    global __IDC_FUNC_CTXS

# Get the context
    f = __IDC_FUNC_CTXS.get(name, None)

# Registering a function that is already registered?
    if f is not None:
# Unregister it first
        del_idc_func(name)

# Convert the tupple argument info to a string
    args = "".join([chr(x) for x in args])

# make sure we don't have an obvious discrepancy between
# the number of args, and the provided default values
    if len(defvals) > len(args):
        return False

    vdefvals = idc_values_t()
    if not _ida_expr.pyw_convert_defvals(vdefvals, defvals):
        return False

# Create a context
    ctxptr = _ida_expr.pyw_register_idc_func(name, args, fp)
    if ctxptr == 0:
        return False

# Bind the context with the IdcFunc object
    f = _IdcFunction(ctxptr)

# Remember the Python context
    __IDC_FUNC_CTXS[name] = f

# Register IDC function with a callback
    return _ida_expr.py_add_idc_func(
                name,
                f.fp_ptr,
                args,
                vdefvals,
                flags)

#</pycode(py_expr)>




