#!/usr/bin/env python3
import unittest

from Text.Voodlewoodlel.voodlewoodlel import voodlewoodlel


class Test(unittest.TestCase):

    def test_voodlewoodlel(self):
        self.assertEqual(voodlewoodlel("Peeves"), "Poodleoodlevoodles")
        self.assertEqual(voodlewoodlel("Sinistra"), "Soodlenoodlestroodle")


if __name__ == "__main__":
    unittest.main()
