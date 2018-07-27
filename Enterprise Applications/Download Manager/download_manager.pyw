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
import os.path
import urllib.request
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tk_messagebox
import tkinter.filedialog as tk_filedialog
from multiprocessing.dummy import Pool as ThreadPool


class MainWindow(tk.Tk):
    """GUI class for interacting with tkinter."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Download Manager")
        self.geometry("")
        self.resizable(width=False, height=False)

        # define frames
        self.download_directory_frame = ttk.Frame(self)
        self.bottom_buttons_frame = ttk.Frame(self)

        # define other widgets
        self.urls_treeview = ttk.Treeview(self,
                                          columns=("url",),
                                          displaycolumns=("url",),
                                          show="tree")
        self.save_downloads_to_button = ttk.Button(self.download_directory_frame,
                                                   text="Save downloads to...",
                                                   command=self.change_download_directory)
        self.download_directory_entry = ttk.Entry(self.download_directory_frame,
                                                  state=tk.DISABLED,
                                                  width=100)
        self.add_url_button = ttk.Button(self.bottom_buttons_frame,
                                         text="Add URL",
                                         command=self.add_url)
        self.remove_url_button = ttk.Button(self.bottom_buttons_frame,
                                            text="Remove URL",
                                            command=self.delete_focused_url)
        self.download_button = ttk.Button(self.bottom_buttons_frame,
                                          text="Download",
                                          command=self.download_current_urls)

        self.urls_treeview.column("#0",
                                  width=0,
                                  minwidth=0)
        self.urls_treeview.column("url", width=700)

        # define bindings
        self.urls_treeview.bind("<Delete>", lambda _: self.delete_focused_url())

        self.display_widgets()
        center_window_on_screen(self)

    def display_widgets(self):
        """Places all widgets in the grid to display them."""
        self.urls_treeview.grid(row=0, column=0, padx=50, pady=50)

        self.download_directory_frame.grid(row=1, column=0, padx=10, pady=10)
        self.save_downloads_to_button.grid(row=0, column=0, padx=5)
        self.download_directory_entry.grid(row=0, column=1, padx=5)

        self.bottom_buttons_frame.grid(row=2, column=0, pady=10)
        self.add_url_button.grid(row=0, column=0, padx=5)
        self.remove_url_button.grid(row=0, column=1, padx=5)
        self.download_button.grid(row=0, column=2, padx=5)

    def add_url(self):
        """Open window for adding new urls and then add them to treeview."""
        window = NewURLWindow()

        self.wait_window(window)

        url = window.get_url()
        if url:
            self.urls_treeview.insert("", "end", values=(url,))

    def delete_focused_url(self):
        """Delete the currently focused url in the treeview."""
        url_iid = self.urls_treeview.focus()
        if url_iid:
            self.urls_treeview.delete(url_iid)

    def change_download_directory(self):
        """Change the download directory."""
        directory = tk_filedialog.askdirectory()
        if directory:
            self.download_directory_entry.config(state=tk.NORMAL)
            self.download_directory_entry.insert(0, directory)
            self.download_directory_entry.config(state=tk.DISABLED)

    def download_current_urls(self):
        """Download all currently added files."""
        downloading_urls = [self.urls_treeview.item(iid, "values")[0]
                            for iid in self.urls_treeview.get_children()]
        download_files(downloading_urls, self.downloads_finished)

    def downloads_finished(self, download_response):
        """Save the files returned by the download threads and alert user."""
        directory = self.download_directory_entry.get()
        save_file_to_directory(download_response, directory)

        tk_messagebox.showinfo("Download finished",
                               "Your downloads have finished!")


class NewURLWindow(tk.Toplevel):
    """Window for adding URLs."""

    def __init__(self):
        super().__init__()
        self.title("Add a new URL")
        self.geometry("")
        self.resizable(width=False, height=False)

        self.new_url = ""

        # define frames
        self.bottom_buttons_frame = ttk.Frame(self)

        # define other widgets
        self.url_entry = ttk.Entry(self, width=50)
        self.add_url_button = ttk.Button(self.bottom_buttons_frame,
                                         text="Add URL",
                                         command=self._set_url)
        self.cancel_button = ttk.Button(self.bottom_buttons_frame,
                                        text="Cancel",
                                        command=self.destroy)

        # define bindings
        self.url_entry.bind("<Return>", lambda _: self._set_url())

        # display widgets
        self.url_entry.grid(row=0, column=0, padx=20, pady=20)
        self.bottom_buttons_frame.grid(row=1, column=0, pady=5)
        self.add_url_button.grid(row=0, column=0, padx=5)
        self.cancel_button.grid(row=0, column=1, padx=5)

        center_window_on_screen(self)
        self.url_entry.focus_set()

    def _set_url(self):
        """Set the url and close window."""
        self.new_url = self.url_entry.get()
        self.destroy()

    def get_url(self):
        """Return the added url."""
        return self.new_url


def download_files(urls: list, callback):
    """Download files from all urls asynchronous."""
    pool = ThreadPool(len(urls))
    pool.map_async(urllib.request.urlopen, urls, callback=callback)


def save_file_to_directory(download_response, directory: str):
    """Save the specified files to the directory."""
    for response in download_response:
        url = response.geturl()
        if url.endswith("/"):
            url = url[0:-1]
        file_name = url.split("/")[-1]
        file_content = response.read()

        with open(os.path.join(directory, file_name), "wb") as file:
            file.write(file_content)


def center_window_on_screen(window):
    """Center the specified window on the screen."""
    window.update_idletasks()
    height = window.winfo_height()
    width = window.winfo_width()
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()

    x_coordinate = int(screen_width / 2 - width / 2)
    y_coordinate = int(screen_height / 2 - height / 2)

    window.geometry("".join((str(width), "x",
                             str(height), "+",
                             str(x_coordinate), "+",
                             str(y_coordinate))))


def _start_gui():
    """Start the Graphical User Interface."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_gui()
