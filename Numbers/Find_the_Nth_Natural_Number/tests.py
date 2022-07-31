#!/usr/bin/env python3
import unittest

from Numbers.Find_the_Nth_Natural_Number.find_the_nth_natural_number import find_natural_number


class Test(unittest.TestCase):

    def test_find_natural_number(self):
        self.assertEqual(find_natural_number(17), (3, 13))


if __name__ == "__main__":
    unittest.main()
