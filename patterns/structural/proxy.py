# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Proxy"""
from abc import ABC, abstractmethod
from functools import partial


class ImageBase(ABC):
    @classmethod
    def create(cls, width, height):
        return cls(width, height)

    @abstractmethod
    def draw(self, x, y, color):
        pass

    @abstractmethod
    def fill(self, color):
        pass

    @abstractmethod
    def save(self, filename):
        pass


class Image(ImageBase):
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def draw(self, x, y, color):
        print(f'Draw a point; coordinates: ({x}, {y}); color: {color}')

    def fill(self, color):
        print(f'Fill with color: {color}')

    def save(self, filename):
        print(f'Saves the image to a file: {filename}')


class ImageProxy(ImageBase):
    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)
        self.operations = []

    def draw(self, *args):
        func = partial(self._image.draw, *args)
        self.operations.append(func)

    def fill(self, *args):
        func = partial(self._image.fill, *args)
        self.operations.append(func)

    def save(self, filename):
        map(lambda f: f(), self.operations)
        self._image.save(filename)


def main():
    img = ImageProxy(200, 200)
    img.fill('gray')
    img.draw(0, 0, 'green')
    img.draw(0, 1, 'green')
    img.draw(1, 0, 'green')
    img.draw(1, 1, 'green')
    img.save('image.png')  # Saves the image to a file: image.png


if __name__ == '__main__':
    main()
