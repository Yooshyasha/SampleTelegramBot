from typing import Optional, List
from sampletelegrambot.src.core import logger

from sampletelegrambot.src.core.tast_manager import TaskManager
from sampletelegrambot.src.core.utils import SingletonMeta
from sampletelegrambot.src.services.base_service import BaseService


class ServiceLoader(metaclass=SingletonMeta):
    _services: Optional[List[BaseService]] = []
    _is_initialized: bool = False

    def load(self):
        """Рекурсивно находим все подклассы BaseService"""
        self._services = [service() for service in self._get_all_subclasses(BaseService)]

    def _get_all_subclasses(self, base_class):
        subclasses = set(base_class.__subclasses__())
        for subclass in subclasses.copy():
            subclasses.update(self._get_all_subclasses(subclass))
        return subclasses

    def initialize(self):
        """Инициализирует все сервисы через TaskManager."""
        logger.debug("Запуск сервисов")
        if self._services is None:
            raise RuntimeError("Services are not loaded. Call 'load' first.")
        task_manager = TaskManager()
        for service in self._services:
            logger.debug(f"Запуск сервиса {service}")
            task_manager.add_task(service.initialization())

        self._is_initialized = True

    def destroy(self):
        logger.debug("Уничтожение сервисов")
        """Останавливает все сервисы через TaskManager."""
        if self._services is None:
            raise RuntimeError("Services are not loaded. Call 'load' first.")
        elif not self._is_initialized:
            raise RuntimeError("Services are not loaded. Call 'initialize' first.")

        task_manager = TaskManager()
        for service in self._services:
            logger.debug(f"Уничтожение сервиса {service}")
            task_manager.add_task(service.destroy())

        self._is_initialized = False