# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This software is licensed for use under the terms of the Riverbank Commercial
# License.  See the file LICENSE for more details.  It is supplied WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.


# Support PyQt5 sub-packages that have been created by setuptools.
__path__ = __import__('pkgutil').extend_path(__path__, __name__)


def find_qt():
    import os, sys

    qtcore_dll = '\\Qt5Core.dll'

    dll_dir = os.path.dirname(sys.executable)
    if not os.path.isfile(dll_dir + qtcore_dll):
        path = os.environ['PATH']

        dll_dir = os.path.dirname(__file__) + '\\Qt5\\bin'
        if os.path.isfile(dll_dir + qtcore_dll):
            path = dll_dir + ';' + path
            os.environ['PATH'] = path
        else:
            for dll_dir in path.split(';'):
                if os.path.isfile(dll_dir + qtcore_dll):
                    break
            else:
                return

    try:
        os.add_dll_directory(dll_dir)
    except AttributeError:
        pass


find_qt()
del find_qt
