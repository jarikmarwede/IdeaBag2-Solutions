#!/usr/bin/env python3
"""

Title:
Bulk Thumbnail Creator

Description:
Picture processing can take a bit of time for some transformations.
Especially if the image is large.
Create an image program which can take hundreds of images
and converts them to a specified size in the background thread
while you do other things.
For added complexity,
have one thread handling re-sizing,
have another bulk renaming of thumbnails etc.
"""
import os
import threading
import PIL


def resize_images(image_files: list, size: tuple):
    """Resize specified images to size and save them in new files."""


def get_images_from_directory(directory_path: str) -> list:
    """Return all images in the specified directory."""
    images = []
    for file_name in os.listdir(directory_path):
        if (file_name.lower().endswith(".jpg")
                or file_name.lower().endswith(".png")):
            images.append(directory_path + "/" + file_name)
    return images


if __name__ == "__main__":
    pass
