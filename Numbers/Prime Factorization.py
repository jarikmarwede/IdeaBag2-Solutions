#!/usr/bin/env python3
"""Calculates the prime factors of any given number.

Title:
Prime Factorization

Description:
Develop a program that has the user enter a number
and find all the Prime Factors (if there are any) and display them.
"""


def find_prime_factors(number: int) -> list:
    """Return all prime factors of the specified number."""
    for num in range(2, number):
        if number % num == 0 and num != number:
            break
    else:
        return [number]

    for num in range(2, number):
        if number % num == 0:
            for num2 in range(2, num):
                if num % num2 == 0 and num2 != num:
                    break
            else:
                return [num, *find_prime_factors(int(number / num))]


def _start_interactively():
    """Start the program interactively."""
    number = int(input("Please enter the number "
                       "you want the prime factors of: "))
    print(f"The prime factors of {number} are: {find_prime_factors(number)}")


if __name__ == "__main__":
    _start_interactively()
