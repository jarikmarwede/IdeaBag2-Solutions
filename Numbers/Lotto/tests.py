#!/usr/bin/env python3
import unittest

from lotto import gamble


class Test(unittest.TestCase):

    def test_gamble(self):
        self.assertTrue(len(gamble()) == 6)
        for number in gamble():
            self.assertIn(number, list(range(1, 50)))


if __name__ == "__main__":
    unittest.main()
