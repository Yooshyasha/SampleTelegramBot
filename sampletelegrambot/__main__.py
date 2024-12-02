import asyncio
import signal
import traceback
from types import FrameType
from typing import Optional

from tortoise import Tortoise

from sampletelegrambot.src.core import logger, config
from sampletelegrambot.src.core.application_config import TORTOISE_ORM
from sampletelegrambot.src.core.service_loader import ServiceLoader
from sampletelegrambot.src.core.task_manager import TaskManager


class Application:
    def __init__(self, stop_event: Optional[asyncio.Event] = None) -> None:
        self.stop_event = stop_event or asyncio.Event()
        self.loader = ServiceLoader()
        self.task_manager = TaskManager()

    def setup_signal_handlers(self) -> None:
        """Установка обработчиков сигналов."""

        def handle_signal(signum: int, frame: Optional[FrameType]) -> None:
            self.stop_event.set()

        for sig in (signal.SIGINT, signal.SIGTERM):
            signal.signal(sig, handle_signal)

    async def monitor_tasks(self) -> None:
        """Мониторинг задач."""
        logger.debug("Мониторинг задач запущен")
        while not self.stop_event.is_set():
            await asyncio.sleep(1)
        logger.debug("Мониторинг завершён.")
        await self.graceful_shutdown()

    async def graceful_shutdown(self) -> None:
        """Асинхронное завершение приложения."""
        logger.debug(f"Завершаем приложение (таймаут {config.shutdown_timeout} сек.)...")
        try:
            self.loader.destroy()
            await asyncio.sleep(config.shutdown_timeout)
        except Exception:
            logger.error(f"Ошибка при уничтожении сервисов: {traceback.format_exc()}")
        finally:
            await self.task_manager.shutdown()
            await Tortoise.close_connections()
            logger.info("Приложение успешно завершено.")


async def main():
    app = Application()
    logger.info("Запуск приложения...")

    # Инициализация базы данных
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    logger.info("База данных инициализирована.")

    app.loader.load().initialize()
    app.setup_signal_handlers()

    monitor_task = asyncio.create_task(app.monitor_tasks())
    tasks = app.task_manager.get_tasks() + [monitor_task]

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        logger.warning("Задачи были отменены.")


def start():
    asyncio.run(main())
