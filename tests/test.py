#!/usr/bin/env python
import sys, os, time
import unittest

import sublime


"""
Detect SublimeText version to deal w/ v2 vs v3 deltas
"""
version = sublime.version()
print("Testing with SublimeText version: %s" % version)


"""
For plugin helper functions, load them so we can hit functionality
within the plugin
"""
if version < "3000":
    vertical_select = sys.modules["vertical_select"]
else:
    vertical_select = sys.modules["sublime-vertical-select.vertical_select"]


"""
Python 2 vs Python 3 - Compatibility:
  * reduce() is functools.reduce
"""
try:
    # Python 2
    _reduce = reduce
except NameError:
    # Python 3
    import functools
    _reduce = functools.reduce


class TestVerticalDiffHelpers(unittest.TestCase):
    """
    Unit tests to validate plugin helpers
    """
    test_lines_0 = "line 0\nline 1\nline 2"
    test_lines_1 = "line A\nline 1"


    """
    Setup / Teardown
    """
    def setUp(self):
        """
        Common setUp() for TestSelectionDiffPlugin
        """
        self.test_view = sublime.active_window().new_file()
        self.test_view.set_name("Test View")
        self.test_view.set_scratch(True)

        # self.settings = sublime.load_settings("clipboard_diff.sublime-settings")


    def tearDown(self):
        """
        Common tearDown() for TestSelectionDiffPlugin
        """
        test_window = self.test_view.window()
        test_window.focus_view(self.test_view)
        test_window.run_command("close_file")


    """
    Helper Function Tests:
    """
    def test_pad_line_above(self):
        """
        Validate the selectionToString helper
        """
        test_str     = "\n0123456789"
        expected_str = " " * 9 + test_str

        self.test_view.run_command("insert", {"characters": test_str})
        self.assertEqual(len(test_str), self.test_view.size())

        view_selection = self.test_view.sel()
        view_selection.clear()
        view_selection.add(sublime.Region(10, 10))

        self.test_view.run_command("vertical_select_up")

        full_text = self.test_view.substr(sublime.Region(0, self.test_view.size()))
        self.assertEqual(expected_str, full_text)

    def test_pad_line_above_multiple(self):
        """
        Validate the selectionToString helper
        """
        test_str     = "0123456789\n\n\n0123456789\n"
        expected_str = "".join([
            "0123456789\n",
            "        \n",
            "        \n",
            "0123456789\n" ])

        self.test_view.run_command("insert", {"characters": test_str})
        self.assertEqual(len(test_str), self.test_view.size())

        view_selection = self.test_view.sel()
        view_selection.clear()
        view_selection.add(sublime.Region(21, 21))


        self.test_view.run_command("vertical_select_up")
        self.test_view.run_command("vertical_select_up")
        self.test_view.run_command("vertical_select_up")

        full_text = self.test_view.substr(sublime.Region(0, self.test_view.size()))
        self.assertEqual(expected_str, full_text)

    def test_pad_line_below(self):
        """
        Validate the selectionToString helper
        """
        test_str     = "0123456789\n"
        expected_str = test_str + " " * 9

        self.test_view.run_command("insert", {"characters": test_str})
        self.assertEqual(len(test_str), self.test_view.size())

        view_selection = self.test_view.sel()
        view_selection.clear()
        view_selection.add(sublime.Region(9, 9))

        self.test_view.run_command("vertical_select_down")

        full_text = self.test_view.substr(sublime.Region(0, self.test_view.size()))
        self.assertEqual(expected_str, full_text)

    def test_pad_line_below_multiple(self):
        """
        Validate the selectionToString helper
        """
        test_str     = "0123456789\n\n\n0123456789\n"
        expected_str = "".join([
            "0123456789\n",
            "        \n",
            "        \n",
            "0123456789\n",
            "        " ])

        self.test_view.run_command("insert", {"characters": test_str})
        self.assertEqual(len(test_str), self.test_view.size())

        view_selection = self.test_view.sel()
        view_selection.clear()
        view_selection.add(sublime.Region(8, 8))

        self.test_view.run_command("vertical_select_down")
        self.test_view.run_command("vertical_select_down")
        self.test_view.run_command("vertical_select_down")
        self.test_view.run_command("vertical_select_down")

        full_text = self.test_view.substr(sublime.Region(0, self.test_view.size()))
        self.assertEqual(expected_str, full_text)

