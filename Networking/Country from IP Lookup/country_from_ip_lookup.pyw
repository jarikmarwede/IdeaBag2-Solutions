#!/usr/bin/env python3
"""Lookup a country of an IP address.

Title:
Country from IP Lookup

Description:
Enter an IP address and find the country that IP is registered in.
"""
import urllib.request
import json
import tkinter as tk
from tkinter import ttk

API_URL = "https://ipapi.co/"
API_FORMAT = "/json"


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Country from IP Lookup")
        self.resizable(width=False, height=False)

        self.ip_frame = ttk.Frame(self)
        self.country_frame = ttk.Frame(self)

        self.ip_label = ttk.Label(self.ip_frame, text="IP")
        self.ip_entry = ttk.Entry(self.ip_frame, justify=tk.CENTER)
        self.country_label = ttk.Label(self.country_frame, text="Country")
        self.country_entry = ttk.Entry(self.country_frame, justify=tk.CENTER, state="disabled")
        self.lookup_button = ttk.Button(self, text="Lookup", command=self.get_country)

        self.ip_frame.grid(row=0, padx=20, pady=10)
        self.country_frame.grid(row=1, padx=20, pady=10)
        self.lookup_button.grid(row=2, padx=20, pady=10)

        self.ip_label.grid(row=0)
        self.ip_entry.grid(row=1)
        self.country_label.grid(row=0)
        self.country_entry.grid(row=1)

        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

    def get_country(self):
        """Output the country of the IP address."""
        country = get_country_from_ip(self.ip_entry.get())
        self.country_entry.config(state=tk.NORMAL)
        self.country_entry.delete(0, tk.END)
        self.country_entry.insert(0, country)
        self.country_entry.config(state="disabled")


def get_country_from_ip(ip: str) -> str:
    """Return the country of the specified ip address."""
    with urllib.request.urlopen(API_URL + ip + API_FORMAT) as response:
        response_data = json.loads(response.read().decode("utf-8"))
        return response_data["country_name"]


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
