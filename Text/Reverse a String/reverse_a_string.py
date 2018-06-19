#!/usr/bin/env python3
"""Reverse a string.

Title:
Reverse a String

Description:
Develop a program that has the user enter a string.
Your program should reverse the string and print it out.
"""


def reverse(string: str) -> str:
    """Return the string reversed."""
    reversed_string = ""
    for index in range(len(string) - 1, -1, -1):
        reversed_string += string[index]
    return reversed_string


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        print(reverse(string) + "\n")


if __name__ == "__main__":
    _start_interactively()
