#!/usr/bin/env python3
"""Translate to and from Rovarspraket.

Title:
Rovarspraket

Description:
Rovarspraket which means "Robber's language" in Swedish
is not very complicated.
You take an ordinary word and replace the consonants
with the consonant doubled with an 'o' between them.
For example 'b' becomes 'bob', 'm' becomes 'mom'.
Vowels are left intact.
Make a program that translates any length of string into Rovarspraket.
For added difficulty,
make it able to translate to and from Rovarspraket.
"""
VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
              "n", "p", "q", "r", "s", "t", "v", "x", "z")


def translate_to(string: str) -> str:
    """Return string translated to Rovarspraket."""
    new_string = ""

    for index, char in enumerate(string):
        if char.lower() in CONSONANTS:
            new_string += "".join((char, "o", char))
        elif char == "w":
            if index < 0:
                if char == "w" and string[index - 1].lower() in VOWELS:
                    new_string += "w"
                else:
                    new_string += "wow"
            else:
                new_string += "wow"
        else:
            new_string += char
    return new_string


def translate_from(string: str) -> str:
    """Return string translated from Rovarspraket."""
    new_string = ""
    skip = 0

    for index, char in enumerate(string):
        if skip > 0:
            skip -= 1
            continue
        if index < len(string) - 2:
            if (char.lower() in CONSONANTS and
                    string[index + 1] == "o" and
                    string[index + 2] == char):
                new_string += char
                skip = 2
            elif index != 0:
                if (char.lower() == "w" and
                        string[index - 1].lower() not in VOWELS and
                        string[index + 1] == "o" and
                        string[index + 2] == char):
                    new_string += char
                    skip = 2
                else:
                    new_string += char
            else:
                new_string += char
        else:
            new_string += char
    return new_string


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        rovarspraket = translate_to(string)
        print("Rovarspraket:", rovarspraket)
        print("Translated back:", translate_from(rovarspraket) + "\n")


if __name__ == "__main__":
    _start_interactively()
