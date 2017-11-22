#!/usr/bin/env python3
"""Replace all vowels in s string with oodle

Title:
Voodlewoodlel

Description:
Boodleb wanted to see how his friend's name would look
if he changed every vowel to "oodle".
But he has no idea what vowels are, or how to chage them.
Help him realize his life's goal.
The user inputs n lines, with one name in each line.
Your program should print out the voodlewoodlel version of each name.
Example:
Peeves
Sinistra
outputs
Poodleoodlevoodles
Soodlenoodlestroodle
"""


def voodlewoodlel(string: str):
    """Return voodlewoodlel version of string
    """
    vowels = ("a", "e", "i", "o", "u")
    new_string = ""

    for line in string.splitlines():
        for character in line:
            if character.lower() in vowels:
                new_string += "oodle"
            else:
                new_string += character
        new_string += "\n"

    new_string = new_string.rstrip()  # remove last new line
    return new_string


if __name__ == "__main__":
    while True:
        # get input from user and replace automatically escaped new lines
        STRING = input("Please input the string "
                       "you want to voodlewoodlel: ").replace("\\n", "\n")
        print(voodlewoodlel(STRING))
