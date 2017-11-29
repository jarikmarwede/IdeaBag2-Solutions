#!/usr/bin/env python3
"""
Title:
Latin Squares

Description:
A Latin square is an n x n array filled with n different symbols 
each occuring exactly once in each row and exactly once in each column.
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
    """Return whether array is a latin square
    """
    # check horizontally
    for index, digit in enumerate(array):
        # check for beginning
        if index == 0:
            row = 1
            column = 0
            numbers = []
        # check for new row
        elif index % row_length == 0:
            row += 1
            column = 0
            numbers = []
        column += 1
        print(index, digit, column, row)
        # check whether the digit is already in the current row
        if digit in numbers:
            return False
        numbers.append(digit)

    # check vertically

    return True


if __name__ == "__main__":
    while True:
        ARRAY = input("Please type in the array"
                      " that should be checked for being a latin square: ")
        ROW_LENGTH = int(input("Please type in the length "
                               "of each row in your array: "))
        print(is_latin_square(ROW_LENGTH, ARRAY))
