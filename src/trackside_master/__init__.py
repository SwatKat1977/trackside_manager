'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
#pylint: disable=wrong-import-position
import asyncio
import sys
sys.path.insert(0,'.')
from quart import Quart
from .service import Service

app = Quart(__name__)

service = Service()

@app.before_serving
async def startup() -> None:
    """!@brief Code executed before Quart has began serving http requests.
    @return None
    """
    app.service_task = asyncio.ensure_future(service.start())

@app.after_serving
async def shutdown() -> None:
    """!@brief Code executed after Quart has stopped serving http requests.
    @return None
    """
    service.signal_shutdown_requested()

    while not service.shutdown_completed:
        await asyncio.sleep(0.5)

if not service.initialise():
    sys.exit()
