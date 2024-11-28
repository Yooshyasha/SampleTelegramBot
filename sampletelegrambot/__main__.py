import asyncio
import atexit
import signal

from tortoise import Tortoise

from sampletelegrambot.src.core import logger
from sampletelegrambot.src.core.application_config import TORTOISE_ORM
from sampletelegrambot.src.core.service_loader import ServiceLoader
from sampletelegrambot.src.core.tast_manager import TaskManager



async def main():
    loader = ServiceLoader()
    task_manager = TaskManager()
    loader.load()

    logger.info("Loading...")

    # Регистрация сигналов остановки приложения
    def graceful_exit(signum=None, frame=None):
        loader.destroy()

    atexit.register(graceful_exit)
    signal.signal(signal.SIGINT, graceful_exit)
    signal.signal(signal.SIGTERM, graceful_exit)

    # Инициализация базы данных
    await Tortoise.init(config=TORTOISE_ORM)

    await Tortoise.generate_schemas()
    logger.info("Database initialized successfully.")

    loader.initialize()  # Инициализация сервисов

    await asyncio.gather(*task_manager.get_tasks())  # Запуск задач


def start():
    asyncio.run(main())
