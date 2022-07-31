#!/usr/bin/env python3
import unittest

from Numbers.Coin_Flip_Simulation.coin_flip_simulation import flip_coin


class Test(unittest.TestCase):

    def test_flip_coin(self):
        test1_result = flip_coin()
        self.assertTrue(test1_result == "head" or test1_result == "tail")


if __name__ == "__main__":
    unittest.main()
