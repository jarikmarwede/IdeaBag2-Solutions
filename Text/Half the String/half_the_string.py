#!/usr/bin/env python3
"""Return first half of a string.

Title:
Half the String

Description:
Make a program that prompts the user to enter a string.
If the string's length is an even number, output exactly half of it.
If it is odd, notify the user that the string is invalid.
Submitted by Ayushman Thakur (Abt)
"""


def first_half(string: str) -> str:
    """Return first half of a string."""
    if len(string) % 2 != 0:
        raise ValueError(f"Invalid string '{string}' with length {len(string)}")
    else:
        return string[:int(len(string) / 2)]


def second_half(string: str) -> str:
    """Return second half of a string."""
    if len(string) % 2 != 0:
        raise ValueError(f"Invalid string '{string}' with length {len(string)}")
    else:
        return string[int(len(string) / 2):]


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        try:
            print("First half:", first_half(string))
            print("Second half:", second_half(string))
        except ValueError as error:
            print(error)
        print("")


if __name__ == "__main__":
    _start_interactively()
