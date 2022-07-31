#!/usr/bin/env python3
import unittest

from Numbers.Roman_to_Arabic_numeral_converter.roman_to_arabic_numeral_converter import \
    convert_to_arabic


class Test(unittest.TestCase):

    def test_convert_to_arabic(self):
        self.assertEqual(convert_to_arabic("MCMLIV"), 1954)


if __name__ == "__main__":
    unittest.main()
