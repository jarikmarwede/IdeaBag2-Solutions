#!/usr/bin/env python3
"""A small lotto game.

Title:
Lotto

Description:
Create a program which asks for 6 numbers in the range 1-49.
The program should then display 6 random numbers form the same range
and check how many numbers the user guessed correctly.
For added complexity, make the program into a mini-game.
Allow the user to retry the lotto, show their payout after each round,
their highest payout etc.
Feel free to add as much complexity as you want.
Submitted by Filipekczek7
"""
import random


def gamble() -> list:
    """Return a list of 6 random integers in the range of 1-49."""
    result = random.choices(range(1, 50), k=6)
    return result


def lotto(guesses: list) -> int:
    """Return number of right guesses."""
    result = gamble()
    right = 0

    for guess in guesses:
        if guess in result:
            right += 1
    return right


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        raw_guesses = input("Please input your guesses "
                            "separated by commas: ")
        guesses = []
        for index, guess in enumerate(raw_guesses.split(",")):
            if index >= 6:
                break
            guesses.append(int(guess))
        print("Right guesses:", lotto(guesses), "\n")


if __name__ == "__main__":
    _start_interactively()
