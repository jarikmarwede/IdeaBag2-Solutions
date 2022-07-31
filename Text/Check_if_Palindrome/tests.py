#!/usr/bin/env python3
import unittest

from Text.Check_if_Palindrome.check_if_palindrome import is_palindrome


class Test(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()
