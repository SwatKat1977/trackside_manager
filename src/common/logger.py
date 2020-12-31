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
    """ Enumeration of log type """
    Debug = 0
    Info = 1
    Warn = 2
    Error = 3
    Critical = 4


class Logger:
    """ Logger class that can write to a console or an external logger """
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
    def write_to_console(self) -> bool:
        """!@brief write_to_console boolean property (getter).
        @param self The object pointer.
        @returns True if write to console, else False.
        """
        return self._write_to_console

    @write_to_console.setter
    def write_to_console(self, value) -> None:
        """!@brief write_to_console boolean property (setter).
        @param self The object pointer.
        @param value New value for property.
        @return None
        """
        self._write_to_console = value

    @property
    def external_logger(self) -> str:
        """!@brief external logger function property (getter).
        @param self The object pointer.
        @returns function.
        """
        return self._external_logger

    @external_logger.setter
    def external_logger(self, value):
        """!@brief external logger function property (setter).
        @param self The object pointer.
        @param value New value for property.
        @return None
        """
        self._external_logger = value

    def __init__(self):
        """!@brief Default constructor.
        @param self The object pointer.
        """
        self._external_logger = None
        self._is_initialised = False
        self._logger_instance = None
        self._write_to_console = False

    def initialise(self) -> None:
        """!@brief Initialise the logger.
        @param self The object pointer.
        @return None
        """
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

    def log(self, log_level, msg, *args) -> None:
        """!@brief Log a message using the logger.
        @param self The object pointer.
        @param log_level Level of the logged message, e.g. debug.
        @param msg Actual message to log.
        @param args Variable arguments used in the message.
        @return None
        """
        if not self._is_initialised:
            raise RuntimeError('Logger is not initialised!')

        if self._write_to_console:
            mapped_method, _ = self.Logger_mappings[log_level]
            method_to_call = getattr(self._logger_instance, mapped_method)
            method_to_call(msg, *args)

        if self._external_logger:
            current_time = time.time()
            compiled_msg = msg % args
            self._external_logger.add_log_event(current_time, log_level,
                                                compiled_msg)
