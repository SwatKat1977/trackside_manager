'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''

class Framework:
    """ Service framework class."""

    @property
    def is_running(self) -> bool:
        """!@brief is_running property (getter).
        @param self The object pointer.
        @return True if running, else False.
        """
        return self._is_running

    @is_running.setter
    def is_running(self, value) -> None:
        """!@brief is_running property (setter).
        @param self The object pointer.
        @param value New value for property.
        @return None
        """
        self._is_running = value

    def __init__(self):
        """!@brief Default constructor.
        @param self The object pointer.
        """
        self._is_running = False

    def run(self) -> None:
        """!@brief ** Overridable 'run' function **
        Start the application.
        @param self The object pointer.
        @return None
        """

        # Initialise the application and then run main loop if initialised.
        if self._initialise():
            while self._is_running:
                self._main_loop()

        # Perform any shutdown required.
        self._shutdown()

    def _initialise(self) -> bool:
        """!@brief Overridable 'initialise' function **
        @param self The object pointer.
        @return True if initialise was successful, otherwise False.
        """
        raise NotImplementedError("Requires implementing")

    def _main_loop(self) -> None:
        """!@brief Overridable 'main loop' function **
        @param self The object pointer.
        @return None
        """
        raise NotImplementedError("Requires implementing")

    def _shutdown(self) -> None:
        """!@brief Overridable 'shutdown' function **
        @param self The object pointer.
        @return None
        """
