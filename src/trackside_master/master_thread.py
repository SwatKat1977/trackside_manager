'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
from common.logger import LogType
from common.service_thread import ServiceThread

class MasterThread(ServiceThread):

    def __init__(self, logger):
        super().__init__()
        self._logger = logger

    def initialise(self) -> bool:
        self._logger.log(LogType.Info, 'init')

        self._is_initialised = True

        return True

    def _main_loop(self) -> None:
        pass
