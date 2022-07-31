#!/usr/bin/env python3
import unittest

from Numbers.Factorial_Finder.factorial_finder import find_factorial


class Test(unittest.TestCase):

    def test_find_factorial(self):
        self.assertEqual(find_factorial(5), 120)
        self.assertEqual(find_factorial(0), 1)
        self.assertRaises(ValueError, find_factorial, -20)


if __name__ == "__main__":
    unittest.main()
