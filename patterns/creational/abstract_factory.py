# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Abstract Factory"""
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_drink(self):
        """Create Drink"""

    @abstractmethod
    def create_food(self):
        """Create Food"""


class Drink:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name


class Food:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-Cola')

    def create_food(self):
        return Food('Nuts')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Beer')

    def create_food(self):
        return Food('Fish')


def get_factory(identifier):
    if identifier == 0:
        return ConcreteFactory1()
    else:
        return ConcreteFactory2()


def main():
    # Creating ConcreteFactory1
    factory1 = get_factory(0)
    # Creating ConcreteFactory2
    factory2 = get_factory(1)
    # Creating drink with name "Coca-Cola"
    drink1 = factory1.create_drink()
    print(drink1)  # Coca Cola
    # Creating food with name "Nuts"
    food1 = factory1.create_food()
    print(food1)  # Nuts
    # Creating drink with name "Beer"
    drink2 = factory2.create_drink()
    print(drink2)  # Beer
    # Creating food with name "Fish"
    food2 = factory2.create_food()
    print(food2)  # Fish


if __name__ == '__main__':
    main()
