'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import enum
import logging
import time


class LogType(enum.Enum):
    Debug = 0
    Info = 1
    Warn = 2
    Error = 3
    Critical = 4


class Logger:
    __slots__ = ['_external_logger', '_is_initialised', '_logger_instance',
                 '_write_to_console']

    Logger_mappings = {
        LogType.Debug : ('debug', logging.DEBUG),
        LogType.Error : ('error', logging.ERROR),
        LogType.Info : ('info', logging.INFO),
        LogType.Warn : ('warn', logging.WARN),
        LogType.Critical : ('critical', logging.CRITICAL),
    }

    @property
    def write_to_console(self):
        return self._write_to_console

    @write_to_console.setter
    def write_to_console(self, value):
        self._write_to_console = value

    @property
    def external_logger(self):
        return self._external_logger

    @external_logger.setter
    def external_logger(self, value):
        self._external_logger = value

    def __init__(self):
        self._external_logger = None
        self._is_initialised = False
        self._logger_instance = None
        self._write_to_console = False

    def initialise(self):
        if self._is_initialised:
            raise RuntimeError('Logger is already initialised!')

        logformat= logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                                     "%Y-%m-%d %H:%M:%S")

        self._logger_instance = logging.getLogger('system log')
        console_stream = logging.StreamHandler()
        console_stream.setFormatter(logformat)
        self._logger_instance.setLevel(logging.DEBUG)
        self._logger_instance.addHandler(console_stream)

        self._is_initialised = True

    def log(self, logLevel, msg, *args):
        if not self._is_initialised:
            raise RuntimeError('Logger is not initialised!')

        if self._write_to_console:
            mapped_method, _ = self.Logger_mappings[logLevel]
            method_to_call = getattr(self._logger_instance, mapped_method)
            method_to_call(msg, *args)

        if self._external_logger:
            current_time = time.time()
            compiled_msg = msg % args
            self._external_logger.add_log_event(current_time, logLevel,
                                                compiled_msg)
