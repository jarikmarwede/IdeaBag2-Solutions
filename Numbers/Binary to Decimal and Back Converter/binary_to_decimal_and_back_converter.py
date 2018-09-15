#!/usr/bin/env python3
"""A converter between multiple numeral systems.

Title:
Binary to Decimal and Back Converter

Description:
Develop a program that converts a decimal number to binary
or a binary number to its decimal equivalent.
For added complexity,
try adding converters to Octals and Hexadecimals too.
"""
import math


def binary_to_decimal(number: int) -> int:
    """Return decimal version of the specified binary number."""
    result = 0

    for index, digit in enumerate(reversed(str(number))):
        if index == 0:
            result += int(digit)
        else:
            result += 2 ** index * int(digit)
    return int(result)


def decimal_to_binary(number: int) -> int:
    """Return binary version of the specified decimal number."""
    binary_list = []

    while number > 1:
        current_number = 2
        while True:
            if current_number * 2 > number:
                break
            current_number *= 2
        binary_list.append(current_number)
        number -= current_number
    if number > 0:
        binary_list.append(1)
        number -= 1

    result = int(math.log(max(binary_list), 2) + 1) * "0"
    for digit in binary_list:
        if digit == 1:
            result = result[:-1] + "1"
        else:
            result = result[:-int(math.log(digit, 2)) - 1] + "1" + result[-int(math.log(digit, 2)):]
    return int(result)


def decimal_to_octal(number: int) -> int:
    """Return octal version of the specified decimal number."""
    result = int(oct(number)[2:])
    return result


def decimal_to_hexadecimal(number: int) -> str:
    """Return hexadecimal version of the specified decimal number."""
    result = hex(number)[2:]
    return result


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        choice = input("Do you want to convert to decimal, "
                       "binary, octal or hexadecimal (dec|bin|oct|hex): ")
        number = int(input("Please type in the number "
                           "that you want to convert: "))

        if choice == "dec":
            print(binary_to_decimal(number))
        elif choice == "bin":
            print(decimal_to_binary(number))
        elif choice == "oct":
            print(decimal_to_octal(number))
        elif choice == "hex":
            print(decimal_to_hexadecimal(number))


if __name__ == "__main__":
    _start_interactively()
