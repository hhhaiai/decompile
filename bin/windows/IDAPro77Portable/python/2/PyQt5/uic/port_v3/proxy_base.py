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


from ..Compiler.proxy_metaclass import ProxyMetaclass


class ProxyBase(metaclass=ProxyMetaclass):
    """ A base class for proxies using Python v3 syntax for setting the
    meta-class.
    """
