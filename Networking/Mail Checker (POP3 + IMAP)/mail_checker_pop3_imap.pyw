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

        self.email_treeview = ttk.Treeview(self)
        self.add_address_button = ttk.Button(
            self,
            text="Add email address",
            command=self.add_address
        )
        self.start_checking_button = ttk.Button(
            self,
            text="Start checking in background",
            command=self.start_checking
        )

    def add_address(self):
        """Add an email address to check."""
        add_address_popup = AddAddressPopup()
        add_address_popup.transient(self)
        self.wait_window(add_address_popup)

    def start_checking(self):
        """Start checking for incoming emails."""


class AddAddressPopup(tk.Toplevel):
    """Window for getting information about the email address to add."""

    def __int__(self):
        super().__init__()
        self.title("Add an email address")

        self.host = ""
        self.username = ""
        self.password = ""

        self.host_frame = ttk.Frame(self)
        self.username_frame = ttk.Frame(self)
        self.password_frame = ttk.Frame(self)

        self.host_label = ttk.Label(self, text="Host:")
        self.host_entry = ttk.Entry(self)
        self.username_label = ttk.Label(self, text="Username:")
        self.username_entry = ttk.Entry(self)
        self.password_label = ttk.Label(self, text="Password:")
        self.password_entry = ttk.Entry(self)

    def add_address(self):
        self.host = self.host_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
