#!/usr/bin/env python3
"""Replace all characters in each word with "r" until a vowel appears in it.

Title:
Scooby Doo

Description
In the popular kids show "Scooby-Doo",
the main character had a speech impediment
that makes him replace all consonants at the start of a word
until it runs into a vowel
with an "r".
For example, the word "scooby" would become "rooby".
Write a program that "Scooby doos" any word or sentence a user inputs.
You can choose to make the letter 'Y' either a consonant or a vowel.
"""
VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g",
              "h", "j", "k", "l", "m",
              "n", "p", "q", "r", "s",
              "t", "v", "w", "x", "z")


def scoobydoo(string: str) -> str:
    """Return a scooby doo version of string."""
    new_string = ""

    for word in string.split():
        skip = False

        for char in word:
            if skip is True:
                new_string += char
            elif char.lower() in VOWELS:
                new_string += char
                skip = True
            elif char.lower() in CONSONANTS:
                new_string += "r"
            else:
                new_string += char
        new_string += " "

    new_string = new_string.rstrip()
    return new_string


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        print(scoobydoo(string) + "\n")


if __name__ == "__main__":
    _start_interactively()
