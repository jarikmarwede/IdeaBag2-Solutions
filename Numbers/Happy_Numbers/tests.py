#!/usr/bin/env python3
import unittest

from Numbers.Happy_Numbers.happy_numbers import find_happy_numbers, is_happy_number, square_of_digits


class Test(unittest.TestCase):

    def test_is_happy_number(self):
        self.assertTrue(is_happy_number(28))
        self.assertFalse(is_happy_number(29))

    def test_square_of_digits(self):
        self.assertEqual(square_of_digits(23), 13)

    def test_find_happy_numbers(self):
        self.assertEqual(list(find_happy_numbers(10)),
                         [1, 7, 10, 13, 19, 23, 28, 31, 32, 44])


if __name__ == "__main__":
    unittest.main()
