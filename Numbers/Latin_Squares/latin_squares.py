#!/usr/bin/env python3
"""Checks for latin squares.

Title:
Latin Squares

Description:
A Latin square is an n x n array filled with n different symbols 
each occurring exactly once in each row and exactly once in each column.
For example
1
And,
1 2
2 1
are both valid Latin squares.
For this program you have to check whether a given array is a Latin square.
If it is a Latin square, then display true otherwise display false.
The user will provide two inputs:
1. n - The length of a row in the array
2. A string representing the array of symbols
Example input
5
1234551234451233451223451
2
1334
4
1234132423414321
Example output
true
false
false
"""


def is_latin_square(row_length: int, array: str) -> bool:
    """Return whether array is a latin square."""
    return _is_latin_square_horizontally(row_length, array) \
        and _is_latin_square_vertically(row_length, array)


def _is_latin_square_horizontally(row_length: int, array: str) -> bool:
    """Return whether array is a latin square just through horizontal checking."""
    row = 1
    column = 0
    numbers = []

    for index, digit in enumerate(array):
        # check for new row
        if index % row_length == 0:
            row += 1
            column = 0
            numbers = []
        column += 1
        # check whether the digit is already in the current row
        if digit in numbers:
            return False
        numbers.append(digit)

    return True


def _is_latin_square_vertically(row_length: int, array: str) -> bool:
    """Return whether array is a latin square just through vertical checking."""
    for column in range(0, row_length):
        numbers = []
        for row in range(0, len(array) // row_length):
            digit = array[row * row_length + column]
            # check whether the digit is already in the current row
            if digit in numbers:
                return False
            numbers.append(digit)

    return True


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        array = input("Please type in the array"
                      " that should be checked for being a latin square: ")
        row_length = int(input("Please type in the length "
                               "of each row in your array: "))
        print(is_latin_square(row_length, array))
        print("")


if __name__ == "__main__":
    _start_interactively()
