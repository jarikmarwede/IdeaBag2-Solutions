#!/usr/bin/env python3
"""Remove vowels and whitespace from a string.
Then return the string that is left
with all vowels added to the end of it.

Title:
Disemvoweler

Description:
Make a program that removes every vowel and whitespace found in a string.
It should output the resultinng disemvoweled string
with the removed vowels concatenated to the end of it.
For example 'Hello world' outputs 'hllwrld eoo'.
"""


def disemvowel(string: str) -> str:
    """Return disemvoweled version of string
    """
    new_string = ""
    extra_chars = " "
    vowels = ("a", "e", "i", "o", "u")
    for char in string:
        if char.lower() in vowels:
            extra_chars += char
        elif char.isspace():
            pass
        else:
            new_string += char
    new_string += extra_chars
    return new_string


if __name__ == "__main__":
    while True:
        STRING = input("Please input a string: ")
        print(disemvowel(STRING))
