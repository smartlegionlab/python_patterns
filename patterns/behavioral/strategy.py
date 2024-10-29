# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Strategy"""


class ImageDecoder:
    @staticmethod
    def decode(filename):
        raise NotImplementedError()


class PNGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('PNG decode')


class JPEGImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('JPEG decode')
        return 'JPEG decode'


class GIFImageDecoder(ImageDecoder):
    @staticmethod
    def decode(filename):
        print('GIF decode')
        return 'GIF decode'


class Image:
    @classmethod
    def open(cls, filename):
        ext = filename.rsplit('.', 1)[-1]
        if ext == 'png':
            decoder = PNGImageDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGImageDecoder
        elif ext == 'gif':
            decoder = GIFImageDecoder
        else:
            raise RuntimeError('Unable to decode file %s' % filename)
        byte_range = decoder.decode(filename)
        return cls(byte_range, filename)

    def __init__(self, byte_range, filename):
        self._byte_range = byte_range
        self._filename = filename


def main():
    Image.open('picture.png')  # PNG decode
    Image.open('picture.jpg')  # JPEG decode
    Image.open('picture.gif')  # GIF decode


if __name__ == '__main__':
    main()
