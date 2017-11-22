#!/usr/bin/env python3
"""
Title:
Tax Calculator

Description:
Develop a program that asks the user to enter a cost
and either a country or state tax.
It then returns the tax plus the total cost with tax.
"""


def add_tax(base_cost: float, tax_rate: int):
    """Return base_cost with tax added to it
    """
    total_cost = base_cost / 100 * tax_rate + base_cost
    return total_cost


def remove_tax(cost: float, tax_rate: int):
    """Return specified cost with tax removed
    """
    base_cost = cost - cost / 100 * tax_rate
    return base_cost


if __name__ == "__main__":
    while True:
        CHOICE = input("Do you want to add tax or remove tax (add|remove): ")
        if CHOICE == "add":
            COST = float(input("Please input the price without tax: "))
            TAX_RATE = int(input("Please input the tax rate in percent: ")
                           .replace("%", ""))
            print(add_tax(COST, TAX_RATE))
        elif CHOICE == "remove":
            COST = float(input("Please input the price with tax: "))
            TAX_RATE = int(input("Please input the tax rate in percent: ")
                           .replace("%", ""))
            print(remove_tax(COST, TAX_RATE))
