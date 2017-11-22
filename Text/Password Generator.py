#!/usr/bin/env python3
"""
Title:
Password Generator

Description:
Create a program that allows a user to enter a password name
eg: "Facebook Account Password"
and length
eg: '24'.
Your program should then proceed to generate a strong password.
This strong password should be generated
by concatenating random characters, words and numbers in lower or uppercase.
The length of the generated password
should match the length the user provided.
For added complexity,
provide a list that shows all the previously generated passwords
and their names.
Also allow a user to regenerate a new for existing use.
For example, if 'Facebook Account Password' was previously 'p@ssw#rc/'
and the user clicks Regenerate,
generate a new password for 'Facebook Account Password'.
Add the ability to save the password as a file
that is encrypted using a master password that the user provides.
Submitted by Andrew J.
"""
import random
import string

passwords = {}


def generate_password(length: int) -> str:
    """Return random password of specified length
    """
    choice = string.ascii_letters + string.digits
    password = ""
    for character in random.choices(choice, k=length):
        password += character
    return password


def new_password(name: str, length: int):
    """Add new password to passwords dictionary
    """
    if name in passwords:
        raise ValueError("A password with name '{}' already exists".format(name))
    password = generate_password(length)
    passwords[name] = password


def refresh_password(name: str, length: int):
    """Refresh existing password
    """
    password = generate_password(length)
    passwords[name] = password


if __name__ == "__main__":
    while True:
        CHOICE = input("Do you want to add a password, "
                       "refresh an existing password "
                       "or see all passwords (new|refresh|show): ")
        if CHOICE == "new":
            NAME = input("Type in the name the password should have: ")
            LENGTH = int(input("Type in the length of the password: "))
            try:
                new_password(NAME, LENGTH)
            except ValueError:
                print("A password with name '{}' already exists".format(NAME))
        elif CHOICE == "refresh":
            NAME = input("Type in the name of the password: ")
            LENGTH = int(input("Type in the length of the password: "))
            refresh_password(NAME, LENGTH)
        elif CHOICE == "show":
            print(passwords)
