'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''

class ApiSettings:
    """ Settings related to the underlying database """
    #pylint: disable=too-few-public-methods
    __slots__ = ['_auth_key']

    @property
    def auth_key(self):
        return self._auth_key

    def __init__(self, auth_key):
        self._auth_key = auth_key

class Configuration:
    __slots__ = ['_api_settings']

    @property
    def api_settings(self):
        return self._api_settings

    def __init__(self, api_settings):
        self._api_settings = api_settings
