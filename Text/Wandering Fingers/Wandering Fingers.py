#!/usr/bin/env python3
"""
Title:
Wandering Fingers

Description:
Software like Swype and SwiftKey lets smartphone users enter text
by dragging their finger over th on-screen keyboard,
rather than tapping on each letter.
You'll be given a string of characters
representing the letters the user has dragged their finger over.
For example, if the user wants "rest",
the string of input characters might be "resdft" or "resert".
Given the following input strings,
find all possible output words 5 characters or longer from:
1. qweryuytresdftyuioknn
2. gijakjthoijerjidsdfnokg
Your program should find all possible words (5+ characters)
that can be derived from the strings supplied.
Use http://norvig.com/ngrams/enable1.txt as your search dictionary.
The order of the output words doesn't matter.
"""


def find_possible_words(word: str, dictionary: list) -> list:
    """Return all possible words from word
    """
    possible_words = []
    first_character = word[0]
    last_character = word[len(word) - 1]
    for dictionary_entry in dictionary:
        if (dictionary_entry.startswith(first_character) and
                dictionary_entry.endswith(last_character)):
            for character in dictionary_entry:
                if character in word:
                    continue
                else:
                    break
            else:
                possible_words.append(dictionary_entry)
    return possible_words


def get_dictionary(file_name: str) -> list:
    """Return dictionary from file
    """
    dictionary = []
    with open(file_name, "r") as file:
        for line in file.readlines():
            if len(line.strip()) > 4:
                dictionary.append(line.strip())
    return dictionary


def get_possible_words(string: str, file_name: str) -> list:
    """Return all possible words from each word in string
    """
    possible_string = []
    dictionary = get_dictionary(file_name)
    for word in string.split():
        if len(word) > 4:
            possible_words = find_possible_words(word, dictionary)
            possible_string.append(possible_words)
        else:
            possible_string.append([word])
    return possible_string


if __name__ == "__main__":
    while True:
        STRING = input("Please enter a string: ")
        FILE_NAME = input("Please enter the path to the dictionary: ")
        print(get_possible_words(STRING, FILE_NAME))
