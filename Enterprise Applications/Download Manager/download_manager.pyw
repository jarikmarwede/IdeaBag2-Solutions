#!/usr/bin/env python3
"""

Title:
Download Manager

Description:
Allow your program to download various files
and each one is downloading in the background on a separate thread.
The main thread will keep track of the other thread’s progress
and notify the user when downloads are completed.
"""
import urllib.request
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tk_messagebox
import tkinter.filedialog as tk_filedialog
import tkinter.colorchooser as tk_colorchooser
from multiprocessing.dummy import Pool as ThreadPool


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("")
        self.geometry("")
        self.resizable(width=True, height=True)


def download_files(urls: list, callback):
    pool = ThreadPool(len(urls))
    pool.map_async(urllib.request.urlopen, urls, callback=callback)
    pool.close()
    pool.join()


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
