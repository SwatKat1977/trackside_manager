'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import asyncio
import signal
import sys
from threading import Thread
from common.logger import Logger, LogType
from common.version import COPYRIGHT_TEXT, LICENSE_TEXT, VERSION
from .master_thread import MasterThread

## Title text logged during initialisation.
TITLE_TEXT = 'Trackside Manager Master Service'

class Service:
    """ Trackside master service class """

    def __init__(self):
        ## Instance of the logging wrapper class.
        self._logger = Logger()

        self._master_thread_class = MasterThread(self._logger)
        self._master_thread = None

    def __del__(self):
        self._logger.log(LogType.Info, 'Service has been destroyed..')

    def start(self):
        self._logger.write_to_console = True
        self._logger.initialise()

        signal.signal(signal.SIGINT, self._signal_handler)

        self._logger.log(LogType.Info, f'{TITLE_TEXT} {VERSION}')
        self._logger.log(LogType.Info, COPYRIGHT_TEXT)
        self._logger.log(LogType.Info, LICENSE_TEXT)

        if not self._master_thread_class.initialise():
            return False

        loop = asyncio.get_event_loop()
        self._master_thread = Thread(target=self._master_thread_class.run,
                                     args=(loop,))
        self._master_thread.start()

        return True

    def _signal_handler(self, signum, frame) -> None:
        """!@brief Handle signals (e.g. ctrl-c) and process them.
        @param self The object pointer.
        @param signum Unused
        @param frame Unused
        @return None
        """
        #pylint: disable=unused-argument

        self._logger.log(LogType.Info, 'Signal caught...')
        self._shutdown()
        sys.exit(1)

    def _shutdown(self):
        self._logger.log(LogType.Info, 'Shutting down...')
