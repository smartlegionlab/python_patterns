# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Black Board"""
import abc
import random


class Blackboard:

    def __init__(self):
        self.experts = []
        self.common_state = {
            'problems': 0,
            'suggestions': 0,
            'contributions': [],
            'progress': 0
        }

    def add_expert(self, expert):
        self.experts.append(expert)


class Controller:

    def __init__(self, black_board):
        self.blackboard = black_board

    def run_loop(self):
        while self.blackboard.common_state['progress'] < 100:
            for expert in self.blackboard.experts:
                if expert.is_eager_to_contribute:
                    expert.contribute()
        return self.blackboard.common_state['contributions']


class AbstractExpert:
    __metaclass__ = abc.ABCMeta

    def __init__(self, black_board):
        self.blackboard = black_board

    @property
    def is_eager_to_contribute(self):
        raise NotImplementedError('Must provide implementation in subclass.')

    @abc.abstractmethod
    def contribute(self):
        raise NotImplementedError('Must provide implementation in subclass.')


class Student(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return True

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 10)
        self.blackboard.common_state['suggestions'] += random.randint(1, 10)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(1, 2)


class Scientist(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return random.randint(0, 1)

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(10, 20)
        self.blackboard.common_state['suggestions'] += random.randint(10, 20)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 30)


class Professor(AbstractExpert):

    @property
    def is_eager_to_contribute(self):
        return True if self.blackboard.common_state['problems'] > 100 else False

    def contribute(self):
        self.blackboard.common_state['problems'] += random.randint(1, 2)
        self.blackboard.common_state['suggestions'] += random.randint(10, 20)
        self.blackboard.common_state['contributions'] += [self.__class__.__name__]
        self.blackboard.common_state['progress'] += random.randint(10, 100)


def main():
    blackboard = Blackboard()
    blackboard.add_expert(Student(blackboard))
    blackboard.add_expert(Scientist(blackboard))
    blackboard.add_expert(Professor(blackboard))
    c = Controller(blackboard)
    contributions = c.run_loop()
    from pprint import pprint
    pprint(contributions)


if __name__ == '__main__':
    # Output:
    # ['Student',
    #  'Student',
    #  'Scientist',
    #  'Student',
    #  'Scientist',
    #  'Student',
    #  'Scientist',
    #  'Student',
    #  'Scientist',
    #  'Student',
    #  'Scientist',
    #  'Professor']
    main()
