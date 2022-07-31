#!/usr/bin/env python3
"""Check whether a string is ordered alphabetically.

Title:
In Order

Description:
Make a program that notifies a user
if an entered word is in alphabetical order or not.
For example, 'almost' would output 'almost - in order',
'baton' would output 'baton - not in order',
'biopsy billowy chef' would output
'biopsy - in order billowy - in order chef - not in order'.
"""
ALPHABET = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
            "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
            "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
            "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
            "y": 25, "z": 26}


def is_in_order(string: str) -> bool:
    """Return whether the string is in alphabetical order."""
    counter = 0
    for char in string:
        if char in ALPHABET:
            if ALPHABET[char] < counter:
                return False
            else:
                counter = ALPHABET[char]
    return True


def check_order(string: str) -> dict:
    """Check whether the words in a string are alphabetically ordered.

    Return analysis in form:
    biopsy - in order
    billowy - in order
    chef - not in order
    """
    result = {}
    for word in string.split():
        if is_in_order(word):
            result[word] = "in order"
        else:
            result[word] = "not in order"
    return result


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        order_analysis = check_order(string)
        for string in order_analysis:
            print(string + " - " + order_analysis[string])
        print("")


if __name__ == "__main__":
    _start_interactively()
