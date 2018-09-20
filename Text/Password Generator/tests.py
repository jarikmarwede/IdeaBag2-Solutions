#!/usr/bin/env python3
import string
import unittest

from password_generator import generate_password, new_password, passwords, refresh_password


class Test(unittest.TestCase):

    def test_generate_password(self):
        test_result = generate_password(24)
        for char in test_result:
            self.assertIn(char, string.ascii_letters + string.digits)
        self.assertEqual(len(test_result), 24)

    def test_new_password(self):
        new_password("facebook", 24)
        for char in passwords["facebook"]:
            self.assertIn(char, string.ascii_letters + string.digits)
        self.assertEqual(len(passwords["facebook"]), 24)

    def test_refresh_password(self):
        refresh_password("facebook", 24)
        for char in passwords["facebook"]:
            self.assertIn(char, string.ascii_letters + string.digits)
        self.assertEqual(len(passwords["facebook"]), 24)


if __name__ == "__main__":
    unittest.main()
