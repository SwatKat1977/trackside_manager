'''
Copyright (C) 2020-2021 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''

class ConfigurationSchema:

    class Elements:
        # -- Top-level json elements --
        toplevel_api_settings = 'api settings'

        # -- Api Settings sub-elements --
        # --------------------------------
        api_settings_auth_key = 'authentication key'
        api_settings_use_auth = 'use authentication'

    json_schema = \
    {
        "$schema": "http://json-schema.org/draft-07/schema#",

        "type" : "object",
        "additionalProperties" : False,

        "properties":
        {
            'api settings':
            {
                "additionalProperties" : False,
                "properties":
                {
                    'authentication key':
                    {
                        "type" : "string"
                    },
                    'use authentication':
                    {
                        "type" : "bool"
                    }
                },
                "required" : ['authentication key', 'use authentication']
            }
        },
        "required" : ['api settings']
    }
