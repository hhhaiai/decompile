"""
Definitions of IDP, LDR, PLUGIN module interfaces.

This file also contains:
* functions to load files into the database
* functions to generate output files
* high level functions to work with the database (open, save, close)

The LDR interface consists of one structure: loader_t
The IDP interface consists of one structure: processor_t
The PLUGIN interface consists of one structure: plugin_t

Modules can't use standard FILE* functions. They must use functions from
<fpro.h>

Modules can't use standard memory allocation functions. They must use functions
from <pro.h>

The exported entry #1 in the module should point to the the appropriate
structure. (loader_t for LDR module, for example)"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _ida_loader
else:
    import _ida_loader

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

SWIG_PYTHON_LEGACY_BOOL = _ida_loader.SWIG_PYTHON_LEGACY_BOOL

import ida_idaapi

class qvector_snapshotvec_t(object):
    r"""
    Proxy of C++ qvector< snapshot_t * > class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> qvector_snapshotvec_t
        __init__(self, x) -> qvector_snapshotvec_t

        @param x: qvector< snapshot_t * > const &
        """
        _ida_loader.qvector_snapshotvec_t_swiginit(self, _ida_loader.new_qvector_snapshotvec_t(*args))
    __swig_destroy__ = _ida_loader.delete_qvector_snapshotvec_t

    def push_back(self, *args) -> "snapshot_t *&":
        r"""
        push_back(self, x)

        @param x: snapshot_t *const &

        push_back(self) -> snapshot_t *&
        """
        return _ida_loader.qvector_snapshotvec_t_push_back(self, *args)

    def pop_back(self, *args) -> "void":
        r"""
        pop_back(self)
        """
        return _ida_loader.qvector_snapshotvec_t_pop_back(self, *args)

    def size(self, *args) -> "size_t":
        r"""
        size(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t_size(self, *args)

    def empty(self, *args) -> "bool":
        r"""
        empty(self) -> bool
        """
        return _ida_loader.qvector_snapshotvec_t_empty(self, *args)

    def at(self, *args) -> "snapshot_t *const &":
        r"""
        at(self, _idx) -> snapshot_t

        @param _idx: size_t
        """
        return _ida_loader.qvector_snapshotvec_t_at(self, *args)

    def qclear(self, *args) -> "void":
        r"""
        qclear(self)
        """
        return _ida_loader.qvector_snapshotvec_t_qclear(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_loader.qvector_snapshotvec_t_clear(self, *args)

    def resize(self, *args) -> "void":
        r"""
        resize(self, _newsize, x)

        @param _newsize: size_t
        @param x: snapshot_t *const &

        resize(self, _newsize)

        @param _newsize: size_t
        """
        return _ida_loader.qvector_snapshotvec_t_resize(self, *args)

    def capacity(self, *args) -> "size_t":
        r"""
        capacity(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t_capacity(self, *args)

    def reserve(self, *args) -> "void":
        r"""
        reserve(self, cnt)

        @param cnt: size_t
        """
        return _ida_loader.qvector_snapshotvec_t_reserve(self, *args)

    def truncate(self, *args) -> "void":
        r"""
        truncate(self)
        """
        return _ida_loader.qvector_snapshotvec_t_truncate(self, *args)

    def swap(self, *args) -> "void":
        r"""
        swap(self, r)

        @param r: qvector< snapshot_t * > &
        """
        return _ida_loader.qvector_snapshotvec_t_swap(self, *args)

    def extract(self, *args) -> "snapshot_t **":
        r"""
        extract(self) -> snapshot_t **
        """
        return _ida_loader.qvector_snapshotvec_t_extract(self, *args)

    def inject(self, *args) -> "void":
        r"""
        inject(self, s, len)

        @param s: snapshot_t **
        @param len: size_t
        """
        return _ida_loader.qvector_snapshotvec_t_inject(self, *args)

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: qvector< snapshot_t * > const &
        """
        return _ida_loader.qvector_snapshotvec_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: qvector< snapshot_t * > const &
        """
        return _ida_loader.qvector_snapshotvec_t___ne__(self, *args)

    def begin(self, *args) -> "qvector< snapshot_t * >::const_iterator":
        r"""
        begin(self) -> qvector< snapshot_t * >::iterator
        begin(self) -> qvector< snapshot_t * >::const_iterator
        """
        return _ida_loader.qvector_snapshotvec_t_begin(self, *args)

    def end(self, *args) -> "qvector< snapshot_t * >::const_iterator":
        r"""
        end(self) -> qvector< snapshot_t * >::iterator
        end(self) -> qvector< snapshot_t * >::const_iterator
        """
        return _ida_loader.qvector_snapshotvec_t_end(self, *args)

    def insert(self, *args) -> "qvector< snapshot_t * >::iterator":
        r"""
        insert(self, it, x) -> qvector< snapshot_t * >::iterator

        @param it: qvector< snapshot_t * >::iterator
        @param x: snapshot_t *const &
        """
        return _ida_loader.qvector_snapshotvec_t_insert(self, *args)

    def erase(self, *args) -> "qvector< snapshot_t * >::iterator":
        r"""
        erase(self, it) -> qvector< snapshot_t * >::iterator

        @param it: qvector< snapshot_t * >::iterator

        erase(self, first, last) -> qvector< snapshot_t * >::iterator

        @param first: qvector< snapshot_t * >::iterator
        @param last: qvector< snapshot_t * >::iterator
        """
        return _ida_loader.qvector_snapshotvec_t_erase(self, *args)

    def find(self, *args) -> "qvector< snapshot_t * >::const_iterator":
        r"""
        find(self, x) -> qvector< snapshot_t * >::iterator

        @param x: snapshot_t *const &

        find(self, x) -> qvector< snapshot_t * >::const_iterator

        @param x: snapshot_t *const &
        """
        return _ida_loader.qvector_snapshotvec_t_find(self, *args)

    def has(self, *args) -> "bool":
        r"""
        has(self, x) -> bool

        @param x: snapshot_t *const &
        """
        return _ida_loader.qvector_snapshotvec_t_has(self, *args)

    def add_unique(self, *args) -> "bool":
        r"""
        add_unique(self, x) -> bool

        @param x: snapshot_t *const &
        """
        return _ida_loader.qvector_snapshotvec_t_add_unique(self, *args)

    def _del(self, *args) -> "bool":
        r"""
        _del(self, x) -> bool

        Parameters
        ----------
        x: snapshot_t *const &

        """
        return _ida_loader.qvector_snapshotvec_t__del(self, *args)

    def __len__(self, *args) -> "size_t":
        r"""
        __len__(self) -> size_t
        """
        return _ida_loader.qvector_snapshotvec_t___len__(self, *args)

    def __getitem__(self, *args) -> "snapshot_t *const &":
        r"""
        __getitem__(self, i) -> snapshot_t

        @param i: size_t
        """
        return _ida_loader.qvector_snapshotvec_t___getitem__(self, *args)

    def __setitem__(self, *args) -> "void":
        r"""
        __setitem__(self, i, v)

        @param i: size_t
        @param v: snapshot_t *const &
        """
        return _ida_loader.qvector_snapshotvec_t___setitem__(self, *args)

    front = ida_idaapi._qvector_front
    back = ida_idaapi._qvector_back
    __iter__ = ida_idaapi._bounded_getitem_iterator


# Register qvector_snapshotvec_t in _ida_loader:
_ida_loader.qvector_snapshotvec_t_swigregister(qvector_snapshotvec_t)

class loader_t(object):
    r"""
    Proxy of C++ loader_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    version = property(_ida_loader.loader_t_version_get, _ida_loader.loader_t_version_set, doc=r"""version""")
    r"""
    api version, should be IDP_INTERFACE_VERSION
    """
    flags = property(_ida_loader.loader_t_flags_get, _ida_loader.loader_t_flags_set, doc=r"""flags""")
    r"""
    Loader flags
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> loader_t
        """
        _ida_loader.loader_t_swiginit(self, _ida_loader.new_loader_t(*args))
    __swig_destroy__ = _ida_loader.delete_loader_t

# Register loader_t in _ida_loader:
_ida_loader.loader_t_swigregister(loader_t)
LDRF_RELOAD = _ida_loader.LDRF_RELOAD
r"""
loader recognizes NEF_RELOAD flag
"""

LDRF_REQ_PROC = _ida_loader.LDRF_REQ_PROC
r"""
Requires a processor to be set. if this bit is not set, load_file() must call
set_processor_type(..., SETPROC_LOADER)
"""

ACCEPT_ARCHIVE = _ida_loader.ACCEPT_ARCHIVE
r"""
Specify that a file format is served by archive loader See loader_t::accept_file
"""

ACCEPT_CONTINUE = _ida_loader.ACCEPT_CONTINUE
r"""
Specify that the function must be called another time See loader_t::accept_file
"""

ACCEPT_FIRST = _ida_loader.ACCEPT_FIRST
r"""
Specify that a file format should be place first in "load file" dialog box. See
loader_t::accept_file
"""

NEF_SEGS = _ida_loader.NEF_SEGS
r"""
Create segments.
"""

NEF_RSCS = _ida_loader.NEF_RSCS
r"""
Load resources.
"""

NEF_NAME = _ida_loader.NEF_NAME
r"""
Rename entries.
"""

NEF_MAN = _ida_loader.NEF_MAN
r"""
Manual load.
"""

NEF_FILL = _ida_loader.NEF_FILL
r"""
Fill segment gaps.
"""

NEF_IMPS = _ida_loader.NEF_IMPS
r"""
Create import segment.
"""

NEF_FIRST = _ida_loader.NEF_FIRST
r"""
This is the first file loaded into the database.
"""

NEF_CODE = _ida_loader.NEF_CODE
r"""
for load_binary_file(): load as a code segment
"""

NEF_RELOAD = _ida_loader.NEF_RELOAD
r"""
reload the file at the same place:
* don't create segments
* don't create fixup info
* don't import segments
* etc.

Load only the bytes into the base. A loader should have the LDRF_RELOAD bit set.
"""

NEF_FLAT = _ida_loader.NEF_FLAT
r"""
Autocreate FLAT group (PE)
"""

NEF_MINI = _ida_loader.NEF_MINI
r"""
Create mini database (do not copy segment bytes from the input file; use only
the file header metadata)
"""

NEF_LOPT = _ida_loader.NEF_LOPT
r"""
Display additional loader options dialog.
"""

NEF_LALL = _ida_loader.NEF_LALL
r"""
Load all segments without questions.
"""


DLLEXT = _ida_loader.DLLEXT

LOADER_DLL = _ida_loader.LOADER_DLL


def load_binary_file(*args) -> "bool":
    r"""
    load_binary_file(filename, li, _neflags, fileoff, basepara, binoff, nbytes) -> bool
    Load a binary file into the database. This function usually is called from ui.

    @param filename: (C++: const char *) the name of input file as is (if the input file is from
                     library, then this is the name from the library)
    @param li: (C++: linput_t *) loader input source
    @param _neflags: (C++: ushort) Load file flags. For the first file, the flag NEF_FIRST must be
                     set.
    @param fileoff: (C++: qoff64_t) Offset in the input file
    @param basepara: (C++: ea_t) Load address in paragraphs
    @param binoff: (C++: ea_t) Load offset (load_address=(basepara<<4)+binoff)
    @param nbytes: (C++: uint64) Number of bytes to load from the file.
    * 0: up to the end of the file
    @retval true: ok
    @retval false: failed (couldn't open the file)
    """
    return _ida_loader.load_binary_file(*args)

def process_archive(*args) -> "qstring *":
    r"""
    process_archive(temp_file, li, module_name, neflags, defmember, loader) -> str
    Calls loader_t::process_archive() For parameters and return value description
    look at loader_t::process_archive(). Additional parameter:

    @param loader: (C++: const load_info_t *) pointer to load_info_t structure.
    @param li: (C++: linput_t *)
    @param module_name: (C++: qstring *)
    @param neflags: (C++: ushort *)
    @param defmember: (C++: const char *) char const *
    @param loader: (C++: const load_info_t *) pointer to load_info_t structure.
    """
    return _ida_loader.process_archive(*args)
OFILE_MAP = _ida_loader.OFILE_MAP
r"""
MAP file.
"""

OFILE_EXE = _ida_loader.OFILE_EXE
r"""
Executable file.
"""

OFILE_IDC = _ida_loader.OFILE_IDC
r"""
IDC file.
"""

OFILE_LST = _ida_loader.OFILE_LST
r"""
Disassembly listing.
"""

OFILE_ASM = _ida_loader.OFILE_ASM
r"""
Assembly.
"""

OFILE_DIF = _ida_loader.OFILE_DIF
r"""
Difference.
"""


def gen_file(*args) -> "int":
    r"""
    gen_file(otype, fp, ea1, ea2, flags) -> int
    Generate an output file.

    @param otype: (C++: ofile_type_t) type of output file.
    @param fp: (C++: FILE *) the output file handle
    @param ea1: (C++: ea_t) start address. For some file types this argument is ignored
    @param ea2: (C++: ea_t) end address. For some file types this argument is ignored as usual
                in ida, the end address of the range is not included
    @param flags: (C++: int) Generate file flagsOFILE_EXE:
    @retval 0: can't generate exe file
    @retval 1: ok
    @return: number of the generated lines. -1 if an error occurred
    """
    return _ida_loader.gen_file(*args)
GENFLG_MAPSEG = _ida_loader.GENFLG_MAPSEG

GENFLG_MAPNAME = _ida_loader.GENFLG_MAPNAME

GENFLG_MAPDMNG = _ida_loader.GENFLG_MAPDMNG

GENFLG_MAPLOC = _ida_loader.GENFLG_MAPLOC

GENFLG_IDCTYPE = _ida_loader.GENFLG_IDCTYPE

GENFLG_ASMTYPE = _ida_loader.GENFLG_ASMTYPE
r"""
OFILE_ASM,OFILE_LST: gen information about types too
"""

GENFLG_GENHTML = _ida_loader.GENFLG_GENHTML
r"""
OFILE_ASM,OFILE_LST: generate html (ui_genfile_callback will be used)
"""

GENFLG_ASMINC = _ida_loader.GENFLG_ASMINC
r"""
OFILE_ASM,OFILE_LST: gen information only about types
"""


def file2base(*args) -> "int":
    r"""
    file2base(li, pos, ea1, ea2, patchable) -> int
    Load portion of file into the database. This function will include (ea1..ea2)
    into the addressing space of the program (make it enabled).

    @param li: (C++: linput_t *) pointer of input source
    @param pos: (C++: qoff64_t) position in the file
    @param ea1: (C++: ea_t) ,ea2: range of destination linear addresses
    @param patchable: (C++: int) should the kernel remember correspondence of file offsets to
                      linear addresses.
    @retval 1: ok
    @retval 0: read error, a warning is displayed
    @note: The storage type of the specified range will be changed to STT_VA.
    @param patchable: (C++: int) should the kernel remember correspondence of file offsets to
                      linear addresses.
    @retval 1: ok
    @retval 0: read error, a warning is displayed
    @note: The storage type of the specified range will be changed to STT_VA.
    """
    return _ida_loader.file2base(*args)
FILEREG_PATCHABLE = _ida_loader.FILEREG_PATCHABLE
r"""
means that the input file may be patched (i.e. no compression, no iterated data,
etc)
"""

FILEREG_NOTPATCHABLE = _ida_loader.FILEREG_NOTPATCHABLE
r"""
the data is kept in some encoded form in the file.
"""


def base2file(*args) -> "int":
    r"""
    base2file(fp, pos, ea1, ea2) -> int
    Unload database to a binary file. This function works for wide byte processors
    too.

    @param fp: (C++: FILE *) pointer to file
    @param pos: (C++: qoff64_t) position in the file
    @param ea1: (C++: ea_t) ,ea2: range of source linear addresses
    @param ea2: (C++: ea_t)
    @return: 1-ok(always), write error leads to immediate exit
    """
    return _ida_loader.base2file(*args)

def get_basic_file_type(*args) -> "filetype_t":
    r"""
    get_basic_file_type(li) -> filetype_t
    Get the input file type. This function can recognize libraries and zip files.

    @param li: (C++: linput_t *)
    """
    return _ida_loader.get_basic_file_type(*args)

def get_file_type_name(*args) -> "size_t":
    r"""
    get_file_type_name() -> str
    Get name of the current file type. The current file type is kept in
    idainfo::filetype.

    @return: size of answer, this function always succeeds
    """
    return _ida_loader.get_file_type_name(*args)

def set_import_ordinal(*args) -> "void":
    r"""
    set_import_ordinal(modnode, ea, ord)
    Set information about the ordinal import entry. This function performs
    'modnode.altset(ord, ea2node(ea));'

    @param modnode: (C++: uval_t) node with information about imported entries
    @param ea: (C++: ea_t) linear address of the entry
    @param ord: (C++: uval_t) ordinal number of the entry
    """
    return _ida_loader.set_import_ordinal(*args)

def set_import_name(*args) -> "void":
    r"""
    set_import_name(modnode, ea, name)
    Set information about the named import entry. This function performs
    'modnode.supset_ea(ea, name);'

    @param modnode: (C++: uval_t) node with information about imported entries
    @param ea: (C++: ea_t) linear address of the entry
    @param name: (C++: const char *) name of the entry
    """
    return _ida_loader.set_import_name(*args)

def load_ids_module(*args) -> "int":
    r"""
    load_ids_module(fname) -> int
    Load and apply IDS file. This function loads the specified IDS file and applies
    it to the database. If the program imports functions from a module with the same
    name as the name of the ids file being loaded, then only functions from this
    module will be affected. Otherwise (i.e. when the program does not import a
    module with this name) any function in the program may be affected.

    @param fname: (C++: char *) name of file to apply
    @retval 1: ok
    @retval 0: some error (a message is displayed). if the ids file does not exist,
               no message is displayed
    """
    return _ida_loader.load_ids_module(*args)

def get_plugin_options(*args) -> "char const *":
    r"""
    get_plugin_options(plugin) -> char const *
    Get plugin options from the command line. If the user has specified the options
    in the -Oplugin_name:options format, them this function will return the
    'options' part of it The 'plugin' parameter should denote the plugin name
    Returns nullptr if there we no options specified

    @param plugin: (C++: const char *) char const *
    """
    return _ida_loader.get_plugin_options(*args)
PLUGIN_DLL = _ida_loader.PLUGIN_DLL
r"""
Pattern to find plugin files.
"""

MODULE_ENTRY_LOADER = _ida_loader.MODULE_ENTRY_LOADER

MODULE_ENTRY_PLUGIN = _ida_loader.MODULE_ENTRY_PLUGIN

MODULE_ENTRY_IDP = _ida_loader.MODULE_ENTRY_IDP

class idp_name_t(object):
    r"""
    Proxy of C++ idp_name_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    lname = property(_ida_loader.idp_name_t_lname_get, _ida_loader.idp_name_t_lname_set, doc=r"""lname""")
    r"""
    long processor name
    """
    sname = property(_ida_loader.idp_name_t_sname_get, _ida_loader.idp_name_t_sname_set, doc=r"""sname""")
    r"""
    short processor name
    """
    hidden = property(_ida_loader.idp_name_t_hidden_get, _ida_loader.idp_name_t_hidden_set, doc=r"""hidden""")
    r"""
    is hidden
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> idp_name_t
        """
        _ida_loader.idp_name_t_swiginit(self, _ida_loader.new_idp_name_t(*args))
    __swig_destroy__ = _ida_loader.delete_idp_name_t

# Register idp_name_t in _ida_loader:
_ida_loader.idp_name_t_swigregister(idp_name_t)

class idp_desc_t(object):
    r"""
    Proxy of C++ idp_desc_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    path = property(_ida_loader.idp_desc_t_path_get, _ida_loader.idp_desc_t_path_set, doc=r"""path""")
    r"""
    module file name
    """
    mtime = property(_ida_loader.idp_desc_t_mtime_get, _ida_loader.idp_desc_t_mtime_set, doc=r"""mtime""")
    r"""
    time of last modification
    """
    family = property(_ida_loader.idp_desc_t_family_get, _ida_loader.idp_desc_t_family_set, doc=r"""family""")
    r"""
    processor's family
    """
    names = property(_ida_loader.idp_desc_t_names_get, _ida_loader.idp_desc_t_names_set, doc=r"""names""")
    r"""
    processor names
    """
    is_script = property(_ida_loader.idp_desc_t_is_script_get, _ida_loader.idp_desc_t_is_script_set, doc=r"""is_script""")
    r"""
    the processor module is a script
    """
    checked = property(_ida_loader.idp_desc_t_checked_get, _ida_loader.idp_desc_t_checked_set, doc=r"""checked""")
    r"""
    internal, for cache management
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> idp_desc_t
        """
        _ida_loader.idp_desc_t_swiginit(self, _ida_loader.new_idp_desc_t(*args))
    __swig_destroy__ = _ida_loader.delete_idp_desc_t

# Register idp_desc_t in _ida_loader:
_ida_loader.idp_desc_t_swigregister(idp_desc_t)

IDP_DLL = _ida_loader.IDP_DLL

class plugin_info_t(object):
    r"""
    Proxy of C++ plugin_info_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    next = property(_ida_loader.plugin_info_t_next_get, _ida_loader.plugin_info_t_next_set, doc=r"""next""")
    r"""
    next plugin information
    """
    path = property(_ida_loader.plugin_info_t_path_get, _ida_loader.plugin_info_t_path_set, doc=r"""path""")
    r"""
    full path to the plugin
    """
    org_name = property(_ida_loader.plugin_info_t_org_name_get, _ida_loader.plugin_info_t_org_name_set, doc=r"""org_name""")
    r"""
    original short name of the plugin
    """
    name = property(_ida_loader.plugin_info_t_name_get, _ida_loader.plugin_info_t_name_set, doc=r"""name""")
    r"""
    short name of the plugin it will appear in the menu
    """
    org_hotkey = property(_ida_loader.plugin_info_t_org_hotkey_get, _ida_loader.plugin_info_t_org_hotkey_set, doc=r"""org_hotkey""")
    r"""
    original hotkey to run the plugin
    """
    hotkey = property(_ida_loader.plugin_info_t_hotkey_get, _ida_loader.plugin_info_t_hotkey_set, doc=r"""hotkey""")
    r"""
    current hotkey to run the plugin
    """
    arg = property(_ida_loader.plugin_info_t_arg_get, _ida_loader.plugin_info_t_arg_set, doc=r"""arg""")
    r"""
    argument used to call the plugin
    """
    entry = property(_ida_loader.plugin_info_t_entry_get, _ida_loader.plugin_info_t_entry_set, doc=r"""entry""")
    r"""
    pointer to the plugin if it is already loaded
    """
    dllmem = property(_ida_loader.plugin_info_t_dllmem_get, _ida_loader.plugin_info_t_dllmem_set, doc=r"""dllmem""")
    flags = property(_ida_loader.plugin_info_t_flags_get, _ida_loader.plugin_info_t_flags_set, doc=r"""flags""")
    r"""
    a copy of plugin_t::flags
    """
    comment = property(_ida_loader.plugin_info_t_comment_get, _ida_loader.plugin_info_t_comment_set, doc=r"""comment""")
    r"""
    a copy of plugin_t::comment
    """

    def __init__(self, *args):
        r"""
        __init__(self) -> plugin_info_t
        """
        _ida_loader.plugin_info_t_swiginit(self, _ida_loader.new_plugin_info_t(*args))
    __swig_destroy__ = _ida_loader.delete_plugin_info_t

# Register plugin_info_t in _ida_loader:
_ida_loader.plugin_info_t_swigregister(plugin_info_t)


def find_plugin(*args) -> "plugin_t *":
    r"""
    find_plugin(name, load_if_needed=False) -> plugin_t *
    Find a user-defined plugin and optionally load it.

    @param name: (C++: const char *) short plugin name without path and extension, or absolute path to
                 the file name
    @param load_if_needed: (C++: bool) if the plugin is not present in the memory, try to load
                           it
    @return: pointer to plugin description block
    """
    return _ida_loader.find_plugin(*args)

def get_fileregion_offset(*args) -> "qoff64_t":
    r"""
    get_fileregion_offset(ea) -> qoff64_t
    Get offset in the input file which corresponds to the given ea. If the specified
    ea can't be mapped into the input file offset, return -1.

    @param ea: (C++: ea_t)
    """
    return _ida_loader.get_fileregion_offset(*args)

def get_fileregion_ea(*args) -> "ea_t":
    r"""
    get_fileregion_ea(offset) -> ea_t
    Get linear address which corresponds to the specified input file offset. If
    can't be found, return BADADDR

    @param offset: (C++: qoff64_t)
    """
    return _ida_loader.get_fileregion_ea(*args)

def gen_exe_file(*args) -> "int":
    r"""
    gen_exe_file(fp) -> int
    Generate an exe file (unload the database in binary form).

    @param fp: (C++: FILE *)
    @return: fp the output file handle. if fp == nullptr then return:
    * 1: can generate an executable file
    * 0: can't generate an executable file
    @retval 1: ok
    @retval 0: failed
    """
    return _ida_loader.gen_exe_file(*args)

def reload_file(*args) -> "bool":
    r"""
    reload_file(file, is_remote) -> bool
    Reload the input file. This function reloads the byte values from the input
    file. It doesn't modify the segmentation, names, comments, etc.

    @param file: (C++: const char *) name of the input file. if file == nullptr then returns:
    * 1: can reload the input file
    * 0: can't reload the input file
    @param is_remote: (C++: bool) is the file located on a remote computer with the debugger
                      server?
    @return: success
    """
    return _ida_loader.reload_file(*args)
MAX_DATABASE_DESCRIPTION = _ida_loader.MAX_DATABASE_DESCRIPTION
r"""
Maximum database snapshot description length.
"""

class snapshot_t(object):
    r"""
    Proxy of C++ snapshot_t class.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    id = property(_ida_loader.snapshot_t_id_get, _ida_loader.snapshot_t_id_set, doc=r"""id""")
    r"""
    snapshot ID. This value is computed using qgettimeofday()
    """
    flags = property(_ida_loader.snapshot_t_flags_get, _ida_loader.snapshot_t_flags_set, doc=r"""flags""")
    r"""
    Snapshot flags
    """
    desc = property(_ida_loader.snapshot_t_desc_get, _ida_loader.snapshot_t_desc_set, doc=r"""desc""")
    r"""
    snapshot description
    """
    filename = property(_ida_loader.snapshot_t_filename_get, _ida_loader.snapshot_t_filename_set, doc=r"""filename""")
    r"""
    snapshot file name
    """
    children = property(_ida_loader.snapshot_t_children_get, _ida_loader.snapshot_t_children_set, doc=r"""children""")
    r"""
    snapshot children
    """

    def __eq__(self, *args) -> "bool":
        r"""
        __eq__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___eq__(self, *args)

    def __ne__(self, *args) -> "bool":
        r"""
        __ne__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___ne__(self, *args)

    def __lt__(self, *args) -> "bool":
        r"""
        __lt__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___lt__(self, *args)

    def __gt__(self, *args) -> "bool":
        r"""
        __gt__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___gt__(self, *args)

    def __le__(self, *args) -> "bool":
        r"""
        __le__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___le__(self, *args)

    def __ge__(self, *args) -> "bool":
        r"""
        __ge__(self, r) -> bool

        @param r: snapshot_t const &
        """
        return _ida_loader.snapshot_t___ge__(self, *args)

    def clear(self, *args) -> "void":
        r"""
        clear(self)
        """
        return _ida_loader.snapshot_t_clear(self, *args)

    def __init__(self, *args):
        r"""
        __init__(self) -> snapshot_t
        """
        _ida_loader.snapshot_t_swiginit(self, _ida_loader.new_snapshot_t(*args))
    __swig_destroy__ = _ida_loader.delete_snapshot_t

# Register snapshot_t in _ida_loader:
_ida_loader.snapshot_t_swigregister(snapshot_t)
SSF_AUTOMATIC = _ida_loader.SSF_AUTOMATIC
r"""
automatic snapshot
"""



def build_snapshot_tree(*args) -> "bool":
    r"""
    build_snapshot_tree(root) -> bool
    Build the snapshot tree.

    @param root: (C++: snapshot_t *) snapshot root that will contain the snapshot tree elements.
    @return: success
    """
    return _ida_loader.build_snapshot_tree(*args)
SSUF_DESC = _ida_loader.SSUF_DESC
r"""
Update the description.
"""

SSUF_PATH = _ida_loader.SSUF_PATH
r"""
Update the path.
"""

SSUF_FLAGS = _ida_loader.SSUF_FLAGS
r"""
Update the flags.
"""


def flush_buffers(*args) -> "int":
    r"""
    flush_buffers() -> int
    Flush buffers to the disk.
    """
    return _ida_loader.flush_buffers(*args)

def is_trusted_idb(*args) -> "bool":
    r"""
    is_trusted_idb() -> bool
    Is the database considered as trusted?
    """
    return _ida_loader.is_trusted_idb(*args)

def save_database(*args) -> "bool":
    r"""
    save_database(outfile, flags, root=None, attr=None) -> bool
    Save current database using a new file name.

    @param outfile: (C++: const char *) output database file name
    @param flags: (C++: uint32) Database flags
    @param root: (C++: const snapshot_t *) optional: snapshot tree root.
    @param attr: (C++: const snapshot_t *) optional: snapshot attributes
    @note: when both root and attr are not nullptr then the snapshot attributes will
           be updated, otherwise the snapshot attributes will be inherited from the
           current database.
    @return: success
    """
    return _ida_loader.save_database(*args)
DBFL_KILL = _ida_loader.DBFL_KILL
r"""
delete unpacked database
"""

DBFL_COMP = _ida_loader.DBFL_COMP
r"""
collect garbage
"""

DBFL_BAK = _ida_loader.DBFL_BAK
r"""
create backup file (if !DBFL_KILL)
"""

DBFL_TEMP = _ida_loader.DBFL_TEMP
r"""
temporary database
"""


def is_database_flag(*args) -> "bool":
    r"""
    is_database_flag(dbfl) -> bool
    Get the current database flag

    @param dbfl: (C++: uint32) flag Database flags
    @return: the state of the flag (set or cleared)
    """
    return _ida_loader.is_database_flag(*args)

def set_database_flag(*args) -> "void":
    r"""
    set_database_flag(dbfl, cnd=True)
    Set or clear database flag

    @param dbfl: (C++: uint32) flag Database flags
    @param cnd: (C++: bool) set if true or clear flag otherwise
    """
    return _ida_loader.set_database_flag(*args)

def clr_database_flag(*args) -> "void":
    r"""
    clr_database_flag(dbfl)

    @param dbfl: uint32
    """
    return _ida_loader.clr_database_flag(*args)
PATH_TYPE_CMD = _ida_loader.PATH_TYPE_CMD
r"""
full path to the file specified in the command line
"""

PATH_TYPE_IDB = _ida_loader.PATH_TYPE_IDB
r"""
full path of IDB file
"""

PATH_TYPE_ID0 = _ida_loader.PATH_TYPE_ID0
r"""
full path of ID0 file
"""


def get_path(*args) -> "char const *":
    r"""
    get_path(pt) -> char const *
    Get the file path

    @param pt: (C++: path_type_t) file path type Types of the file pathes
    @return: file path, never returns nullptr
    """
    return _ida_loader.get_path(*args)

def set_path(*args) -> "void":
    r"""
    set_path(pt, path)
    Set the file path

    @param pt: (C++: path_type_t) file path type Types of the file pathes
    @param path: (C++: const char *) new file path, use nullptr or empty string to clear the file path
    """
    return _ida_loader.set_path(*args)

def get_elf_debug_file_directory(*args) -> "char const *":
    r"""
    get_elf_debug_file_directory() -> char const *
    Get the value of the ELF_DEBUG_FILE_DIRECTORY configuration directive.
    """
    return _ida_loader.get_elf_debug_file_directory(*args)

def mem2base(*args) -> "int":
    r"""
    mem2base(py_mem, ea, fpos=-1) -> int
    Load database from the memory.

    @param py_mem: the buffer
    @param ea: start linear addresses
    @param fpos: position in the input file the data is taken from.
                 if == -1, then no file position correspond to the data.
    @return:     - Returns zero if the passed buffer was not a string
        - Otherwise 1 is returned
    """
    return _ida_loader.mem2base(*args)

def load_plugin(*args) -> "PyObject *":
    r"""
    load_plugin(name) -> PyCapsule or None
    Loads a plugin

    @param name: char const *
    @return:     - None if plugin could not be loaded
        - An opaque object representing the loaded plugin
    """
    return _ida_loader.load_plugin(*args)

def run_plugin(*args) -> "bool":
    r"""
    run_plugin(plg, arg) -> bool
    Runs a plugin

    @param plg: A plugin object (returned by load_plugin())
    @param arg: size_t
    @return: Boolean
    """
    return _ida_loader.run_plugin(*args)

def load_and_run_plugin(*args) -> "bool":
    r"""
    load_and_run_plugin(name, arg) -> bool
    Load & run a plugin.

    @param name: (C++: const char *) char const *
    @param arg: (C++: size_t)
    """
    return _ida_loader.load_and_run_plugin(*args)

def extract_module_from_archive(*args) -> "PyObject *":
    r"""
    extract_module_from_archive(fname, is_remote=False) -> (NoneType, NoneType), (str, str)
    Extract a module for an archive file. Parse an archive file, show the list of
    modules to the user, allow him to select a module, extract the selected module
    to a file (if the extract module is an archive, repeat the process). This
    function can handle ZIP, AR, AIXAR, OMFLIB files. The temporary file will be
    automatically deleted by IDA at the end.

    @param filename: (C++: char *) in: input file. out: name of the selected module.
    @param is_remote: (C++: bool) is the input file remote?
    @retval true: ok
    @retval false: something bad happened (error message has been displayed to the
                   user)
    """
    return _ida_loader.extract_module_from_archive(*args)



