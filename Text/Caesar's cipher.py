#!/usr/bin/env python3
"""Encrypt/Decrypt strings by shifting them in alphabeticall order

Title: Caesar's cipher

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


def encrypt(string: str, shift: int) -> str:
    """Return encrypted version of string
    """
    encrypted_string = ""
    alphabet = ("a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x",
                "y", "z")

    for char in string:
        if char == char.lower():
            uppercase = False
        else:
            uppercase = True

        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            encrypted_char_index = char_index - shift
            while encrypted_char_index > 25:
                encrypted_char_index -= 26
            while encrypted_char_index < 0:
                encrypted_char_index += 26
            if uppercase is True:
                encrypted_string += alphabet[encrypted_char_index].upper()
            else:
                encrypted_string += alphabet[encrypted_char_index]
        else:
            encrypted_string += char
    return encrypted_string


def decrypt(string: str, shift: int) -> str:
    """Return decrypted version of string
    """
    return encrypt(string, 26 - shift)
    

if __name__ == "__main__":
    STRING = input("Please input the string that you want to encrypt: ")
    SHIFT = int(input("Please input the rotation: "))
    ENCRYPTED = encrypt(STRING, SHIFT)
    print("Encrypted: " + ENCRYPTED)
    print("Decrypted: " + decrypt(ENCRYPTED, SHIFT))
