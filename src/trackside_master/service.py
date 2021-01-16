'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import os
from common.logger import Logger, LogType
from common.version import COPYRIGHT_TEXT, LICENSE_TEXT, VERSION
from common.service_base import ServiceBase
from .api.utilities import UtilitiesApi
from .configuration_manager import ConfigurationManager

## Title text logged during initialisation.
TITLE_TEXT = 'Trackside Manager Master Service'

class Service(ServiceBase):
    """ Trackside master service class """

    def __init__(self, quart_app):
        super().__init__()

        ## Instance of the logging wrapper class
        self._logger = Logger()

        ## _is_initialised is inherited from parent class ServiceThread
        self._is_initialised = False

        self._quart_app = quart_app
        self._utilities_api = None
        self._config = None

    def _initialise(self) -> bool:
        self._logger.write_to_console = True
        self._logger.initialise()

        self._logger.log(LogType.Info, f'{TITLE_TEXT} {VERSION}')
        self._logger.log(LogType.Info, COPYRIGHT_TEXT)
        self._logger.log(LogType.Info, LICENSE_TEXT)

        config_file = os.getenv('TSM_MASTER_CONFIG')
        if not config_file:
            self._logger.log(LogType.Error,
                             'TSM_MASTER_CONFIG environment variable missing!')
            return False

        config_manager = ConfigurationManager()

        config = config_manager.parse_config_file(config_file)

        if not config:
            self._logger.log(LogType.Error, config_manager.last_error_msg)
            return False

        self._logger.log(LogType.Info, "Configuration file load...")

        self._logger.log(LogType.Info, "+==========================+")
        self._logger.log(LogType.Info, "|= Configuration Settings =|")
        self._logger.log(LogType.Info, "+==========================+")
        self._logger.log(LogType.Info, "Api Settings =>")

        auth_key_defined = 'Yes' if config.api_settings.auth_key else 'No'
        self._logger.log(LogType.Info,
                         f"Auth key defined   : {auth_key_defined}")
        self._logger.log(LogType.Info,
                         f"Use authentication : {config.api_settings.use_auth_key}")

        self._utilities_api = UtilitiesApi(self._quart_app, config)

        self._is_initialised = True

        return True

    async def _main_loop(self):
        # if not self._master_thread_class.initialise():
        #     return False
        pass

    def _shutdown(self):
        self._logger.log(LogType.Info, 'Shutting down...')
