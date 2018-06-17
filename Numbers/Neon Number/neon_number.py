#!/usr/bin/env python3
"""Find neon numbers in a given range.

Title:
Neon Number

Description:
A number is said to be a Neon Number
if the sum of digits of the square of the number
is equal to the number itself.
Example- 9 is a Neon Number.
9*9=81 and 8+1=9.
Hence it is a Neon Number.
The user is prompted to input a range eg 1-90.
Your program should print out the neon numbers in that range.
Submitted by Shib Shankar Ghosh
"""


def is_neon(number: int) -> bool:
    """Return whether the specified number is a neon number."""
    square = number ** 2
    result = 0
    for digit in str(square):
        result += int(digit)
    if result == number:
        return True
    return False


def find_neons(start: int, end: int) -> list:
    """Return a list of all neon numbers in the specified range."""
    neons = []
    for number in range(start, end + 1):
        if is_neon(number):
            neons.append(number)
    return neons


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        start = int(input("Please enter the starting number: "))
        end = int(input("Please enter the ending number: "))
        print(str(find_neons(start, end)) + "\n")


if __name__ == "__main__":
    _start_interactively()
