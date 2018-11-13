#!/usr/bin/env python3
"""A program that checks for new mail on your email accounts.
Title:
Mail Checker (POP3 / IMAP)

Description:
The user enters various account information including web server, IP, protocol type (POP3 or IMAP)
and the application will check for email on several accounts at a given interval.
"""
import imaplib
import poplib
import time
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tk_messagebox


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Mail Checker (POP3 / IMAP)")

        self.email_treeview_frame = ttk.Frame(self)
        self.bottom_buttons_frame = ttk.Frame(self)

        self.email_treeview = ttk.Treeview(
            self.email_treeview_frame,
            columns=("Host", "Protocol", "Username", "Password"),
            displaycolumns=("Host", "Protocol", "Username"),
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
        self.remove_address_button = ttk.Button(
            self.bottom_buttons_frame,
            text="Remove email address",
            command=self.remove_address,
        )
        self.start_checking_button = ttk.Button(
            self.bottom_buttons_frame,
            text="Start checking in background",
            command=self.start_checking,
        )

        self.email_treeview.column("#0", minwidth=0, width=0)
        self.email_treeview.column(0, anchor=tk.CENTER)
        self.email_treeview.column(1, anchor=tk.CENTER)
        self.email_treeview.column(2, anchor=tk.CENTER)
        self.email_treeview.column(3, anchor=tk.CENTER)
        self.email_treeview.heading(0, text="Host")
        self.email_treeview.heading(1, text="Protocol")
        self.email_treeview.heading(2, text="Username")
        self.email_treeview.heading(3, text="Password")

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
        self.remove_address_button.grid(row=0, column=1, padx=5)
        self.start_checking_button.grid(row=0, column=2, padx=(5, 0))

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())
        center_window_on_screen(self)

    def add_address(self):
        """Add an email address to check."""
        add_address_popup = AddAddressPopup()
        add_address_popup.transient(self)
        center_window_on_screen(add_address_popup)
        self.wait_window(add_address_popup)
        self.email_treeview.insert(
            parent="",
            index="end",
            values=(
                add_address_popup.host,
                add_address_popup.protocol,
                add_address_popup.username,
                add_address_popup.password,
            ),
        )

    def remove_address(self):
        """Remove the selected addresses from the treeview."""
        selected_items = self.email_treeview.selection()
        for item in selected_items:
            self.email_treeview.delete(item)

    def start_checking(self):
        """Start checking for incoming emails."""
        self.withdraw()
        while True:
            found = checking_mainloop(
                [
                    self.email_treeview.item(children_id, "values")
                    for children_id in self.email_treeview.get_children()
                ]
            )
            if found:
                tk_messagebox.showinfo("New message", "You have got a new message!")


class AddAddressPopup(tk.Toplevel):
    """Window for getting information about the email address to add."""

    def __init__(self):
        super().__init__()
        self.title("Add an email address")
        self.resizable(width=False, height=False)

        self.host = ""
        self.protocol = ""
        self.username = ""
        self.password = ""

        self.host_frame = ttk.Frame(self)
        self.protocol_frame = ttk.Frame(self)
        self.username_frame = ttk.Frame(self)
        self.password_frame = ttk.Frame(self)

        self.host_label = ttk.Label(self.host_frame, text="Host:")
        self.host_entry = ttk.Entry(self.host_frame, width=40, justify=tk.CENTER)
        self.protocol_label = ttk.Label(self.protocol_frame, text="Protocol")
        self.protocol_listbox = tk.Listbox(
            self.protocol_frame, listvariable=tk.StringVar(value="IMAP POP3")
        )
        self.username_label = ttk.Label(self.username_frame, text="Username:")
        self.username_entry = ttk.Entry(
            self.username_frame, width=40, justify=tk.CENTER
        )
        self.password_label = ttk.Label(self.password_frame, text="Password:")
        self.password_entry = ttk.Entry(
            self.password_frame, width=40, justify=tk.CENTER, show="*"
        )
        self.add_address_button = ttk.Button(
            self, text="Add address", command=self.add_address
        )

        self.host_frame.grid(row=0, column=0, padx=10, pady=10)
        self.protocol_frame.grid(row=1, column=0, padx=20, pady=10)
        self.username_frame.grid(row=2, column=0, padx=20, pady=10)
        self.password_frame.grid(row=3, column=0, padx=20, pady=10)

        self.host_label.grid(row=0, column=0)
        self.host_entry.grid(row=1, column=0)
        self.protocol_label.grid(row=0, column=0)
        self.protocol_listbox.grid(row=1, column=0)
        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=1, column=0)
        self.password_label.grid(row=0, column=0)
        self.password_entry.grid(row=1, column=0)
        self.add_address_button.grid(row=4, column=0, pady=10)

        self.host_entry.bind("<KeyPress-Return>", lambda _: self.add_address())
        self.username_entry.bind("<KeyPress-Return>", lambda _: self.add_address())
        self.password_entry.bind("<KeyPress-Return>", lambda _: self.add_address())
        self.host_entry.focus()

    def add_address(self):
        self.host = self.host_entry.get()
        self.protocol = self.protocol_listbox.selection_get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.destroy()


def checking_mainloop(addresses_information: list) -> bool:
    """Return True when a new email is found."""
    number_of_emails = {}
    new_number_of_emails = {}
    while True:
        for host, protocol, username, password in addresses_information:
            new_number_of_emails[username] = get_email_amount(
                host, protocol, username, password
            )
            if number_of_emails.get(username) is None:
                number_of_emails[username] = new_number_of_emails[username]
            elif new_number_of_emails[username] > number_of_emails[username]:
                return True
            number_of_emails[username] = new_number_of_emails[username]
        time.sleep(1)


def get_email_amount(host: str, protocol: str, username: str, password: str) -> int:
    """Return the number of emails in the accounts inbox."""
    if protocol == "IMAP":
        with imaplib.IMAP4_SSL(host) as M:
            M.login(username, password)
            number_of_emails = int(M.select()[1][0].decode("UTF-8"))
    else:
        M = poplib.POP3_SSL(host)
        M.user(username)
        M.pass_(password)
        number_of_emails = len(M.list()[1])
    return number_of_emails


def center_window_on_screen(window):
    """Center the specified window on the screen."""
    window.update_idletasks()
    height = window.winfo_height()
    width = window.winfo_width()
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()

    x_coordinate = int(screen_width / 2 - width / 2)
    y_coordinate = int(screen_height / 2 - height / 2)

    window.geometry(
        "".join(
            (
                str(width),
                "x",
                str(height),
                "+",
                str(x_coordinate),
                "+",
                str(y_coordinate),
            )
        )
    )


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
