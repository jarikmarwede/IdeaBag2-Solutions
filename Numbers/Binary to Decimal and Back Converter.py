#!/usr/bin/env python3
"""
Title:
Binary to Decimal and Back Converter

Description:
Develop a program that converts a decimal number to its decimal equivalent.
For added complexity,
try adding converters to Octals and Hexadecimals too.
"""


def binary_to_decimal(number: int) -> int:
    """Return decimal version of the specified binary number
    """
    result = 0
    for index, digit in enumerate(reversed(str(number))):
        if index == 0:
            result += int(digit)
        else:
            result += index * 2 * int(digit)
    return int(result)


def decimal_to_binary(number: int) -> str:
    """Return binary version of the specified decimal number
    """
    result = bin(number)[2:]
    return result


def decimal_to_octal(number: int) -> str:
    """Return octal version of the specified decimal number
    """
    result = oct(number)[2:]
    return result


def decimal_to_hexadecimal(number: int) -> str:
    """Return hexadecimal version of the specified decimal number
    """
    result = hex(number)[2:]
    return result


if __name__ == "__main__":
    while True:
        CHOICE = input("Do you want to convert to decimal, "
                       "binary, octal or hexadecimal (dec|bin|oct|hex): ")
        NUMBER = int(input("Please type in the number "
                           "that you want to convert: "))
        if CHOICE == "dec":
            print(decimal_to_binary(NUMBER))
        elif CHOICE == "bin":
            print(binary_to_decimal(NUMBER))
        elif CHOICE == "oct":
            print(decimal_to_octal(NUMBER))
        elif CHOICE == "hex":
            print(decimal_to_hexadecimal(NUMBER))
