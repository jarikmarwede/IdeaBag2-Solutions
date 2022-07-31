#!/usr/bin/env python3
"""Encrypt/Decrypt text by shifting letters in alphabetical order.

Title:
Caesar's cipher

Description:
The user first enters a number to be used as the shift parameter.
The shift parameter is the key to the cipher and
would be used for encrypting and decrypting text.
During encryption, shifting is done to the left of the alphabets
till the shift parameter matches the number of shifts done.
For decryption, reverse the above process.
For example with a shift parameter of 3:
Plain:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher:
XYZABCDEFGHIJKLMNOPQRSTUVW
During decryption:
Plaintext:
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext:
QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
Submitted by Neo
"""
ALPHABET = ("a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z")


def encrypt(string: str, shift: int) -> str:
    """Return encrypted version of string."""
    encrypted_string = ""

    for char in string:
        if char == char.lower():
            uppercase = False
        else:
            uppercase = True

        if char.lower() in ALPHABET:
            char_index = ALPHABET.index(char.lower())
            encrypted_char_index = char_index - shift
            while encrypted_char_index > 25:
                encrypted_char_index -= 26
            while encrypted_char_index < 0:
                encrypted_char_index += 26
            if uppercase is True:
                encrypted_string += ALPHABET[encrypted_char_index].upper()
            else:
                encrypted_string += ALPHABET[encrypted_char_index]
        else:
            encrypted_string += char
    return encrypted_string


def decrypt(string: str, shift: int) -> str:
    """Return decrypted version of string."""
    return encrypt(string, 26 - shift)


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input the string that you want to encrypt: ")
        shift = int(input("Please input the rotation: "))
        encrypted = encrypt(string, shift)
        print("Encrypted: " + encrypted)
        print("Decrypted: " + decrypt(encrypted, shift) + "\n")


if __name__ == "__main__":
    _start_interactively()
