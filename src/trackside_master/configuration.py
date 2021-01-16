'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''

class ApiSettings:
    """ Settings related to the API """
    #pylint: disable=too-few-public-methods
    __slots__ = ['_auth_key', '_use_auth_key']

    @property
    def auth_key(self) -> str:
        """!@brief Authentication Key (Getter).
        @param self The object pointer.
        @returns Authentication key.
        """
        return self._auth_key

    @property
    def use_auth_key(self) -> bool:
        """!@brief Using authentication flag (Getter).
        @param self The object pointer.
        @returns True if using authentication, else False.
        """
        return self._use_auth_key

    def __init__(self, auth_key, use_auth_key):
        self._auth_key = auth_key
        self._use_auth_key = use_auth_key

class Configuration:
    """ Main configuration class """
    #pylint: disable=too-few-public-methods
    __slots__ = ['_api_settings']

    @property
    def api_settings(self) -> ApiSettings:
        """!@brief Settings relating to the API (Getter).
        @param self The object pointer.
        @returns Instance of class representing the API settings.
        """
        return self._api_settings

    def __init__(self, api_settings):
        self._api_settings = api_settings
