# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Bridge"""
from abc import ABC, abstractmethod


class TvBase(ABC):
    @abstractmethod
    def tune_channel(self, channel):
        pass


class SharpTv(TvBase):
    def tune_channel(self, channel):
        print(f'{self.__class__.__name__}: selected {channel} channel.')


class SonyTv(TvBase):
    def tune_channel(self, channel):
        print(f'SonyTv: selected {channel} channel.')


class RemoteControlBase(ABC):
    def __init__(self):
        self._tv = self.get_tv()

    @abstractmethod
    def get_tv(self):
        pass

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0

    def get_tv(self):
        return SharpTv()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def prev_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)

    def reset_channel(self):
        self._channel = 0
        self.tune_channel(self._channel)


def main():
    remote_control = RemoteControl()
    remote_control.tune_channel(5)  # SharpTv: selected 5 channel.
    remote_control.prev_channel()  # SharpTv: selected 4 channel.
    remote_control.next_channel()  # SharpTv: selected 5 channel.
    remote_control.reset_channel()  # SharpTv: selected 0 channel.


if __name__ == '__main__':
    main()
