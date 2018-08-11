#!/usr/bin/env python3
"""A pig latin translator.

Title:
Pig Latin

Description:
Pig Latin is a game of alterations played on the English language game.
To create the pig latin form of a word
the initial consonant sound is transposed to the end of the word
and an 'ay' is affixed.
Example: "banana" would yield 'ananabay'.
Make a program that converts a word or a sentence to Pig Latin.
For added difficulty,
if users input only numbers notify them of a translation error.
"""


def translate_to(string: str) -> str:
    """Return pig latin version of string."""
    vowels = ("a", "e", "i", "o", "u")
    consonants = ("b", "c", "d", "f", "g",
                  "h", "j", "k", "l", "m",
                  "n", "p", "q", "r", "s",
                  "t", "v", "w", "x", "z")
    translated = ""

    for word in string.split():
        contains_letters = False
        skip = False
        beginning = ""

        for character in word:
            if skip is False:
                if character in consonants:
                    contains_letters = True
                    beginning += character
                elif character in vowels:
                    skip = True
                    contains_letters = True
                    translated += character
                else:
                    translated += character
            elif skip is True:
                translated += character
        if contains_letters is True:
            translated += beginning + "ay"
        translated += " "
    translated = translated.rstrip()
    if translated == string:
        raise ValueError(f"Nothing to translate in: {string}")
    return translated


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input the string you want to have translated: ")
        try:
            translated = translate_to(string)
        except ValueError:
            print(f"'{string}' doesn't have any words to translate")
        else:
            print(translated)


if __name__ == "__main__":
    _start_interactively()
