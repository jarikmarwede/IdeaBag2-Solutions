#!/usr/bin/env python3
"""A minimalistic launcher program.

Title:
Quick Launcher

Description:
A utility program that allows the user to assign various programs
to icons on a toolbar.
Then by clicking the buttons
they can quickly launch the programs with parameters etc.
Much like Windows quick launch.
"""
import os
import subprocess
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk

WINDOW_ICON_PATH = "./icon_small.png"
DEFAULT_FILE_TYPE = "executable"
BUTTONS_PER_ROW = 4


class MainWindow:
    """The class for interacting with the tkinter GUI."""

    def __init__(self, master):
        """Create widgets and initialize window."""
        # set up main window
        self.master = master
        self.master.title("Quick Launcher")
        self.master.resizable(width=False, height=False)
        self.master.minsize(width=200, height=50)
        self.master.geometry()
        self.master.window_icon = tk.PhotoImage(file=WINDOW_ICON_PATH)
        self.master.iconphoto(self.master, self.master.window_icon)

        # create widgets
        self.toolbar_frame = ttk.Frame(self.master)

        self.entries = []
        self.add_entry_button = ttk.Button(self.master,
                                           command=self.add_new_entry,
                                           compound=tk.TOP,
                                           text="Add new entry")

        # display widgets
        self.toolbar_frame.grid(column=0, row=0, padx=10, pady=10)

        self.add_entry_button.grid(column=0, row=1, padx=5, pady=5)

    def refresh_entries(self):
        """Display all entries."""
        for index, entry in enumerate(self.entries):
            entry.grid(column=index % BUTTONS_PER_ROW,
                       row=index // BUTTONS_PER_ROW,
                       padx=5,
                       pady=5)

    def add_new_entry(self):
        """Create the NewEntryWindow and add the data entered into it to the toolbar."""
        new_entry_window = NewEntryWindow(self.master)
        self.master.wait_window(new_entry_window)
        if new_entry_window.saved:
            title = new_entry_window.new_title
            icon = new_entry_window.icon
            icon_path = new_entry_window.icon_path
            file_type = new_entry_window.file_type
            executable_path = new_entry_window.executable_file
            commandline_arguments = new_entry_window.command_line_arguments
            code = new_entry_window.code

            if file_type == "executable":
                button = ttk.Button(self.toolbar_frame,
                                    text=title,
                                    image=icon,
                                    compound=tk.LEFT,
                                    command=lambda: launch_program(executable_path,
                                                                   commandline_arguments))
                button.icon_path = icon_path
                button.file_type = "executable"
                button.executable_path = executable_path
                button.commandline_arguments = commandline_arguments
                self.entries.append(button)
                self.refresh_entries()
            elif file_type == "commandline":
                button = ttk.Button(self.toolbar_frame,
                                    text=title,
                                    image=icon,
                                    compound=tk.LEFT,
                                    command=lambda: run_script(code))
                button.icon_path = icon_path
                button.file_type = "commandline"
                button.code = code
                self.entries.append(button)
                self.refresh_entries()


class NewEntryWindow(tk.Toplevel):
    """The window that allows the user to add a new entry to the toolbar."""

    def __init__(self, master):
        """Create widgets and initialize window."""
        # set up window
        self.master = master
        super().__init__(self.master)
        self.title("Add a new entry")
        self.resizable(width=False, height=False)
        self.geometry()
        self.transient(self.master)

        # load images
        self.icon = self.master.window_icon

        # create variables
        self.saved = False
        self.executable_file = None
        self.file_type_choice = tk.StringVar(value=DEFAULT_FILE_TYPE)

        # create widgets
        self.title_frame = ttk.Frame(self)
        self.icon_frame = ttk.Frame(self)
        self.file_type_frame = ttk.Frame(self)
        self.command_line_frame = ttk.Frame(self)
        self.executable_frame = ttk.Frame(self)
        self.executable_file_frame = ttk.Frame(self.executable_frame)
        self.command_line_arguments_frame = ttk.Frame(self.executable_frame)
        self.bottom_buttons_frame = ttk.Frame(self)

        self.title_label = ttk.Label(self.title_frame,
                                     text="Title: ")
        self.title_entry = ttk.Entry(self.title_frame)
        self.icon_label = ttk.Label(self.icon_frame,
                                    text="Icon: ")
        self.icon_button = ttk.Button(self.icon_frame,
                                      image=self.icon,
                                      command=self.pick_icon)
        self.file_type_label = ttk.Label(self.file_type_frame,
                                         text="Choose a filetype: ",
                                         justify=tk.CENTER)
        self.executable_radiobutton = ttk.Radiobutton(self.file_type_frame,
                                                      value="executable",
                                                      variable=self.file_type_choice,
                                                      text="Executable (*.exe)",
                                                      command=self.change_file_type)
        self.command_line_radiobutton = ttk.Radiobutton(self.file_type_frame,
                                                        value="commandline",
                                                        variable=self.file_type_choice,
                                                        text="Command Line Script",
                                                        command=self.change_file_type)
        self.executable_file_label = ttk.Label(self.executable_file_frame,
                                               text="Choose an executable: ")
        self.executable_file_button = ttk.Button(self.executable_file_frame,
                                                 command=self.pick_executable_file,
                                                 text="(No file selected)")
        self.command_line_arguments_label = ttk.Label(self.command_line_arguments_frame,
                                                      text="Additional command line arguments: ")
        self.command_line_arguments_entry = ttk.Entry(self.command_line_arguments_frame)
        self.code_label = ttk.Label(self.command_line_frame,
                                    text="Please enter your commands here: ")
        self.code_text = tk.Text(self.command_line_frame)
        self.save_entry_button = ttk.Button(self.bottom_buttons_frame,
                                            command=self.save_entry,
                                            text="Save")
        self.cancel_button = ttk.Button(self.bottom_buttons_frame,
                                        command=self.destroy,
                                        text="Cancel")

        # display widgets
        self.title_frame.grid(column=0, row=0, padx=10, pady=10)
        self.icon_frame.grid(column=0, row=1, padx=10, pady=10)
        self.file_type_frame.grid(column=0, row=2, padx=10, pady=10)
        self.executable_frame.grid(column=0, row=3, padx=10, pady=10)
        self.executable_file_frame.grid(column=0, row=0, padx=10, pady=2.5)
        self.command_line_arguments_frame.grid(column=0, row=1, padx=10, pady=2.5)
        self.command_line_frame.grid(column=0, row=4, padx=10, pady=10)
        self.bottom_buttons_frame.grid(column=0, row=5, padx=10, pady=10)

        self.title_label.grid(column=0, row=0)
        self.title_entry.grid(column=1, row=0)
        self.icon_label.grid(column=0, row=0)
        self.icon_button.grid(column=1, row=0)
        self.file_type_label.grid(column=0, row=0, columnspan=2)
        self.executable_radiobutton.grid(column=0, row=1)
        self.command_line_radiobutton.grid(column=1, row=1)
        self.executable_file_label.grid(column=0, row=0)
        self.executable_file_button.grid(column=0, row=1)
        self.command_line_arguments_label.grid(column=0, row=0)
        self.command_line_arguments_entry.grid(column=0, row=1)
        self.code_label.grid(column=0, row=0)
        self.code_text.grid(column=0, row=1)
        self.save_entry_button.grid(column=0, row=0, padx=5)
        self.cancel_button.grid(column=1, row=0, padx=5)

        self.command_line_frame.grid_remove()

    def change_file_type(self):
        """Display correct widgets for the current file type."""
        if self.file_type_choice.get() == "executable":
            self.command_line_frame.grid_remove()
            self.executable_frame.grid()
        elif self.file_type_choice.get() == "commandline":
            self.executable_frame.grid_remove()
            self.command_line_frame.grid()

    def pick_icon(self):
        """Ask user to enter an image then load that image on self.icon_button."""
        file_name = tkinter.filedialog.askopenfilename(defaultextension=".png",
                                                       filetypes=[("PNG", "*.png")],
                                                       parent=self,
                                                       title="Choose an icon")
        if file_name:
            self.icon = tk.PhotoImage(file=file_name)
            self.icon_button.config(image=self.icon)

    def pick_executable_file(self):
        """Ask user to enter a file then display file name on self.executable_file_button."""
        file_name = tkinter.filedialog.askopenfilename(defaultextension=".exe",
                                                       filetypes=[("EXE", "*.exe")],
                                                       parent=self,
                                                       title="Choose an executable")
        if file_name:
            self.executable_file = file_name
            self.executable_file_button.config(text=file_name.split("/")[-1])

    def save_entry(self):
        """Save entry and close window."""
        self.new_title = self.title_entry.get()
        self.icon_path = self.icon.cget("file")
        self.file_type = self.file_type_choice.get()
        self.command_line_arguments = self.command_line_arguments_entry.get()
        self.code = self.code_text.get(0.1, tk.END)

        if (self.file_type == "executable" and self.executable_file
                or self.file_type == "commandline" and self.code != "\n"):
            self.saved = True
            self.destroy()
        else:
            tkinter.messagebox.showwarning(title="Invalid input",
                                           message="Please either enter an executable file "
                                           "or a commandline script!")


def launch_program(executable_path: str, commandlineargs=""):
    """Execute specified executable with commandlineargs."""
    subprocess.call(executable=executable_path, args=commandlineargs)


def run_script(code: str):
    """Run script in commandline."""
    os.system(code)


if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()
