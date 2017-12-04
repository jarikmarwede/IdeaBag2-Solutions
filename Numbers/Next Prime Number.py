#!/usr/bin/env python3
"""
Title:
Next Prime Number

Description:
Develop a program that starting at any number the user inputs,
generates the next prime number.
Ask the user for confirmation to keep going,
if it is granted print the next prime number again
otherwise quit the program.
"""


def next_prime(number: int) -> int:
    """Return the next prime number after the specified number
    """
    while True:
        number += 1
        for num in range(2, number):
            if number % num == 0 and num != number:
                break
        else:
            return number


if __name__ == "__main__":
    NUMBER = int(input("Please specify the staring number: "))
    while True:
        NUMBER = next_prime(NUMBER)
        print(NUMBER)
        CHOICE = input("Display next prime number? (y|n)")
        if CHOICE == "y":
            continue
        elif CHOICE == "n":
            break
