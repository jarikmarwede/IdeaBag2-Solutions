#!/usr/bin/env python3
"""Tool to search a text with regular expressions.

Title:
Regex Query Tool

Description:
Create a tool that allows the user to specify a string
and then a regular expression to match against it.
It will then return all matches it finds as output.
This can be done within a form where then each match can be highlighted in the string itself.
This will help developers who want to know, on the fly,
if a string can be matched by a given regular expression.
"""
import re
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Regex Query Tool")
        self.resizable(width=False, height=False)

        self.regex_frame = ttk.Frame(self)
        self.search_text_frame = ttk.Frame(self)

        self.regex_label = ttk.Label(self.regex_frame, text="Regular Expression")
        self.regex_entry = ttk.Entry(self.regex_frame)
        self.search_text_label = ttk.Label(self.search_text_frame, text="Text to search")
        self.search_text = tk.Text(self.search_text_frame)
        self.search_button = ttk.Button(self, text="Search", command=self.search)

        self.search_text.tag_config("match", background="yellow")

        self.regex_frame.grid(row=0, padx=5, pady=5)
        self.search_text_frame.grid(row=1, padx=10, pady=5)
        self.search_button.grid(row=2, padx=5, pady=5)

        self.regex_label.grid(row=0)
        self.regex_entry.grid(row=1)
        self.search_text_label.grid(row=0)
        self.search_text.grid(row=1)

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

    def search(self):
        """Search the text using the regular expression."""
        self.search_text.tag_remove("match", "0.0", tk.END)

        regex = self.regex_entry.get()
        search_text = self.search_text.get("0.0", tk.END)

        matches = re.finditer(regex, search_text)
        for match in matches:
            index1 = self.search_text.index("0.0 + " + str(match.span()[0]) + " chars")
            index2 = self.search_text.index("0.0 + " + str(match.span()[1]) + " chars")
            self.search_text.tag_add("match", index1, index2)


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
