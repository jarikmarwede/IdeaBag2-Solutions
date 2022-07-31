#!/usr/bin/env python3
import unittest

from Numbers.Change_Return_Program.change_return_program import calculate_change


class Test(unittest.TestCase):

    def test_calculate_change(self):
        test1_result = calculate_change(25.34, 30.0)
        test1_expected = {
            "one_hundred": 0,
            "fifty": 0,
            "twenty": 0,
            "ten": 0,
            "five": 0,
            "two": 2,
            "one": 0,
            "half": 1,
            "quarter": 0,
            "dime": 1,
            "nickel": 1,
            "penny": 0
        }
        self.assertEqual(test1_result, test1_expected)


if __name__ == "__main__":
    unittest.main()
