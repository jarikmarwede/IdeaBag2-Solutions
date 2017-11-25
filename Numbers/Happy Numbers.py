#!/usr/bin/env python3
"""
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


def is_happy_number(number: int) -> bool:
    """Return whether the specified number is a happy number or not
    """
    if square_of_digits(number) == 1:
        return True
    else:
        try:
            return is_happy_number(square_of_digits(number))
        except RecursionError:
            return False


def square_of_digits(number: int) -> int:
    """Return the sum of the digits of the specified number squared
    """
    output = 0
    for digit in str(number):
        output += int(digit) * int(digit)
    return output


if __name__ == "__main__":
    HAPPY_NUMBERS = []
    CURRENT_NUMBER = 1
    while len(HAPPY_NUMBERS) < 8:
        if is_happy_number(CURRENT_NUMBER) is True:
            HAPPY_NUMBERS.append(CURRENT_NUMBER)
            CURRENT_NUMBER += 1
        else:
            CURRENT_NUMBER += 1
    print("These are the first 8 happy numbers: " + str(HAPPY_NUMBERS))
    while True:
        NUMBER = int(input("Please type in a number: "))
        print(is_happy_number(NUMBER))
