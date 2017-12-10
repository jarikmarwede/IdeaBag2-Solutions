#!/usr/bin/env python3
"""
Title:
Find the N-th Natural Number

Description:
The task is to find which natural number
(or rather a digit between 0-9) is at the 1986th position.
The number range is from 1 to 1000.
Optionally find the number that the 0-9 digit is a part of.
Example:
Given number range from 1-20 (1234567891011121314151617181920)
the digit at position 17 would be '3'
and it is a part of number '13'.
Submitted by Dusan N.
"""


def find_natural_number(position: int) -> tuple:
    """Return the natural number at specified position
    and the number its a part of
    """
    num_range = ""
    counter = 0
    while len(str(num_range)) < position:
        counter += 1
        num_range += str(counter)
    return num_range[-1], counter


if __name__ == "__main__":
    while True:
        POSITION = int(input("Please input the position "
                             "you want to get information on: "))
        print(*find_natural_number(POSITION))
        print("")
