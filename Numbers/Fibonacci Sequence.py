#!/usr/bin/env python3
"""
Title:
Fibonacci Sequence

Description:
Develop a program that has the user enter a number.
Your program should print out the Fibonacci sequence to that number
or to the Nth number.
"""


def get_fibonacci_sequence(length: int):
    fibonacci_sequence = [0, 1]
    if length == 1:
        return fibonacci_sequence[0]
    elif length == 2:
        return fibonacci_sequence[1]
    for _ in range(0, length - 2):
        fibonacci_sequence.append(fibonacci_sequence[len(fibonacci_sequence) - 2]
                                  + fibonacci_sequence[len(fibonacci_sequence) - 1])
    return fibonacci_sequence


if __name__ == "__main__":
    while True:
        LENGTH = int(input("Please input the length of the fibonacci sequence "
                           "you want to calculate: "))
        print(get_fibonacci_sequence(LENGTH))
