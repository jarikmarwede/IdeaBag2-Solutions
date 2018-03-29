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
import tkinter as tk
from tkinter import ttk


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
        self.bottom_audio_buttons_frame = ttk.Frame(self)

        # create other widgets
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

        # display frames
        self.bottom_audio_buttons_frame.grid(padx=10, pady=10)

        # display other widgets
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


def _start_window():
    """Start the tkinter GUI."""
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    _start_window()
