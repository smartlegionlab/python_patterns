# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
"""Chain of responsibility"""


class HttpHandler:
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    def handle(self, code):
        if code == 404:
            return 'Page not found'


class Http500Handler(HttpHandler):
    def handle(self, code):
        if code == 500:
            return 'server error'


class Client:
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print('Answer: %s' % msg)
                break
        else:
            print('Code not processed')


def main():
    client = Client()
    client.add_handler(Http404Handler())
    client.add_handler(Http500Handler())
    client.response(400)
    client.response(404)
    client.response(500)


if __name__ == '__main__':
    # Output:
    # Code not processed
    # Answer: Page not found
    # Answer: Server error
    main()
