#!/usr/bin/env python3
"""
Print numbers from 1-100
but replace every number that is a multiple of 3 with Fizz,
every number that is a multiple of 5 with Buzz
and every number that is both with FizzBuzz

Title: Fizz Buzz

Description:
Develop a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number and
for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

def fizzbuzz() -> list:
    """Return a list of numbers from 1 to 100,
    replacing multiples of three with Fizz,
    multiples of five with Buzz and
    multiples of both with FizzBuzz
    """
    fizzbuzz_list = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif num % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif num % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(num)
    return fizzbuzz_list

def xfizzbuzz():
    """Generator function for numbers from 1 to 100
    with every multiple of three replaced with Fizz,
    every multiple of five replaced with Buzz and
    every multiple of both five and three with FizzBuzz
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            yield "FizzBuzz"
        elif num % 3 == 0:
            yield "Fizz"
        elif num % 5 == 0:
            yield "Buzz"
        else:
            yield num

if __name__ == "__main__":
    for num in fizzbuzz():
        print(num)
    for num in xfizzbuzz():
        print(num)
