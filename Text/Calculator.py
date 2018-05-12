#!/usr/bin/env python3
"""Calculates a mathematical expression.

Title:
Calculator

Description:
Your program will accept a mathematical expression as a string,
parse it and output the answer of the expression.
For example, "2*3+2-(4+5)" will output 9.
For added complexity,
add the ability to calculate expressions with scientifix terms
like cos, sin, tan, log, mod, dqr etc.
Submitted by David
"""


def evaluate(expression: str) -> float:
    """Return the value of expression using eval()."""
    try:
        result = eval(expression)
        return result
    except Exception:
        raise ValueError(expression + " is not a mathematical expression.")


if __name__ == "__main__":
    while True:
        EXPRESSION = input("Please input a mathematical expresion: ")
        print(evaluate(EXPRESSION))
