#!/usr/bin/env python3
"""A simple text editor with tabs.

Title:
Text Editor

Description:
Develop a Notepad style application that can
open, edit, and save text documents.
For added complexity,
add syntax highlighting, find and replace, text formatting etc.
"""
import os
import tkinter as tk
from tkinter import filedialog as tk_filedialog, messagebox as tk_messagebox, ttk
INDENT_SIZE = 4


class MainWindow(tk.Tk):
    """Main tkinter window."""

    def __init__(self):
        """Initialize the window."""
        super().__init__()
        self.title("Text Editor")
        self.resizable(width=False, height=False)
        self.geometry()

        # create variables
        self.notebook_tabs = {}
        self.status_text = tk.StringVar()

        # create widgets
        self.tab_notebook = ttk.Notebook(self)
        self.status_bar = ttk.Label(self,
                                    textvariable=self.status_text)
        self.main_menu = tk.Menu(self,
                                 tearoff=0)
        self.file_sub_menu = tk.Menu(self.main_menu,
                                     tearoff=0)

        # configure widgets
        self.tab_notebook.enable_traversal()
        self.config(menu=self.main_menu)
        self.main_menu.add_cascade(menu=self.file_sub_menu,
                                   label="File")

        self.file_sub_menu.add_command(label="New file",
                                       accelerator="Ctrl+N",
                                       command=self.add_new_tab)
        self.file_sub_menu.add_command(label="Open file",
                                       accelerator="Ctrl+O",
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
        self.tab_notebook.bind("<<NotebookTabChanged>>", lambda _: self.tab_changed())
        self.bind_all("<Control-KeyPress-n>", lambda _: self.add_new_tab())
        self.bind_all("<Control-KeyPress-o>", lambda _: self.open_file())
        self.tab_notebook.bind("<Button-3>", self.show_context_menu)

        # display widgets
        self.tab_notebook.grid(row=0, column=0)
        self.status_bar.grid(row=1, column=0, sticky=tk.EW)

        # load empty text editor
        self.add_new_tab()

    def add_new_tab(self, tab_name="New file", file_path="", editor_text=""):
        """Add new editor tab to notebook."""
        # create widgets
        notebook_tab_frame = ttk.Frame(self.tab_notebook)
        text_editor_scroll_x = ttk.Scrollbar(notebook_tab_frame, orient=tk.HORIZONTAL)
        text_editor_scroll_y = ttk.Scrollbar(notebook_tab_frame, orient=tk.VERTICAL)
        text_editor = tk.Text(notebook_tab_frame, wrap=tk.NONE,
                              xscrollcommand=text_editor_scroll_x.set,
                              yscrollcommand=text_editor_scroll_y.set)

        # configure widgets
        text_editor.insert("0.0", editor_text)
        text_editor_scroll_x.config(command=text_editor.xview)
        text_editor_scroll_y.config(command=text_editor.yview)

        # create bindings
        text_editor.bind("<Tab>", lambda _: tab_pressed(text_editor))
        text_editor.bind("<Shift-KeyPress-Tab>", lambda _: shift_tab_pressed(text_editor))
        text_editor.bind("<Return>", lambda _: enter_pressed(text_editor))
        text_editor.bind("<Control-KeyPress-w>", lambda _: self.close_tab(notebook_tab_frame))
        text_editor.bind("<Control-KeyPress-s>", lambda _: self.save_file(notebook_tab_frame))

        # display widgets
        text_editor.grid(row=0, column=0)
        text_editor_scroll_y.grid(row=0, column=1, sticky=tk.NS)
        text_editor_scroll_x.grid(row=1, column=0, sticky=tk.EW)

        self.notebook_tabs[notebook_tab_frame] = {
            "text_editor": text_editor,
            "file_path": file_path
        }
        self.tab_notebook.add(notebook_tab_frame, text=tab_name)
        self.tab_notebook.select(notebook_tab_frame)

    def open_file(self):
        """Open a file."""
        file_path = tk_filedialog.askopenfilename(parent=self,
                                                  defaultextension=".txt")
        with open(file_path, "r") as file:
            file_content = file.read()
        file_name = os.path.basename(file_path)

        self.add_new_tab(file_name, file_path, file_content)

    def save_file(self, notebook_tab_frame):
        """Save current file."""
        tab = self.notebook_tabs[notebook_tab_frame]
        if not tab["file_path"]:
            self.save_file_as(notebook_tab_frame)
        else:
            with open(tab["file_path"], "w") as file:
                file.write(tab["text_editor"].get("0.0", tk.END))

    def save_file_as(self, notebook_tab_frame):
        """Save current file as filename specified by the user."""
        file_path = tk_filedialog.asksaveasfilename(parent=self,
                                                    defaultextension=".txt",
                                                    filetypes=[("All types", "*.*")])
        self.notebook_tabs[notebook_tab_frame]["file_path"] = file_path
        tab = self.notebook_tabs[notebook_tab_frame]
        if file_path:
            with open(file_path, "w") as file:
                file.write(tab["text_editor"].get("0.0", tk.END))

    def show_context_menu(self, event):
        """Show the context menu at position specified by event."""
        context_menu = tk.Menu(self.master, tearoff=0)
        context_menu.add_command(label="Close current tab (Ctrl+W)",
                                 command=self.close_tab)
        try:
            context_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            context_menu.grab_release()

    def close_tab(self, notebook_tab_frame):
        """Close the current tab in the notebook."""
        tab = self.notebook_tabs[notebook_tab_frame]
        if tab["file_path"]:
            with open(tab["file_path"], "r") as file:
                file_content = file.read()
            if (file_content == tab["text_editor"].get("0.0", tk.END) or
                    file_content == tab["text_editor"].get("0.0", tk.END).rstrip()):
                del self.notebook_tabs[notebook_tab_frame]
                self.tab_notebook.forget(tk.CURRENT)
                if len(self.tab_notebook.tabs()) <= 0:
                    self.add_new_tab()
                return
        if tab["text_editor"].get("0.0", tk.END) == "\n":
            save = False
        else:
            save = tk_messagebox.askyesnocancel(title="Save Document?",
                                                message="Do you want to save the document "
                                                        "before closing it?")
        if save:
            self.save_file(notebook_tab_frame)
        elif save is None:
            return
        del self.notebook_tabs[notebook_tab_frame]
        self.tab_notebook.forget(tk.CURRENT)
        if len(self.tab_notebook.tabs()) <= 0:
            self.add_new_tab()

    def tab_changed(self):
        """Change focus and update status bar on tab change."""
        selected_tab = self.nametowidget(self.tab_notebook.select())
        self.notebook_tabs[selected_tab]["text_editor"].focus_set()

        file_path = self.notebook_tabs[selected_tab]["file_path"]
        self.status_text.set(file_path)


def tab_pressed(text_widget):
    """Insert spaces instead of tabs."""
    text_widget.insert(tk.INSERT, " " * INDENT_SIZE)
    return "break"


def shift_tab_pressed(text_widget):
    """Remove spaces according to indent size."""
    reversed_text = text_widget.get("insert linestart", tk.INSERT)[::-1]
    if reversed_text.startswith(" " * INDENT_SIZE):
        new_text = reversed_text[:INDENT_SIZE-1:-1]
        text_widget.delete("insert linestart", tk.INSERT)
        text_widget.insert(tk.INSERT, new_text)


def enter_pressed(text_widget):
    """Handle indentation when pressing enter."""
    current_line = text_widget.get("insert linestart", "insert lineend")
    preceding_spaces = 0
    for character in current_line:
        if character == " ":
            preceding_spaces += 1
        else:
            break
    text_widget.insert("insert lineend", "\n" + " " * preceding_spaces)
    return "break"


def _start_gui():
    """Start the graphical user interface."""
    root = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    _start_gui()
