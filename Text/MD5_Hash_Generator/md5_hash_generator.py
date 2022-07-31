#!/usr/bin/env python3
"""
Title:
MD5 Hash Generator

Description:
Make an MD5 hash code generator for strings and files.
MD5 is a widely used hash function algorithm that produces a 128 bit hash value.
Submitted by JoFo
"""
import hashlib
import os


def hash_string(string: str) -> str:
    hash_object = hashlib.md5()
    hash_object.update(bytes(string, "utf-8"))
    return hash_object.hexdigest()


def hash_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise ValueError(f"The file '{file_path}' does not exist!")
    else:
        with open(file_path, "r") as file:
            return hash_string(file.read())


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        choice = input("Do you want to hash a string or a file? (s|f) ")
        if choice == "s":
            to_hash = input("Which string do you want to hash? ")
            print(f"The hash of '{to_hash}' is '{hash_string(to_hash)}'\n")
        elif choice == "f":
            file_to_hash = input(
                "Please type in the path to the file you want to hash: "
            )
            try:
                print(f"The hash of '{file_to_hash}' is '{hash_file(file_to_hash)}'\n")
            except ValueError as error:
                print(f"{error}\n")


if __name__ == "__main__":
    _start_interactively()
