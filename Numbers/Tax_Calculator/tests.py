#!/usr/bin/env python3
import unittest

from Numbers.Tax_Calculator.tax_calculator import apply_tax, get_tax


class Test(unittest.TestCase):

    def test_get_tax(self):
        self.assertEqual(get_tax(2.50, 1.9), 0.0475)

    def test_apply_tax(self):
        self.assertEqual(apply_tax(2.50, 1.9), 2.5475)


if __name__ == "__main__":
    unittest.main()
