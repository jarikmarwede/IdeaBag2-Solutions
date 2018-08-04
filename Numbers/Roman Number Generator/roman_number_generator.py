#!/usr/bin/env python3
"""Convert arabic numbers to roman numbers.

Title:
Roman Number Generator

Description:
Develop a program that accepts an integer
and outputs the Roman Number equivalent of that number.
Examples:
4 - IV
12 - XII
20 - XX
Submitted by SoReNa
"""


def arabic_to_roman(number: int) -> str:
    """Return roman version of the specified arabic number."""
    if number > 3999:
        raise ValueError(f"Number can not be represented with roman numerals: "
                         f"{number}")
    roman_number = ""

    for index, digit in enumerate(reversed(str(number))):
        if index == 0:
            first = "I"
            fifth = "V"
            tenth = "X"
        elif index == 1:
            first = "X"
            fifth = "L"
            tenth = "C"
        elif index == 2:
            first = "C"
            fifth = "D"
            tenth = "M"
        elif index == 3:
            first = "M"
            fifth = ""
            tenth = ""
        else:
            raise ValueError(f"Invalid input: {number}")

        if digit == "0":
            continue
        elif digit == "1":
            roman_number = first + roman_number
        elif digit == "2":
            roman_number = first * 2 + roman_number
        elif digit == "3":
            roman_number = first * 3 + roman_number
        elif digit == "4":
            roman_number = first + fifth + roman_number
        elif digit == "5":
            roman_number = fifth + roman_number
        elif digit == "6":
            roman_number = fifth + first + roman_number
        elif digit == "7":
            roman_number = fifth + first * 2 + roman_number
        elif digit == "8":
            roman_number = fifth + first * 3 + roman_number
        elif digit == "9":
            roman_number = first + tenth + roman_number
    return roman_number


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        number = int(input("Please type in the number "
                           "you want to convert: "))
        print(arabic_to_roman(number))
        print("")


if __name__ == "__main__":
    _start_interactively()
