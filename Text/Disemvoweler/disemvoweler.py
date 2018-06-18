#!/usr/bin/env python3
"""Remove vowels and whitespace from a string and put the vowels at the end.

Title:
Disemvoweler

Description:
Make a program that removes every vowel and whitespace found in a string.
It should output the resulting disemvoweled string
with the removed vowels concatenated to the end of it.
For example 'Hello world' outputs 'hllwrld eoo'.
"""
VOWELS = ("a", "e", "i", "o", "u")


def disemvowel(string: str) -> str:
    """Return disemvoweled version of string."""
    new_string = ""
    extra_chars = " "

    for char in string:
        if char.lower() in VOWELS:
            extra_chars += char
        elif char.isspace():
            pass
        else:
            new_string += char
    new_string += extra_chars
    return new_string


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        print(disemvowel(string) + "\n")


if __name__ == "__main__":
    _start_interactively()
