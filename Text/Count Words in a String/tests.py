#!/usr/bin/env python3
import unittest

from count_words_in_a_string import count_lines, count_paragraphs, count_words


class Test(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words("This sentence has five words"), 5)

    def test_count_lines(self):
        self.assertEqual(count_lines("""This sentence
                                     is split over 
                                     three lines."""), 3)

    def test_count_paragraphs(self):
        self.assertEqual(count_paragraphs("""This text
                                          has two paragraphs.

                                          Here comes the 
                                          second one"""), 2)


if __name__ == "__main__":
    unittest.main()
