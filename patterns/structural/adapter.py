# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Adapter"""


class Dog:
    def __init__(self, name):
        self._name = name

    def bark(self):
        return f'{self._name}: wof! wof!'

    @property
    def name(self):
        return self._name


class Cat:
    def __init__(self, name):
        self._name = name

    def meow(self):
        return f'{self._name}: meow! meow!'

    @property
    def name(self):
        return self._name


class CatAdapter(Dog):
    def __init__(self, name):
        super(CatAdapter, self).__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        return self._cat.meow()


def main():
    # Dog object
    dog = Dog('Brave')
    print(dog.bark())  # Brave wof! wof!
    dog_adapted = CatAdapter('Brave')
    print(dog_adapted.bark())  # Brave meow! meow!


if __name__ == '__main__':
    main()
