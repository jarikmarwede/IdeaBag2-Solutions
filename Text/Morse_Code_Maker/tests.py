#!/usr/bin/env python3
import unittest

from Text.Morse_Code_Maker.morse_code_maker import convert_from_morse_code, convert_to_morse_code


class Test(unittest.TestCase):

    def test_convert_to_morse_code(self):
        self.assertEqual(convert_to_morse_code("hello"), ".... . .-.. .-.. ---")

    def test_convert_from_morse_code(self):
        self.assertEqual(convert_from_morse_code(".... . .-.. .-.. ---"), "hello")


if __name__ == "__main__":
    unittest.main()
