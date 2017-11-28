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
    """Return arabic version of number
    """
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


def convert_to_roman(number: int):
    """Return roman version of number
    """
    pass


if __name__ == "__main__":
    while True:
        ARABIC_OR_ROMAN = input("Do you want to convert"
                                " to arabic or roman (arabic|roman): ")
        NUMBER = input("Please input the number you want to convert: ")
        if ARABIC_OR_ROMAN == "arabic":
            print(convert_to_arabic(NUMBER))
        elif ARABIC_OR_ROMAN == "roman":
            print(convert_to_roman(int(NUMBER)))
