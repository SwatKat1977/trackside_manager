'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import env
from common.framework import Framework
from common.logger import Logger

class TracksideMaster(Framework):
    """ tbd """

    def __init__(self):
        super().__init__()

        self._logger = Logger()

        ## Test test.
        self._app = None

    def _initialise(self):
        print('_initialise() called')
        self._is_running = True
        return True

    def _main_loop(self):
        print('_main_loop() called')

def main() -> None:
    """!@brief Main entry point
    @return None
    """
    app = TracksideMaster()

    app.run()

    print(f'Master version: {env.MASTER_VERSION}')

main()
