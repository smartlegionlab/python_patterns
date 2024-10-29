# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Builder"""
from abc import ABC, abstractmethod


# Abstract Flashlight builder
class FlashlightBuilderBase(ABC):
    @abstractmethod
    def build_body(self):
        """Build body"""

    @abstractmethod
    def build_lamp(self):
        """Build lamp"""

    @abstractmethod
    def build_battery(self):
        """Build battery"""

    @abstractmethod
    def create_flashlight(self):
        """Create flashlight"""


# Flashlight
class FlashLight:
    def __init__(self, body, lamp, battery):
        self._body = body
        self._lamp = lamp
        self._battery = battery
        self._shine = False

    def on(self):
        self._shine = True

    def off(self):
        self._shine = False

    def __str__(self):
        status = 'On' if self._shine else 'Off'
        return f'Flashlight: [{status}]'


class Body:
    """Body"""


class Lamp:
    """Lamp"""


class Battery:
    """Battery"""


class FlashLightBuilder(FlashlightBuilderBase):
    def build_body(self):
        return Body()

    def build_lamp(self):
        return Lamp()

    def build_battery(self):
        return Battery()

    def create_flashlight(self):
        body = self.build_body()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return FlashLight(body=body, lamp=lamp, battery=battery)


def main():
    # Creating flashlight builder
    builder = FlashLightBuilder()
    # Creating flashlight
    flashlight = builder.create_flashlight()
    # Using flashlight
    flashlight.on()
    print(flashlight)  # Flashlight: [On]
    flashlight.off()
    print(flashlight)  # Flashlight: [Off]


if __name__ == '__main__':
    main()
