#!/usr/bin/env python3
import unittest

from binary_to_decimal_and_back_converter import binary_to_decimal, decimal_to_binary, \
    decimal_to_hexadecimal, decimal_to_octal


class Test(unittest.TestCase):

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal(1000101011), 555)

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(555), 1000101011)

    def test_decimal_to_octal(self):
        self.assertEqual(decimal_to_octal(555), 1053)

    def test_decimal_to_hexadecimal(self):
        self.assertEqual(decimal_to_hexadecimal(555), "22b")


if __name__ == "__main__":
    unittest.main()
