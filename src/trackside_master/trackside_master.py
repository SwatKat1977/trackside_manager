'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import signal
import sys
from env import TITLE_TEXT
from common.framework import Framework
from common.logger import Logger, LogType
from common.version import COPYRIGHT_TEXT, LICENSE_TEXT, VERSION

class TracksideMaster(Framework):
    """ tbd """

    def __init__(self):
        super().__init__()

        self._logger = Logger()

        ## Test test.
        self._app = None

    def _initialise(self):
        self._logger.write_to_console = True
        self._logger.initialise()

        signal.signal(signal.SIGINT, self._signal_handler)

        self._logger.log(LogType.Info, f'{TITLE_TEXT} {VERSION}')
        self._logger.log(LogType.Info, COPYRIGHT_TEXT)
        self._logger.log(LogType.Info, LICENSE_TEXT)

        self.is_running = True

        return True

    def _main_loop(self):
        pass

    def _signal_handler(self, signum, frame):
        #pylint: disable=unused-argument

        self._logger.log(LogType.Info, 'Shutting down...')
        self._shutdown()
        sys.exit(1)

def main() -> None:
    """!@brief Main entry point
    @return None
    """
    app = TracksideMaster()

    app.run()

main()
