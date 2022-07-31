#!/usr/bin/env python3
"""Count vowels used in a string.

Title:
Count Vowels

Description:
Develop a program that has the user enter a string.
Your program counts the number of vowels in the text
and prints it out.
For added complexity,
have it report a sum of each vowel found
and its position/index in the string.
"""
VOWELS = ("a", "e", "i", "o", "u")


def count_vowels(string: str):
    """Analyze vowels in string and print out results."""
    vowel_count = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    for index, character in enumerate(string):
        for vowel in VOWELS:
            if character.lower() == vowel:
                vowel_count[vowel] += 1
                print(f"{vowel} found at index {index}")

    total_vowels = 0
    for vowel in VOWELS:
        total_vowels += vowel_count[vowel]

    print("\nSummary")
    print(f"Total amount of vowels: {total_vowels}")
    for vowel in VOWELS:
        print(f"Total amount of {vowel}s: {vowel_count[vowel]}")


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        print("")
        count_vowels(string)
        print("")


if __name__ == "__main__":
    _start_interactively()
