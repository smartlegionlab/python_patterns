# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Decorator"""


class Man:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def say(self):
        print(f'Hello, my name is {self._name}.')


class JetPack:
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        print(f'{self._man.name} flies on a jetpack.')


def main():
    man = Man('Smart Bear')
    super_man = JetPack(man)
    super_man.say()  # Hello, my name is Smart Bear.
    super_man.fly()  # Smart Bear flies on a jetpack.


if __name__ == '__main__':
    main()
