#!/usr/bin/env python3
"""Calculate Pi to any given digit.

Title:
Find Pi to the Nth digit

Description:
Develop a program that has the user enter a number.
Your program should print out Pi up to that many decimal places.
Try to keep a limit as to how far the program will go.
"""
from sympy import N, pi  # type: ignore


def get_pi_to(length: int) -> float:
    """Return the constant PI up to a specified length."""
    return float(str(N(pi, length + 2))[:-1])


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        print("To how many digits would you like to calculate Pi?")
        length = int(input())
        print(get_pi_to(length))
        print("")


if __name__ == "__main__":
    _start_interactively()
