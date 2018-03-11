#!/usr/bin/env python3
"""
Title:
Code Snippet Manager

Description:
Another utility program
that allows coders to put in functions, classes or other tidbits
to save for use later.
Organized by the type of snippet or language
the coder can quickly look up code.
For extra practice
try adding syntax highlighting based on the language.
"""
import string
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
DEFAULT_SEARCH_SELECTION = "name"


class CodeSnippet:
    """A code snippet."""

    def __init__(self, name: str, language: str, code_type: str, code: str, tags=()):
        """Define code snippet properties."""
        self.name = name
        self.language = language
        self.code_type = code_type
        self.code = code
        self.tags = tags

    def not_empty(self):
        """Return whether snippet is empty or not."""
        if self.code:
            return True
        return False


class MainWindow:
    """The class for interacting with tkinter."""

    def __init__(self, master: tk.Tk):
        """Initialize window."""
        self.master = master
        self.master.title("Code Snippet Manager")
        self.master.geometry()
        self.master.resizable(width=False, height=False)

        # define instance variables
        self.code_snippets = []
        self.table = []

        # create variables for widgets
        self.search_selection = tk.StringVar(value=DEFAULT_SEARCH_SELECTION)

        # create frames
        self.search_frame = ttk.Frame(self.master)
        self.search_radiobuttons_frame = ttk.Frame(self.search_frame)
        self.selection_buttons_frame = ttk.Frame(self.master)
        self.code_buttons_frame = ttk.Frame(self.master)

        # create other widgets
        self.search_button = ttk.Button(self.search_frame,
                                        text="Search",
                                        command=self.refresh_treeview)
        self.search_bar_entry = ttk.Entry(self.search_frame,
                                          width=40)
        self.name_search_selection_radiobutton = ttk.Radiobutton(self.search_radiobuttons_frame,
                                                                 text="Name",
                                                                 value="name",
                                                                 variable=self.search_selection)
        self.language_search_selection_radiobutton = ttk.Radiobutton(self.search_radiobuttons_frame,
                                                                     text="Language",
                                                                     value="language",
                                                                     variable=self.search_selection)
        self.type_search_selection_radiobutton = ttk.Radiobutton(self.search_radiobuttons_frame,
                                                                 text="Type",
                                                                 value="type",
                                                                 variable=self.search_selection)
        self.tags_search_selection_radiobutton = ttk.Radiobutton(self.search_radiobuttons_frame,
                                                                 text="Tags",
                                                                 value="tags",
                                                                 variable=self.search_selection)
        self.snippet_selection_treeview = ttk.Treeview(self.master,
                                                       columns=("Name", "Type", "Language", "Tags"),
                                                       selectmode="browse")
        self.add_snippet_button = ttk.Button(self.selection_buttons_frame,
                                             text="+",
                                             command=self.add_new_snippet)
        self.remove_snippet_button = ttk.Button(self.selection_buttons_frame,
                                                text="-",
                                                command=self.remove_snippet)
        self.change_properties_button = ttk.Button(self.selection_buttons_frame,
                                                   text="Edit Properties",
                                                   command=self.change_properties)
        self.code_editor_text = tk.Text(self.master)
        self.save_changes_button = ttk.Button(self.code_buttons_frame,
                                              text="Save changes",
                                              command=self.save_code_changes)
        self.copy_snippet_button = ttk.Button(self.code_buttons_frame,
                                              text="Copy snippet",
                                              command=self.copy_snippet)

        # widget bindings
        self.search_bar_entry.bind("<KeyPress-Return>", lambda _: self.refresh_treeview())
        self.snippet_selection_treeview.bind("<<TreeviewSelect>>", self.refresh_text_editor)

        # configure treeview widget
        self.snippet_selection_treeview.column("#0", minwidth=0, width=0)
        self.snippet_selection_treeview.heading("Name", text="Name")
        self.snippet_selection_treeview.heading("Type", text="Type")
        self.snippet_selection_treeview.heading("Language", text="Language")
        self.snippet_selection_treeview.heading("Tags", text="Tags")

        # display frames
        self.search_frame.grid(row=0, column=0, padx=10, pady=10)
        self.search_radiobuttons_frame.grid(row=0, column=2, padx=10)
        self.selection_buttons_frame.grid(row=2, column=0, padx=10, pady=10)
        self.code_buttons_frame.grid(row=2, column=1, padx=10, pady=10)

        # display other widgets
        self.search_button.grid(row=0, column=0, padx=2.5)
        self.search_bar_entry.grid(row=0, column=1, padx=10)
        self.name_search_selection_radiobutton.grid(row=0, column=0, padx=5)
        self.language_search_selection_radiobutton.grid(row=0, column=1, padx=5)
        self.type_search_selection_radiobutton.grid(row=0, column=2, padx=5)
        self.tags_search_selection_radiobutton.grid(row=0, column=3, padx=5)
        self.snippet_selection_treeview.grid(row=1, column=0, padx=10, pady=10)
        self.code_editor_text.grid(row=1, column=1, padx=10, pady=10)
        self.add_snippet_button.grid(row=0, column=0, padx=2.5)
        self.remove_snippet_button.grid(row=0, column=1, padx=2.5)
        self.change_properties_button.grid(row=0, column=2, padx=2.5)
        self.save_changes_button.grid(row=0, column=0, padx=2.5)
        self.copy_snippet_button.grid(row=0, column=1, padx=2.5)

    def copy_snippet(self):
        """Copy code of current snippet to clipboard."""
        self.master.clipboard_clear()
        self.master.clipboard_append(self.code_editor_text.get(0.1, tk.END))

    def add_new_snippet(self):
        """Create new snippet window."""
        new_snippet_window = NewCodeSnippetWindow(self.master)
        self.master.wait_window(new_snippet_window)

        new_snippet = new_snippet_window.code_snippet
        if new_snippet.not_empty():
            self.code_snippets.append(new_snippet)
            self.refresh_treeview()

    def remove_snippet(self):
        """Remove currently selected snippet."""
        try:
            selected_snippet_index = self.snippet_selection_treeview.index(self.snippet_selection_treeview.selection()[0])
        except IndexError:
            return None

        user_input = tkinter.messagebox.askyesno(title="Delete Snippet?",
                                                 message="Do you really want to delete \"" + self.code_snippets[selected_snippet_index].name + "\" ?",
                                                 default=tkinter.messagebox.NO,
                                                 parent=self.master)

        if user_input:
            self.code_snippets.pop(selected_snippet_index)
            self.table.pop(selected_snippet_index)
            self.refresh_treeview()

    def refresh_treeview(self):
        """Sync treeview widget with self.code_snippets."""
        self.snippet_selection_treeview.delete(*self.snippet_selection_treeview.get_children())
        self.table = []
        search_term = self.search_bar_entry.get()
        search_selection = self.search_selection.get()
        filtered_snippets = []

        for snippet in self.code_snippets:
            if search_selection == "name":
                if search_term in snippet.name:
                    filtered_snippets.append(snippet)
            elif search_selection == "type":
                if search_term in snippet.code_type:
                    filtered_snippets.append(snippet)
            elif search_selection == "language":
                if search_term in snippet.language:
                    filtered_snippets.append(snippet)
            elif search_selection == "tags":
                if search_term in snippet.tags:
                    filtered_snippets.append(snippet)

        if filtered_snippets:
            for snippet in filtered_snippets:
                self.table.append(
                    self.snippet_selection_treeview.insert("", tk.END, values=(snippet.name,
                                                                               snippet.code_type,
                                                                               snippet.language,
                                                                               ", ".join(
                                                                                   snippet.tags))))
            self.snippet_selection_treeview.selection_set(self.table[-1])

        self.refresh_text_editor()

    def refresh_text_editor(self, tk_event=None):
        """Refresh code text editor widget with new snippet data."""
        self.code_editor_text.delete(0.1, tk.END)

        try:
            selected_snippet_index = self.snippet_selection_treeview.index(self.snippet_selection_treeview.selection()[0])
        except IndexError:
            return None
        snippet = self.code_snippets[selected_snippet_index]

        self.code_editor_text.insert(0.1, snippet.code)

    def save_code_changes(self):
        """Save changes to the code in the text editor."""
        try:
            selected_snippet_index = self.snippet_selection_treeview.index(self.snippet_selection_treeview.selection()[0])
        except IndexError:
            return None

        self.code_snippets[selected_snippet_index].code = self.code_editor_text.get(0.1, tk.END)

    def change_properties(self):
        """Open window for changing properties of selected snippet."""
        try:
            selected_snippet_index = self.snippet_selection_treeview.index(self.snippet_selection_treeview.selection()[0])
        except IndexError:
            return None
        properties_window = PropertiesWindow(self.master,
                                             self.code_snippets[selected_snippet_index])
        self.master.wait_window(properties_window)

        changed_snippet = properties_window.changed_snippet
        if changed_snippet.not_empty():
            self.code_snippets[selected_snippet_index] = changed_snippet
            self.refresh_treeview()


class NewCodeSnippetWindow(tk.Toplevel):
    """Window for creating a new code snippet."""

    def __init__(self, master: tk.Tk):
        self.master = master
        super().__init__(self.master)
        self.title("New Code Snippet")
        self.geometry()
        self.resizable(width=False, height=False)

        self.code_snippet = CodeSnippet("", "", "", "")

        # create frames
        self.input_frame = ttk.Frame(self)
        self.name_frame = ttk.Frame(self.input_frame)
        self.code_type_frame = ttk.Frame(self.input_frame)
        self.language_frame = ttk.Frame(self.input_frame)
        self.tags_frame = ttk.Frame(self.input_frame)
        self.code_frame = ttk.Frame(self.input_frame)
        self.bottom_buttons = ttk.Frame(self)

        # create other widgets
        self.name_label = ttk.Label(self.name_frame,
                                    text="Snippet name:")
        self.name_entry = ttk.Entry(self.name_frame)
        self.code_type_label = ttk.Label(self.code_type_frame,
                                         text="Code type:")
        self.code_type_entry = ttk.Entry(self.code_type_frame)
        self.language_label = ttk.Label(self.language_frame,
                                        text="Programming language:")
        self.language_entry = ttk.Entry(self.language_frame)
        self.tags_label = ttk.Label(self.tags_frame,
                                    text="Additional tags (separated by comma)")
        self.tags_entry = ttk.Entry(self.tags_frame,
                                    width=100)
        self.code_label = ttk.Label(self.code_frame,
                                    text="Snippet code:")
        self.code_text = tk.Text(self.code_frame)
        self.save_snippet_button = ttk.Button(self.bottom_buttons,
                                              text="Save snippet",
                                              command=self.save_and_exit)
        self.cancel_button = ttk.Button(self.bottom_buttons,
                                        text="Cancel",
                                        command=self.destroy)

        # widget bindings
        self.name_entry.bind("<KeyPress-Return>", self.save_and_exit)
        self.code_type_entry.bind("<KeyPress-Return>", self.save_and_exit)
        self.language_entry.bind("<KeyPress-Return>", self.save_and_exit)
        self.tags_entry.bind("<KeyPress-Return>", self.save_and_exit)

        # display frames
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)
        self.name_frame.grid(row=0, column=0, pady=5)
        self.code_type_frame.grid(row=1, column=0, pady=5)
        self.language_frame.grid(row=2, column=0, pady=5)
        self.tags_frame.grid(row=3, column=0, pady=5)
        self.code_frame.grid(row=4, column=0, pady=5)
        self.bottom_buttons.grid(row=1, column=0, padx=10, pady=10)

        # display other widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=1, column=0)
        self.code_type_label.grid(row=0, column=0)
        self.code_type_entry.grid(row=1, column=0)
        self.language_label.grid(row=0, column=0)
        self.language_entry.grid(row=1, column=0)
        self.tags_label.grid(row=0, column=0)
        self.tags_entry.grid(row=1, column=0)
        self.code_label.grid(row=0, column=0)
        self.code_text.grid(row=1, column=0)
        self.save_snippet_button.grid(row=0, column=0, padx=5)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def save_and_exit(self, event=None):
        """Save all input into new snippet."""
        name = self.name_entry.get()
        code_type = self.code_type_entry.get()
        language = self.language_entry.get()
        tags = [tag.strip() for tag in self.tags_entry.get().split(",")]
        code = self.code_text.get(0.1, tk.END)

        if name in string.whitespace:
            tkinter.messagebox.showerror(title="Missing name",
                                         message="Please enter a name for the Snippet!",
                                         parent=self)
            return None
        elif code in string.whitespace:
            tkinter.messagebox.showerror(title="No code",
                                         message="Please first type in some code for the Snippet!",
                                         parent=self)
            return None

        self.code_snippet = CodeSnippet(name, language, code_type, code, tags)

        self.destroy()


class PropertiesWindow(tk.Toplevel):
    """Window for editing properties of a snippet."""

    def __init__(self, master: tk.Tk, snippet: CodeSnippet):
        self.master = master
        super().__init__(self.master)
        self.title("Properties")
        self.geometry()
        self.resizable(width=False, height=False)

        self.changed_snippet = CodeSnippet("", "", "", "")
        self.snippet = snippet

        # create variables for widgets
        self.name = tk.StringVar(value=self.snippet.name)
        self.code_type = tk.StringVar(value=self.snippet.code_type)
        self.language = tk.StringVar(value=self.snippet.language)
        self.tags = tk.StringVar(value=", ".join(self.snippet.tags))

        # create frames
        self.properties_frame = ttk.Frame(self)
        self.name_frame = ttk.Frame(self.properties_frame)
        self.type_frame = ttk.Frame(self.properties_frame)
        self.language_frame = ttk.Frame(self.properties_frame)
        self.tags_frame = ttk.Frame(self.properties_frame)
        self.bottom_buttons_frame = ttk.Frame(self)

        # create other widgets
        self.name_label = ttk.Label(self.name_frame,
                                    text="Snippet name: ")
        self.name_entry = ttk.Entry(self.name_frame,
                                    textvariable=self.name)
        self.type_label = ttk.Label(self.type_frame,
                                    text="Code type: ")
        self.type_entry = ttk.Entry(self.type_frame,
                                    textvariable=self.code_type)
        self.language_label = ttk.Label(self.language_frame,
                                        text="Programming language: ")
        self.language_entry = ttk.Entry(self.language_frame,
                                        textvariable=self.language)
        self.tags_label = ttk.Label(self.tags_frame,
                                    text="Additional tags (separated by comma): ")
        self.tags_entry = ttk.Entry(self.tags_frame,
                                    textvariable=self.tags,
                                    width=100)
        self.save_button = ttk.Button(self.bottom_buttons_frame,
                                      text="Save changes",
                                      command=self.save_changes)
        self.cancel_button = ttk.Button(self.bottom_buttons_frame,
                                        text="Cancel",
                                        command=self.destroy)

        # widget bindings
        self.name_entry.bind("<KeyPress-Return>", self.save_changes)
        self.type_entry.bind("<KeyPress-Return>", self.save_changes)
        self.language_entry.bind("<KeyPress-Return>", self.save_changes)
        self.tags_entry.bind("<KeyPress-Return>", self.save_changes)

        # display frames
        self.properties_frame.grid(row=0, column=0, padx=10, pady=10)
        self.name_frame.grid(row=0, column=0, pady=10)
        self.type_frame.grid(row=1, column=0, pady=10)
        self.language_frame.grid(row=2, column=0, pady=10)
        self.tags_frame.grid(row=3, column=0, pady=10)
        self.bottom_buttons_frame.grid(row=1, column=0, padx=10, pady=10)

        # display other widgets
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=1, column=0)
        self.type_label.grid(row=0, column=0)
        self.type_entry.grid(row=1, column=0)
        self.language_label.grid(row=0, column=0)
        self.language_entry.grid(row=1, column=0)
        self.tags_label.grid(row=0, column=0)
        self.tags_entry.grid(row=1, column=0)
        self.save_button.grid(row=0, column=0, padx=5)
        self.cancel_button.grid(row=0, column=1, padx=5)

    def save_changes(self, event=None):
        """Save changes to properties and exit window."""
        name = self.name.get()
        language = self.language.get()
        code_type = self.code_type.get()
        tags = [tag.strip() for tag in self.tags.get().split(",")]

        if name in string.whitespace:
            tkinter.messagebox.showerror(title="Missing name",
                                         message="Please enter a name for the Snippet!",
                                         parent=self)
            return None

        self.changed_snippet = CodeSnippet(name, language, code_type, self.snippet.code, tags)

        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()
