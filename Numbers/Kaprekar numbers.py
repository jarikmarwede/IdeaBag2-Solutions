#!/usr/bin/env python3
"""
Title:
Kaprekar numbers

Description:
In mathematics, a Kaprekar number for a given base is a non-negative integer,
the representation of whose square in that base can be split into two parts
that add up to the original number again.
For instance, 45 is a Kaprekar number, because 45^2 = 2025 and 20+25 = 45.
The Kaprekar numbers are named after D. R. Kaprekar.
Your program will receive two integers per line
telling you the start and end of the range to scan, inclusively.
Example: '1 50'.
Your program should emit the Kaprekar numbers in that range.
From the example: 45 is the Kaprekar number in that range.
For your program focus only on base 10 numbers.
For added complexity, see if you can make it work in arbitrary bases.
"""


def is_kaprekar(number: int) -> bool:
    """Return whether the specified number is a kaprekar number
    """
    squared = str(number ** 2)
    # check whether squared has an even length
    if len(str(squared)) % 2 == 0:
        first = int(squared[:int(len(squared) / 2)])
        second = int(squared[int(len(squared) / 2):])
    # check whether squared has only one digit
    elif int(squared) < 10:
        first = 0
        second = int(squared)
    # executes when squared has an odd length
    else:
        first = int(squared[:int(len(squared) / 2)])
        second = int(squared[int(len(squared) / 2) + 1:])
    if first + second == number and second != 0:
        return True
    return False


def find_kaprekars(search_range: tuple) -> list:
    """Return all kaprekar number in the specified range
    """
    kaprekars = []
    for number in range(search_range[0], search_range[1] + 1):
        if is_kaprekar(number):
            kaprekars.append(number)
    return kaprekars


if __name__ == "__main__":
    while True:
        RANGE0 = int(input("Please specify the starting number: "))
        RANGE1 = int(input("Plese specify the ending number: "))
        print(find_kaprekars((RANGE0, RANGE1)))
