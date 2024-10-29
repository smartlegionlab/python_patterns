# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Template Method"""


class ExampleBase:
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError()

    def step_two(self):
        raise NotImplementedError()

    def step_three(self):
        raise NotImplementedError()


class Example(ExampleBase):
    def step_one(self):
        print('The first step of the algorithm')

    def step_two(self):
        print('The second step of the algorithm')

    def step_three(self):
        print('The third step of the algorithm')


def main():
    example = Example()
    example.template_method()


if __name__ == '__main__':
    # Output:
    # The first step of the algorithm
    # The second step of the algorithm
    # The third step of the algorithm
    main()
