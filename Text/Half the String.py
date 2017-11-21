#!/usr/bin/env python3
"""Return first half of a string

Title:
Half the String

Description:
Make a program that prompts the user to enter a string.
If the string's length is an even number, output exactly half of it.
If it is odd, notify the user that the string is invalid.
Submitted by Ayushman Thakur (Abt)
"""


def string_half(string: str) -> str:
    """Return first half of string
    """
    if len(string) % 2 != 0:
        raise ValueError("Invalid string '{}' with length {}"
                         .format(string, len(string)))
    else:
        return string[:int(len(string) / 2)]


if __name__ == "__main__":
    while True:
        STRING = input("Please input a string: ")
        try:
            print(string_half(STRING))
            print("")
        except ValueError as e:
            print(e)
            print("")
