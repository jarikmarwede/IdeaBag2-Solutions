#!/usr/bin/env python3
import unittest

from Text.Half_the_String.half_the_string import first_half, second_half


class Test(unittest.TestCase):

    def test_first_half(self):
        self.assertEqual(first_half("word"), "wo")

    def test_second_half(self):
        self.assertEqual(second_half("word"), "rd")


if __name__ == "__main__":
    unittest.main()
