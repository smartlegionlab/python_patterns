# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Flyweight"""
import weakref


class Color:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ColorsFactory:
    _colors = weakref.WeakValueDictionary()

    @classmethod
    def get_color(cls, name):
        value = cls._colors.get(name)
        if value is None:
            value = Color(name)
            cls._colors[name] = value
        return value


class PlaceMark:
    def __init__(self, latitude, longitude, color_name):
        self._latitude = latitude
        self._longitude = longitude
        self._color = ColorsFactory.get_color(color_name)

    def __str__(self):
        args = (self._color, self._latitude, self._longitude)
        return 'Color: {}; Coordinates({}, {})'.format(*args)

    @property
    def color(self):
        return self._color


def main():
    place_mark0 = PlaceMark(-74.007121, 40.714551, 'green')
    place_mark1 = PlaceMark(37.617761, 55.755773, 'green')
    print(place_mark0)  # Color: green; Coordinates(-74.007121, 40.714551)
    print(place_mark1)  # Color: green; Coordinates(37.617761, 55.755773)
    print(place_mark0.color is place_mark1.color)  # True


if __name__ == '__main__':
    main()
