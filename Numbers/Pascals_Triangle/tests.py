#!/usr/bin/env python3
import unittest

from Numbers.Pascals_Triangle.pascals_triangle import pascals_triangle


class Test(unittest.TestCase):

    def test_pascals_triangle(self):
        self.assertEqual(pascals_triangle(0), ())
        self.assertEqual(pascals_triangle(3), ((1,), (1, 1), (1, 2, 1)))


if __name__ == "__main__":
    unittest.main()
