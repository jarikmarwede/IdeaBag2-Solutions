#!/usr/bin/env python3
"""A program that finds the factorial to any given number.

Title:
Factorial Finder

Description:
The Factorial of a positive integer, n,
is defined as the product of the sequence n, n-1, n-2, ...1.
Also the factorial of zero, 0, is defined as being 1.
Develop a program that solves the factorial
of any user given number using both loops and recursion.
"""


def find_factorial(number: int) -> int:
    """Return factorial for specified number."""
    if number > 0:
        return number * find_factorial(number - 1)
    elif number == 0:
        return 1
    else:
        raise ValueError("Negative number")


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        number = int(input("Please type in the number "
                           "you want to get the factorial from: "))
        try:
            print(find_factorial(number))
        except ValueError:
            print(f"Invalid number: {number}")
        print("")


if __name__ == "__main__":
    _start_interactively()
