import sublime
import sublime_plugin


class GroupControlFocusGroup(sublime_plugin.WindowCommand):
    def run(self, direction):
        window = self.window
        direction = -1 if direction == 'next' else 1
        current_group = window.active_group()
        group_to_show = (current_group + direction) % 2

        if window.num_groups() == 1:
            return None

        if window.num_groups() == 2:
            cols = [0.0, 0.3, 1.0] if group_to_show == 1 else [0.0, 0.7, 1.0]
            cells = [[0, 0, 1, 1], [1, 0, 2, 1]]
        elif window.num_groups() == 3:
            cols_sizes = [[0.0, 0.7, 0.85, 1.0],
                          [0.0, 0.15, 0.85, 1.0],
                          [0.0, 0.15, 0.3, 1.0]]
            # cols = cols_sizes[group_to_show]
            cols = [0.0, 0.7, 0.85, 1.0]
            cells = [[0, 0, 1, 1], [0, 1, 1, 2], [0, 2, 1, 3]]
            print cols, cols_sizes

        window.run_command(
            "set_layout", {
                "cols": cols,
                "rows": [0.0, 1.0],
                "cells": cells
            }
        )

        window.focus_group(group_to_show)


class GroupControlFocusTab(sublime_plugin.WindowCommand):
    """Cycles through tabs in a group"""
    def run(self, direction):
        window = self.window
        direction = -1 if direction == 'next' else 1
        current_view = window.get_view_index(window.active_view())[1]
        views_in_group = window.views_in_group(window.active_group())
        view_to_show = (current_view + direction) % len(views_in_group)

        window.focus_view(window.views_in_group(window.active_group())[view_to_show])
