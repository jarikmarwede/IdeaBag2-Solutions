#!/usr/bin/env python3
import unittest

from Numbers.Fibonacci_Sequence.fibonacci_sequence import get_fibonacci_sequence


class Test(unittest.TestCase):

    def test_get_fibonacci_sequence(self):
        self.assertEqual(get_fibonacci_sequence(1), [0])
        self.assertEqual(get_fibonacci_sequence(2), [0, 1])
        self.assertEqual(get_fibonacci_sequence(10),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == "__main__":
    unittest.main()
