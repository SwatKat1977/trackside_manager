'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import env
from common.framework import Framework

class App(Framework):
    """ tbd """

    def __init__(self):
        super().__init__()
        self._app = None

    def _initialise(self):
        print('_initialise() called')

    def _main_loop(self):
        print('_initialise() called')

def main():
    """ Main entry point """

    app = App()

    print(f'Master version: {env.MASTER_VERSION}')
    print(app.is_running)

main()
