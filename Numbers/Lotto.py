#!/usr/bin/env python3
"""
Title:
Lotto

Description:
Create a program which asks for 6 numbers in the range 1-49.
The program should then display 6 random numbers form the same range
and check how many numbers the user guessed correctly.
For added complexity, make the program into a mini-game.
Allow the user to retry the lotto, show their payout after each round,
their highest payout after each round, their hoghest payout etc.
Feel free to add as much complexity as you want.
Submitted by Filipekczek7
"""
import random


def gamble() -> list:
    """Return a list of 6 random integers in the range of 1-49
    """
    result = random.choices(range(1, 50), k=6)
    return result


def lotto(guesses: list) -> int:
    """Return number of right guesses
    """
    result = gamble()
    right = 0
    for guess in guesses:
        if guess in result:
            right += 1
    return right


if __name__ == "__main__":
    while True:
        RAW_GUESSES = input("Please input your guesses "
                            "separated by commas: ")
        GUESSES = []
        for GUESS in RAW_GUESSES.split(","):
            GUESSES.append(int(GUESS))
        print(lotto(GUESSES))
