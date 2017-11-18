#!/usr/bin/env python3
"""Count vowels used in a string

Title: Count Vowels

Description:
Develop a program that has the user enter a string.
Your program counts the number of vowels in the text
and prints it out.
For added complexity,
have it report a sum of each vowel found
and its position/index in the string.
"""


def count_vowels(string: str):
    """Analyze vowels in string and print out results
    """
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0

    for index, char in enumerate(string):
        if char.lower() == "a":
            a_count += 1
            print("a found at index {}".format(index))
        elif char.lower() == "e":
            e_count += 1
            print("e found at index {}".format(index))
        elif char.lower() == "i":
            i_count += 1
            print("i found at index {}".format(index))
        elif char.lower() == "o":
            o_count += 1
            print("o found at index {}".format(index))
        elif char.lower() == "u":
            u_count += 1
            print("u found at index {}".format(index))

    vowel_count = a_count + e_count + i_count + o_count + u_count

    print("\nSummary")
    print("Total amount of vowels: {}".format(vowel_count))
    print("Total amount of as: {}".format(a_count))
    print("Total amount of es: {}".format(e_count))
    print("Total amount of is: {}".format(i_count))
    print("Total amount of os: {}".format(o_count))
    print("Total amount of us: {}".format(u_count))


if __name__ == "__main__":
    STRING = input("Please input a string: ")
    print("")
    count_vowels(STRING)
