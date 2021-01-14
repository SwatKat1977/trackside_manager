'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
import json
from quart import request
from common.http_status_code import HTTPStatusCode
from common.logger import LogType
from common.mime_type import MIMEType

HEADERKEY_AUTH = 'AuthKey'

class UtilitiesApi:

    def __init__(self, interface_instance):
        self._interface = interface_instance
        self._auth_key = 'TesT_KeY@{2021}'

        # Add route : /utilities/ping
        self._interface.add_url_rule('/utilities/ping',
            methods = ['GET'], view_func = self._ping)

        # Add route : /utilities/status
        self._interface.add_url_rule('/utilities/status',
            methods = ['GET'], view_func = self._status)

    async def _ping(self):
        return self._interface.response_class(response = 'pong',
            status = HTTPStatusCode.OK, mimetype = MIMEType.Text)

    async def _status(self):

        # Validate the request to ensure the auth key is present and valid.
        validate_return = self._validate_auth_key()
        if validate_return is not HTTPStatusCode.OK:

            return self._interface.response_class(
                response = json.dumps('Invalid authentication key'),
                status = validate_return, mimetype = MIMEType.Text)

        status_response = {
            'health': 'Fully Functional'
        }

        return self._interface.response_class(
            response = json.dumps(status_response),
            status = HTTPStatusCode.OK, mimetype = MIMEType.JSON)

    def _validate_auth_key(self):
        """!@brief Validate the authentication key for a request.
        @param self The object pointer.
        @returns a status code:
        * 200 (OK) - Authentication key good
        * 401 (Unauthenticated) - Missing or invalid authentication key
        * 403 (Forbidden) - Invalid authentication key
        """

        # Verify that an authorisation key exists in the request header.
        if HEADERKEY_AUTH not in request.headers:
            return HTTPStatusCode.Unauthenticated

        authorisation_key = request.headers[HEADERKEY_AUTH]

        # Verify the authorisation key against what is specified in the
        # configuration file.  If it isn't valid then return 403 (Forbidden).
        if authorisation_key != self._auth_key:
            return HTTPStatusCode.Forbidden

        return HTTPStatusCode.OK
