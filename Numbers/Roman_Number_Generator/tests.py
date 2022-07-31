#!/usr/bin/env python3
import unittest

from Numbers.Roman_Number_Generator.roman_number_generator import arabic_to_roman


class Test(unittest.TestCase):

    def _start_arabic_to_roman(self):
        self.assertRaises(ValueError, arabic_to_roman, 4000)
        self.assertEqual(arabic_to_roman(4), "IV")
        self.assertEqual(arabic_to_roman(12), "XII")
        self.assertEqual(arabic_to_roman(20), "XX")


if __name__ == "__main__":
    unittest.main()
