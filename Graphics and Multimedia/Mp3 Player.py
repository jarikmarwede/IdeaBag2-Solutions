#!/usr/bin/env python3
"""

Title:
Mp3 Player (and Other Formats)

Description:
A simple program for playing your favorite music files.
It should have the ability to Play, Pause, Fast Forward,
Rewind, Next, Previous, Repeat Once, Repeat Forever and Randomly Shuffle.
For extra complexity
see if you can add the ability to create playlists and an equalizer.
You could also generate a Like/Dislike playlist
by rating songs based on if a song is skipped or played to the end
or if the volume is increased/decreased whilst the song is being played.
"""
import os
import tkinter as tk
from tkinter import filedialog, ttk


class MainWindow(tk.Tk):
    """Tkinter root window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Mp3 Player")
        self.resizable(width=False, height=False)

        # define variables
        self.repeat_forever = tk.BooleanVar(self,
                                            value=False)

        # create frames
        self.treeview_frame = ttk.Frame(self)
        self.bottom_audio_buttons_frame = ttk.Frame(self)

        # create other widgets
        self.playlist_treeview = ttk.Treeview(self.treeview_frame,
                                              columns=("filename",),
                                              selectmode="browse",
                                              show="tree")
        self.playlist_scroll_x = ttk.Scrollbar(self.treeview_frame,
                                               command=self.playlist_treeview.xview,
                                               orient=tk.HORIZONTAL)
        self.playlist_scroll_y = ttk.Scrollbar(self.treeview_frame,
                                               command=self.playlist_treeview.yview,)
        self.playlist_treeview["xscrollcommand"] = self.playlist_scroll_x.set
        self.playlist_treeview["yscrollcommand"] = self.playlist_scroll_y.set
        self.current_file_label = ttk.Label(self,
                                            text="Currently playing: ")
        self.play_pause_button = ttk.Button(self.bottom_audio_buttons_frame,
                                            text="Play",
                                            command=self.play_pause_audio)
        self.fast_forward_button = ttk.Button(self.bottom_audio_buttons_frame,
                                              text="Fast forward",
                                              command=self.fast_forward_audio)
        self.rewind_button = ttk.Button(self.bottom_audio_buttons_frame,
                                        text="Rewind",
                                        command=self.rewind_audio)
        self.next_button = ttk.Button(self.bottom_audio_buttons_frame,
                                      text="Next",
                                      command=self.play_next_file)
        self.previous_button = ttk.Button(self.bottom_audio_buttons_frame,
                                          text="previous",
                                          command=self.play_previous_file)
        self.repeat_once_button = ttk.Button(self.bottom_audio_buttons_frame,
                                             text="Repeat once",
                                             command=self.repeat_once)
        self.repeat_forever_checkbutton = ttk.Checkbutton(self.bottom_audio_buttons_frame,
                                                          text="Repeat forever",
                                                          variable=self.repeat_forever)
        self.shuffle_playlist_button = ttk.Button(self.bottom_audio_buttons_frame,
                                                  text="Shuffle",
                                                  command=self.shuffle_playlist)
        self.main_menu = tk.Menu(self,
                                 tearoff=0)
        self.file_sub_menu = tk.Menu(self.main_menu,
                                     tearoff=0)

        # configure playlist_treeview
        self.playlist_treeview.column("#0",
                                      minwidth=0,
                                      width=0)
        self.playlist_treeview.column("filename",
                                      width=500)
        self.playlist_treeview.heading("filename",
                                       text="Filename",
                                       anchor=tk.CENTER)

        # configure main menu
        self.config(menu=self.main_menu)
        self.main_menu.add_cascade(menu=self.file_sub_menu,
                                   label="File")

        # configure file sub menu
        self.file_sub_menu.add_command(label="Open file(s)",
                                       command=self.open_file)
        self.file_sub_menu.add_command(label="Open playlist",
                                       command=self.open_playlist)
        self.file_sub_menu.add_separator()
        self.file_sub_menu.add_command(label="Exit",
                                       command=self.destroy)

        # display frames
        self.treeview_frame.grid(row=0, column=0, padx=10, pady=10)
        self.bottom_audio_buttons_frame.grid(row=2, column=0, padx=10, pady=10)

        # display other widgets
        self.playlist_treeview.grid(row=0, column=0)
        self.playlist_scroll_y.grid(row=0, column=1, sticky=tk.NS)
        self.playlist_scroll_x.grid(row=1, column=0, sticky=tk.EW)
        self.current_file_label.grid(row=1, column=0, padx=10, pady=10)
        self.shuffle_playlist_button.grid(row=0, column=0, padx=5)
        self.previous_button.grid(row=0, column=1, padx=5)
        self.rewind_button.grid(row=0, column=2, padx=5)
        self.play_pause_button.grid(row=0, column=3, padx=5)
        self.fast_forward_button.grid(row=0, column=4, padx=5)
        self.next_button.grid(row=0, column=5, padx=5)
        self.repeat_once_button.grid(row=0, column=6, padx=5)
        self.repeat_forever_checkbutton.grid(row=0, column=7, padx=5)

    def play_pause_audio(self):
        """Play the audio if paused otherwise pause."""

    def fast_forward_audio(self):
        """Fast forward the current audio."""

    def rewind_audio(self):
        """Rewind the current audio."""

    def play_next_file(self):
        """Play the next file in playlist."""

    def play_previous_file(self):
        """Play the previous file in playlist."""

    def repeat_once(self):
        """Repeat current file once."""

    def shuffle_playlist(self):
        """Shuffle files in current playlist randomly."""

    def open_file(self):
        """Open new audio file."""
        files = filedialog.askopenfilenames(defaultextension=".mp3",
                                            filetypes=[("Mp3", "*.mp3")],
                                            parent=self)
        for file in files:
            file_name = os.path.basename(file)
            self.playlist_treeview.insert("", "end", values=(file_name,))

    def open_playlist(self):
        """Open all audio files in a folder as a playlist."""
        directory = filedialog.askdirectory(parent=self)
        for file in os.listdir(directory):
            if file.endswith(".mp3"):
                file_name = os.path.basename(file)
                self.playlist_treeview.insert("", "end", values=(file_name,))


def _start_window():
    """Start the tkinter GUI."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_window()
