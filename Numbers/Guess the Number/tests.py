#!/usr/bin/env python3
import unittest

from guess_the_number import guess_number


class Test(unittest.TestCase):

    def test_guess_number(self):
        self.assertIn(guess_number(0, 10), list(range(0, 11)))


if __name__ == "__main__":
    unittest.main()
