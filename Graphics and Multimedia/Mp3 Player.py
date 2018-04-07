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
import random
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
        self.repeat = False
        self.currently_playing = tk.StringVar(self)
        self.current_index = None

        # create frames
        self.treeview_frame = ttk.Frame(self)
        self.currently_playing_frame = ttk.Frame(self)
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
        self.currently_playing_label = ttk.Label(self.currently_playing_frame,
                                                 text="Currently playing: ")
        self.current_file_label = ttk.Label(self.currently_playing_frame,
                                            text="",
                                            textvariable=self.currently_playing)
        self.play_button = ttk.Button(self.bottom_audio_buttons_frame,
                                      text="Play",
                                      command=self.play_audio)
        self.pause_resume_button = ttk.Button(self.bottom_audio_buttons_frame,
                                              text="Pause",
                                              command=self.pause_resume)
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
                                          text="Previous",
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
        self.currently_playing_frame.grid(row=1, column=0, padx=10, pady=10)
        self.bottom_audio_buttons_frame.grid(row=3, column=0, padx=10, pady=10)

        # display other widgets
        self.playlist_treeview.grid(row=0, column=0)
        self.playlist_scroll_y.grid(row=0, column=1, sticky=tk.NS)
        self.playlist_scroll_x.grid(row=1, column=0, sticky=tk.EW)
        self.currently_playing_label.grid(row=0, column=0, padx=10)
        self.current_file_label.grid(row=1, column=0, padx=10, pady=5)
        self.shuffle_playlist_button.grid(row=0, column=0, padx=5)
        self.previous_button.grid(row=0, column=1, padx=5)
        self.rewind_button.grid(row=0, column=2, padx=5)
        self.play_button.grid(row=0, column=3, padx=5)
        self.pause_resume_button.grid(row=0, column=4, padx=5)
        self.fast_forward_button.grid(row=0, column=5, padx=5)
        self.next_button.grid(row=0, column=6, padx=5)
        self.repeat_once_button.grid(row=0, column=7, padx=5)
        self.repeat_forever_checkbutton.grid(row=0, column=8, padx=5)

        # create bindings
        self.playlist_treeview.bind("<Double-Button-1>",
                                    lambda _: self.play_audio())

    def play_audio(self, file: tuple=None):
        """Play the currently selected file."""
        if not file:
            selection = self.playlist_treeview.selection()
            if selection:
                self.currently_playing.set(self.playlist_treeview.item(selection, "values")[0])
                self.current_index = self.playlist_treeview.index(selection)
        else:
            self.currently_playing.set(file[0])
            self.current_index = file[1]

    def pause_resume(self):
        """Pause the audio that is currently playing/resume playing it."""

    def fast_forward_audio(self):
        """Fast forward the current audio."""

    def rewind_audio(self):
        """Rewind the current audio."""

    def play_next_file(self):
        """Play the next file in playlist."""
        if self.repeat_forever.get():
            self.play_audio((self.currently_playing.get(),
                             self.current_index))
        elif self.repeat:
            self.play_audio((self.currently_playing.get(),
                             self.current_index))
            self.repeat = False
        else:
            new_index = self.current_index + 1
            new_item = self.playlist_treeview.get_children()[new_index]
            self.playlist_treeview.see(new_item)
            self.play_audio((self.playlist_treeview.item(new_item, "values")[0],
                             new_index))

    def play_previous_file(self):
        """Play the previous file in playlist."""

    def repeat_once(self):
        """Repeat current file once."""
        self.repeat = True

    def shuffle_playlist(self):
        """Shuffle files in current playlist randomly."""
        old_entries = self.playlist_treeview.get_children()
        entries = [self.playlist_treeview.item(entry, "values") for entry in old_entries]
        random.shuffle(entries)
        self.playlist_treeview.delete(*old_entries)
        for entry in entries:
            self.playlist_treeview.insert("", "end", values=entry)

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
