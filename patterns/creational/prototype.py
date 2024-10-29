# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Prototype"""
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class Bird:
    """Bird"""


def main():
    prototype = Prototype()
    prototype.register('Bird', Bird())
    duck = prototype.clone('Bird', {'name': 'Duck'})
    print(type(duck), duck.name)  # <class '__main__.Bird'> Duck


if __name__ == '__main__':
    main()
