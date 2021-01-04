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

def main() -> None:
    """!@brief Main entry point
    @return None
    """
    service = Service()

    if not service.start():
        sys.exit()

main()
