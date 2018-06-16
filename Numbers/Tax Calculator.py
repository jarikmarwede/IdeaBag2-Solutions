#!/usr/bin/env python3
"""A tax calculator for the command line.

Title:
Tax Calculator

Description:
Develop a program that asks the user to enter a cost
and either a country or state tax.
It then returns the tax plus the total cost with tax.
"""


def get_tax(base_cost: float, tax_rate: float) -> float:
    """Return the tax on base_cost."""
    tax = base_cost / 100 * tax_rate
    return tax


def apply_tax(base_cost: float, tax_rate: float) -> float:
    """Return base_cost with tax applied to it."""
    total_cost = base_cost + get_tax(base_cost, tax_rate)
    return total_cost


def _start_interactively():
    """Start program interactively in the command line."""
    while True:
        cost = float(input("Please input the price without tax: "))
        tax_rate = float(input("Please input the tax rate in percent: ")
                       .replace("%", ""))
        print(f"Tax: {get_tax(cost, tax_rate)}")
        print(f"Final cost: {apply_tax(cost, tax_rate)}")


if __name__ == "__main__":
    _start_interactively()
