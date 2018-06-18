#!/usr/bin/env python3
"""Checks whether a string is a palindrome or not.

Title:
Check if Palindrome

Description:
Develop a program that checks if a string entered by a user is a palindrome.
A palindrome is a word that reads the same forwerds as backwards.
An example is "racecar" or "madam".
"""


def is_palindrome(string: str) -> bool:
    """Return whether string is a palindrome or not."""
    if "".join(reversed(string)).lower() == string.lower():
        return True
    return False


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input the string that should be checked: ")
        palindrome = is_palindrome(string)
        if palindrome:
            print(f"'{string}' is a palindrome!")
        else:
            print(f"'{string}' is not a palindrome!")
        print("")


if __name__ == "__main__":
    _start_interactively()
