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
    """Return either "tail" or "head" randomly."""
    return random.choice(("tail", "head"))


def _start_interactively():
    """Start the program interactively through the command line."""
    results = {"head": 0,
               "tail": 0}
    while True:
        print(f"Head: {results['head']} Tail: {results['tail']}")
        input("Press enter to flip a coin")
        result = flip_coin()
        if result == "head":
            results["head"] += 1
        else:
            results["tail"] += 1
        print(result + "\n")


if __name__ == "__main__":
    _start_interactively()
