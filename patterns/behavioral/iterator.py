# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Iterator"""


class IteratorBase:
    """Base iterator class"""
    def first(self):
        """
        Returns the first item in the collection.
        If the element does not exist, an IndexError exception is thrown.

        """
        raise NotImplementedError()

    def last(self):
        """
        Returns the last item in the collection.
        If the element does not exist, an IndexError exception is thrown.

        """
        raise NotImplementedError()

    def next(self):
        """Returns the next item in the collection"""
        raise NotImplementedError()

    def prev(self):
        """Returns the previous item in the collection"""
        raise NotImplementedError()

    def current_item(self):
        """Returns the current item in the collection"""
        raise NotImplementedError()

    def is_done(self, index):
        """Returns true if the element at the specified index exists, false otherwise"""
        raise NotImplementedError()

    def get_item(self, index):
        """Returns the collection item at the specified index,
        otherwise throws an IndexError exception"""
        raise NotImplementedError()


class Iterator(IteratorBase):
    def __init__(self, list_=None):
        self._list = list_ or []
        self._current = 0

    def first(self):
        return self._list[0]

    def last(self):
        return self._list[-1]

    def current_item(self):
        return self._list[self._current]

    def is_done(self, index):
        last_index = len(self._list) - 1
        return 0 <= index <= last_index

    def next(self):
        self._current += 1
        if not self.is_done(self._current):
            self._current = 0
        return self.current_item()

    def prev(self):
        self._current -= 1
        if not self.is_done(self._current):
            self._current = len(self._list) - 1
        return self.current_item()

    def get_item(self, index):
        if not self.is_done(index):
            raise IndexError('No item with index: %d' % index)
        return self._list[index]


def main():
    it = Iterator(['one', 'two', 'three', 'four', 'five'])
    print([it.prev() for _ in range(5)])
    print([it.next() for _ in range(5)])


if __name__ == '__main__':
    # Output:
    # ['five', 'four', 'three', 'two', 'one']
    # ['two', 'three', 'four', 'five', 'one']
    main()
