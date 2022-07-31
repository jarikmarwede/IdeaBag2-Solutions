#!/usr/bin/env python3
"""Find the next prime number for any given number.

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
    """Return the next prime number after the specified number."""
    while True:
        number += 1
        for num in range(2, number):
            if number % num == 0 and num != number:
                break
        else:
            return number


def _start_interactively():
    """Start the program interactively through the command line."""
    number = int(input("Please specify the staring number: "))
    while True:
        number = next_prime(number)
        print(str(number) + "\n")
        choice = input("Display next prime number? (y|n)")
        if choice == "y":
            continue
        elif choice == "n":
            break


if __name__ == "__main__":
    _start_interactively()
