#!/usr/bin/env python3
import unittest

from kaprekar_numbers import get_kaprekars, is_kaprekar


class Test(unittest.TestCase):

    def test_is_kaprekar(self):
        self.assertTrue(is_kaprekar(45))
        self.assertFalse(is_kaprekar(46))

    def test_get_kaprekars(self):
        self.assertEqual(list(get_kaprekars(1, 50)), [1, 9, 45])


if __name__ == "__main__":
    unittest.main()
