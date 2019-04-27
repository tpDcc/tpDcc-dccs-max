#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains DCC functionality for 3ds Max
"""

from __future__ import print_function, division, absolute_import

import tpDccLib
from tpDccLib.abstract import dcc as abstract_dcc


from tpMaxLib.core import gui, helpers, scene, directory


class MaxDcc(abstract_dcc.AbstractDCC, object):

    @staticmethod
    def get_name():
        return tpDccLib.Dccs.Max

    @staticmethod
    def get_main_window():
        return gui.get_max_window()

    @staticmethod
    def get_version():
        return helpers.get_max_version()

    @staticmethod
    def new_scene(force=True, do_save=True):
        scene.new_scene(force=force, do_save=do_save)

    @staticmethod
    def select_file(caption, filters, start_dir=None):
        """
        Opens a select file dialog with DCC dialog
        :param caption: str, caption of the dialog
        :param filters: str, filter to use
        :param start_dir: str, start directory of the dialog
        :return: str, selected path
        """

        return directory.get_file(caption=caption, filters=filters)


tpDccLib.Dcc = MaxDcc
