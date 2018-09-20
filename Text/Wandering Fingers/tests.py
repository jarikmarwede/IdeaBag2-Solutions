#!/usr/bin/env python3
import unittest

from wandering_fingers import find_possible_words, get_dictionary, get_possible_words

DICTIONARY_FILE = "enable1.txt"


class Test(unittest.TestCase):

    def test_find_possible_words(self):
        dictionary = get_dictionary(DICTIONARY_FILE)
        self.assertIn("reset", find_possible_words("resdft", dictionary))
        self.assertIn("reset", find_possible_words("resert", dictionary))

    def test_get_possible_words(self):
        test_result = get_possible_words("resdft resert", DICTIONARY_FILE)
        self.assertIn("reset", test_result[0])
        self.assertIn("reset", test_result[1])


if __name__ == "__main__":
    unittest.main()
