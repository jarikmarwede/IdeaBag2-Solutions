#!/usr/bin/env python3
"""

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


if __name__ == "__main__":
    pass
