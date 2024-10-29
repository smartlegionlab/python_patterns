# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Factory method"""
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def show(self):
        """Show document"""


class PDFDocument(Document):
    def show(self):
        print('PDF document format.')


class ODFDocument(Document):
    def show(self):
        print('ODF document format.')


class NoneDocument(Document):
    def show(self):
        print('None type document format')


class ApplicationBase(ABC):
    @abstractmethod
    def create_doc(self, type_):
        """Create document"""


class Application(ApplicationBase):
    def create_doc(self, type_):
        if type_ == 'pdf':
            return PDFDocument()
        elif type_ == 'odf':
            return ODFDocument()
        else:
            return NoneDocument()


def main():
    # Creating application
    app = Application()
    # Creating docs
    app.create_doc('pdf').show()  # PDF document format.
    app.create_doc('odf').show()  # ODF document format.
    app.create_doc('bad').show()  # None type document format


if __name__ == '__main__':
    main()
