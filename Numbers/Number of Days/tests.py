#!/usr/bin/env python3
import unittest

from number_of_days import _parse_date, number_of_days


class Test(unittest.TestCase):

    def test_number_of_days(self):
        self.assertEqual(number_of_days("01/01/2001", "01/01/2001"), 0)
        self.assertEqual(number_of_days("13/03/2015", "03/08/2016"), 508)

    def test_parse_date(self):
        self.assertEqual(_parse_date("13/03/2015"), (13, 3, 2015))


if __name__ == "__main__":
    unittest.main()
