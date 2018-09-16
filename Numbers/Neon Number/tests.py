#!/usr/bin/env python3
import unittest

from neon_number import find_neons, is_neon


class Test(unittest.TestCase):

    def test_is_neon(self):
        self.assertTrue(is_neon(9))
        self.assertFalse(is_neon(10))

    def find_neons(self):
        self.assertEqual(list(find_neons(1, 100)), [1, 9])


if __name__ == "__main__":
    unittest.main()
