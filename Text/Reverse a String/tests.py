#!/usr/bin/env python3
import unittest

from reverse_a_string import reverse


class Test(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")


if __name__ == "__main__":
    unittest.main()
