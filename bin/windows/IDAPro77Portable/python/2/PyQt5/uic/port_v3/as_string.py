#############################################################################
##
## Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
## 
## This file is part of PyQt5.
## 
## This software is licensed for use under the terms of the Riverbank Commercial
## License.  See the file LICENSE for more details.  It is supplied WITHOUT ANY
## WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
## A PARTICULAR PURPOSE.
##
#############################################################################


import re


def as_string(obj):
    if isinstance(obj, str):
        return '"' + _escape(obj) + '"'

    return str(obj)


_esc_regex = re.compile(r"(\"|\'|\\)")

def _escape(text):
    # This escapes any escaped single or double quote or backslash.
    x = _esc_regex.sub(r"\\\1", text)

    # This replaces any '\n' with an escaped version and a real line break.
    return re.sub(r'\n', r'\\n"\n"', x)
