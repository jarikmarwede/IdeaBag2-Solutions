#!/usr/bin/env python3
import unittest

from Text.Pig_Latin.pig_latin import translate_to


class Test(unittest.TestCase):

    def test_translate_to(self):
        self.assertEqual(translate_to("banana"), "ananabay")


if __name__ == "__main__":
    pass
