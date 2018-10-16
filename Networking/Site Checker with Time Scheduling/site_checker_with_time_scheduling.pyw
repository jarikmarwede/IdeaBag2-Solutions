#!/usr/bin/env python3
"""Check whether a website is online.

Title:
Site Checker with Time Scheduling

Description:
An application that attempts to connect to a website or server every so many minutes
or a given time and check if it is up.
If it is down, it will notify you by email or by posting a notice on screen.
"""
import socket
import urllib.request
import urllib.error
import time
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Site Checker with Time Scheduling")
        self.resizable(False, False)

        self.url_frame = ttk.Frame(self)
        self.timeout_frame = ttk.Frame(self)
        self.interval_frame = ttk.Frame(self)

        self.url_label = ttk.Label(self.url_frame,
                                   text="URL:")
        self.url_entry = ttk.Entry(self.url_frame,
                                   width=80)
        self.timeout_labael = ttk.Label(self.timeout_frame,
                                        text="Time out in s:")
        self.timeout_entry = ttk.Entry(self.timeout_frame)
        self.interval_label = ttk.Label(self.interval_frame,
                                        text="Interval in s:")
        self.interval_entry = ttk.Entry(self.interval_frame)
        self.start_button = ttk.Button(self,
                                       text="Start",
                                       command=self.start)

        self.url_frame.grid(row=0, column=0, padx=5, pady=5)
        self.timeout_frame.grid(row=1, column=0, padx=5, pady=5)
        self.interval_frame.grid(row=2, column=0, padx=5, pady=5)
        self.start_button.grid(row=3, column=0, padx=5, pady=5)

        self.url_label.grid(row=0, column=0)
        self.url_entry.grid(row=1, column=0)
        self.timeout_labael.grid(row=0, column=0)
        self.timeout_entry.grid(row=1, column=0)
        self.interval_label.grid(row=0, column=0)
        self.interval_entry.grid(row=1, column=0)

        self.url_entry.bind("<KeyPress-Return>", lambda _: self.start())
        self.timeout_entry.bind("<KeyPress-Return>", lambda _: self.start())
        self.interval_entry.bind("<KeyPress-Return>", lambda _: self.start())

        self.url_entry.focus_set()

    def start(self):
        """Start checking for website status."""
        self.withdraw()
        while True:
            if not is_online(self.url_entry.get(), int(self.timeout_entry.get())):
                break
            else:
                time.sleep(self.interval_entry.get())
        tkinter.messagebox.showwarning("Website does not respond",
                                       f"{self.url_entry.get()} can not be reached!")
        self.deiconify()


def is_online(url: str, timeout: int) -> bool:
    """Return whether a website is online."""
    try:
        urllib.request.urlopen(url, timeout=timeout)
    except (socket.timeout, urllib.error.URLError):
        return False
    return True


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
