#!/usr/bin/env python3
"""Check whether a string is alphabetically ordered

Title: In Order

Description:
Make a program that notifies a user
if an enterd woed is in alphabetical order or not.
For example, 'almost' would output 'almost - in order',
'baton' would output 'baton - not in order',
'biopsy billowy chef' would output
'biopsy - in order billowy - in order chef - not in order'.
"""


def check_order(string: str) -> str:
    """Check whether the words in string are alphabetically ordered
    Return analysis in form:
    "biopsy - in order billowy - in order chef - not in order"
    """
    output = ""
    alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6,
                "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,
                "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
                "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
                "y": 25, "z": 26}
    for word in string.split():
        counter = 0
        for char in word:
            if char in alphabet:
                if alphabet[char] < counter:
                    output += word + " - not in order "
                    break
                else:
                    counter = alphabet[char]
        else:
            output += word + " - in order "
    output = output.rstrip()
    return output


if __name__ == "__main__":
    STRING = input("Please input a string: ")
    print(check_order(STRING))
