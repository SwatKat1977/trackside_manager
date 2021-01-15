'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import json
import jsonschema
from .configuration import ApiSettings, Configuration
from .configuration_schema import ConfigurationSchema as schema

class ConfigurationManager:
    ''' Configuration Manager '''

    ## Property getter : Last error message
    @property
    def last_error_msg(self):
        return self._last_error_msg

    def __init__(self) -> object:
        self._last_error_msg = ''

    def parse_config_file(self, filename) -> Configuration:
        #  @param self The object pointer.

        self._last_error_msg = ''

        try:
            with open(filename) as file_handle:
                file_contents = file_handle.read()

        except IOError as excpt:
            self._last_error_msg = "Unable to open configuration file '" + \
                f"{filename}', reason: {excpt.strerror}"
            return None

        try:
            raw_config = json.loads(file_contents)

        except json.JSONDecodeError as excpt:
            self._last_error_msg = "Unable to parse configuration file" + \
                f"{filename}, reason: {excpt}"
            return None

        try:
            jsonschema.validate(instance=raw_config, schema=schema.json_schema)

        except jsonschema.exceptions.ValidationError:
            self._last_error_msg = f"Configuration file {filename} failed " + \
                "to validate against expected schema.  Please check!"
            return None

        raw_api_settings = raw_config[schema.Elements.toplevel_api_settings]
        api_settings = self._process_api_settings(raw_api_settings)

        return Configuration(api_settings)

    def _process_api_settings(self, settings) -> ApiSettings:
        '''
        ## Process the api settings section.
        #  @param self The object pointer.
        '''
        auth_key = settings[schema.Elements.api_settings_auth_key]
        use_auth_key = settings[schema.Elements.api_settings_use_auth]
        return ApiSettings(auth_key, use_auth_key)
