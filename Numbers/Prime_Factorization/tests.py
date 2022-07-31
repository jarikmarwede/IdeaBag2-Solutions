#!/usr/bin/env python3
import unittest

from Numbers.Prime_Factorization.prime_factorization import find_prime_factors


class Test(unittest.TestCase):

    def test_find_prime_factors(self):
        self.assertEqual(find_prime_factors(12), [2, 2, 3])


if __name__ == "__main__":
    unittest.main()
