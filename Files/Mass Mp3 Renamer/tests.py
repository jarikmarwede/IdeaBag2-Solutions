#!/usr/bin/env python3
import re
import unittest

from mass_mp3_renamer import _convert_filenames, _convert_to_regex, _get_format_order


class Test(unittest.TestCase):

    def test_convert_filenames(self):
        self.assertEqual(_convert_filenames(["Bob Dylan - 01 You're No Good (1962).mp3",
                                             "Bob Dylan - 02 Talkin' New York (1962).mp3",
                                             "Bob Dylan - 03 In My Time of Dyin' (1962).mp3",
                                             "Bob Dylan - 04 Man of Constant Sorrow (1962).mp3",
                                             "Bob Dylan - 05 Fixin' to Die (1962).mp3",
                                             "Bob Dylan - 06 Pretty Peggy-O (1962).mp3"],
                                            "<artiste> - <track> <title> (<year>).mp3",
                                            "<year> <artiste>/<track> <title>.mp3"),
                         ["1962 Bob Dylan/01 You're No Good.mp3",
                          "1962 Bob Dylan/02 Talkin' New York.mp3",
                          "1962 Bob Dylan/03 In My Time of Dyin'.mp3",
                          "1962 Bob Dylan/04 Man of Constant Sorrow.mp3",
                          "1962 Bob Dylan/05 Fixin' to Die.mp3",
                          "1962 Bob Dylan/06 Pretty Peggy-O.mp3"])

    def test_convert_to_regex(self):
        self.assertEqual(type(_convert_to_regex("<artiste> - <track> <title> (<year>).mp3")),
                         re.Pattern)

    def test_get_format_order(self):
        self.assertEqual(_get_format_order("<artiste> - <track> <title> (<year>).mp3"),
                         ['artiste', 'track', 'title', 'year'])


if __name__ == "__main__":
    unittest.main()
