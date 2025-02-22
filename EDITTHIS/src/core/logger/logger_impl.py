"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from loguru import Logger as LoguruLogger

@DeprecationWarning
class Logger(LoguruLogger):
    def __init__(self):
        super().__init__()
