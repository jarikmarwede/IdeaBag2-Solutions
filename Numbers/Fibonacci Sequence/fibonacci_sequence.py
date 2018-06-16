#!/usr/bin/env python3
"""A program for calculating the fibonacci sequence.

Title:
Fibonacci Sequence

Description:
Develop a program that has the user enter a number.
Your program should print out the Fibonacci sequence to that number
or to the Nth number.
"""


def get_fibonacci_sequence(length: int) -> list:
    """Return the fibonacci sequence to the specified length."""
    fibonacci_sequence = [0, 1]
    if length == 1:
        return [fibonacci_sequence[0], ]
    elif length == 2:
        return fibonacci_sequence
    for _ in range(0, length - 2):
        second_to_last = fibonacci_sequence[-2]
        last = fibonacci_sequence[-1]
        fibonacci_sequence.append(second_to_last + last)
    return fibonacci_sequence


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        length = int(input("Please input the length of the fibonacci sequence "
                           "you want to calculate: "))
        print(str(get_fibonacci_sequence(length)) + "\n")


if __name__ == "__main__":
    _start_interactively()
