#!/usr/bin/env python3
import unittest

from circular_primes import circular_primes, is_circular_prime, is_prime


class Test(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(20))
        self.assertTrue(is_prime(97))

    def test_is_circular_prime(self):
        self.assertFalse(is_circular_prime(1194))
        self.assertTrue(is_circular_prime(1193))

    def test_circular_primes(self):
        self.assertEqual(list(circular_primes(1, 100)),
                         [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])


if __name__ == "__main__":
    unittest.main()
