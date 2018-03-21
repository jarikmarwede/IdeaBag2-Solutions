#!/usr/bin/env python3
"""

Title:
Page Scraper

Description:
Create an application which connects to a site
and pulls out all links, or images,
and saves them to a list.
For added complexity,
organize the indexed content and don't allow duplicates.
Have it put the results into an easily searchable index file.
"""
import urllib.request
import bs4 as bs


def get_html(url: str):
    """Return html code of the specified website."""
    html = urllib.request.urlopen(url).read()
    return html


def get_image_urls(source: str):
    """Return the urls of all images in the specified html code."""
    soup = bs.BeautifulSoup(source, "lxml")

    images = soup.find_all("img")
    urls = [image.get("src") for image in images]
    return urls


def _start():
    """Starts the program interactively."""
    url = input("What url do you want to get images from? ")
    html = get_html(url)
    images = get_image_urls(html)
    print(", ".join(images))


if __name__ == "__main__":
    _start()
