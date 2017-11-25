#!/usr/bin/env python3
"""
Title:
Coin Flip Simulation

Description:
Write some code that simulates flipping a single coin
however many times the user decides.
The code should record the outcomes
and count the number of tails and heads.
"""
import random


def flip_coin() -> str:
    """Return either "tail" or "head" randomly
    """
    return random.choice(("tail", "head"))


def flip_coins(flips: int) -> list:
    """Return either "tail" or "head" randomly flips times
    """
    results = []
    for _ in range(0, flips):
        results.append(flip_coin())
    return results


if __name__ == "__main__":
    while True:
        FLIPS = int(input("Please input the number of flips "
                          "you want to simulate: "))
        print(flip_coins(FLIPS))
