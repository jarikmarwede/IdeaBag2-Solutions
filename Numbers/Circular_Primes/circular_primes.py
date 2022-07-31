#!/usr/bin/env python3
"""Find all circular primes in any given range.

Title:
Circular Primes

Description:
A number is a circular prime if all of its cycles are also primes.
To cycle a number just take its first digit and stick it on its end.
For example, 197 -> 971 -> 719 -> 197.
Make a program that takes in a input of a number
and outputs if the given number is a circular prime.
The output should look something like:
INPUT 197 -> OUTPUT [971 -> 719 -> 197] - Valid/Invalid
For added complexity,
allow the program to accept two numbers
and output all the circular primes between them, inclusive.
You could choose to format the output for each circular prime
just like in the example above.
Also you could try to do the cycling part
purely mathematically - without converting to a string and slicing it.
Submitted by Lovecraft
"""
from typing import Generator


def is_prime(number: int) -> bool:
    """Return whether the specified number is a prime number."""
    if number <= 1:
        return False
    for num in range(1, number):
        if number % num == 0 and number != num and num != 1:
            return False
    return True


def is_circular_prime(number: int) -> bool:
    """Return whether the specified number is a circular prime number."""
    for index in range(0, len(str(number))):
        if not is_prime(int(str(number)[index:] + str(number)[:index])):
            return False
    return True


def circular_primes(start: int, end: int) -> Generator[int, None, None]:
    """Return all circular prime numbers in the specified range."""
    for number in range(start, end):
        if is_circular_prime(number):
            yield number


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        start = int(input("Please input the starting number: "))
        end = int(input("Please input the ending number: ")) + 1
        print(*circular_primes(start, end))
        print("")


if __name__ == "__main__":
    _start_interactively()
