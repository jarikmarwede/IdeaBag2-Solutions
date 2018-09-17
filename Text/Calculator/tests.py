#!/usr/bin/env python3
import unittest

from Calculator import evaluate


class Test(unittest.TestCase):

    def test_evaluate(self):
        self.assertEqual(evaluate("5+5"), 10.0)
        self.assertEqual(evaluate("5/5"), 1.0)
        self.assertEqual(evaluate("5-5"), 0.0)
        self.assertEqual(evaluate("5*5"), 25.0)


if __name__ == "__main__":
    unittest.main()
