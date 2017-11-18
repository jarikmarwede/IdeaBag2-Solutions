#!/usr/bin/env python3
"""Count words, lines and paragraphs in a string

Title: Count Words in a String

Description:
Develop a program that counts the number of individual woeds in a string.
For added complexity,
try to see if you can find the number of paragraphs in it too.
"""


def count_words(string: str) -> int:
    """Count number of words in string
    """
    count = 0
    for word in line.split():
        count += 1
    return count


def count_lines(string: str) -> int:
    """Count number of lines in string
    """
    count = 0
    for word in string.split("\n"):
        count += 1
    return count


def count_paragraphs(string: str) -> int:
    """Count number of paragraphs in string
    """
    count = 0
    for word in string.split("\n\n"):
        count += 1
    return count


if __name__ == "__main__":
    STRING = input("Please input a string: ")
    print("Words: " + str(count_words(STRING)))
    print("Lines: " + str(count_lines(STRING)))
    print("Paragraphs: " + str(count_paragraphs(STRING)))
