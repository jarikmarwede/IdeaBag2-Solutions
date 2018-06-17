#!/usr/bin/env python3
"""A program for calculating optimal change.

Title:
Change Return Program

Description:
Develop a program that has the user enter the cost of an item
and then the amount the user paid for the item.
Your program should figure out the change
and the number of quarters, dimes, nickels, pennies needed for the change.
"""
from pprint import pprint


def calculate_change(price: float, paid: float) -> dict:
    """Return the optimal amount of currency to be given back as change."""
    change_dictionary = {
        "one_hundred": 0,
        "fifty": 0,
        "twenty": 0,
        "ten": 0,
        "five": 0,
        "two": 0,
        "one": 0,
        "half": 0,
        "quarter": 0,
        "dime": 0,
        "nickel": 0,
        "penny": 0
    }
    change = round(paid - price, 2)
    while change > 0:
        if change - 100 >= 0:
            change -= 100
            change_dictionary["one_hundred"] += 1
        elif change - 50 >= 0:
            change -= 50
            change_dictionary["fifty"] += 1
        elif change - 20 >= 0:
            change -= 20
            change_dictionary["twenty"] += 1
        elif change - 10 >= 0:
            change -= 10
            change_dictionary["ten"] += 1
        elif change - 5 >= 0:
            change -= 5
            change_dictionary["five"] += 1
        elif change - 2 >= 0:
            change -= 2
            change_dictionary["two"] += 1
        elif change - 1 >= 0:
            change -= 1
            change_dictionary["one"] += 1
        elif change - 0.5 >= 0:
            change -= 0.5
            change_dictionary["half"] += 1
        elif change - 0.25 >= 0:
            change -= 0.25
            change_dictionary["quarter"] += 1
        elif change - 0.1 >= 0:
            change -= 0.1
            change_dictionary["dime"] += 1
        elif change - 0.05 >= 0:
            change -= 0.05
            change_dictionary["nickel"] += 1
        elif change - 0.01 >= 0:
            change -= 0.01
            change_dictionary["penny"] += 1
    return change_dictionary


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        price = float(input("Please input the original price: "))
        paid = float(input("Please input how much was paid: "))
        pprint(calculate_change(price, paid))
        print("")


if __name__ == "__main__":
    _start_interactively()
