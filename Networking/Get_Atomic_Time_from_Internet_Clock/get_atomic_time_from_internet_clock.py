#!/usr/bin/env python3
"""Get the atomic time via ntp.

Title:
Get Atomic Time from Internet Clock

Description:
International Atomic Time (TAI,
from the French name Temps Atomique International
is a high-precision atomic coordinate time standard
based on the notional passage of proper time on Earth's geoid.
Develop a program will get
the true atomic time from an atomic time clock on the Internet.
There are various clocks across the world.
Do a search for a list of them and use one.
"""
import datetime
import ntplib


def get_time(ntp_server: str) -> datetime.time:
    """Return a datetime.time object from an ntp server."""
    client = ntplib.NTPClient()
    timestamp = client.request(ntp_server).tx_time
    date = datetime.datetime.utcfromtimestamp(timestamp)
    time = date.time()
    return time


def _start_interactively():
    """Start the program interactively through the command line."""
    while True:
        server = input("Please input the address of an ntp server (e.g. pool.ntp.org): ")
        print(get_time(server), "\n")


if __name__ == "__main__":
    _start_interactively()
