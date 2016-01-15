"""
tests for magic_gui
"""

import wx
import unittest
import os
import sys
import demag_gui
import lib.pmag as pmag

WD = os.getcwd()

#@unittest.skip('seg fault')
class TestMainFrame(unittest.TestCase):

    def setUp(self):
        self.app = wx.App()
        self.frame = demag_gui.Zeq_GUI(WD, None)
        self.pnl = self.frame.GetChildren()[0]

    def test_main_panel_is_created(self):
        """
        test for existence of main panel
        """
        self.assertTrue(self.pnl.IsEnabled())
        print self.pnl.GetName()
        #self.assertEqual("main panel", str(self.pnl.GetName()))

