#!/usr/bin/env python3
import unittest

from cd_key_generator import generate_key


class Test(unittest.TestCase):

    def test_generate_key(self):
        test1_result = generate_key(("a", "b", "c"), 10)
        self.assertEqual(len(test1_result), 10)
        for character in test1_result:
            self.assertIn(character, ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
