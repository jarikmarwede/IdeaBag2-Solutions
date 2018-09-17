#!/usr/bin/env python3
import unittest

from disemvoweler import disemvowel


class Test(unittest.TestCase):

    def test_disemvowel(self):
        self.assertEqual(disemvowel("Hello world"), "Hllwrld eoo")


if __name__ == "__main__":
    unittest.main()
