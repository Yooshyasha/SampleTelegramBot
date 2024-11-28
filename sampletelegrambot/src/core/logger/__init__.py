import logging
from loguru import logger

# logger = Logger()  ToDo реализовать собственный класс логера

logger.add("data/log/log_{time}.log", format="{time} {level} {message}", level="DEBUG")

logging.basicConfig(level=logging.INFO)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        level = logger.level(record.levelname).name
        logger.log(level, record.getMessage())