#!/usr/bin/env python3
"""Replace all vowels in s string with oodle

Title: Voodlewoodlel

Description:
Boodleb wanted to see how his friend's name would look
if he changed every vowel to "oodle".
But he has no idea what vowels are, or how to chage them.
Help him realize his life's gial.
The user inputs n lines, with one name in each line.
Your program should print out the voodlewoodlel version of each name.
Example:
Peeves
Sinistra
outputs
Poodleoodlevoodles
Soodlenoodlestroodle
"""


def voodlewoodlel(string):
    """Return voodlewoodlel version of string as a list of each line
    """
    vowels = ("a", "e", "i", "o", "u")
    new_string = ""
    for line in string.splitlines():
        for char in line:
            if char.lower() in vowels:
                new_string += "oodle"
            else:
                new_string += char
        new_string += "\n"
    # remove last newline
    new_string = new_string[:len(new_string) - 1]
    return new_string


if __name__ == "__main__":
    STRING = input("Please input a string: ").replace("\\n", "\n")
    print(voodlewoodlel(STRING))
