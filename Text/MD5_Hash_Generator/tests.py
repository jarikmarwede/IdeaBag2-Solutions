#!/usr/bin/env python3
import unittest

from Text.MD5_Hash_Generator.md5_hash_generator import hash_string


class Tests(unittest.TestCase):
    def test_hash_string(self):
        self.assertEqual(hash_string("hello"), "5d41402abc4b2a76b9719d911017c592")
        self.assertEqual(hash_string(""), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(
            hash_string("The quick brown fox jumps over the lazy dog."),
            "e4d909c290d0fb1ca068ffaddf22cbd0",
        )


if __name__ == "__main__":
    unittest.main()
