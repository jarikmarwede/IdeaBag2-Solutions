#!/usr/bin/env python3
import unittest

from Text.Scooby_Doo.scooby_doo import scoobydoo


class Test(unittest.TestCase):

    def test_scoobydoo(self):
        self.assertEqual(scoobydoo("scooby"), "rrooby")


if __name__ == "__main__":
    unittest.main()
