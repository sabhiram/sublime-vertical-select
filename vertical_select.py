#!/usr/bin/env python

import sublime
import sublime_plugin

import sys, os, re

"""
Helper functions
"""
def insertTextToView(view, text):
    view.run_command("append", {"characters": text})

def updateYmlLintStatus(view, status):
    view.erase_status("yml-lint-status")
    view.set_status("yml-lint-status", status)

def padLineToSize(view, edit, point, size, pad_char=" "):
    """
    Given a view, a point, and a size - ensure that the line
    has space for `size` number of chars, if not pad it out
    using the `pad_char`
    """
    current_line_region = view.line(point)
    current_line_string = view.substr(current_line_region)
    size_to_pad         = size - len(current_line_string)
    if size_to_pad > 0:
        new_line_string = current_line_string + pad_char * size_to_pad
        view.replace(edit, current_line_region, new_line_string)


"""
Sublime commands that this plugin implements
"""
class VerticalSelectUpCommand(sublime_plugin.TextCommand):
    """
    Command to run the travis linter against the currently
    selected "active" view. It will only allow the lint to
    occur if the file name matches our whitelist
    """

    def run(self, edit):
        """
        """
        current_window = self.view.window()
        selected_regions = self.view.sel()

        # For now this assumes that the only valid selections are points
        # and not regions

        new_selections = []
        for region in selected_regions:
            row, col = self.view.rowcol(region.a)
            if row > 0:
                n_row, n_col = row-1, col
                new_point = self.view.text_point(n_row, n_col)

                # Hack: We need to validate that the previous line had *at-least*
                # `n_col` number of chars from the start. So we just take the
                # rowcol of the text_point we just calculated and see if the column
                # had enough space
                row, col = self.view.rowcol(new_point)

                if row == n_row + 1:
                    # Now we need to figure out the size of the last line... so we need a point
                    # from it. One minus the text point of the first char of this row should
                    # in theory point at the last char in the previous row :)
                    point_in_prev_line = self.view.text_point(row, 0) - 1
                    padLineToSize(self.view, edit, point_in_prev_line, n_col)
                    new_point = self.view.text_point(n_row, n_col)

                selection_above_line = sublime.Region(new_point, new_point)
                new_selections.append(selection_above_line)

        for region in new_selections:
            selected_regions.add(region)


class VerticalSelectDownCommand(sublime_plugin.TextCommand):
    """
    Command to run the travis linter against the currently
    selected "active" view. It will only allow the lint to
    occur if the file name matches our whitelist
    """

    def run(self, edit):
        """
        Called when the lint_travis_yml text command is triggered. This
        command is responsible for grabbing the yml out of the active view,
        and then submitting it to the travis-ci weblint on a separate thread
        """
        current_window = self.view.window()
        selected_regions = self.view.sel()

        # For now this assumes that the only valid selections are points
        # and not regions
        max_row, last_col = self.view.rowcol(self.view.size())
        new_selections = []
        for region in selected_regions:
            row, col = self.view.rowcol(region.a)
            if row < max_row:

                n_row, n_col = row + 1, col
                new_point = self.view.text_point(n_row, n_col)
                row, col = self.view.rowcol(new_point)

                if row == n_row - 1:
                    point_in_next_line = self.view.text_point(n_row, 0)
                    padLineToSize(self.view, edit, point_in_next_line, n_col)
                    new_point = self.view.text_point(n_row, n_col)

                selection_below_line = sublime.Region(new_point, new_point)
                new_selections.append(selection_below_line)

        for region in new_selections:
            selected_regions.add(region)
