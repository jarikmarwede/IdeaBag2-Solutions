#!/usr/bin/env python3
"""A program to find happy numbers.

Title:
Happy Numbers

Description:
A happy number is defined by the following process.
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
Find the first 8 happy numbers.
"""
from typing import Generator


def is_happy_number(number: int) -> bool:
    """Return whether the specified number is a happy number or not."""
    if square_of_digits(number) == 1:
        return True
    else:
        try:
            return is_happy_number(square_of_digits(number))
        except RecursionError:
            return False


def square_of_digits(number: int) -> int:
    """Return the sum of the digits of the specified number squared."""
    output = 0

    for digit in str(number):
        output += int(digit) * int(digit)
    return output


def find_happy_numbers(amount: int) -> Generator[int, None, None]:
    """Return happy numbers up to the given amount."""
    happy_numbers = 0
    current_number = 1

    while happy_numbers < amount:
        if is_happy_number(current_number):
            yield current_number
            current_number += 1
            happy_numbers += 1
        else:
            current_number += 1


def _start_interactively():
    """Start the program interactively from the command line."""
    print("These are the first 8 happy numbers:",
          *find_happy_numbers(8))

    while True:
        number = int(input("Please type in a number: "))
        happy_number = is_happy_number(number)
        if happy_number:
            print(f"{number} is a happy number")
        else:
            print(f"{number} is not a happy number")


if __name__ == "__main__":
    _start_interactively()
