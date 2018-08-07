#!/usr/bin/env python3
"""A script that prints out a UUID version 4 in different formats.

Title:
UUID

Description:
Make a program that generates a UUID.
A universally unique identifier (UUID) is a 128-bit number
used to identify information in computer systems.
Note that your implementation should conform
to RFC4122 here > https://tools.ietf.org/html/rfc4122.html
For more information on UUIDs,
try > https://en.wikipedia.org/wiki/Universally_unique_identifier
Submitted by Ilya
"""
import uuid


def _print_uuid():
    uuid4 = uuid.uuid4()
    print(f"UUID: {uuid4}")
    print(f"URN: {uuid4.urn}")
    print(f"Bytes: {uuid4.bytes}")
    print(f"Hex: {uuid4.hex}")
    print(f"Int: {uuid4.int}")


if __name__ == "__main__":
    _print_uuid()
