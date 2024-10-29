# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Command"""
from abc import ABC


class Light:

    @staticmethod
    def turn_on():
        print('To turn on the light')

    @staticmethod
    def turn_off():
        print('Turn the lights off')


class CommandBase:
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase, ABC):
    def __init__(self, light_):
        self.light = light_


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch:
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        self.on_cmd.execute()

    def off(self):
        self.off_cmd.execute()


def main():
    light = Light()
    switch = Switch(on_cmd=TurnOnLightCommand(light),
                    off_cmd=TurnOffLightCommand(light))
    switch.on()
    switch.off()


if __name__ == '__main__':
    # Output:
    # To turn on the light
    # Turn the lights off
    main()
