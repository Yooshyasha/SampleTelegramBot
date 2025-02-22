"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

import asyncio
from typing import List, Coroutine

from EDITTHIS.src.core import logger


class TaskManager:
    _instance = None
    _tasks: List[asyncio.Task] = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_task(self, coro: Coroutine):
        """Добавляет асинхронную задачу в список и сразу запускает её."""
        task = asyncio.create_task(coro)
        self._tasks.append(task)
        logger.info(f"Task started: {coro}")

    def get_tasks(self):
        """Возвращает список текущих задач."""
        return self._tasks

    async def shutdown(self):
        """Останавливает все запущенные задачи."""
        for task in self._tasks:
            try:
                task.cancel()
            except asyncio.CancelledError:
                pass
        logger.debug("Все задачи остановлены.")