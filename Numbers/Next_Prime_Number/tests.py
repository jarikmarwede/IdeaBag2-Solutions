#!/usr/bin/env python3
import unittest

from Numbers.Next_Prime_Number.next_prime_number import next_prime


class Test(unittest.TestCase):
    def test_next_prime(self):
        self.assertEqual(next_prime(27), 29)


if __name__ == "__main__":
    unittest.main()
