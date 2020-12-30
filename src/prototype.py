'''
Copyright (C) 2020 Trackside Manager Project

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
'''
from framework import Framework

class App(Framework):
    def __init__(self):
        super().__init__()

def main():
    app = App()

    print(app.is_running)

main()
