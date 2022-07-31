#!/usr/bin/env python3
"""Find the least and greatest common denominator of two fractions.

Title:
Least/Greatest Common Denominator

Description:
Create a program that asks the user to enter two fractions.
Have the program find the least common or the greatest common denominator
between those two fractions and print it out.
"""


def least_common_multiple(number1: int, number2: int) -> int:
    """Return least common multiple of number1 and number2."""
    start1 = number1
    start2 = number2

    while number1 != number2:
        if number1 < number2:
            number1 += start1
        elif number2 < number1:
            number2 += start2
    return number1


def greatest_common_divisor(number1: int, number2: int) -> int:
    """Return greatest common divisor of number1 and number2."""
    if number1 < number2:
        divisor = number1
    else:
        divisor = number2
    while divisor > 0:
        if number1 % divisor == 0 and number2 % divisor == 0:
            break
        divisor -= 1
    return divisor


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        fraction1 = input("Please input the first fraction (eg. 2/3): ")
        fraction2 = input("Please input the second fraction (eg. 4/7): ")
        number1 = int(fraction1.split("/")[-1])
        number2 = int(fraction2.split("/")[-1])
        print("Least Common Denominator:",
              least_common_multiple(number1, number2))
        print("Greatest Common Divisor:",
              greatest_common_divisor(number1, number2))
        print("")


if __name__ == "__main__":
    _start_interactively()
