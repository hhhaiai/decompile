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


# A translation table for converting ASCII lower case to upper case.
_ascii_trans_table = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz',
        b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')


# Convert a string to ASCII upper case irrespective of the current locale.
def ascii_upper(s):
    return s.translate(_ascii_trans_table)
