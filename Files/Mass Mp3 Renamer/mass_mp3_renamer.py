#!/usr/bin/env python3
"""Mass Mp3 file renamer.

Title:
Mass Mp3 Renamer

Description:
You have songs in a folder that you want to rename
but you'd hate to do it one by one.
Write a program that takes three(3) inputs.
1. The path to the directory in which the songs are.
2. An input format string that lets the program know
how the songs are currently named.
3. An output format string that should form the new song filename.
The program should finish by printing a list of old -> new filename tuples.
The input/output format string can be any string
that contains any number of the following labels:
<artiste>, <album>, <track>, <year>
Assume that the filenames of the songs to be renamed
matches the input format string.
Sample list of input files:
Bob Dylan - 01 You're No Good (1962).mp3
Bob Dylan - 02 Talkin' New York (1962).mp3
Bob Dylan - 03 In My Time of Dyin' (1962).mp3
Bob Dylan - 04 Man of Constant Sorrow (1962).mp3
Bob Dylan - 05 Fixin' to Die (1962).mp3
Bob Dylan - 06 Pretty Peggy-O (1962).mp3
Sample input format string:
<artiste> - <track> <title> (<year>).mp3
Sample output format string:
<year> <artiste>/<track> <title>.mp3
Expected output:
Bob Dylan - 01 You're No Good (1962).mp3
-> 1962 Bob Dylan/01 You're No Good.mp3
Bob Dylan - 02 Talkin' New York (1962).mp3
-> 1962 Bob Dylan/02 Talkin' New York.mp3
Bob Dylan - 03 In My Time of Dyin' (1962).mp3
-> 1962 Bob Dylan/03 In My Time of Dyin'.mp3
Bob Dylan - 04 Man of Constant Sorrow (1962).mp3
-> 1962 Bob Dylan/04 Man of Constant Sorrow.mp3
Bob Dylan - 05 Fixin' to Die (1962).mp3
-> 1962 Bob Dylan/05 Fixin' to Die.mp3
Bob Dylan - 06 Pretty Peggy-O (1962).mp3
-> 1962 Bob Dylan/06 Pretty Peggy-O.mp3
Submitted by Kaustubh
"""
import os
import re
from collections import OrderedDict
from typing import List, Tuple


def rename_mp3s(directory_path: str, input_format: str, output_format: str)\
        -> List[Tuple[str, str]]:
    """Return files in directory with names changed to output_format."""
    old_filenames = os.listdir(directory_path)
    new_filenames = _convert_filenames(old_filenames,
                                       input_format,
                                       output_format)
    return [*zip(old_filenames, new_filenames)]


def _convert_filenames(old_filenames: List[str], input_format: str, output_format: str)\
        -> List[str]:
    """Convert filenames from input_format to output_format."""
    new_filenames = []
    input_format_regex = _convert_to_regex(input_format)
    format_order = _get_format_order(input_format)

    for file_name in old_filenames:
        match = input_format_regex.match(file_name)
        format_items_dict = {}

        for index, format_item in enumerate(format_order):
            format_items_dict[format_item] = match.group(index+1)
        new_filename = (output_format
                        .replace("<artiste>", format_items_dict["artiste"])
                        .replace("<track>", format_items_dict["track"])
                        .replace("<title>", format_items_dict["title"])
                        .replace("<year>", format_items_dict["year"]))
        new_filenames.append(new_filename)

    return new_filenames


def _convert_to_regex(input_format: str):
    """Return regex of input_format."""
    return re.compile(input_format.replace("(", "\\(")
                      .replace(")", "\\)")
                      .replace("<artiste>", "(.+)")
                      .replace("<track>", "(\\w+)")
                      .replace("<title>", "(.+)")
                      .replace("<year>", "(.+)"))


def _get_format_order(input_format: str):
    """Return order of <artiste>, <album>, <track>, <year> in input_format."""
    unordered_dictionary = {input_format.find("<artiste>"): "artiste",
                            input_format.find("<track>"): "track",
                            input_format.find("<title>"): "title",
                            input_format.find("<year>"): "year"}
    ordered_dictionary = OrderedDict(sorted(unordered_dictionary.items()))
    order = [name for name in ordered_dictionary.values()]
    return order


def _start():
    """Start running an example."""
    sample_input_format = "<artiste> - <track> <title> (<year>).mp3"
    sample_output_format = "<year> <artiste>/<track> <title>.mp3"

    sample_output = rename_mp3s("./Sample files",
                                sample_input_format,
                                sample_output_format)
    for file in sample_output:
        print(file[0] + " -> " + file[1])


if __name__ == "__main__":
    _start()
