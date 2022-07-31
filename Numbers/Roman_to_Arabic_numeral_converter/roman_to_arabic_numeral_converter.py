#!/usr/bin/env python3
"""
Title:
Roman to Arabic numeral converter

Description:
Create a program that converts Roman numbers (such as MCMLIV)
to Arabic numbers (1954) and back.
Roman numerals are read from left to right,
as you add or subtract the value of each symbol.
If a value is lower than the following value, it will be subtracted.
Otherwise it will be added.
For example,
we want to convert the Roman numeral MCMLIV to an Arabic number:
M = 1000 must be added, because the following letter C = 100 is lower.
C = 100 must be subtracted because the following letter M = 1000 is greater.
M = 1000 must be added, because the following letter L = 50 is lower.
L = 50 must be added, because the following letter I = 1 is lower.
I = 1 must be subtracted, because the following letter V = 5 is greater.
V = 5 must be added, because there are no more symbols left.
We can now calculate the number:
1000 - 100 + 1000 + 50 - 1 + 5 = 1954
Submitted by Alex Lushiku
"""


def convert_to_arabic(number: str) -> int:
    """Return arabic version of number."""
    result = 0
    roman_digits = {"M": 1000,
                    "D": 500,
                    "C": 100,
                    "L": 50,
                    "X": 10,
                    "V": 5,
                    "I": 1}

    for index, character in enumerate(number):
        if character in roman_digits:
            if index == len(number) - 1:
                result += roman_digits[character]
            elif roman_digits[character] >= roman_digits[number[index + 1]]:
                result += roman_digits[character]
            else:
                result -= roman_digits[character]
    return result


def convert_to_roman(number: int) -> str:
    """Return roman version of number."""
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
        arabic_or_roman = input("Do you want to convert"
                                " to arabic or roman (arabic|roman): ")
        number = input("Please input the number you want to convert: ")
        if arabic_or_roman == "arabic":
            print(convert_to_arabic(number))
        elif arabic_or_roman == "roman":
            print(convert_to_roman(int(number)))
        print("")


if __name__ == "__main__":
    _start_interactively()
