#!/usr/bin/env python3
"""Multi threaded bulk image resizer.

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

from PIL import Image

IMAGE_FILE_EXTENSIONS = (".jpg", ".png")


class ImageResizer:
    """Class for multi threaded image resizing."""

    def __init__(self):
        """Define instance variables."""
        self.threads = 0
        self._size = None
        self._image_files = []
        self._lock = threading.Lock()

    def resize_images(self, image_files: list, size: tuple):
        """Resize specified images to size and save them in a new files."""
        self._image_files = image_files
        self._size = size

        while self._image_files:
            if self.threads < 4:
                new_thread = threading.Thread(target=self._resize_image)
                self.threads += 1
                new_thread.start()

    def _resize_image(self):
        """Resize the next image from self._image_files to self._size."""
        with self._lock:
            image_path = self._image_files.pop()

        old_image = Image.open(image_path)
        new_image = old_image.resize(self._size)
        new_image.save(image_path)
        self.threads -= 1


def get_images_from_directory(directory_path: str) -> list:
    """Return all images in the specified directory."""
    images = []

    for file_name in os.listdir(directory_path):
        file_name = file_name.lower()

        for file_extension in IMAGE_FILE_EXTENSIONS:
            if file_name.endswith(file_extension):
                images.append(directory_path + "/" + file_name)
                break

    return images


def _start_interactively():
    """Start program interactively through the command line."""
    directory = input("Please specify the directory the images are in: ")
    size_input = input("Please specify the size that the images "
                       "should be resized to (e.g. 1920x1080): ").split("x")
    size = (int(size_input[0]), int(size_input[1]))
    images = get_images_from_directory(directory)
    image_resizer = ImageResizer()
    image_resizer.resize_images(images, size)


if __name__ == "__main__":
    _start_interactively()
