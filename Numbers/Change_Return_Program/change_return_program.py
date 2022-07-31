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
        if round(change - 100.0, 2) >= 0:
            change = round(change - 100.0, 2)
            change_dictionary["one_hundred"] += 1
        elif round(change - 50.0, 2) >= 0:
            change = round(change - 50.0, 2)
            change_dictionary["fifty"] += 1
        elif round(change - 20.0, 2) >= 0:
            change = round(change - 20.0, 2)
            change_dictionary["twenty"] += 1
        elif round(change - 10.0, 2) >= 0:
            change = round(change - 10.0, 2)
            change_dictionary["ten"] += 1
        elif round(change - 5.0, 2) >= 0:
            change = round(change - 5.0, 2)
            change_dictionary["five"] += 1
        elif round(change - 2.0, 2) >= 0:
            change = round(change - 2.0, 2)
            change_dictionary["two"] += 1
        elif round(change - 1.0, 2) >= 0:
            change = round(change - 1.0, 2)
            change_dictionary["one"] += 1
        elif round(change - 0.5, 2) >= 0:
            change = round(change - 0.5, 2)
            change_dictionary["half"] += 1
        elif round(change - 0.25, 2) >= 0:
            change = round(change - 0.25)
            change_dictionary["quarter"] += 1
        elif round(change - 0.1, 2) >= 0:
            change = round(change - 0.1, 2)
            change_dictionary["dime"] += 1
        elif round(change - 0.05, 2) >= 0:
            change = round(change - 0.05)
            change_dictionary["nickel"] += 1
        elif round(change - 0.01, 2) >= 0:
            change = round(change - 0.01, 2)
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
