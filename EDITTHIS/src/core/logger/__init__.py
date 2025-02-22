"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

import logging
from loguru import logger as loguru_logger

# logger = Logger()  ToDo реализовать собственный класс логера
logger = loguru_logger

logger.add("data/log/log_{time}.log", format="{time} {level} {message}", level="DEBUG")

logging.basicConfig(level=logging.INFO)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())