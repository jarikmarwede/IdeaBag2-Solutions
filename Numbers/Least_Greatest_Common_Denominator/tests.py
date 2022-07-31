#!/usr/bin/env python3
import unittest

from Numbers.Least_Greatest_Common_Denominator.least_greatest_common_denominator import \
    greatest_common_divisor, least_common_multiple


class Test(unittest.TestCase):

    def test_least_common_multiple(self):
        self.assertEqual(least_common_multiple(4, 6), 12)

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(8, 12), 4)


if __name__ == "__main__":
    unittest.main()
