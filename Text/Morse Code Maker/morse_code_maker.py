#!/usr/bin/env python3
"""Convert text to morse code or morse code to text.

Title:
Morse Code Maker

Description:
Make a program which takes in a sting from the user
and then outputs that as a string of Morse Code.
If you are unfamiliar with Morse Code, you can find it on Wikipedia.
"""
MORSE_CODE_DICT = {" ": "/", "a": ".-", "b": "-...", "c": "-.-.",
                   "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                   "h": "....", "i": "..", "j": ".---", "k": "-.-",
                   "l": ".-..", "m": "--", "n": "-.", "o": "---",
                   "p": ".--.", "q": "--.-", "r": ".-.", "s": "...",
                   "t": "-", "u": "..-", "v": "...-", "w": ".--",
                   "x": "-..-", "y": "-.--", "z": "--..", "0": "-----",
                   "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                   "5": ".....", "6": "-....", "7": "--...", "8": "---..",
                   "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..",
                   "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
                   ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.",
                   "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
                   "\"": ".-..-.", "$": "...-..-", "@": ".--.-.", "à": ".--.-",
                   "ä": ".-.-", "å": ".--.-", "ą": ".-.-", "æ": ".-.-",
                   "ć": "-.-..", "ĉ": "-.-..", "ç": "-.-..", "đ": "..-..",
                   "ð": "..--.", "é": "..-..", "è": ".-..-", "ę": "..-..",
                   "ĝ": "--.-.", "ĥ": "----", "ĵ": ".---.", "ł": ".-..-",
                   "ń": "--.--", "ñ": "--.--", "ó": "---.", "ö": "---.",
                   "ø": "---.", "ś": "...-...", "ŝ": "...-.", "š": "----",
                   "þ": ".--..", "ü": "..--", "ŭ": "..--", "ź": "--..-.",
                   "ż": "--..-"}


def convert_to_morse_code(string: str) -> str:
    """Convert to morse code."""
    new_string = ""

    for char in string:
        if char.lower() in MORSE_CODE_DICT:
            new_string += MORSE_CODE_DICT[char.lower()] + " "
        else:
            raise ValueError(f"Invalid character: {char}")
    new_string = new_string[:len(new_string) - 1]
    return new_string


def convert_from_morse_code(string: str) -> str:
    """Convert from morse code."""
    new_string = ""

    for letter_code in string.split():
        for char, morse_code in MORSE_CODE_DICT.items():
            if letter_code == morse_code:
                new_string += char
    return new_string


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        string = input("Please input a string: ")
        morse_code = convert_to_morse_code(string)
        print("Morse Code: " + morse_code)
        print("Converted back: " + convert_from_morse_code(morse_code) + "\n")


if __name__ == "__main__":
    _start_interactively()
