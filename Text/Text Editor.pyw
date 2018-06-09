#!/usr/bin/env python3
"""
Title:
Text Editor

Description:
Develop a Notepad style application that can
open, edit, and save text documents.
For added complexity,
add syntax highlighting, find and replace, text formatting etc.
"""
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    """Main tkinter window."""

    def __init__(self):
        """Initialize the window."""
        super().__init__()
        self.title("Text Editor")
        self.resizable(width=False, height=False)
        self.geometry()

        # create widgets
        self.tab_notebook = ttk.Notebook(self)
        self.text_editor_scroll_x = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.text_editor_scroll_y = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.text_editor = tk.Text(self, wrap=tk.NONE,
                                   xscrollcommand=self.text_editor_scroll_x.set,
                                   yscrollcommand=self.text_editor_scroll_y.set)
        self.main_menu = tk.Menu(self,
                                 tearoff=0)
        self.file_sub_menu = tk.Menu(self.main_menu,
                                     tearoff=0)

        # configure widgets
        self.text_editor_scroll_x.config(command=self.text_editor.xview)
        self.text_editor_scroll_y.config(command=self.text_editor.yview)

        self.config(menu=self.main_menu)
        self.main_menu.add_cascade(menu=self.file_sub_menu,
                                   label="File")

        self.file_sub_menu.add_command(label="Open file",
                                       command=self.open_file)
        self.file_sub_menu.add_separator()
        self.file_sub_menu.add_command(label="Save file",
                                       accelerator="Ctrl+S",
                                       command=self.save_file)
        self.file_sub_menu.add_command(label="Save file as...",
                                       command=self.save_file_as)
        self.file_sub_menu.add_separator()
        self.file_sub_menu.add_command(label="Exit",
                                       command=self.destroy)

        # create bindings
        self.text_editor.bind("<Tab>", lambda _: tab_pressed(self.text_editor))

        # display widgets
        self.text_editor.grid(row=0, column=0)
        self.text_editor_scroll_y.grid(row=0, column=1, sticky=tk.NS)
        self.text_editor_scroll_x.grid(row=1, column=0, sticky=tk.EW)

    def open_file(self):
        """Open a file."""

    def save_file(self):
        """Save current file."""

    def save_file_as(self):
        """Save current file as filename specified by the user."""


def tab_pressed(text_widget):
    """Insert spaces instead of tabs."""
    text_widget.insert(tk.INSERT, " " * 4)
    return "break"


def _start_gui():
    """Start the graphical user interface."""
    root = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    _start_gui()
