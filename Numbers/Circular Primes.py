#!/usr/bin/env python3
"""
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


def is_prime(number: int) -> bool:
    """Return whether the specified number is a prime number
    """
    if number < 1:
        return False
    for num in range(1, number):
        if number % num == 0 and number != num and num != 1:
            return False
    return True


def is_circular_prime(number: int) -> bool:
    """Return whether the specified number is a circular prime number
    """
    for index in range(0, len(str(number))):
        if not is_prime(int(str(number)[index:] + str(number)[:index])):
            return False
    return True


def circular_primes(number_range: tuple) -> list:
    """Return all circular prime number in the specified range
    """
    result = []
    for number in range(number_range[0], number_range[1]):
        if is_circular_prime(number):
            result.append(number)
    return result


if __name__ == "__main__":
    while True:
        START = int(input("Please input the starting number: "))
        END = int(input("Please input the ending number: ")) + 1
        RANGE = (START, END)
        print(*circular_primes(RANGE))
        print("")
