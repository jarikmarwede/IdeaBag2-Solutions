#!/usr/bin/env python3
"""A simple zip archive creator.

Title:
Create Zip File Maker

Description:
The user enters various files from different directories
and maybe even another computer on the network
and the program transfers them
and zips them up into a zip file.
For added complexity,
apply actual compression to the files.
"""
import os
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from zipfile import ZipFile, ZIP_DEFLATED


class MainWindow:
    """The class for interacting with tkinter."""

    def __init__(self, master: tk.Tk):
        """Initialize main window."""
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry()
        self.master.title("Zip File Maker")

        # create frames
        self.treeview_frame = ttk.Frame(self.master)
        self.button_row_frame = ttk.Frame(self.master)

        # create other widgets
        self.files_treeview = ttk.Treeview(self.treeview_frame,
                                           columns=("path",),
                                           selectmode="browse",
                                           show="tree")
        self.files_treeview.column("#0", minwidth=0, width=0)
        self.files_treeview.column("path", width=400)
        self.files_treeview_scrollbar_y = ttk.Scrollbar(self.treeview_frame,
                                                        orient=tk.VERTICAL,
                                                        command=self.files_treeview.yview)
        self.files_treeview_scrollbar_x = ttk.Scrollbar(self.treeview_frame,
                                                        orient=tk.HORIZONTAL,
                                                        command=self.files_treeview.xview)
        self.files_treeview.config(yscrollcommand=self.files_treeview_scrollbar_y.set)
        self.files_treeview.config(xscrollcommand=self.files_treeview_scrollbar_x.set)

        self.add_file_button = ttk.Button(self.button_row_frame,
                                          text="Add new file(s)",
                                          command=self.add_files)
        self.remove_file_button = ttk.Button(self.button_row_frame,
                                             text="Remove file",
                                             command=self.remove_file)
        self.compress_button = ttk.Button(self.button_row_frame,
                                          text="Compress",
                                          command=self.compress_files)

        # display frames
        self.treeview_frame.grid(row=0, column=0, padx=10, pady=10)
        self.button_row_frame.grid(row=1, column=0, padx=10, pady=10)

        # display other widgets
        self.files_treeview.grid(row=0, column=0)
        self.files_treeview_scrollbar_y.grid(row=0, column=1, sticky=tk.NS)
        self.files_treeview_scrollbar_x.grid(row=1, column=0, sticky=tk.EW)
        self.add_file_button.grid(row=0, column=0, padx=2.5)
        self.remove_file_button.grid(row=0, column=1, padx=2.5)
        self.compress_button.grid(row=0, column=2, padx=2.5)

    def add_files(self):
        """Ask user to give file path and save new file."""
        file_paths = tkinter.filedialog.askopenfilenames(parent=self.master)
        if file_paths:
            for file_path in file_paths:
                self.files_treeview.insert("", "end", values=(file_path,))
            self.files_treeview.selection_set(self.files_treeview.get_children()[-1])

    def remove_file(self):
        """Remove currently selected file."""
        selected_column = self.files_treeview.selection()

        if selected_column:
            self.files_treeview.delete(selected_column)
            if self.files_treeview.get_children():
                self.files_treeview.selection_set(self.files_treeview.get_children()[-1])

    def compress_files(self):
        """Compress all files to zip archive."""
        archive_file_path = tkinter.filedialog.asksaveasfilename(parent=self.master,
                                                                 defaultextension=".zip",
                                                                 filetypes=[("Zip File", "*.zip")])
        if archive_file_path and self.files_treeview.get_children():
            with ZipFile(archive_file_path, "w", ZIP_DEFLATED) as archive:
                for row in self.files_treeview.get_children():
                    file_path = self.files_treeview.item(row, "values")[0]
                    file_name = os.path.basename(file_path)
                    archive.write(file_path, arcname=file_name)


def start_gui():
    """Start the GUI."""
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    start_gui()
