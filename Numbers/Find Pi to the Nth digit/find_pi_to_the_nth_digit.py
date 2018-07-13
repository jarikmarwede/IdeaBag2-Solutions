#!/usr/bin/env python3
"""Calculate Pi to any given digit.

Title:
Find Pi to the Nth digit

Description:
Develop a program that has the user enter a number.
Your program should print out Pi up to that many decimal places.
Try to keep a limit as to how far the program will go.
"""
from sympy import N, pi


def _start_interactively():
    while True:
        print("To how many digits would you like to calculate Pi?")
        length = input()
        print(N(pi, length))


if __name__ == "__main__":
    _start_interactively()
