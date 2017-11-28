#!/usr/bin/env python3


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
