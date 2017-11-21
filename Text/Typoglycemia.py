#!/usr/bin/env python3
"""

Title:
Typoglycemia

Description:
Make a program that accepts a string
and outputs the typoglycemic version of it.
Typoglycemia is the minds's ability to decipher a mispelled word
if the first and last letters of the word are correct.
For example, an input of 'I deciphered a mispelled word'
yields 'I dceipehers a msiepeelld wrod'.
"""
import random


def misspell(string: str) -> str:
    """Return typoglycemic version of string
    """
    new_string = ""
    alphabet = ("a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z")
    for word in string.split():
        chars = []
        first = ""
        last = ""
        characters = ""
        for index, char in enumerate(word):
            if index == 0:
                first = char
                continue
            if char in alphabet:
                last = char
                chars.append(char)
            else:
                characters += char
        middle = ""
        for _ in range(0, len(chars)):
            middle += random.choice(chars)
        new_word = first + middle + last + characters
        new_string += new_word + " "
    new_string = new_string.rstrip()
    return new_string


if __name__ == "__main__":
    while True:
        STRING = input("Please input a string: ")
        print(misspell(STRING))
