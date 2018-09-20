#!/usr/bin/env python3
import unittest

from rovarspraket import translate_from, translate_to


class Test(unittest.TestCase):

    def test_translate_to(self):
        self.assertEqual(translate_to("b"), "bob")
        self.assertEqual(translate_to("m"), "mom")

    def test_translate_from(self):
        self.assertEqual(translate_from("bob"), "b")
        self.assertEqual(translate_from("mom"), "m")


if __name__ == "__main__":
    unittest.main()
