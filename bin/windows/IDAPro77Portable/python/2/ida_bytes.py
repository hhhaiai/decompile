"""
Contains functions that deal with individual byte characteristics.

Each byte of the disassembled program is represented by a 32-bit value. We will
call this value 'flags'. The structure of the flags is here.

You are not allowed to inspect individual bits of flags and modify them
directly. Use special functions to inspect and/or modify flags.

Flags are kept in a virtual array file (*.id1). Addresses (ea) are all 32-bit
(or 64-bit) quantities."""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _ida_bytes
else:
    import _ida_bytes

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

SWIG_PYTHON_LEGACY_BOOL = _ida_bytes.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

import ida_range
class compiled_binpat_vec_t(object):
    r"""
    Proxy of C++ qvector< compiled_binpat_t > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> compiled_binpat_vec_t
        __init__(self, x) -> compiled_binpat_vec_t

        @param x: qvector< compiled_binpat_t > const &
        """
        _ida_bytes.compiled_binpat_vec_t_swiginit(self, _ida_bytes.new_compiled_binpat_vec_t(*args))
    __swig_destroy__ = _ida_bytes.delete_compiled_binpat_vec_t

    def push_back(self, *args):
        r"""
        push_back(self, x)

        @param x: compiled_binpat_t const &

        push_back(self) -> compiled_binpat_t
        """
        return _ida_bytes.compiled_binpat_vec_t_push_back(self, *args)

    def pop_back(self, *args):
        r"""
        pop_back(self)
        """
        return _ida_bytes.compiled_binpat_vec_t_pop_back(self, *args)

    def size(self, *args):
        r"""
        size(self) -> size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_size(self, *args)

    def empty(self, *args):
        r"""
        empty(self) -> bool
        """
        return _ida_bytes.compiled_binpat_vec_t_empty(self, *args)

    def at(self, *args):
        r"""
        at(self, _idx) -> compiled_binpat_t

        @param _idx: size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_at(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_bytes.compiled_binpat_vec_t_qclear(self, *args)

    def clear(self, *args):
        r"""
        clear(self)
        """
        return _ida_bytes.compiled_binpat_vec_t_clear(self, *args)

    def resize(self, *args):
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: compiled_binpat_t const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_resize(self, *args)

    def grow(self, *args):
        r"""
        grow(self, x=compiled_binpat_t())

        @param x: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_vec_t_grow(self, *args)

    def capacity(self, *args):
        r"""
        capacity(self) -> size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_capacity(self, *args)

    def reserve(self, *args):
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_reserve(self, *args)

    def truncate(self, *args):
        r"""
        truncate(self)
        """
        return _ida_bytes.compiled_binpat_vec_t_truncate(self, *args)

    def swap(self, *args):
        r"""
        swap(self, r)

        @param r: qvector< compiled_binpat_t > &
        """
        return _ida_bytes.compiled_binpat_vec_t_swap(self, *args)

    def extract(self, *args):
        r"""
        extract(self) -> compiled_binpat_t
        """
        return _ida_bytes.compiled_binpat_vec_t_extract(self, *args)

    def inject(self, *args):
        r"""
        inject(self, s, len)

        @param s: compiled_binpat_t *
        @param len: size_t
        """
        return _ida_bytes.compiled_binpat_vec_t_inject(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< compiled_binpat_t > const &
        """
        return _ida_bytes.compiled_binpat_vec_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< compiled_binpat_t > const &
        """
        return _ida_bytes.compiled_binpat_vec_t___ne__(self, *args)

    def begin(self, *args):
        r"""
        begin(self) -> compiled_binpat_t
        """
        return _ida_bytes.compiled_binpat_vec_t_begin(self, *args)

    def end(self, *args):
        r"""
        end(self) -> compiled_binpat_t
        """
        return _ida_bytes.compiled_binpat_vec_t_end(self, *args)

    def insert(self, *args):
        r"""
        insert(self, it, x) -> compiled_binpat_t

        @param it: qvector< compiled_binpat_t >::iterator
        @param x: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_vec_t_insert(self, *args)

    def erase(self, *args):
        r"""
        erase(self, it) -> compiled_binpat_t

        @param it: qvector< compiled_binpat_t >::iterator

        erase(self, first, last) -> compiled_binpat_t

        @param first: qvector< compiled_binpat_t >::iterator
        @param last: qvector< compiled_binpat_t >::iterator
        """
        return _ida_bytes.compiled_binpat_vec_t_erase(self, *args)

    def find(self, *args):
        r"""
        find(self, x) -> compiled_binpat_t

        @param x: compiled_binpat_t const &

        """
        return _ida_bytes.compiled_binpat_vec_t_find(self, *args)

    def has(self, *args):
        r"""
        has(self, x) -> bool

        @param x: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_vec_t_has(self, *args)

    def add_unique(self, *args):
        r"""
        add_unique(self, x) -> bool

        @param x: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_vec_t_add_unique(self, *args)

    def _del(self, *args):
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: compiled_binpat_t const &

        """
        return _ida_bytes.compiled_binpat_vec_t__del(self, *args)

    def __len__(self, *args):
        r"""
        __len__(self) -> size_t
        """
        return _ida_bytes.compiled_binpat_vec_t___len__(self, *args)

    def __getitem__(self, *args):
        r"""
        __getitem__(self, i) -> compiled_binpat_t

        @param i: size_t
        """
        return _ida_bytes.compiled_binpat_vec_t___getitem__(self, *args)

    def __setitem__(self, *args):
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_vec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register compiled_binpat_vec_t in _ida_bytes:
_ida_bytes.compiled_binpat_vec_t_swigregister(compiled_binpat_vec_t)


def enable_flags(*args):
    r"""
    enable_flags(start_ea, end_ea, stt) -> error_t
    Allocate flags for address range. This function does not change the storage type
    of existing ranges. Exit with an error message if not enough disk space.

    @param start_ea: (C++: ea_t) should be lower than end_ea.
    @param end_ea: (C++: ea_t) does not belong to the range.
    @param stt: (C++: storage_type_t)
    @return: 0 if ok, otherwise an error code
    """
    return _ida_bytes.enable_flags(*args)

def disable_flags(*args):
    r"""
    disable_flags(start_ea, end_ea) -> error_t
    Deallocate flags for address range. Exit with an error message if not enough
    disk space (this may occur too).

    @param start_ea: (C++: ea_t) should be lower than end_ea.
    @param end_ea: (C++: ea_t) does not belong to the range.
    @return: 0 if ok, otherwise return error code
    """
    return _ida_bytes.disable_flags(*args)

def change_storage_type(*args):
    r"""
    change_storage_type(start_ea, end_ea, stt) -> error_t
    Change flag storage type for address range.

    @param start_ea: (C++: ea_t) should be lower than end_ea.
    @param end_ea: (C++: ea_t) does not belong to the range.
    @param stt: (C++: storage_type_t)
    @return: error code
    """
    return _ida_bytes.change_storage_type(*args)

def next_addr(*args):
    r"""
    next_addr(ea) -> ea_t
    Get next address in the program (i.e. next address which has flags).

    @param ea: (C++: ea_t)
    @return: BADADDR if no such address exist.
    """
    return _ida_bytes.next_addr(*args)

def prev_addr(*args):
    r"""
    prev_addr(ea) -> ea_t
    Get previous address in the program.

    @param ea: (C++: ea_t)
    @return: BADADDR if no such address exist.
    """
    return _ida_bytes.prev_addr(*args)

def next_chunk(*args):
    r"""
    next_chunk(ea) -> ea_t
    Get the first address of next contiguous chunk in the program.

    @param ea: (C++: ea_t)
    @return: BADADDR if next chunk doesn't exist.
    """
    return _ida_bytes.next_chunk(*args)

def prev_chunk(*args):
    r"""
    prev_chunk(ea) -> ea_t
    Get the last address of previous contiguous chunk in the program.

    @param ea: (C++: ea_t)
    @return: BADADDR if previous chunk doesn't exist.
    """
    return _ida_bytes.prev_chunk(*args)

def chunk_start(*args):
    r"""
    chunk_start(ea) -> ea_t
    Get start of the contiguous address block containing 'ea'.

    @param ea: (C++: ea_t)
    @return: BADADDR if 'ea' doesn't belong to the program.
    """
    return _ida_bytes.chunk_start(*args)

def chunk_size(*args):
    r"""
    chunk_size(ea) -> asize_t
    Get size of the contiguous address block containing 'ea'.

    @param ea: (C++: ea_t)
    @return: 0 if 'ea' doesn't belong to the program.
    """
    return _ida_bytes.chunk_size(*args)

def free_chunk(*args):
    r"""
    free_chunk(bottom, size, step) -> ea_t
    Search for a hole in the addressing space of the program.

    @param bottom: (C++: ea_t) address to start searching
    @param size: (C++: asize_t) size of desired block
    @param step: (C++: int32) bit mask for the start of hole (0xF would align hole to a
                 paragraph). if 'step' is negative, the bottom address with be
                 aligned. otherwise the kernel will try to use it as is and align it
                 only when the hole is too small.
    @return: start of the hole or BADADDR
    """
    return _ida_bytes.free_chunk(*args)

def next_that(*args):
    r"""
    next_that(ea, maxea, testf) -> ea_t
    Find next address with a flag satisfying the function 'testf'.
    @note: do not pass is_unknown() to this function to find unexplored bytes. It
           will fail under the debugger. To find unexplored bytes, use
           next_unknown().

    @param ea: (C++: ea_t) start searching at this address + 1
    @param maxea: (C++: ea_t) not included in the search range.
    @param testf: (C++: testf_t *) test function to find next address
    @return: the found address or BADADDR.
    """
    return _ida_bytes.next_that(*args)

def next_unknown(*args):
    r"""
    next_unknown(ea, maxea) -> ea_t
    Similar to next_that(), but will find the next address that is unexplored.

    @param ea: (C++: ea_t)
    @param maxea: (C++: ea_t)
    """
    return _ida_bytes.next_unknown(*args)

def prev_that(*args):
    r"""
    prev_that(ea, minea, testf) -> ea_t
    Find previous address with a flag satisfying the function 'testf'.
    @note: do not pass is_unknown() to this function to find unexplored bytes It
           will fail under the debugger. To find unexplored bytes, use
           prev_unknown().

    @param ea: (C++: ea_t) start searching from this address - 1.
    @param minea: (C++: ea_t) included in the search range.
    @param testf: (C++: testf_t *) test function to find previous address
    @return: the found address or BADADDR.
    """
    return _ida_bytes.prev_that(*args)

def prev_unknown(*args):
    r"""
    prev_unknown(ea, minea) -> ea_t
    Similar to prev_that(), but will find the previous address that is unexplored.

    @param ea: (C++: ea_t)
    @param minea: (C++: ea_t)
    """
    return _ida_bytes.prev_unknown(*args)

def prev_head(*args):
    r"""
    prev_head(ea, minea) -> ea_t
    Get start of previous defined item.

    @param ea: (C++: ea_t) begin search at this address
    @param minea: (C++: ea_t) included in the search range
    @return: BADADDR if none exists.
    """
    return _ida_bytes.prev_head(*args)

def next_head(*args):
    r"""
    next_head(ea, maxea) -> ea_t
    Get start of next defined item.

    @param ea: (C++: ea_t) begin search at this address
    @param maxea: (C++: ea_t) not included in the search range
    @return: BADADDR if none exists.
    """
    return _ida_bytes.next_head(*args)

def prev_not_tail(*args):
    r"""
    prev_not_tail(ea) -> ea_t
    Get address of previous non-tail byte.

    @param ea: (C++: ea_t)
    @return: BADADDR if none exists.
    """
    return _ida_bytes.prev_not_tail(*args)

def next_not_tail(*args):
    r"""
    next_not_tail(ea) -> ea_t
    Get address of next non-tail byte.

    @param ea: (C++: ea_t)
    @return: BADADDR if none exists.
    """
    return _ida_bytes.next_not_tail(*args)

def prev_visea(*args):
    r"""
    prev_visea(ea) -> ea_t
    Get previous visible address.

    @param ea: (C++: ea_t)
    @return: BADADDR if none exists.
    """
    return _ida_bytes.prev_visea(*args)

def next_visea(*args):
    r"""
    next_visea(ea) -> ea_t
    Get next visible address.

    @param ea: (C++: ea_t)
    @return: BADADDR if none exists.
    """
    return _ida_bytes.next_visea(*args)

def get_item_head(*args):
    r"""
    get_item_head(ea) -> ea_t
    Get the start address of the item at 'ea'. If there is no current item, then
    'ea' will be returned (see definition at the end of bytes.hpp source)

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_item_head(*args)

def get_item_end(*args):
    r"""
    get_item_end(ea) -> ea_t
    Get the end address of the item at 'ea'. The returned address doesn't belong to
    the current item. Unexplored bytes are counted as 1 byte entities.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_item_end(*args)

def calc_max_item_end(*args):
    r"""
    calc_max_item_end(ea, how=15) -> ea_t
    Calculate maximal reasonable end address of a new item. This function will limit
    the item with the current segment bounds.

    @param ea: (C++: ea_t) linear address
    @param how: (C++: int) when to stop the search. A combination of Item end search flags
    @return: end of new item. If it is not possible to create an item, it will
             return 'ea'.
    """
    return _ida_bytes.calc_max_item_end(*args)
ITEM_END_FIXUP = _ida_bytes.ITEM_END_FIXUP
r"""
stop at the first fixup
"""

ITEM_END_INITED = _ida_bytes.ITEM_END_INITED
r"""
stop when initialization changes i.e.
* if is_loaded(ea): stop if uninitialized byte is encountered
* if !is_loaded(ea): stop if initialized byte is encountered
"""

ITEM_END_NAME = _ida_bytes.ITEM_END_NAME
r"""
stop at the first named location
"""

ITEM_END_XREF = _ida_bytes.ITEM_END_XREF
r"""
stop at the first referenced location
"""


def get_item_size(*args):
    r"""
    get_item_size(ea) -> asize_t
    Get size of item (instruction/data) in bytes. Unexplored bytes have length of 1
    byte. This function never returns 0.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_item_size(*args)

def is_mapped(*args):
    r"""
    is_mapped(ea) -> bool
    Is the specified address 'ea' present in the program?

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.is_mapped(*args)

def get_flags_ex(*args):
    r"""
    get_flags_ex(ea, how) -> flags_t
    Get flags for the specified address, extended form.

    @param ea: (C++: ea_t)
    @param how: (C++: int)
    """
    return _ida_bytes.get_flags_ex(*args)
GFE_VALUE = _ida_bytes.GFE_VALUE
r"""
get flags with FF_IVL & MS_VAL. It is much slower under remote debugging because
the kernel needs to read the process memory.
"""


def get_flags(*args):
    r"""
    get_flags(ea) -> flags_t
    get flags with FF_IVL & MS_VAL. It is much slower under remote debugging because
    the kernel needs to read the process memory.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_flags(*args)

def get_full_flags(*args):
    r"""
    get_full_flags(ea) -> flags_t
    Get flags value for address 'ea'.

    @param ea: (C++: ea_t)
    @return: 0 if address is not present in the program
    """
    return _ida_bytes.get_full_flags(*args)

def get_item_flag(*args):
    r"""
    get_item_flag(_from, n, ea, appzero) -> flags_t
    Get flag of the item at 'ea' even if it is a tail byte of some array or
    structure. This function is used to get flags of structure members or array
    elements.

    @param from: (C++: ea_t) linear address of the instruction which refers to 'ea'
    @param n: (C++: int) number of operand which refers to 'ea'
    @param ea: (C++: ea_t) the referenced address
    @param appzero: (C++: bool) append a struct field name if the field offset is zero?
                    meaningful only if the name refers to a structure.
    @return: flags or 0 (if failed)
    """
    return _ida_bytes.get_item_flag(*args)
MS_VAL = _ida_bytes.MS_VAL
r"""
Mask for byte value.
"""

FF_IVL = _ida_bytes.FF_IVL
r"""
Byte has value ?
"""


def has_value(*args):
    r"""
    has_value(F) -> bool
    Do flags contain byte value?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_value(*args)

def del_value(*args):
    r"""
    del_value(ea)
    Delete byte value from flags. The corresponding byte becomes uninitialized.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.del_value(*args)

def is_loaded(*args):
    r"""
    is_loaded(ea) -> bool
    Does the specified address have a byte value (is initialized?)

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.is_loaded(*args)

def nbits(*args):
    r"""
    nbits(ea) -> int
    Get number of bits in a byte at the given address.

    @param ea: (C++: ea_t)
    @return: processor_t::dnbits() if the address doesn't belong to a segment,
             otherwise the result depends on the segment type
    """
    return _ida_bytes.nbits(*args)

def bytesize(*args):
    r"""
    bytesize(ea) -> int
    Get number of bytes required to store a byte at the given address.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.bytesize(*args)

def get_byte(*args):
    r"""
    get_byte(ea) -> uchar
    Get one byte (8-bit) of the program at 'ea'. This function works only for 8bit
    byte processors.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_byte(*args)

def get_db_byte(*args):
    r"""
    get_db_byte(ea) -> uchar
    Get one byte (8-bit) of the program at 'ea' from the database. Works even if the
    debugger is active. See also get_dbg_byte() to read the process memory directly.
    This function works only for 8bit byte processors.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_db_byte(*args)

def get_word(*args):
    r"""
    get_word(ea) -> ushort
    Get one word (16-bit) of the program at 'ea'. This function takes into account
    order of bytes specified in idainfo::is_be() This function works only for 8bit
    byte processors.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_word(*args)

def get_dword(*args):
    r"""
    get_dword(ea) -> uint32
    Get one dword (32-bit) of the program at 'ea'. This function takes into account
    order of bytes specified in idainfo::is_be() This function works only for 8bit
    byte processors.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_dword(*args)

def get_qword(*args):
    r"""
    get_qword(ea) -> uint64
    Get one qword (64-bit) of the program at 'ea'. This function takes into account
    order of bytes specified in idainfo::is_be() This function works only for 8bit
    byte processors.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_qword(*args)

def get_wide_byte(*args):
    r"""
    get_wide_byte(ea) -> uint64
    Get one wide byte of the program at 'ea'. Some processors may access more than
    8bit quantity at an address. These processors have 32-bit byte organization from
    the IDA's point of view.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_wide_byte(*args)

def get_wide_word(*args):
    r"""
    get_wide_word(ea) -> uint64
    Get one wide word (2 'byte') of the program at 'ea'. Some processors may access
    more than 8bit quantity at an address. These processors have 32-bit byte
    organization from the IDA's point of view. This function takes into account
    order of bytes specified in idainfo::is_be()

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_wide_word(*args)

def get_wide_dword(*args):
    r"""
    get_wide_dword(ea) -> uint64
    Get two wide words (4 'bytes') of the program at 'ea'. Some processors may
    access more than 8bit quantity at an address. These processors have 32-bit byte
    organization from the IDA's point of view. This function takes into account
    order of bytes specified in idainfo::is_be()
    @note: this function works incorrectly if processor_t::nbits > 16

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_wide_dword(*args)

def get_16bit(*args):
    r"""
    get_16bit(ea) -> uint32
    Get 16bits of the program at 'ea'.

    @param ea: (C++: ea_t)
    @return: 1 byte (getFullByte()) if the current processor has 16-bit byte,
             otherwise return get_word()
    """
    return _ida_bytes.get_16bit(*args)

def get_32bit(*args):
    r"""
    get_32bit(ea) -> uint32
    Get not more than 32bits of the program at 'ea'.

    @param ea: (C++: ea_t)
    @return: 32 bit value, depending on processor_t::nbits:
    * if ( nbits <= 8 ) return get_dword(ea);
    * if ( nbits <= 16) return get_wide_word(ea);
    * return get_wide_byte(ea);
    """
    return _ida_bytes.get_32bit(*args)

def get_64bit(*args):
    r"""
    get_64bit(ea) -> uint64
    Get not more than 64bits of the program at 'ea'.

    @param ea: (C++: ea_t)
    @return: 64 bit value, depending on processor_t::nbits:
    * if ( nbits <= 8 ) return get_qword(ea);
    * if ( nbits <= 16) return get_wide_dword(ea);
    * return get_wide_byte(ea);
    """
    return _ida_bytes.get_64bit(*args)

def get_data_value(*args):
    r"""
    get_data_value(v, ea, size) -> bool
    Get the value at of the item at 'ea'. This function works with entities up to
    sizeof(ea_t) (bytes, word, etc)

    @param v: (C++: uval_t *) pointer to the result. may be nullptr
    @param ea: (C++: ea_t) linear address
    @param size: (C++: asize_t) size of data to read. If 0, then the item type at 'ea' will be used
    @return: success
    """
    return _ida_bytes.get_data_value(*args)

def get_original_byte(*args):
    r"""
    get_original_byte(ea) -> uint64
    Get original byte value (that was before patching). This function works for wide
    byte processors too.

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_original_byte(*args)

def get_original_word(*args):
    r"""
    get_original_word(ea) -> uint64
    Get original word value (that was before patching). This function works for wide
    byte processors too. This function takes into account order of bytes specified
    in idainfo::is_be()

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_original_word(*args)

def get_original_dword(*args):
    r"""
    get_original_dword(ea) -> uint64
    Get original dword (that was before patching) This function works for wide byte
    processors too. This function takes into account order of bytes specified in
    idainfo::is_be()

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_original_dword(*args)

def get_original_qword(*args):
    r"""
    get_original_qword(ea) -> uint64
    Get original qword value (that was before patching) This function DOESN'T work
    for wide byte processors too. This function takes into account order of bytes
    specified in idainfo::is_be()

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.get_original_qword(*args)

def put_byte(*args):
    r"""
    put_byte(ea, x) -> bool
    Set value of one byte of the program. This function modifies the database. If
    the debugger is active then the debugged process memory is patched too.
    @note: The original value of the byte is completely lost and can't be recovered
           by the get_original_byte() function. See also put_dbg_byte() to write to
           the process memory directly when the debugger is active. This function
           can handle wide byte processors.

    @param ea: (C++: ea_t) linear address
    @param x: (C++: uint64) byte value
    @return: true if the database has been modified
    """
    return _ida_bytes.put_byte(*args)

def put_word(*args):
    r"""
    put_word(ea, x)
    Set value of one word of the program. This function takes into account order of
    bytes specified in idainfo::is_be() This function works for wide byte processors
    too.
    @note: The original value of the word is completely lost and can't be recovered
           by the get_original_word() function. ea - linear address x - word value

    @param ea: (C++: ea_t)
    @param x: (C++: uint64)
    """
    return _ida_bytes.put_word(*args)

def put_dword(*args):
    r"""
    put_dword(ea, x)
    Set value of one dword of the program. This function takes into account order of
    bytes specified in idainfo::is_be() This function works for wide byte processors
    too.

    @param ea: (C++: ea_t) linear address
    @param x: (C++: uint64) dword value
    @note: the original value of the dword is completely lost and can't be recovered
           by the get_original_dword() function.
    """
    return _ida_bytes.put_dword(*args)

def put_qword(*args):
    r"""
    put_qword(ea, x)
    Set value of one qword (8 bytes) of the program. This function takes into
    account order of bytes specified in idainfo::is_be() This function DOESN'T works
    for wide byte processors.

    @param ea: (C++: ea_t) linear address
    @param x: (C++: uint64) qword value
    """
    return _ida_bytes.put_qword(*args)

def patch_byte(*args):
    r"""
    patch_byte(ea, x) -> bool
    Patch a byte of the program. The original value of the byte is saved and can be
    obtained by get_original_byte(). This function works for wide byte processors
    too.
    @retval true: the database has been modified,
    @retval false: the debugger is running and the process' memory has value 'x' at
                   address 'ea', or the debugger is not running, and the IDB has
                   value 'x' at address 'ea already.

    @param ea: (C++: ea_t)
    @param x: (C++: uint64)
    """
    return _ida_bytes.patch_byte(*args)

def patch_word(*args):
    r"""
    patch_word(ea, x) -> bool
    Patch a word of the program. The original value of the word is saved and can be
    obtained by get_original_word(). This function works for wide byte processors
    too. This function takes into account order of bytes specified in
    idainfo::is_be()
    @retval true: the database has been modified,
    @retval false: the debugger is running and the process' memory has value 'x' at
                   address 'ea', or the debugger is not running, and the IDB has
                   value 'x' at address 'ea already.

    @param ea: (C++: ea_t)
    @param x: (C++: uint64)
    """
    return _ida_bytes.patch_word(*args)

def patch_dword(*args):
    r"""
    patch_dword(ea, x) -> bool
    Patch a dword of the program. The original value of the dword is saved and can
    be obtained by get_original_dword(). This function DOESN'T work for wide byte
    processors. This function takes into account order of bytes specified in
    idainfo::is_be()
    @retval true: the database has been modified,
    @retval false: the debugger is running and the process' memory has value 'x' at
                   address 'ea', or the debugger is not running, and the IDB has
                   value 'x' at address 'ea already.

    @param ea: (C++: ea_t)
    @param x: (C++: uint64)
    """
    return _ida_bytes.patch_dword(*args)

def patch_qword(*args):
    r"""
    patch_qword(ea, x) -> bool
    Patch a qword of the program. The original value of the qword is saved and can
    be obtained by get_original_qword(). This function DOESN'T work for wide byte
    processors. This function takes into account order of bytes specified in
    idainfo::is_be()
    @retval true: the database has been modified,
    @retval false: the debugger is running and the process' memory has value 'x' at
                   address 'ea', or the debugger is not running, and the IDB has
                   value 'x' at address 'ea already.

    @param ea: (C++: ea_t)
    @param x: (C++: uint64)
    """
    return _ida_bytes.patch_qword(*args)

def revert_byte(*args):
    r"""
    revert_byte(ea) -> bool
    Revert patched byte
    @retval true: byte was patched before and reverted now

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.revert_byte(*args)

def add_byte(*args):
    r"""
    add_byte(ea, value)
    Add a value to one byte of the program. This function works for wide byte
    processors too.

    @param ea: (C++: ea_t) linear address
    @param value: (C++: uint32) byte value
    """
    return _ida_bytes.add_byte(*args)

def add_word(*args):
    r"""
    add_word(ea, value)
    Add a value to one word of the program. This function works for wide byte
    processors too. This function takes into account order of bytes specified in
    idainfo::is_be()

    @param ea: (C++: ea_t) linear address
    @param value: (C++: uint64) byte value
    """
    return _ida_bytes.add_word(*args)

def add_dword(*args):
    r"""
    add_dword(ea, value)
    Add a value to one dword of the program. This function works for wide byte
    processors too. This function takes into account order of bytes specified in
    idainfo::is_be()
    @note: this function works incorrectly if processor_t::nbits > 16

    @param ea: (C++: ea_t) linear address
    @param value: (C++: uint64) byte value
    """
    return _ida_bytes.add_dword(*args)

def add_qword(*args):
    r"""
    add_qword(ea, value)
    Add a value to one qword of the program. This function does not work for wide
    byte processors. This function takes into account order of bytes specified in
    idainfo::is_be()

    @param ea: (C++: ea_t) linear address
    @param value: (C++: uint64) byte value
    """
    return _ida_bytes.add_qword(*args)

def get_zero_ranges(*args):
    r"""
    get_zero_ranges(zranges, range) -> bool
    Return set of ranges with zero initialized bytes. The returned set includes only
    big zero initialized ranges (at least >1KB). Some zero initialized byte ranges
    may be not included. Only zero bytes that use the sparse storage method (STT_MM)
    are reported.

    @param zranges: (C++: rangeset_t *) pointer to the return value. cannot be nullptr
    @param range: (C++: const range_t *) the range of addresses to verify. can be nullptr - means all
                  ranges
    @return: true if the result is a non-empty set
    """
    return _ida_bytes.get_zero_ranges(*args)
GMB_READALL = _ida_bytes.GMB_READALL
r"""
try to read all bytes; if this bit is not set, fail at first uninited byte
"""

GMB_WAITBOX = _ida_bytes.GMB_WAITBOX
r"""
show wait box (may return -1 in this case)
"""


def put_bytes(*args):
    r"""
    put_bytes(ea, buf)
    Modify the specified number of bytes of the program. This function does not save
    the original values of bytes. See also patch_bytes().

    @param ea: (C++: ea_t) linear address
    @param buf: (C++: const void *) buffer with new values of bytes
    """
    return _ida_bytes.put_bytes(*args)

def patch_bytes(*args):
    r"""
    patch_bytes(ea, buf)
    Patch the specified number of bytes of the program. Original values of bytes are
    saved and are available with get_original...() functions. See also put_bytes().

    @param ea: (C++: ea_t) linear address
    @param buf: (C++: const void *) buffer with new values of bytes
    """
    return _ida_bytes.patch_bytes(*args)
MS_CLS = _ida_bytes.MS_CLS
r"""
Mask for typing.
"""

FF_CODE = _ida_bytes.FF_CODE
r"""
Code ?
"""

FF_DATA = _ida_bytes.FF_DATA
r"""
Data ?
"""

FF_TAIL = _ida_bytes.FF_TAIL
r"""
Tail ?
"""

FF_UNK = _ida_bytes.FF_UNK
r"""
Unknown ?
"""


def is_code(*args):
    r"""
    is_code(F) -> bool
    Does flag denote start of an instruction?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_code(*args)

def f_is_code(*args):
    r"""
    f_is_code(F, arg2) -> bool
    Does flag denote start of an instruction?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_code(*args)

def is_data(*args):
    r"""
    is_data(F) -> bool
    Does flag denote start of data?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_data(*args)

def f_is_data(*args):
    r"""
    f_is_data(F, arg2) -> bool
    Does flag denote start of data?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_data(*args)

def is_tail(*args):
    r"""
    is_tail(F) -> bool
    Does flag denote tail byte?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_tail(*args)

def f_is_tail(*args):
    r"""
    f_is_tail(F, arg2) -> bool
    Does flag denote tail byte?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_tail(*args)

def is_not_tail(*args):
    r"""
    is_not_tail(F) -> bool
    Does flag denote tail byte?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_not_tail(*args)

def f_is_not_tail(*args):
    r"""
    f_is_not_tail(F, arg2) -> bool
    Does flag denote tail byte?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_not_tail(*args)

def is_unknown(*args):
    r"""
    is_unknown(F) -> bool
    Does flag denote unexplored byte?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_unknown(*args)

def is_head(*args):
    r"""
    is_head(F) -> bool
    Does flag denote start of instruction OR data?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_head(*args)

def f_is_head(*args):
    r"""
    f_is_head(F, arg2) -> bool
    Does flag denote start of instruction OR data?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_head(*args)

def del_items(*args):
    r"""
    del_items(ea, flags=0, nbytes=1, may_destroy=None) -> bool
    Convert item (instruction/data) to unexplored bytes. The whole item (including
    the head and tail bytes) will be destroyed. It is allowed to pass any address in
    the item to this function

    @param ea: (C++: ea_t) any address within the first item to delete
    @param flags: (C++: int) combination of Unexplored byte conversion flags
    @param nbytes: (C++: asize_t) number of bytes in the range to be undefined
    @param may_destroy: (C++: may_destroy_cb_t *) optional routine invoked before deleting a head item. If
                        callback returns false then item is not to be deleted and
                        operation fails
    @return: true on sucessful operation, otherwise false
    """
    return _ida_bytes.del_items(*args)
DELIT_SIMPLE = _ida_bytes.DELIT_SIMPLE
r"""
simply undefine the specified item(s)
"""

DELIT_EXPAND = _ida_bytes.DELIT_EXPAND
r"""
propagate undefined items; for example if removing an instruction removes all
references to the next instruction, then plan to convert to unexplored the next
instruction too.
"""

DELIT_DELNAMES = _ida_bytes.DELIT_DELNAMES
r"""
delete any names at the specified address range (except for the starting
address). this bit is valid if nbytes > 1
"""

DELIT_NOTRUNC = _ida_bytes.DELIT_NOTRUNC
r"""
don't truncate the current function even if AF_TRFUNC is set
"""

DELIT_NOUNAME = _ida_bytes.DELIT_NOUNAME
r"""
reject to delete if a user name is in address range (except for the starting
address). this bit is valid if nbytes > 1
"""

DELIT_NOCMT = _ida_bytes.DELIT_NOCMT
r"""
reject to delete if a comment is in address range (except for the starting
address). this bit is valid if nbytes > 1
"""

DELIT_KEEPFUNC = _ida_bytes.DELIT_KEEPFUNC
r"""
do not undefine the function start. Just delete xrefs, ops e.t.c.
"""


def is_manual_insn(*args):
    r"""
    is_manual_insn(ea) -> bool
    Is the instruction overridden?

    @param ea: (C++: ea_t) linear address of the instruction or data item
    """
    return _ida_bytes.is_manual_insn(*args)

def get_manual_insn(*args):
    r"""
    get_manual_insn(ea) -> str
    Retrieve the user-specified string for the manual instruction.

    @param ea: (C++: ea_t) linear address of the instruction or data item
    @return: size of manual instruction or -1
    """
    return _ida_bytes.get_manual_insn(*args)

def set_manual_insn(*args):
    r"""
    set_manual_insn(ea, manual_insn)
    Set manual instruction string.

    @param ea: (C++: ea_t) linear address of the instruction or data item
    @param manual_insn: (C++: const char *) "" - delete manual string. nullptr - do nothing
    """
    return _ida_bytes.set_manual_insn(*args)
MS_COMM = _ida_bytes.MS_COMM
r"""
Mask of common bits.
"""

FF_COMM = _ida_bytes.FF_COMM
r"""
Has comment ?
"""

FF_REF = _ida_bytes.FF_REF
r"""
has references
"""

FF_LINE = _ida_bytes.FF_LINE
r"""
Has next or prev lines ?
"""

FF_NAME = _ida_bytes.FF_NAME
r"""
Has name ?
"""

FF_LABL = _ida_bytes.FF_LABL
r"""
Has dummy name?
"""

FF_FLOW = _ida_bytes.FF_FLOW
r"""
Exec flow from prev instruction.
"""

FF_SIGN = _ida_bytes.FF_SIGN
r"""
Inverted sign of operands.
"""

FF_BNOT = _ida_bytes.FF_BNOT
r"""
Bitwise negation of operands.
"""

FF_UNUSED = _ida_bytes.FF_UNUSED
r"""
unused bit (was used for variable bytes)
"""


def is_flow(*args):
    r"""
    is_flow(F) -> bool
    Does the previous instruction exist and pass execution flow to the current byte?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_flow(*args)

def has_extra_cmts(*args):
    r"""
    has_extra_cmts(F) -> bool
    Does the current byte have additional anterior or posterior lines?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_extra_cmts(*args)

def f_has_extra_cmts(*args):
    r"""
    f_has_extra_cmts(f, arg2) -> bool

    @param f: flags_t
    @param arg2: void *
    """
    return _ida_bytes.f_has_extra_cmts(*args)

def has_cmt(*args):
    r"""
    has_cmt(F) -> bool
    Does the current byte have an indented comment?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_cmt(*args)

def f_has_cmt(*args):
    r"""
    f_has_cmt(f, arg2) -> bool

    @param f: flags_t
    @param arg2: void *
    """
    return _ida_bytes.f_has_cmt(*args)

def has_xref(*args):
    r"""
    has_xref(F) -> bool
    Does the current byte have cross-references to it?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_xref(*args)

def f_has_xref(*args):
    r"""
    f_has_xref(f, arg2) -> bool
    Does the current byte have cross-references to it?

    @param f: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_has_xref(*args)

def has_name(*args):
    r"""
    has_name(F) -> bool
    Does the current byte have non-trivial (non-dummy) name?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_name(*args)

def f_has_name(*args):
    r"""
    f_has_name(f, arg2) -> bool
    Does the current byte have non-trivial (non-dummy) name?

    @param f: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_has_name(*args)
FF_ANYNAME = _ida_bytes.FF_ANYNAME


def has_dummy_name(*args):
    r"""
    has_dummy_name(F) -> bool
    Does the current byte have dummy (auto-generated, with special prefix) name?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_dummy_name(*args)

def f_has_dummy_name(*args):
    r"""
    f_has_dummy_name(f, arg2) -> bool
    Does the current byte have dummy (auto-generated, with special prefix) name?

    @param f: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_has_dummy_name(*args)

def has_auto_name(*args):
    r"""
    has_auto_name(F) -> bool
    Does the current byte have auto-generated (no special prefix) name?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_auto_name(*args)

def has_any_name(*args):
    r"""
    has_any_name(F) -> bool
    Does the current byte have any name?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_any_name(*args)

def has_user_name(*args):
    r"""
    has_user_name(F) -> bool
    Does the current byte have user-specified name?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_user_name(*args)

def f_has_user_name(*args):
    r"""
    f_has_user_name(F, arg2) -> bool
    Does the current byte have user-specified name?

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_has_user_name(*args)

def is_invsign(*args):
    r"""
    is_invsign(ea, F, n) -> bool
    Should sign of n-th operand inverted during output?. allowed values of n:
    0-first operand, 1-other operands

    @param ea: (C++: ea_t)
    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_invsign(*args)

def toggle_sign(*args):
    r"""
    toggle_sign(ea, n) -> bool
    Toggle sign of n-th operand. allowed values of n: 0-first operand, 1-other
    operands

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.toggle_sign(*args)

def is_bnot(*args):
    r"""
    is_bnot(ea, F, n) -> bool
    Should we negate the operand?. asm_t::a_bnot should be defined in the idp module
    in order to work with this function

    @param ea: (C++: ea_t)
    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_bnot(*args)

def toggle_bnot(*args):
    r"""
    toggle_bnot(ea, n) -> bool
    Toggle binary negation of operand. also see is_bnot()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.toggle_bnot(*args)

def is_lzero(*args):
    r"""
    is_lzero(ea, n) -> bool
    Display leading zeroes in operands. The global switch for the leading zeroes is
    in idainfo::s_genflags The leading zeroes doesn't work if the octal numbers
    start with 0 Display leading zeroes? (takes into account idainfo::s_genflags)

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_lzero(*args)

def set_lzero(*args):
    r"""
    set_lzero(ea, n) -> bool
    Set toggle lzero bit.

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.set_lzero(*args)

def clr_lzero(*args):
    r"""
    clr_lzero(ea, n) -> bool
    Clear lzero bit.

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.clr_lzero(*args)

def toggle_lzero(*args):
    r"""
    toggle_lzero(ea, n) -> bool

    @param ea: ea_t
    @param n: int
    """
    return _ida_bytes.toggle_lzero(*args)

def leading_zero_important(*args):
    r"""
    leading_zero_important(ea, n) -> bool
    Check if leading zeroes are important.

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.leading_zero_important(*args)
MS_0TYPE = _ida_bytes.MS_0TYPE
r"""
Mask for 1st arg typing.
"""

FF_0VOID = _ida_bytes.FF_0VOID
r"""
Void (unknown)?
"""

FF_0NUMH = _ida_bytes.FF_0NUMH
r"""
Hexadecimal number?
"""

FF_0NUMD = _ida_bytes.FF_0NUMD
r"""
Decimal number?
"""

FF_0CHAR = _ida_bytes.FF_0CHAR
r"""
Char ('x')?
"""

FF_0SEG = _ida_bytes.FF_0SEG
r"""
Segment?
"""

FF_0OFF = _ida_bytes.FF_0OFF
r"""
Offset?
"""

FF_0NUMB = _ida_bytes.FF_0NUMB
r"""
Binary number?
"""

FF_0NUMO = _ida_bytes.FF_0NUMO
r"""
Octal number?
"""

FF_0ENUM = _ida_bytes.FF_0ENUM
r"""
Enumeration?
"""

FF_0FOP = _ida_bytes.FF_0FOP
r"""
Forced operand?
"""

FF_0STRO = _ida_bytes.FF_0STRO
r"""
Struct offset?
"""

FF_0STK = _ida_bytes.FF_0STK
r"""
Stack variable?
"""

FF_0FLT = _ida_bytes.FF_0FLT
r"""
Floating point number?
"""

FF_0CUST = _ida_bytes.FF_0CUST
r"""
Custom representation?
"""

MS_1TYPE = _ida_bytes.MS_1TYPE
r"""
Mask for the type of other operands.
"""

FF_1VOID = _ida_bytes.FF_1VOID
r"""
Void (unknown)?
"""

FF_1NUMH = _ida_bytes.FF_1NUMH
r"""
Hexadecimal number?
"""

FF_1NUMD = _ida_bytes.FF_1NUMD
r"""
Decimal number?
"""

FF_1CHAR = _ida_bytes.FF_1CHAR
r"""
Char ('x')?
"""

FF_1SEG = _ida_bytes.FF_1SEG
r"""
Segment?
"""

FF_1OFF = _ida_bytes.FF_1OFF
r"""
Offset?
"""

FF_1NUMB = _ida_bytes.FF_1NUMB
r"""
Binary number?
"""

FF_1NUMO = _ida_bytes.FF_1NUMO
r"""
Octal number?
"""

FF_1ENUM = _ida_bytes.FF_1ENUM
r"""
Enumeration?
"""

FF_1FOP = _ida_bytes.FF_1FOP
r"""
Forced operand?
"""

FF_1STRO = _ida_bytes.FF_1STRO
r"""
Struct offset?
"""

FF_1STK = _ida_bytes.FF_1STK
r"""
Stack variable?
"""

FF_1FLT = _ida_bytes.FF_1FLT
r"""
Floating point number?
"""

FF_1CUST = _ida_bytes.FF_1CUST
r"""
Custom representation?
"""


def is_defarg0(*args):
    r"""
    is_defarg0(F) -> bool
    Is the first operand defined? Initially operand has no defined representation.

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_defarg0(*args)

def is_defarg1(*args):
    r"""
    is_defarg1(F) -> bool
    Is the second operand defined? Initially operand has no defined representation.

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_defarg1(*args)

def is_off0(*args):
    r"""
    is_off0(F) -> bool
    Is the first operand offset? (example: push offset xxx)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_off0(*args)

def is_off1(*args):
    r"""
    is_off1(F) -> bool
    Is the second operand offset? (example: mov ax, offset xxx)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_off1(*args)

def is_char0(*args):
    r"""
    is_char0(F) -> bool
    Is the first operand character constant? (example: push 'a')

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_char0(*args)

def is_char1(*args):
    r"""
    is_char1(F) -> bool
    Is the second operand character constant? (example: mov al, 'a')

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_char1(*args)

def is_seg0(*args):
    r"""
    is_seg0(F) -> bool
    Is the first operand segment selector? (example: push seg seg001)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_seg0(*args)

def is_seg1(*args):
    r"""
    is_seg1(F) -> bool
    Is the second operand segment selector? (example: mov dx, seg dseg)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_seg1(*args)

def is_enum0(*args):
    r"""
    is_enum0(F) -> bool
    Is the first operand a symbolic constant (enum member)?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_enum0(*args)

def is_enum1(*args):
    r"""
    is_enum1(F) -> bool
    Is the second operand a symbolic constant (enum member)?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_enum1(*args)

def is_stroff0(*args):
    r"""
    is_stroff0(F) -> bool
    Is the first operand an offset within a struct?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_stroff0(*args)

def is_stroff1(*args):
    r"""
    is_stroff1(F) -> bool
    Is the second operand an offset within a struct?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_stroff1(*args)

def is_stkvar0(*args):
    r"""
    is_stkvar0(F) -> bool
    Is the first operand a stack variable?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_stkvar0(*args)

def is_stkvar1(*args):
    r"""
    is_stkvar1(F) -> bool
    Is the second operand a stack variable?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_stkvar1(*args)

def is_float0(*args):
    r"""
    is_float0(F) -> bool
    Is the first operand a floating point number?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_float0(*args)

def is_float1(*args):
    r"""
    is_float1(F) -> bool
    Is the second operand a floating point number?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_float1(*args)

def is_custfmt0(*args):
    r"""
    is_custfmt0(F) -> bool
    Does the first operand use a custom data representation?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_custfmt0(*args)

def is_custfmt1(*args):
    r"""
    is_custfmt1(F) -> bool
    Does the second operand use a custom data representation?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_custfmt1(*args)

def is_numop0(*args):
    r"""
    is_numop0(F) -> bool
    Is the first operand a number (i.e. binary, octal, decimal or hex?)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_numop0(*args)

def is_numop1(*args):
    r"""
    is_numop1(F) -> bool
    Is the second operand a number (i.e. binary, octal, decimal or hex?)

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_numop1(*args)

def get_optype_flags0(*args):
    r"""
    get_optype_flags0(F) -> flags_t
    Get flags for first operand.

    @param F: (C++: flags_t)
    """
    return _ida_bytes.get_optype_flags0(*args)

def get_optype_flags1(*args):
    r"""
    get_optype_flags1(F) -> flags_t
    Get flags for second operand.

    @param F: (C++: flags_t)
    """
    return _ida_bytes.get_optype_flags1(*args)
OPND_OUTER = _ida_bytes.OPND_OUTER
r"""
outer offset base (combined with operand number). used only in set, get,
del_offset() functions
"""

OPND_MASK = _ida_bytes.OPND_MASK
r"""
mask for operand number
"""

OPND_ALL = _ida_bytes.OPND_ALL
r"""
all operands
"""


def is_defarg(*args):
    r"""
    is_defarg(F, n) -> bool
    is defined?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_defarg(*args)

def is_off(*args):
    r"""
    is_off(F, n) -> bool
    is offset?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_off(*args)

def is_char(*args):
    r"""
    is_char(F, n) -> bool
    is character constant?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_char(*args)

def is_seg(*args):
    r"""
    is_seg(F, n) -> bool
    is segment?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_seg(*args)

def is_enum(*args):
    r"""
    is_enum(F, n) -> bool
    is enum?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_enum(*args)

def is_manual(*args):
    r"""
    is_manual(F, n) -> bool
    is forced operand? (use is_forced_operand())

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_manual(*args)

def is_stroff(*args):
    r"""
    is_stroff(F, n) -> bool
    is struct offset?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_stroff(*args)

def is_stkvar(*args):
    r"""
    is_stkvar(F, n) -> bool
    is stack variable?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_stkvar(*args)

def is_fltnum(*args):
    r"""
    is_fltnum(F, n) -> bool
    is floating point number?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_fltnum(*args)

def is_custfmt(*args):
    r"""
    is_custfmt(F, n) -> bool
    is custom data format?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_custfmt(*args)

def is_numop(*args):
    r"""
    is_numop(F, n) -> bool
    is number (bin, oct, dec, hex)?

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_numop(*args)

def is_suspop(*args):
    r"""
    is_suspop(ea, F, n) -> bool
    is suspicious operand?

    @param ea: (C++: ea_t)
    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.is_suspop(*args)

def op_adds_xrefs(*args):
    r"""
    op_adds_xrefs(F, n) -> bool
    Should processor module create xrefs from the operand?. Currently 'offset' and
    'structure offset' operands create xrefs

    @param F: (C++: flags_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_adds_xrefs(*args)

def set_op_type(*args):
    r"""
    set_op_type(ea, type, n) -> bool
    (internal function) change representation of operand(s).

    @param ea: (C++: ea_t) linear address
    @param type: (C++: flags_t) new flag value (should be obtained from char_flag(), num_flag() and
                 similar functions)
    @param n: (C++: int) number of operand (0, 1, -1)
    @retval 1: ok
    @retval 0: failed (applied to a tail byte)
    """
    return _ida_bytes.set_op_type(*args)

def op_seg(*args):
    r"""
    op_seg(ea, n) -> bool
    Set operand representation to be 'segment'. If applied to unexplored bytes,
    converts them to 16/32bit word data

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: success
    """
    return _ida_bytes.op_seg(*args)

def op_enum(*args):
    r"""
    op_enum(ea, n, id, serial) -> bool
    Set operand representation to be 'enum_t'. If applied to unexplored bytes,
    converts them to 16/32bit word data

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @param id: (C++: enum_t) id of enum
    @param serial: (C++: uchar) the serial number of the constant in the enumeration, usually 0.
                   the serial numbers are used if the enumeration contains several
                   constants with the same value
    @return: success
    """
    return _ida_bytes.op_enum(*args)

def get_enum_id(*args):
    r"""
    get_enum_id(ea, n) -> enum_t
    Get enum id of 'enum' operand.

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: id of enum or BADNODE
    """
    return _ida_bytes.get_enum_id(*args)

def op_stroff(*args):
    r"""
    op_stroff(insn, n, path, path_len, delta) -> bool
    Set operand representation to be 'struct offset'. If applied to unexplored
    bytes, converts them to 16/32bit word data

    @param insn: (C++: const insn_t &) the instruction
    @param n: (C++: int) number of operand (0, 1, -1)
    @param path: (C++: const tid_t *) structure path (strpath). see nalt.hpp for more info.
    @param path_len: (C++: int) length of the structure path
    @param delta: (C++: adiff_t) struct offset delta. usually 0. denotes the difference between the
                  structure base and the pointer into the structure.
    @return: success
    """
    return _ida_bytes.op_stroff(*args)

def get_stroff_path(*args):
    r"""
    get_stroff_path(path, delta, ea, n) -> int
    Get struct path of operand.

    @param path: (C++: tid_t *) buffer for structure path (strpath). see nalt.hpp for more info.
    @param delta: (C++: adiff_t *) struct offset delta
    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: length of strpath
    """
    return _ida_bytes.get_stroff_path(*args)

def op_stkvar(*args):
    r"""
    op_stkvar(ea, n) -> bool
    Set operand representation to be 'stack variable'. Should be applied to an
    instruction within a function. Should be applied after creating a stack var
    using insn_t::create_stkvar().

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: success
    """
    return _ida_bytes.op_stkvar(*args)

def set_forced_operand(*args):
    r"""
    set_forced_operand(ea, n, op) -> bool
    Set forced operand.

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, 2)
    @param op: (C++: const char *) text of operand
    * nullptr: do nothing (return 0)
    * "" : delete forced operand
    @return: success
    """
    return _ida_bytes.set_forced_operand(*args)

def get_forced_operand(*args):
    r"""
    get_forced_operand(ea, n) -> str
    Get forced operand.

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, 2)
    @return: size of forced operand or -1
    """
    return _ida_bytes.get_forced_operand(*args)

def is_forced_operand(*args):
    r"""
    is_forced_operand(ea, n) -> bool
    Is operand manually defined?.

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, 2)
    """
    return _ida_bytes.is_forced_operand(*args)

def char_flag(*args):
    r"""
    char_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.char_flag(*args)

def off_flag(*args):
    r"""
    off_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.off_flag(*args)

def enum_flag(*args):
    r"""
    enum_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.enum_flag(*args)

def stroff_flag(*args):
    r"""
    stroff_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.stroff_flag(*args)

def stkvar_flag(*args):
    r"""
    stkvar_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.stkvar_flag(*args)

def flt_flag(*args):
    r"""
    flt_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.flt_flag(*args)

def custfmt_flag(*args):
    r"""
    custfmt_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.custfmt_flag(*args)

def seg_flag(*args):
    r"""
    seg_flag() -> flags_t
    see Bits: instruction operand types
    """
    return _ida_bytes.seg_flag(*args)

def num_flag(*args):
    r"""
    num_flag() -> flags_t
    Get number of default base (bin, oct, dec, hex)
    """
    return _ida_bytes.num_flag(*args)

def hex_flag(*args):
    r"""
    hex_flag() -> flags_t
    Get number flag of the base, regardless of current processor - better to use
    num_flag()
    """
    return _ida_bytes.hex_flag(*args)

def dec_flag(*args):
    r"""
    dec_flag() -> flags_t
    Get number flag of the base, regardless of current processor - better to use
    num_flag()
    """
    return _ida_bytes.dec_flag(*args)

def oct_flag(*args):
    r"""
    oct_flag() -> flags_t
    Get number flag of the base, regardless of current processor - better to use
    num_flag()
    """
    return _ida_bytes.oct_flag(*args)

def bin_flag(*args):
    r"""
    bin_flag() -> flags_t
    Get number flag of the base, regardless of current processor - better to use
    num_flag()
    """
    return _ida_bytes.bin_flag(*args)

def op_chr(*args):
    r"""
    op_chr(ea, n) -> bool
    set op type to char_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_chr(*args)

def op_num(*args):
    r"""
    op_num(ea, n) -> bool
    set op type to num_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_num(*args)

def op_hex(*args):
    r"""
    op_hex(ea, n) -> bool
    set op type to hex_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_hex(*args)

def op_dec(*args):
    r"""
    op_dec(ea, n) -> bool
    set op type to dec_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_dec(*args)

def op_oct(*args):
    r"""
    op_oct(ea, n) -> bool
    set op type to oct_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_oct(*args)

def op_bin(*args):
    r"""
    op_bin(ea, n) -> bool
    set op type to bin_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_bin(*args)

def op_flt(*args):
    r"""
    op_flt(ea, n) -> bool
    set op type to flt_flag()

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    """
    return _ida_bytes.op_flt(*args)

def op_custfmt(*args):
    r"""
    op_custfmt(ea, n, fid) -> bool
    Set custom data format for operand (fid-custom data format id)

    @param ea: (C++: ea_t)
    @param n: (C++: int)
    @param fid: (C++: int)
    """
    return _ida_bytes.op_custfmt(*args)

def clr_op_type(*args):
    r"""
    clr_op_type(ea, n) -> bool
    Remove operand representation information. (set operand representation to be
    'undefined')

    @param ea: (C++: ea_t) linear address
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: success
    """
    return _ida_bytes.clr_op_type(*args)

def get_default_radix(*args):
    r"""
    get_default_radix() -> int
    Get default base of number for the current processor.

    @return: 2, 8, 10, 16
    """
    return _ida_bytes.get_default_radix(*args)

def get_radix(*args):
    r"""
    get_radix(F, n) -> int
    Get radix of the operand, in: flags. If the operand is not a number, returns
    get_default_radix()

    @param F: (C++: flags_t) flags
    @param n: (C++: int) number of operand (0, 1, -1)
    @return: 2, 8, 10, 16
    """
    return _ida_bytes.get_radix(*args)
DT_TYPE = _ida_bytes.DT_TYPE
r"""
Mask for DATA typing.
"""

FF_BYTE = _ida_bytes.FF_BYTE
r"""
byte
"""

FF_WORD = _ida_bytes.FF_WORD
r"""
word
"""

FF_DWORD = _ida_bytes.FF_DWORD
r"""
double word
"""

FF_QWORD = _ida_bytes.FF_QWORD
r"""
quadro word
"""

FF_TBYTE = _ida_bytes.FF_TBYTE
r"""
tbyte
"""

FF_STRLIT = _ida_bytes.FF_STRLIT
r"""
string literal
"""

FF_STRUCT = _ida_bytes.FF_STRUCT
r"""
struct variable
"""

FF_OWORD = _ida_bytes.FF_OWORD
r"""
octaword/xmm word (16 bytes/128 bits)
"""

FF_FLOAT = _ida_bytes.FF_FLOAT
r"""
float
"""

FF_DOUBLE = _ida_bytes.FF_DOUBLE
r"""
double
"""

FF_PACKREAL = _ida_bytes.FF_PACKREAL
r"""
packed decimal real
"""

FF_ALIGN = _ida_bytes.FF_ALIGN
r"""
alignment directive
"""

FF_CUSTOM = _ida_bytes.FF_CUSTOM
r"""
custom data type
"""

FF_YWORD = _ida_bytes.FF_YWORD
r"""
ymm word (32 bytes/256 bits)
"""

FF_ZWORD = _ida_bytes.FF_ZWORD
r"""
zmm word (64 bytes/512 bits)
"""


def code_flag(*args):
    r"""
    code_flag() -> flags_t
    FF_CODE
    """
    return _ida_bytes.code_flag(*args)

def byte_flag(*args):
    r"""
    byte_flag() -> flags_t
    Get a flags_t representing a byte.
    """
    return _ida_bytes.byte_flag(*args)

def word_flag(*args):
    r"""
    word_flag() -> flags_t
    Get a flags_t representing a word.
    """
    return _ida_bytes.word_flag(*args)

def dword_flag(*args):
    r"""
    dword_flag() -> flags_t
    Get a flags_t representing a double word.
    """
    return _ida_bytes.dword_flag(*args)

def qword_flag(*args):
    r"""
    qword_flag() -> flags_t
    Get a flags_t representing a quad word.
    """
    return _ida_bytes.qword_flag(*args)

def oword_flag(*args):
    r"""
    oword_flag() -> flags_t
    Get a flags_t representing a octaword.
    """
    return _ida_bytes.oword_flag(*args)

def yword_flag(*args):
    r"""
    yword_flag() -> flags_t
    Get a flags_t representing a ymm word.
    """
    return _ida_bytes.yword_flag(*args)

def zword_flag(*args):
    r"""
    zword_flag() -> flags_t
    Get a flags_t representing a zmm word.
    """
    return _ida_bytes.zword_flag(*args)

def tbyte_flag(*args):
    r"""
    tbyte_flag() -> flags_t
    Get a flags_t representing a tbyte.
    """
    return _ida_bytes.tbyte_flag(*args)

def strlit_flag(*args):
    r"""
    strlit_flag() -> flags_t
    Get a flags_t representing a string literal.
    """
    return _ida_bytes.strlit_flag(*args)

def stru_flag(*args):
    r"""
    stru_flag() -> flags_t
    Get a flags_t representing a struct.
    """
    return _ida_bytes.stru_flag(*args)

def cust_flag(*args):
    r"""
    cust_flag() -> flags_t
    Get a flags_t representing custom type data.
    """
    return _ida_bytes.cust_flag(*args)

def align_flag(*args):
    r"""
    align_flag() -> flags_t
    Get a flags_t representing an alignment directive.
    """
    return _ida_bytes.align_flag(*args)

def float_flag(*args):
    r"""
    float_flag() -> flags_t
    Get a flags_t representing a float.
    """
    return _ida_bytes.float_flag(*args)

def double_flag(*args):
    r"""
    double_flag() -> flags_t
    Get a flags_t representing a double.
    """
    return _ida_bytes.double_flag(*args)

def packreal_flag(*args):
    r"""
    packreal_flag() -> flags_t
    Get a flags_t representing a packed decimal real.
    """
    return _ida_bytes.packreal_flag(*args)

def is_byte(*args):
    r"""
    is_byte(F) -> bool
    FF_BYTE

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_byte(*args)

def is_word(*args):
    r"""
    is_word(F) -> bool
    FF_WORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_word(*args)

def is_dword(*args):
    r"""
    is_dword(F) -> bool
    FF_DWORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_dword(*args)

def is_qword(*args):
    r"""
    is_qword(F) -> bool
    FF_QWORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_qword(*args)

def is_oword(*args):
    r"""
    is_oword(F) -> bool
    FF_OWORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_oword(*args)

def is_yword(*args):
    r"""
    is_yword(F) -> bool
    FF_YWORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_yword(*args)

def is_zword(*args):
    r"""
    is_zword(F) -> bool
    FF_ZWORD

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_zword(*args)

def is_tbyte(*args):
    r"""
    is_tbyte(F) -> bool
    FF_TBYTE

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_tbyte(*args)

def is_float(*args):
    r"""
    is_float(F) -> bool
    FF_FLOAT

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_float(*args)

def is_double(*args):
    r"""
    is_double(F) -> bool
    FF_DOUBLE

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_double(*args)

def is_pack_real(*args):
    r"""
    is_pack_real(F) -> bool
    FF_PACKREAL

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_pack_real(*args)

def is_strlit(*args):
    r"""
    is_strlit(F) -> bool
    FF_STRLIT

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_strlit(*args)

def is_struct(*args):
    r"""
    is_struct(F) -> bool
    FF_STRUCT

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_struct(*args)

def is_align(*args):
    r"""
    is_align(F) -> bool
    FF_ALIGN

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_align(*args)

def is_custom(*args):
    r"""
    is_custom(F) -> bool
    FF_CUSTOM

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_custom(*args)

def f_is_byte(*args):
    r"""
    f_is_byte(F, arg2) -> bool
    See is_byte()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_byte(*args)

def f_is_word(*args):
    r"""
    f_is_word(F, arg2) -> bool
    See is_word()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_word(*args)

def f_is_dword(*args):
    r"""
    f_is_dword(F, arg2) -> bool
    See is_dword()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_dword(*args)

def f_is_qword(*args):
    r"""
    f_is_qword(F, arg2) -> bool
    See is_qword()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_qword(*args)

def f_is_oword(*args):
    r"""
    f_is_oword(F, arg2) -> bool
    See is_oword()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_oword(*args)

def f_is_yword(*args):
    r"""
    f_is_yword(F, arg2) -> bool
    See is_yword()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_yword(*args)

def f_is_tbyte(*args):
    r"""
    f_is_tbyte(F, arg2) -> bool
    See is_tbyte()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_tbyte(*args)

def f_is_float(*args):
    r"""
    f_is_float(F, arg2) -> bool
    See is_float()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_float(*args)

def f_is_double(*args):
    r"""
    f_is_double(F, arg2) -> bool
    See is_double()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_double(*args)

def f_is_pack_real(*args):
    r"""
    f_is_pack_real(F, arg2) -> bool
    See is_pack_real()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_pack_real(*args)

def f_is_strlit(*args):
    r"""
    f_is_strlit(F, arg2) -> bool
    See is_strlit()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_strlit(*args)

def f_is_struct(*args):
    r"""
    f_is_struct(F, arg2) -> bool
    See is_struct()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_struct(*args)

def f_is_align(*args):
    r"""
    f_is_align(F, arg2) -> bool
    See is_align()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_align(*args)

def f_is_custom(*args):
    r"""
    f_is_custom(F, arg2) -> bool
    See is_custom()

    @param F: (C++: flags_t)
    @param arg2: void *
    """
    return _ida_bytes.f_is_custom(*args)

def is_same_data_type(*args):
    r"""
    is_same_data_type(F1, F2) -> bool
    Do the given flags specify the same data type?

    @param F1: (C++: flags_t)
    @param F2: (C++: flags_t)
    """
    return _ida_bytes.is_same_data_type(*args)

def get_flags_by_size(*args):
    r"""
    get_flags_by_size(size) -> flags_t
    Get flags from size (in bytes). Supported sizes: 1, 2, 4, 8, 16, 32. For other
    sizes returns 0

    @param size: (C++: size_t)
    """
    return _ida_bytes.get_flags_by_size(*args)

def create_data(*args):
    r"""
    create_data(ea, dataflag, size, tid) -> bool
    Convert to data (byte, word, dword, etc). This function may be used to create
    arrays.

    @param ea: (C++: ea_t) linear address
    @param dataflag: (C++: flags_t) type of data. Value of function byte_flag(), word_flag(), etc.
    @param size: (C++: asize_t) size of array in bytes. should be divisible by the size of one item
                 of the specified type. for variable sized items it can be specified
                 as 0, and the kernel will try to calculate the size.
    @param tid: (C++: tid_t) type id. If the specified type is a structure, then tid is structure
                id. Otherwise should be BADNODE.
    @return: success
    """
    return _ida_bytes.create_data(*args)

def calc_dflags(*args):
    r"""
    calc_dflags(f, force) -> flags_t

    @param f: flags_t
    @param force: bool
    """
    return _ida_bytes.calc_dflags(*args)

def create_byte(*args):
    r"""
    create_byte(ea, length, force=False) -> bool
    Convert to byte.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_byte(*args)

def create_word(*args):
    r"""
    create_word(ea, length, force=False) -> bool
    Convert to word.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_word(*args)

def create_dword(*args):
    r"""
    create_dword(ea, length, force=False) -> bool
    Convert to dword.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_dword(*args)

def create_qword(*args):
    r"""
    create_qword(ea, length, force=False) -> bool
    Convert to quadword.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_qword(*args)

def create_oword(*args):
    r"""
    create_oword(ea, length, force=False) -> bool
    Convert to octaword/xmm word.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_oword(*args)

def create_yword(*args):
    r"""
    create_yword(ea, length, force=False) -> bool
    Convert to ymm word.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_yword(*args)

def create_zword(*args):
    r"""
    create_zword(ea, length, force=False) -> bool
    Convert to zmm word.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_zword(*args)

def create_tbyte(*args):
    r"""
    create_tbyte(ea, length, force=False) -> bool
    Convert to tbyte.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_tbyte(*args)

def create_float(*args):
    r"""
    create_float(ea, length, force=False) -> bool
    Convert to float.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_float(*args)

def create_double(*args):
    r"""
    create_double(ea, length, force=False) -> bool
    Convert to double.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_double(*args)

def create_packed_real(*args):
    r"""
    create_packed_real(ea, length, force=False) -> bool
    Convert to packed decimal real.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_packed_real(*args)

def create_struct(*args):
    r"""
    create_struct(ea, length, tid, force=False) -> bool
    Convert to struct.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param tid: (C++: tid_t)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_struct(*args)

def create_custdata(*args):
    r"""
    create_custdata(ea, length, dtid, fid, force=False) -> bool
    Convert to custom data type.

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    @param dtid: (C++: int)
    @param fid: (C++: int)
    @param force: (C++: bool)
    """
    return _ida_bytes.create_custdata(*args)

def create_align(*args):
    r"""
    create_align(ea, length, alignment) -> bool
    Create an alignment item.

    @param ea: (C++: ea_t) linear address
    @param length: (C++: asize_t) size of the item in bytes. 0 means to infer from ALIGNMENT
    @param alignment: (C++: int) alignment exponent. Example: 3 means align to 8 bytes. 0 means
                      to infer from LENGTH It is forbidden to specify both LENGTH
                      and ALIGNMENT as 0.
    @return: success
    """
    return _ida_bytes.create_align(*args)

def calc_min_align(*args):
    r"""
    calc_min_align(length) -> int
    Calculate the minimal possible alignment exponent.

    @param length: (C++: asize_t) size of the item in bytes.
    @return: a value in the 1..32 range
    """
    return _ida_bytes.calc_min_align(*args)

def calc_max_align(*args):
    r"""
    calc_max_align(endea) -> int
    Calculate the maximal possible alignment exponent.

    @param endea: (C++: ea_t) end address of the alignment item.
    @return: a value in the 0..32 range
    """
    return _ida_bytes.calc_max_align(*args)

def calc_def_align(*args):
    r"""
    calc_def_align(ea, mina, maxa) -> int
    Calculate the default alignment exponent.

    @param ea: (C++: ea_t) linear address
    @param mina: (C++: int) minimal possible alignment exponent.
    @param maxa: (C++: int) minimal possible alignment exponent.
    """
    return _ida_bytes.calc_def_align(*args)

def create_16bit_data(*args):
    r"""
    create_16bit_data(ea, length) -> bool
    Convert to 16-bit quantity (take the byte size into account)

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    """
    return _ida_bytes.create_16bit_data(*args)

def create_32bit_data(*args):
    r"""
    create_32bit_data(ea, length) -> bool
    Convert to 32-bit quantity (take the byte size into account)

    @param ea: (C++: ea_t)
    @param length: (C++: asize_t)
    """
    return _ida_bytes.create_32bit_data(*args)
ALOPT_IGNHEADS = _ida_bytes.ALOPT_IGNHEADS
r"""
don't stop if another data item is encountered. only the byte values will be
used to determine the string length. if not set, a defined data item or
instruction will truncate the string
"""

ALOPT_IGNPRINT = _ida_bytes.ALOPT_IGNPRINT
r"""
if set, don't stop at non-printable codepoints, but only at the terminating
character (or not unicode-mapped character (e.g., 0x8f in CP1252))
"""

ALOPT_IGNCLT = _ida_bytes.ALOPT_IGNCLT
r"""
if set, don't stop at codepoints that are not part of the current 'culture';
accept all those that are graphical (this is typically used used by user-
initiated actions creating string literals.)
"""

ALOPT_MAX4K = _ida_bytes.ALOPT_MAX4K
r"""
if string length is more than 4K, return the accumulated length
"""

ALOPT_ONLYTERM = _ida_bytes.ALOPT_ONLYTERM
r"""
only the termination characters can be at the string end. Without this option
illegal characters also terminate the string.
"""


def get_max_strlit_length(*args):
    r"""
    get_max_strlit_length(ea, strtype, options=0) -> size_t
    Determine maximum length of string literal.

    If the string literal has a length prefix (e.g., STRTYPE_LEN2 has a two-byte
    length prefix), the length of that prefix (i.e., 2) will be part of the returned
    value.

    @param ea: (C++: ea_t) starting address
    @param strtype: (C++: int32) string type. one of String type codes
    @param options: (C++: int) combination of string literal length options
    @return: length of the string in octets (octet==8bit)
    """
    return _ida_bytes.get_max_strlit_length(*args)
STRCONV_ESCAPE = _ida_bytes.STRCONV_ESCAPE
r"""
convert non-printable characters to C escapes (
, \xNN, \uNNNN)
"""

STRCONV_REPLCHAR = _ida_bytes.STRCONV_REPLCHAR
r"""
convert non-printable characters to the Unicode replacement character (U+FFFD)
"""

STRCONV_INCLLEN = _ida_bytes.STRCONV_INCLLEN
r"""
for Pascal-style strings, include the prefixing length byte(s) as C-escaped
sequence
"""


def create_strlit(*args):
    r"""
    create_strlit(start, len, strtype) -> bool
    Convert to string literal and give a meaningful name. 'start' may be higher than
    'end', the kernel will swap them in this case

    @param start: (C++: ea_t) starting address
    @param len: (C++: size_t) length of the string in bytes. if 0, then get_max_strlit_length()
                will be used to determine the length
    @param strtype: (C++: int32) string type. one of String type codes
    @return: success
    """
    return _ida_bytes.create_strlit(*args)
PSTF_TNORM = _ida_bytes.PSTF_TNORM
r"""
use normal name
"""

PSTF_TBRIEF = _ida_bytes.PSTF_TBRIEF
r"""
use brief name (e.g., in the 'Strings' window)
"""

PSTF_TINLIN = _ida_bytes.PSTF_TINLIN
r"""
use 'inline' name (e.g., in the structures comments)
"""

PSTF_TMASK = _ida_bytes.PSTF_TMASK
r"""
type mask
"""

PSTF_HOTKEY = _ida_bytes.PSTF_HOTKEY
r"""
have hotkey markers part of the name
"""

PSTF_ENC = _ida_bytes.PSTF_ENC
r"""
if encoding is specified, append it
"""

PSTF_ONLY_ENC = _ida_bytes.PSTF_ONLY_ENC
r"""
generate only the encoding name
"""


def get_opinfo(*args):
    r"""
    get_opinfo(buf, ea, n, flags) -> opinfo_t
    Get additional information about an operand representation.

    @param buf: (C++: opinfo_t *) buffer to receive the result. may not be nullptr
    @param ea: (C++: ea_t) linear address of item
    @param n: (C++: int) number of operand, 0 or 1
    @param flags: (C++: flags_t) flags of the item
    @return: nullptr if no additional representation information
    """
    return _ida_bytes.get_opinfo(*args)

def set_opinfo(*args):
    r"""
    set_opinfo(ea, n, flag, ti, suppress_events=False) -> bool
    Set additional information about an operand representation. This function is a
    low level one. Only the kernel should use it.

    @param ea: (C++: ea_t) linear address of the item
    @param n: (C++: int) number of operand, 0 or 1 (see the note below)
    @param flag: (C++: flags_t) flags of the item
    @param ti: (C++: const opinfo_t *) additional representation information
    @param suppress_events: (C++: bool) do not generate changing_op_type and op_type_changed
                            events
    @return: success
    @note: for custom formats (if is_custfmt(flag, n) is true) or for offsets (if
           is_off(flag, n) is true) N can be in range -1..UA_MAXOP-1. In the case of
           -1 the additional information about all operands will be set.
    """
    return _ida_bytes.set_opinfo(*args)

def get_data_elsize(*args):
    r"""
    get_data_elsize(ea, F, ti=None) -> asize_t
    Get size of data type specified in flags 'F'.

    @param ea: (C++: ea_t) linear address of the item
    @param F: (C++: flags_t) flags
    @param ti: (C++: const opinfo_t *) additional information about the data type. For example, if the
               current item is a structure instance, then ti->tid is structure id.
               Otherwise is ignored (may be nullptr). If specified as nullptr, will
               be automatically retrieved from the database
    @return: * byte : 1
    * word : 2
    * etc...
    """
    return _ida_bytes.get_data_elsize(*args)

def get_full_data_elsize(*args):
    r"""
    get_full_data_elsize(ea, F, ti=None) -> asize_t
    Get full size of data type specified in flags 'F'. takes into account processors
    with wide bytes e.g. returns 2 for a byte element with 16-bit bytes

    @param ea: (C++: ea_t)
    @param F: (C++: flags_t)
    @param ti: (C++: const opinfo_t *) opinfo_t const *
    """
    return _ida_bytes.get_full_data_elsize(*args)

def is_varsize_item(*args):
    r"""
    is_varsize_item(ea, F, ti=None, itemsize=None) -> int
    Is the item at 'ea' variable size?.

    @param ea: (C++: ea_t) linear address of the item
    @param F: (C++: flags_t) flags
    @param ti: (C++: const opinfo_t *) additional information about the data type. For example, if the
               current item is a structure instance, then ti->tid is structure id.
               Otherwise is ignored (may be nullptr). If specified as nullptr, will
               be automatically retrieved from the database
    @param itemsize: (C++: asize_t *) if not nullptr and the item is varsize, itemsize will contain
                     the calculated item size (for struct types, the minimal size is
                     returned)
    @retval 1: varsize item
    @retval 0: fixed item
    @retval -1: error (bad data definition)
    """
    return _ida_bytes.is_varsize_item(*args)

def can_define_item(*args):
    r"""
    can_define_item(ea, length, flags) -> bool
    Can define item (instruction/data) of the specified 'length', starting at 'ea'?
    @note: if there is an item starting at 'ea', this function ignores it
    @note: this function converts to unexplored all encountered data items with
           fixup information. Should be fixed in the future.

    @param flags: (C++: flags_t) if not 0, then the kernel will ignore the data types specified by
                  the flags and destroy them. For example:
    1000 dw 5
                     1002 db 5 ; undef
                     1003 db 5 ; undef
                     1004 dw 5
                     1006 dd 5
                      can_define_item(1000, 6, 0) - false because of dw at 1004
    can_define_item(1000, 6, word_flag()) - true, word at 1004 is destroyed
    @param length: (C++: asize_t)
    @param flags: (C++: flags_t) if not 0, then the kernel will ignore the data types specified by
                  the flags and destroy them. For example:
    1000 dw 5
                     1002 db 5 ; undef
                     1003 db 5 ; undef
                     1004 dw 5
                     1006 dd 5
                      can_define_item(1000, 6, 0) - false because of dw at 1004
    can_define_item(1000, 6, word_flag()) - true, word at 1004 is destroyed
    @return: 1-yes, 0-no
    * a new item would cross segment boundaries
    * a new item would overlap with existing items (except items specified by
    'flags')
    """
    return _ida_bytes.can_define_item(*args)
MS_CODE = _ida_bytes.MS_CODE
r"""
Mask for code bits.
"""

FF_FUNC = _ida_bytes.FF_FUNC
r"""
function start?
"""

FF_IMMD = _ida_bytes.FF_IMMD
r"""
Has Immediate value ?
"""

FF_JUMP = _ida_bytes.FF_JUMP
r"""
Has jump table or switch_info?
"""


def has_immd(*args):
    r"""
    has_immd(F) -> bool
    Has immediate value?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.has_immd(*args)

def is_func(*args):
    r"""
    is_func(F) -> bool
    Is function start?

    @param F: (C++: flags_t)
    """
    return _ida_bytes.is_func(*args)

def set_immd(*args):
    r"""
    set_immd(ea) -> bool
    Set 'has immediate operand' flag. Returns true if the FF_IMMD bit was not set
    and now is set

    @param ea: (C++: ea_t)
    """
    return _ida_bytes.set_immd(*args)
class data_type_t(object):
    r"""
    Proxy of C++ data_type_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    props = property(_ida_bytes.data_type_t_props_get, _ida_bytes.data_type_t_props_set, doc=r"""props""")
    r"""
    properties
    """
    name = property(_ida_bytes.data_type_t_name_get, _ida_bytes.data_type_t_name_set, doc=r"""name""")
    r"""
    name of the data type. must be unique
    """
    menu_name = property(_ida_bytes.data_type_t_menu_name_get, _ida_bytes.data_type_t_menu_name_set, doc=r"""menu_name""")
    r"""
    Visible data type name to use in menus if nullptr, no menu item will be created
    """
    hotkey = property(_ida_bytes.data_type_t_hotkey_get, _ida_bytes.data_type_t_hotkey_set, doc=r"""hotkey""")
    r"""
    Hotkey for the corresponding menu item if nullptr, no hotkey will be associated
    with the menu item
    """
    asm_keyword = property(_ida_bytes.data_type_t_asm_keyword_get, _ida_bytes.data_type_t_asm_keyword_set, doc=r"""asm_keyword""")
    r"""
    keyword to use for this type in the assembly if nullptr, the data type cannot be
    used in the listing it can still be used in cpuregs window
    """
    value_size = property(_ida_bytes.data_type_t_value_size_get, _ida_bytes.data_type_t_value_size_set, doc=r"""value_size""")
    r"""
    size of the value in bytes
    """

    def is_present_in_menus(self, *args):
        r"""
        is_present_in_menus(self) -> bool
        Should this type be shown in UI menus

        @return: success
        """
        return _ida_bytes.data_type_t_is_present_in_menus(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self, _self, name, value_size=0, menu_name=None, hotkey=None, asm_keyword=None, props=0) -> data_type_t

        @param self: PyObject *
        @param name: char const *
        @param value_size: asize_t
        @param menu_name: char const *
        @param hotkey: char const *
        @param asm_keyword: char const *
        @param props: int
        """
        _ida_bytes.data_type_t_swiginit(self, _ida_bytes.new_data_type_t(*args))
    __swig_destroy__ = _ida_bytes.delete_data_type_t

    def __get_id(self, *args):
        r"""
        __get_id(self) -> int
        """
        return _ida_bytes.data_type_t___get_id(self, *args)

    id = property(__get_id)
    __real__init__ = __init__
    def __init__(self, *args):
        self.__real__init__(self, *args) # pass 'self' as part of args


# Register data_type_t in _ida_bytes:
_ida_bytes.data_type_t_swigregister(data_type_t)
DTP_NODUP = _ida_bytes.DTP_NODUP
r"""
do not use dup construct
"""


class data_format_t(object):
    r"""
    Proxy of C++ data_format_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    props = property(_ida_bytes.data_format_t_props_get, _ida_bytes.data_format_t_props_set, doc=r"""props""")
    r"""
    properties (currently 0)
    """
    name = property(_ida_bytes.data_format_t_name_get, _ida_bytes.data_format_t_name_set, doc=r"""name""")
    r"""
    Format name, must be unique.
    """
    menu_name = property(_ida_bytes.data_format_t_menu_name_get, _ida_bytes.data_format_t_menu_name_set, doc=r"""menu_name""")
    r"""
    Visible format name to use in menus if nullptr, no menu item will be created
    """
    hotkey = property(_ida_bytes.data_format_t_hotkey_get, _ida_bytes.data_format_t_hotkey_set, doc=r"""hotkey""")
    r"""
    Hotkey for the corresponding menu item if nullptr, no hotkey will be associated
    with the menu item
    """
    value_size = property(_ida_bytes.data_format_t_value_size_get, _ida_bytes.data_format_t_value_size_set, doc=r"""value_size""")
    r"""
    size of the value in bytes 0 means any size is ok data formats that are
    registered for standard types (dtid 0) may be called with any value_size
    (instruction operands only)
    """
    text_width = property(_ida_bytes.data_format_t_text_width_get, _ida_bytes.data_format_t_text_width_set, doc=r"""text_width""")
    r"""
    Usual width of the text representation This value is used to calculate the width
    of the control to display values of this type
    """

    def is_present_in_menus(self, *args):
        r"""
        is_present_in_menus(self) -> bool
        Should this format be shown in UI menus

        @return: success
        """
        return _ida_bytes.data_format_t_is_present_in_menus(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self, _self, name, value_size=0, menu_name=None, props=0, hotkey=None, text_width=0) -> data_format_t

        @param self: PyObject *
        @param name: char const *
        @param value_size: asize_t
        @param menu_name: char const *
        @param props: int
        @param hotkey: char const *
        @param text_width: int32
        """
        _ida_bytes.data_format_t_swiginit(self, _ida_bytes.new_data_format_t(*args))
    __swig_destroy__ = _ida_bytes.delete_data_format_t

    def __get_id(self, *args):
        r"""
        __get_id(self) -> int
        """
        return _ida_bytes.data_format_t___get_id(self, *args)

    id = property(__get_id)
    __real__init__ = __init__
    def __init__(self, *args):
        self.__real__init__(self, *args) # pass 'self' as part of args


# Register data_format_t in _ida_bytes:
_ida_bytes.data_format_t_swigregister(data_format_t)


def get_custom_data_type(*args):
    r"""
    get_custom_data_type(dtid) -> data_type_t
    Get definition of a registered custom data type.

    @param dtid: (C++: int) data type id
    @return: data type definition or nullptr
    """
    return _ida_bytes.get_custom_data_type(*args)

def get_custom_data_format(*args):
    r"""
    get_custom_data_format(dfid) -> data_format_t
    Get definition of a registered custom data format.

    @param dfid: (C++: int) data format id
    @return: data format definition or nullptr
    """
    return _ida_bytes.get_custom_data_format(*args)

def attach_custom_data_format(*args):
    r"""
    attach_custom_data_format(dtid, dfid) -> bool
    Attach the data format to the data type.

    @param dtid: (C++: int) data type id that can use the data format. 0 means all standard
                 data types. Such data formats can be applied to any data item or
                 instruction operands. For instruction operands, the
                 data_format_t::value_size check is not performed by the kernel.
    @param dfid: (C++: int) data format id
    @retval true: ok
    @retval false: no such `dtid', or no such `dfid', or the data format has already
                   been attached to the data type
    """
    return _ida_bytes.attach_custom_data_format(*args)

def detach_custom_data_format(*args):
    r"""
    detach_custom_data_format(dtid, dfid) -> bool
    Detach the data format from the data type. Unregistering a custom data type
    detaches all attached data formats, no need to detach them explicitly. You still
    need unregister them. Unregistering a custom data format detaches it from all
    attached data types.

    @param dtid: (C++: int) data type id to detach data format from
    @param dfid: (C++: int) data format id to detach
    @retval true: ok
    @retval false: no such `dtid', or no such `dfid', or the data format was not
                   attached to the data type
    """
    return _ida_bytes.detach_custom_data_format(*args)

def is_attached_custom_data_format(*args):
    r"""
    is_attached_custom_data_format(dtid, dfid) -> bool
    Is the custom data format attached to the custom data type?

    @param dtid: (C++: int) data type id
    @param dfid: (C++: int) data format id
    @return: true or false
    """
    return _ida_bytes.is_attached_custom_data_format(*args)

def get_custom_data_types(*args):
    r"""
    get_custom_data_types(out, min_size=0, max_size=BADADDR) -> int
    Get list of registered custom data type ids.

    @param out: (C++: intvec_t *) buffer for the output. may be nullptr
    @param min_size: (C++: asize_t) minimum value size
    @param max_size: (C++: asize_t) maximum value size
    @return: number of custom data types with the specified size limits
    """
    return _ida_bytes.get_custom_data_types(*args)

def get_custom_data_formats(*args):
    r"""
    get_custom_data_formats(out, dtid) -> int
    Get list of attached custom data formats for the specified data type.

    @param out: (C++: intvec_t *) buffer for the output. may be nullptr
    @param dtid: (C++: int) data type id
    @return: number of returned custom data formats. if error, returns -1
    """
    return _ida_bytes.get_custom_data_formats(*args)

def find_custom_data_type(*args):
    r"""
    find_custom_data_type(name) -> int
    Get id of a custom data type.

    @param name: (C++: const char *) name of the custom data type
    @return: id or -1
    """
    return _ida_bytes.find_custom_data_type(*args)

def find_custom_data_format(*args):
    r"""
    find_custom_data_format(name) -> int
    Get id of a custom data format.

    @param name: (C++: const char *) name of the custom data format
    @return: id or -1
    """
    return _ida_bytes.find_custom_data_format(*args)

def set_cmt(*args):
    r"""
    set_cmt(ea, comm, rptble) -> bool
    Set an indented comment.

    @param ea: (C++: ea_t) linear address
    @param comm: (C++: const char *) comment string
    * nullptr: do nothing (return 0)
    * "" : delete comment
    @param rptble: (C++: bool) is repeatable?
    @return: success
    """
    return _ida_bytes.set_cmt(*args)

def get_cmt(*args):
    r"""
    get_cmt(ea, rptble) -> str
    Get an indented comment.

    @param ea: (C++: ea_t) linear address. may point to tail byte, the function will find start
               of the item
    @param rptble: (C++: bool) get repeatable comment?
    @return: size of comment or -1
    """
    return _ida_bytes.get_cmt(*args)

def append_cmt(*args):
    r"""
    append_cmt(ea, str, rptble) -> bool
    Append to an indented comment. Creates a new comment if none exists. Appends a
    newline character and the specified string otherwise.

    @param ea: (C++: ea_t) linear address
    @param str: (C++: const char *) comment string to append
    @param rptble: (C++: bool) append to repeatable comment?
    @return: success
    """
    return _ida_bytes.append_cmt(*args)

def get_predef_insn_cmt(*args):
    r"""
    get_predef_insn_cmt(ins) -> str
    Get predefined comment.

    @param ins: (C++: const insn_t &) current instruction information
    @return: size of comment or -1
    """
    return _ida_bytes.get_predef_insn_cmt(*args)

def find_byte(*args):
    r"""
    find_byte(sEA, size, value, bin_search_flags) -> ea_t
    Find forward a byte with the specified value (only 8-bit value from the
    database). example: ea=4 size=3 will inspect addresses 4, 5, and 6

    @param sEA: (C++: ea_t) linear address
    @param size: (C++: asize_t) number of bytes to inspect
    @param value: (C++: uchar) value to find
    @param bin_search_flags: (C++: int) combination of Search flags
    @return: address of byte or BADADDR
    """
    return _ida_bytes.find_byte(*args)

def find_byter(*args):
    r"""
    find_byter(sEA, size, value, bin_search_flags) -> ea_t
    Find reverse a byte with the specified value (only 8-bit value from the
    database). example: ea=4 size=3 will inspect addresses 6, 5, and 4

    @param sEA: (C++: ea_t) the lower address of the search range
    @param size: (C++: asize_t) number of bytes to inspect
    @param value: (C++: uchar) value to find
    @param bin_search_flags: (C++: int) combination of Search flags
    @return: address of byte or BADADDR
    """
    return _ida_bytes.find_byter(*args)
class compiled_binpat_t(object):
    r"""
    Proxy of C++ compiled_binpat_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    bytes = property(_ida_bytes.compiled_binpat_t_bytes_get, _ida_bytes.compiled_binpat_t_bytes_set, doc=r"""bytes""")
    mask = property(_ida_bytes.compiled_binpat_t_mask_get, _ida_bytes.compiled_binpat_t_mask_set, doc=r"""mask""")
    strlits = property(_ida_bytes.compiled_binpat_t_strlits_get, _ida_bytes.compiled_binpat_t_strlits_set, doc=r"""strlits""")
    encidx = property(_ida_bytes.compiled_binpat_t_encidx_get, _ida_bytes.compiled_binpat_t_encidx_set, doc=r"""encidx""")

    def __init__(self, *args):
        r"""
        __init__(self) -> compiled_binpat_t
        """
        _ida_bytes.compiled_binpat_t_swiginit(self, _ida_bytes.new_compiled_binpat_t(*args))

    def all_bytes_defined(self, *args):
        r"""
        all_bytes_defined(self) -> bool
        """
        return _ida_bytes.compiled_binpat_t_all_bytes_defined(self, *args)

    def qclear(self, *args):
        r"""
        qclear(self)
        """
        return _ida_bytes.compiled_binpat_t_qclear(self, *args)

    def __eq__(self, *args):
        r"""
        __eq__(self, r) -> bool

        @param r: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_t___eq__(self, *args)

    def __ne__(self, *args):
        r"""
        __ne__(self, r) -> bool

        @param r: compiled_binpat_t const &
        """
        return _ida_bytes.compiled_binpat_t___ne__(self, *args)
    __swig_destroy__ = _ida_bytes.delete_compiled_binpat_t

# Register compiled_binpat_t in _ida_bytes:
_ida_bytes.compiled_binpat_t_swigregister(compiled_binpat_t)

PBSENC_DEF1BPU = _ida_bytes.PBSENC_DEF1BPU

PBSENC_ALL = _ida_bytes.PBSENC_ALL


def parse_binpat_str(*args):
    r"""
    parse_binpat_str(out, ea, _in, radix, strlits_encoding=0) -> str
    Convert user-specified binary string to internal representation. The 'in'
    parameter contains space-separated tokens:
    - numbers (numeric base is determined by 'radix')
    - if value of number fits a byte, it is considered as a byte
    - if value of number fits a word, it is considered as 2 bytes
    - if value of number fits a dword,it is considered as 4 bytes
    - "..." string constants
    - 'x'  single-character constants
    - ?    variable bytes

    Note that string constants are surrounded with double quotes.

    Here are a few examples (assuming base 16):
    CD 21          - bytes 0xCD, 0x21
    21CD           - bytes 0xCD, 0x21 (little endian ) or 0x21, 0xCD (big-endian)
    "Hello", 0     - the null terminated string "Hello"
    L"Hello"       - 'H', 0, 'e', 0, 'l', 0, 'l', 0, 'o', 0
    B8 ? ? ? ? 90  - byte 0xB8, 4 bytes with any value, byte 0x90

    @param out: (C++: compiled_binpat_vec_t *) a vector of compiled binary patterns, for use with bin_search2()
    @param ea: (C++: ea_t) linear address to convert for (the conversion depends on the address,
               because the number of bits in a byte depend on the segment type)
    @param in: (C++: const char *) input text string
    @param radix: (C++: int) numeric base of numbers (8,10,16)
    @param strlits_encoding: (C++: int) the target encoding into which the string literals
                             present in 'in', should be encoded. Can be any from [1,
                             get_encoding_qty()), or the special values PBSENC_*
    @return: false either in case of parsing error, or if at least one requested
             target encoding couldn't encode the string literals present in "in".
    """
    return _ida_bytes.parse_binpat_str(*args)

def bin_search3(*args):
    r"""
    bin_search3(start_ea, end_ea, data, flags) -> ea_t
    Search for a patter in the program.

    @param start_ea: (C++: ea_t) linear address, start of range to search
    @param end_ea: (C++: ea_t) linear address, end of range to search (exclusive)
    @param data: (C++: const compiled_binpat_vec_t &) the prepared data to search for (see parse_binpat_str())
    @param flags: (C++: int) combination of Search flags
    @return: BADADDR (if pressed Ctrl-Break or not found) or pattern address.
    """
    return _ida_bytes.bin_search3(*args)
BIN_SEARCH_CASE = _ida_bytes.BIN_SEARCH_CASE
r"""
case sensitive
"""

BIN_SEARCH_NOCASE = _ida_bytes.BIN_SEARCH_NOCASE
r"""
case insensitive
"""

BIN_SEARCH_NOBREAK = _ida_bytes.BIN_SEARCH_NOBREAK
r"""
don't check for Ctrl-Break
"""

BIN_SEARCH_INITED = _ida_bytes.BIN_SEARCH_INITED
r"""
find_byte, find_byter: any initilized value
"""

BIN_SEARCH_NOSHOW = _ida_bytes.BIN_SEARCH_NOSHOW
r"""
don't show search progress or update screen
"""

BIN_SEARCH_FORWARD = _ida_bytes.BIN_SEARCH_FORWARD
r"""
search forward for bytes
"""

BIN_SEARCH_BACKWARD = _ida_bytes.BIN_SEARCH_BACKWARD
r"""
search backward for bytes
"""

BIN_SEARCH_BITMASK = _ida_bytes.BIN_SEARCH_BITMASK
r"""
searching using strict bit mask
"""


def next_inited(*args):
    r"""
    next_inited(ea, maxea) -> ea_t
    Find the next initialized address.

    @param ea: (C++: ea_t)
    @param maxea: (C++: ea_t)
    """
    return _ida_bytes.next_inited(*args)

def prev_inited(*args):
    r"""
    prev_inited(ea, minea) -> ea_t
    Find the previous initialized address.

    @param ea: (C++: ea_t)
    @param minea: (C++: ea_t)
    """
    return _ida_bytes.prev_inited(*args)

def equal_bytes(*args):
    r"""
    equal_bytes(ea, image, mask, len, bin_search_flags) -> bool
    Compare 'len' bytes of the program starting from 'ea' with 'image'.

    @param ea: (C++: ea_t) linear address
    @param image: (C++: const uchar *) bytes to compare with
    @param mask: (C++: const uchar *) array of mask bytes, it's length is 'len'. if the flag
                 BIN_SEARCH_BITMASK is passsed, 'bitwise AND' is used to compare. if
                 not; 1 means to perform the comparison of the corresponding byte. 0
                 means not to perform. if mask == nullptr, then all bytes of 'image'
                 will be compared. if mask == SKIP_FF_MASK then 0xFF bytes will be
                 skipped
    @param len: (C++: size_t) length of block to compare in bytes.
    @param bin_search_flags: (C++: int) combination of Search flags
    @retval 1: equal
    @retval 0: not equal
    """
    return _ida_bytes.equal_bytes(*args)
class hidden_range_t(ida_range.range_t):
    r"""
    Proxy of C++ hidden_range_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    description = property(_ida_bytes.hidden_range_t_description_get, _ida_bytes.hidden_range_t_description_set, doc=r"""description""")
    r"""
    description to display if the range is collapsed
    """
    header = property(_ida_bytes.hidden_range_t_header_get, _ida_bytes.hidden_range_t_header_set, doc=r"""header""")
    r"""
    header lines to display if the range is expanded
    """
    footer = property(_ida_bytes.hidden_range_t_footer_get, _ida_bytes.hidden_range_t_footer_set, doc=r"""footer""")
    r"""
    footer lines to display if the range is expanded
    """
    visible = property(_ida_bytes.hidden_range_t_visible_get, _ida_bytes.hidden_range_t_visible_set, doc=r"""visible""")
    r"""
    the range state
    """
    color = property(_ida_bytes.hidden_range_t_color_get, _ida_bytes.hidden_range_t_color_set, doc=r"""color""")
    r"""
    range color
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> hidden_range_t
        """
        _ida_bytes.hidden_range_t_swiginit(self, _ida_bytes.new_hidden_range_t(*args))
    __swig_destroy__ = _ida_bytes.delete_hidden_range_t

# Register hidden_range_t in _ida_bytes:
_ida_bytes.hidden_range_t_swigregister(hidden_range_t)


def update_hidden_range(*args):
    r"""
    update_hidden_range(ha) -> bool
    Update hidden range information in the database. You cannot use this function to
    change the range boundaries

    @param ha: (C++: const hidden_range_t *) range to update
    @return: success
    """
    return _ida_bytes.update_hidden_range(*args)

def add_hidden_range(*args):
    r"""
    add_hidden_range(ea1, ea2, description, header, footer, color) -> bool
    Mark a range of addresses as hidden. The range will be created in the invisible
    state with the default color

    @param ea1: (C++: ea_t) linear address of start of the address range
    @param ea2: (C++: ea_t) linear address of end of the address range
    @param description: (C++: const char *) ,header,footer: range parameters
    @param header: (C++: const char *) char const *
    @param footer: (C++: const char *) char const *
    @param color: (C++: bgcolor_t)
    @return: success
    """
    return _ida_bytes.add_hidden_range(*args)

def get_hidden_range(*args):
    r"""
    get_hidden_range(ea) -> hidden_range_t
    Get pointer to hidden range structure, in: linear address.

    @param ea: (C++: ea_t) any address in the hidden range
    """
    return _ida_bytes.get_hidden_range(*args)

def getn_hidden_range(*args):
    r"""
    getn_hidden_range(n) -> hidden_range_t
    Get pointer to hidden range structure, in: number of hidden range.

    @param n: (C++: int) number of hidden range, is in range 0..get_hidden_range_qty()-1
    """
    return _ida_bytes.getn_hidden_range(*args)

def get_hidden_range_qty(*args):
    r"""
    get_hidden_range_qty() -> int
    Get number of hidden ranges.
    """
    return _ida_bytes.get_hidden_range_qty(*args)

def get_hidden_range_num(*args):
    r"""
    get_hidden_range_num(ea) -> int
    Get number of a hidden range.

    @param ea: (C++: ea_t) any address in the hidden range
    @return: number of hidden range (0..get_hidden_range_qty()-1)
    """
    return _ida_bytes.get_hidden_range_num(*args)

def get_prev_hidden_range(*args):
    r"""
    get_prev_hidden_range(ea) -> hidden_range_t
    Get pointer to previous hidden range.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to hidden range or nullptr if previous hidden range doesn't exist
    """
    return _ida_bytes.get_prev_hidden_range(*args)

def get_next_hidden_range(*args):
    r"""
    get_next_hidden_range(ea) -> hidden_range_t
    Get pointer to next hidden range.

    @param ea: (C++: ea_t) any address in the program
    @return: ptr to hidden range or nullptr if next hidden range doesn't exist
    """
    return _ida_bytes.get_next_hidden_range(*args)

def get_first_hidden_range(*args):
    r"""
    get_first_hidden_range() -> hidden_range_t
    Get pointer to the first hidden range.

    @return: ptr to hidden range or nullptr
    """
    return _ida_bytes.get_first_hidden_range(*args)

def get_last_hidden_range(*args):
    r"""
    get_last_hidden_range() -> hidden_range_t
    Get pointer to the last hidden range.

    @return: ptr to hidden range or nullptr
    """
    return _ida_bytes.get_last_hidden_range(*args)

def del_hidden_range(*args):
    r"""
    del_hidden_range(ea) -> bool
    Delete hidden range.

    @param ea: (C++: ea_t) any address in the hidden range
    @return: success
    """
    return _ida_bytes.del_hidden_range(*args)

def add_mapping(*args):
    r"""
    add_mapping(_from, to, size) -> bool
    IDA supports memory mapping. References to the addresses from the mapped range
    use data and meta-data from the mapping range.
    @note: You should set flag PR2_MAPPING in ph.flag2 to use memory mapping Add
           memory mapping range.

    @param from: (C++: ea_t) start of the mapped range (nonexistent address)
    @param to: (C++: ea_t) start of the mapping range (existent address)
    @param size: (C++: asize_t) size of the range
    @return: success
    """
    return _ida_bytes.add_mapping(*args)

def del_mapping(*args):
    r"""
    del_mapping(ea)
    Delete memory mapping range.

    @param ea: (C++: ea_t) any address in the mapped range
    """
    return _ida_bytes.del_mapping(*args)

def use_mapping(*args):
    r"""
    use_mapping(ea) -> ea_t
    Translate address according to current mappings.

    @param ea: (C++: ea_t) address to translate
    @return: translated address
    """
    return _ida_bytes.use_mapping(*args)

def get_mappings_qty(*args):
    r"""
    get_mappings_qty() -> size_t
    Get number of mappings.
    """
    return _ida_bytes.get_mappings_qty(*args)

def get_mapping(*args):
    r"""
    get_mapping(n) -> bool
    Get memory mapping range by its number.

    @param n: (C++: size_t) number of mapping range (0..get_mappings_qty()-1)
    @return: false if the specified range doesn't exist, otherwise returns `from',
             `to', `size'
    """
    return _ida_bytes.get_mapping(*args)

def visit_patched_bytes(*args):
    r"""
    visit_patched_bytes(ea1, ea2, py_callable) -> int
    Enumerates patched bytes in the given range and invokes a callable

    @param ea1: start address
    @param ea2: end address
    @param py_callable: a Python callable with the following prototype:
                     callable(ea, fpos, org_val, patch_val).
                     If the callable returns non-zero then that value will be
                     returned to the caller and the enumeration will be
                     interrupted.
    @return: Zero if the enumeration was successful or the return
             value of the callback if enumeration was interrupted.
    """
    return _ida_bytes.visit_patched_bytes(*args)

def get_bytes(*args):
    r"""
    get_bytes(ea, size, gmb_flags=0x01) -> bytes or None
    Get the specified number of bytes of the program.

    @param ea: program address
    @param size: number of bytes to return
    @param gmb_flags: int
    @return: the bytes (as a str), or None in case of failure
    """
    return _ida_bytes.get_bytes(*args)

def get_bytes_and_mask(*args):
    r"""
    get_bytes_and_mask(ea, size, gmb_flags=0x01) -> PyObject *
    Get the specified number of bytes of the program, and a bitmask
    specifying what bytes are defined and what bytes are not.

    @param ea: program address
    @param size: number of bytes to return
    @param gmb_flags: int
    @return: a tuple (bytes, mask), or None in case of failure.
             Both 'bytes' and 'mask' are 'str' instances.
    """
    return _ida_bytes.get_bytes_and_mask(*args)

def get_strlit_contents(*args):
    r"""
    get_strlit_contents(ea, py_len, type, flags=0) -> bytes or None
    Get contents of string literal, as UTF-8-encoded codepoints.
    It works even if the string has not been created in the database yet.

    Note that the returned value will be of type 'bytes'; if
    you want auto-conversion to unicode strings (that is: real Python
    strings), you should probably be using the idautils.Strings class.

    @param ea: linear address of the string
    @param py_len: length of the string in bytes (including terminating 0)
    @param type: type of the string. Represents both the character encoding,
                 <u>and</u> the 'type' of string at the given location.
    @param flags: combination of STRCONV_..., to perform output conversion.
    @return: a bytes-filled str object.
    """
    return _ida_bytes.get_strlit_contents(*args)

def bin_search(*args):
    r"""
    bin_search(start_ea, end_ea, data, flags) -> ea_t
    Search for a set of bytes in the program

    @param start_ea: linear address, start of range to search
    @param end_ea: linear address, end of range to search (exclusive)
    @param data: the prepared data to search for (see parse_binpat_str())
    @param flags: combination of BIN_SEARCH_* flags
    @return: the address of a match, or ida_idaapi.BADADDR if not found
    bin_search(start_ea, end_ea, image, imask, step, flags) -> ea_t

    @param start_ea: ea_t
    @param end_ea: ea_t
    @param image: bytevec_t const &
    @param imask: bytevec_t const &
    @param step: int
    @param flags: int
    """
    return _ida_bytes.bin_search(*args)

def print_strlit_type(*args):
    r"""
    print_strlit_type(strtype, flags=0) -> (str, str)
    Get string type information: the string type name (possibly decorated with
    hotkey markers), and the tooltip.

    @param strtype: (C++: int32) the string type
    @param flags: (C++: int) or'ed PSTF_* constants
    @return: length of generated text
    """
    return _ida_bytes.print_strlit_type(*args)

def get_octet(*args):
    r"""
    get_octet(ea, v, nbit) -> (int, int, int, int)
    Get 8 bits of the program at 'ea'. The main usage of this function is to iterate
    range of bytes. Here is an example:
    uint64 v;
    int nbit = 0;
    for ( ... ) {
    uchar byte = get_octet(&ea, &v, &nbit);
    ...
    }
    'ea' is incremented each time when a new byte is read. In the above example, it
    will be incremented in the first loop iteration.

    @param ea: (C++: ea_t *) ea_t
    @param v: (C++: uint64 *) uint64
    @param nbit: (C++: int *) int
    """
    return _ida_bytes.get_octet(*args)

def get_8bit(*args):
    r"""
    get_8bit(ea, v, nbit) -> PyObject *

    @param ea: ea_t
    @param v: uint32
    @param nbit: int
    """
    return _ida_bytes.get_8bit(*args)

#<pycode(py_bytes)>
#</pycode(py_bytes)>


def register_custom_data_type(*args):
    r"""
    register_custom_data_type(py_dt) -> int
    Registers a custom data type.

    @param py_dt: an instance of the data_type_t class
    @return:     < 0 if failed to register
        > 0 data type id
    """
    return _ida_bytes.register_custom_data_type(*args)

def unregister_custom_data_type(*args):
    r"""
    unregister_custom_data_type(dtid) -> bool
    Unregisters a custom data type.

    @param dtid: the data type id
    @return: Boolean
    """
    return _ida_bytes.unregister_custom_data_type(*args)

def register_custom_data_format(*args):
    r"""
    register_custom_data_format(py_df) -> int
    Registers a custom data format with a given data type.

    @param py_df: an instance of data_format_t
    @return:     < 0 if failed to register
        > 0 data format id
    """
    return _ida_bytes.register_custom_data_format(*args)

def unregister_custom_data_format(*args):
    r"""
    unregister_custom_data_format(dfid) -> bool
    Unregisters a custom data format

    @param dfid: data format id
    @return: Boolean
    """
    return _ida_bytes.unregister_custom_data_format(*args)

#<pycode(py_bytes_custdata)>
DTP_NODUP = 0x0001
# -----------------------------------------------------------------------
def __walk_types_and_formats(formats, type_action, format_action, installing):
    broken = False
    for f in formats:
        if len(f) == 1:
            if not format_action(f[0], 0):
                broken = True
                break
        else:
            dt  = f[0]
            dfs = f[1:]
# install data type before installing formats
            if installing and not type_action(dt):
                broken = True
                break
# process formats using the correct dt.id
            for df in dfs:
                if not format_action(df, dt.id):
                    broken = True
                    break
# uninstall data type after uninstalling formats
            if not installing and not type_action(dt):
                broken = True
                break
    return not broken

# -----------------------------------------------------------------------
def register_data_types_and_formats(formats):
    r"""
    Registers multiple data types and formats at once.
    To register one type/format at a time use register_custom_data_type/register_custom_data_format

    It employs a special table of types and formats described below:

    The 'formats' is a list of tuples. If a tuple has one element then it is the format to be registered with dtid=0
    If the tuple has more than one element, then tuple[0] is the data type and tuple[1:] are the data formats. For example:
    many_formats = [
      (pascal_data_type(), pascal_data_format()),
      (simplevm_data_type(), simplevm_data_format()),
      (makedword_data_format(),),
      (simplevm_data_format(),)
    ]
    The first two tuples describe data types and their associated formats.
    The last two tuples describe two data formats to be used with built-in data types.
    The data format may be attached to several data types. The id of the
    data format is stored in the first data_format_t object. For example:
    assert many_formats[1][1] != -1
    assert many_formats[2][0] != -1
    assert many_formats[3][0] == -1
    """
    def __reg_format(df, dtid):
        dfid = register_custom_data_format(df);
        if dfid == -1:
            dfid = find_custom_data_format(df.name);
            if dfid == -1:
              return False
        attach_custom_data_format(dtid, dfid)
        if dtid == 0:
            print("Registered format '%s' with built-in types, ID=%d" % (df.name, dfid))
        else:
            print("   Registered format '%s', ID=%d (dtid=%d)" % (df.name, dfid, dtid))
        return True

    def __reg_type(dt):
        register_custom_data_type(dt)
        print("Registered type '%s', ID=%d" % (dt.name, dt.id))
        return dt.id != -1
    ok = __walk_types_and_formats(formats, __reg_type, __reg_format, True)
    return 1 if ok else -1

# -----------------------------------------------------------------------
def unregister_data_types_and_formats(formats):
    r"""
    As opposed to register_data_types_and_formats(), this function
    unregisters multiple data types and formats at once.
    """
    def __unreg_format(df, dtid):
        print("%snregistering format '%s'" % ("U" if dtid == 0 else "   u", df.name))
        unregister_custom_data_format(df.id)
        return True

    def __unreg_type(dt):
        print("Unregistering type '%s', ID=%d" % (dt.name, dt.id))
        unregister_custom_data_type(dt.id)
        return True
    ok = __walk_types_and_formats(formats, __unreg_type, __unreg_format, False)
    return 1 if ok else -1

#--------------------------------------------------------------------------
#
#
#<pydoc>
#class data_type_t(object):
#    """
#    The following optional callback methods can be implemented
#    in a data_type_t subclass
#    """
#
#    def may_create_at(self, ea, nbytes):
#        """May create data?
#        No such callback means: always succeed (i.e., no restriction where
#        such a data type can be created.)
#        @param ea: candidate address for the data item
#        @param nbytes: candidate size for the data item
#        @return: True/False
#        """
#        return True
#
#    def calc_item_size(self, ea, maxsize):
#        """This callback is used to determine size of the (possible)
#        item at `ea`.
#        No such callback means that datatype is of fixed size `value_size`.
#        (thus, this callback is required only for varsize datatypes.)
#        @param ea: address of the item
#        @param maxsize: maximum size of the item
#        @return: 0 - no such item can be created/displayed
#        """
#        return 0
#
#
#class data_format_t(object):
#    """
#    The following callback methods can be implemented
#    in a data_format_t subclass
#    """
#
#    def printf(self, value, current_ea, operand_num, dtid):
#        """Convert `value` to colored string using custom format.
#        @param value: value to print (of type 'str', sequence of bytes)
#        @param current_ea: current address (BADADDR if unknown)
#        @param operand_num: current operand number
#        @param dtid: custom data type id
#        @return: string representing data
#        """
#        return None
#
#    def scan(self, input, current_ea, operand_num):
#        """Convert uncolored string (user input) to the value.
#        This callback is called from the debugger when an user enters a
#        new value for a register with a custom data representation (e.g.,
#        an MMX register.)
#        @param input: input string
#        @param current_ea: current address (BADADDR if unknown)
#        @param operand_num: current operand number (-1 if unknown)
#        @return: tuple(bool, string)
#                 (True, output value) or
#                 (False, error message)
#        """
#        return (False, "Not implemented")
#
#    def analyze(self, current_ea, operand_num):
#        """Analyze custom data format occurrence.
#        This callback is called in 2 cases:
#        - after emulating an instruction (after a call of
#          'ev_emu_insn') if its operand is marked as "custom data
#          representation"
#        - when emulating data (this is done using a call of
#          'ev_out_data' with analyze_only == true). This is the right
#          place to create cross references from the current item.
#        @param current_ea: current address (BADADDR if unknown)
#        @param operand_num: current operand number
#        """
#        pass
#
#
#</pydoc>
#</pycode(py_bytes_custdata)>




