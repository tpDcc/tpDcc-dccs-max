#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpMaxLib
"""

from __future__ import print_function, division, absolute_import

import os
import inspect

# Do not remove 3ds Max imports
import MaxPlus

from tpPyUtils import importer

# =================================================================================

logger = None

# =================================================================================


class tpMaxLib(importer.Importer, object):
    def __init__(self):
        super(tpMaxLib, self).__init__(module_name='tpMaxLib')

    def get_module_path(self):
        """
        Returns path where tpMaxLib module is stored
        :return: str
        """

        try:
            mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
        except Exception:
            try:
                mod_dir = os.path.dirname(__file__)
            except Exception:
                try:
                    import tpDccLib
                    mod_dir = tpDccLib.__path__[0]
                except Exception:
                    return None

        return mod_dir


def init(do_reload=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    """

    tpmaxlib_importer = importer.init_importer(importer_class=tpMaxLib, do_reload=do_reload)

    global logger
    logger = tpmaxlib_importer.logger

    tpmaxlib_importer.import_modules()
    tpmaxlib_importer.import_packages(only_packages=True)
