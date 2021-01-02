'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
#pylint: disable=wrong-import-position
import sys
sys.path.insert(0,'.')
from quart import Quart
from .service import Service

app = Quart(__name__)

service = Service()

if not service.initialise():
    sys.exit()

service.run()

# ## Flask startup function.
# #  @param test_config Unused.
# def create_app(test_config=None) -> Quart:
#     """!@brief is_running property (setter).
#     @param test_config Configuration that defaults to None.
#     @return Quart application
#     """

#     #app = TracksideMaster()
#     #app.run()

#     return app

'''
def main() -> None:
    """!@brief Main entry point
    @return None
    """
    app = TracksideMaster()

    app.run()

main()
'''
