# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Visitor"""


class FruitVisitor:
    """Visitor"""
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)
        draw(fruit)

    def draw_apple(self, fruit):
        print('Apple')
        return fruit

    def draw_pear(self, fruit):
        print('Pear')
        return fruit

    def draw_unknown(self, fruit):
        print('Fruit')
        return fruit


class Fruit:
    """Fruits"""
    def draw(self, visitor_):
        visitor_.draw(self)


class Apple(Fruit):
    """Apple"""


class Pear(Fruit):
    """Pear"""


class Banana(Fruit):
    """Banana"""


def main():
    visitor = FruitVisitor()
    apple = Apple()
    apple.draw(visitor)
    # Apple
    pear = Pear()
    pear.draw(visitor)
    # Pear
    banana = Banana()
    banana.draw(visitor)
    # Fruit


if __name__ == '__main__':
    main()
