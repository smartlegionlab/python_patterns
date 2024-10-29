# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Memento"""


class Memento:
    """The keeper"""
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class CareTaker:
    def __init__(self):
        self._memento = None

    def get_memento(self):
        return self._memento

    def set_memento(self, memento):
        self._memento = memento


class Originator:
    """The creator"""
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()


def main():
    originator = Originator()
    caretaker = CareTaker()
    originator.set_state('on')
    print('Originator state:', originator.get_state())
    caretaker.set_memento(originator.save_state())
    originator.set_state('off')
    print('Originator change state:', originator.get_state())
    originator.restore_state(caretaker.get_memento())
    print('Originator restore state:', originator.get_state())


if __name__ == '__main__':
    # Output:
    # Originator state: on
    # Originator change state: off
    # Originator restore state: on
    main()
