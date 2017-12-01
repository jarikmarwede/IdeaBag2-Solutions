#!/usr/bin/env python3
"""
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


def guess_number(number_range: tuple) -> int:
    """Return a number in specified range
    """
    result = random.choice(range(number_range[0], number_range[1]))
    return result


if __name__ == "__main__":
    while True:
        START = int(input("Please input which number the program "
                          "should start with guessing from: "))
        END = int(input("Please input which number the program "
                        "should end with guessing from: "))
        while True:
            RANGE = (START, END)
            GUESS = guess_number(RANGE)
            print("Is the number {}?".format(GUESS))
            CHOICE = input("Or is it to high or to low? "
                           "(correct|high|low): ")
            if CHOICE == "high":
                END = GUESS
            elif CHOICE == "low":
                START = GUESS
            elif CHOICE == "correct":
                print("")
                break
