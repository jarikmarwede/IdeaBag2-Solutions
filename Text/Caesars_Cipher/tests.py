#!/usr/bin/env python3
import unittest

from Text.Caesars_Cipher.caesars_cipher import decrypt, encrypt


class Test(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt("hello", 13), "uryyb")

    def test_decrypt(self):
        self.assertEqual(decrypt("uryyb", 13), "hello")


if __name__ == "__main__":
    unittest.main()
