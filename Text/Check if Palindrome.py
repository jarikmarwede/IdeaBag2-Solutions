#!/usr/bin/env python3
"""Checks whether a string is a palindrome or not

Title: Check if Palindrome

Description:
Develop a program that checks if a string entered by a user is a palindrome.
A palindrome is a word that reads the same forwerds as backwards.
An example is "racecar" or "madam".
"""


def check_palindrome(string: str) -> bool:
    """Return whether string is a palindrome or not
    """
    reversed_string = ""
    for char in reversed(string.lower()):
        reversed_string += char
    if reversed_string == string.lower():
        return True
    return False


if __name__ == "__main__":
    STRING = input("Please input the string that should be checked: ")
    print(check_palindrome(STRING))
