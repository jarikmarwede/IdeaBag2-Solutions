#!/usr/bin/env python3
import unittest

from latin_squares import is_latin_square


class Test(unittest.TestCase):

    def test_is_latin_square(self):
        self.assertTrue(is_latin_square(5, "1234551234451233451223451"))
        self.assertFalse(is_latin_square(4, "1234132423414321"))


if __name__ == "__main__":
    unittest.main()
