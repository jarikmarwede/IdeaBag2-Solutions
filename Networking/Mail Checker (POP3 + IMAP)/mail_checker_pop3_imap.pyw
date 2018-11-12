#!/usr/bin/env python3
import imaplib
import poplib
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tk_messagebox


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Mail Checker (POP3 / IMAP)")
        self.resizable(width=True, height=True)

        self.email_treeview_frame = ttk.Frame(self)
        self.bottom_buttons_frame = ttk.Frame(self)

        self.email_treeview = ttk.Treeview(
            self.email_treeview_frame,
            columns=("Host", "Username", "Password"),
            displaycolumns=("Host", "Username"),
        )
        self.email_treeview_scrollbar = ttk.Scrollbar(
            self.email_treeview_frame, command=self.email_treeview.yview
        )
        self.email_treeview["yscrollcommand"] = self.email_treeview_scrollbar.set
        self.add_address_button = ttk.Button(
            self.bottom_buttons_frame,
            text="Add email address",
            command=self.add_address,
        )
        self.start_checking_button = ttk.Button(
            self.bottom_buttons_frame,
            text="Start checking in background",
            command=self.start_checking,
        )

        self.email_treeview_frame.grid(
            row=0, column=0, padx=15, pady=15, sticky=tk.NSEW
        )
        self.bottom_buttons_frame.grid(row=1, column=0, padx=10, pady=(10, 20))
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.email_treeview_frame.rowconfigure(0, weight=1)
        self.email_treeview_frame.columnconfigure(0, weight=1)

        self.email_treeview.grid(row=0, column=0, sticky=tk.NSEW)
        self.email_treeview_scrollbar.grid(row=0, column=1, sticky=tk.NS + tk.E)
        self.add_address_button.grid(row=0, column=0, padx=(0, 5))
        self.start_checking_button.grid(row=0, column=1, padx=(5, 0))

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

    def add_address(self):
        """Add an email address to check."""
        add_address_popup = AddAddressPopup()
        add_address_popup.transient(self)
        self.wait_window(add_address_popup)
        self.email_treeview.insert(
            parent="",
            index="end",
            values=(
                add_address_popup.host,
                add_address_popup.username,
                add_address_popup.password,
            ),
        )

    def start_checking(self):
        """Start checking for incoming emails."""


class AddAddressPopup(tk.Toplevel):
    """Window for getting information about the email address to add."""

    def __init__(self):
        super().__init__()
        self.title("Add an email address")
        self.resizable(width=False, height=False)

        self.host = ""
        self.username = ""
        self.password = ""

        self.host_frame = ttk.Frame(self)
        self.username_frame = ttk.Frame(self)
        self.password_frame = ttk.Frame(self)

        self.host_label = ttk.Label(self.host_frame, text="Host:")
        self.host_entry = ttk.Entry(self.host_frame, width=30, justify=tk.CENTER)
        self.username_label = ttk.Label(self.username_frame, text="Username:")
        self.username_entry = ttk.Entry(
            self.username_frame, width=30, justify=tk.CENTER
        )
        self.password_label = ttk.Label(self.password_frame, text="Password:")
        self.password_entry = ttk.Entry(
            self.password_frame, width=30, justify=tk.CENTER, show="*"
        )
        self.add_address_button = ttk.Button(
            self, text="Add address", command=self.add_address
        )

        self.host_frame.grid(row=0, column=0, padx=10, pady=10)
        self.username_frame.grid(row=1, column=0, padx=10, pady=10)
        self.password_frame.grid(row=2, column=0, padx=10, pady=10)

        self.host_label.grid(row=0, column=0)
        self.host_entry.grid(row=1, column=0)
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=1, column=0)
        self.password_label.grid(row=0, column=0)
        self.password_entry.grid(row=1, column=0)
        self.add_address_button.grid(row=3, column=0, pady=10)

    def add_address(self):
        self.host = self.host_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.destroy()


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
