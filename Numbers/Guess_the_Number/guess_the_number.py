#!/usr/bin/env python3
"""A number guessing game.

Title:
Guess the Number

Description:
Your program asks the user to guess a number
and keep it in their head.
It then asks the user to input a range
that would dictate the maximum and minimum range
your program should guess the number from.
If your program guesses too high or too low,
the user should be able to input "too high or "too low"
to notify you to fix your guess.
Submitted by Sebastien Cadot
"""
import random


def guess_number(start: int, end: int) -> int:
    """Return a number in specified range."""
    result = random.choice(range(start, end + 1))
    return result


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        start = int(input("Please input which number the program "
                          "should start with guessing from: "))
        end = int(input("Please input which number the program "
                        "should end with guessing from: "))
        while True:
            guess = guess_number(start, end)
            print(f"Is the number {guess}?")
            choice = input("Or is it to high or to low? "
                           "(correct|high|low): ")
            if choice == "high":
                end = guess
            elif choice == "low":
                start = guess
            elif choice == "correct":
                print("")
                break


if __name__ == "__main__":
    _start_interactively()
