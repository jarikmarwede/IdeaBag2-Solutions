#!/usr/bin/env python3
import unittest

from in_order import check_order, is_in_order


class Test(unittest.TestCase):

    def test_is_in_order(self):
        self.assertTrue(is_in_order("almost"))
        self.assertTrue(is_in_order("biopsy"))
        self.assertTrue(is_in_order("billowy"))
        self.assertFalse(is_in_order("baton"))
        self.assertFalse(is_in_order("chef"))

    def test_check_order(self):
        self.assertEqual(check_order("biopsy billowy chef"), {
            "biopsy": "in order",
            "billowy": "in order",
            "chef": "not in order"
        })


if __name__ == "__main__":
    unittest.main()
