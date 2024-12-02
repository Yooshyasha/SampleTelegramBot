from typing import Optional, List, Type
from sampletelegrambot.src.core import logger

from sampletelegrambot.src.core.tast_manager import TaskManager
from sampletelegrambot.src.core.utils import SingletonMeta
from sampletelegrambot.src.services.base_service import BaseService


class ServiceLoader(metaclass=SingletonMeta):
    _services: Optional[List[BaseService]] = []
    _is_initialized: bool = False

    def load(self) -> "ServiceLoader":
        """
        Загружает сервисы, создавая их экземпляр
        :return: None
        """
        self._services = [service() for service in self._get_all_subclasses(BaseService)]
        return self

    def _get_all_subclasses(self, base_class) -> set[Type[BaseService]]:
        """
        Рекурсивно возвращает все дочерние классы
        :param base_class: Класс, у которого ищутся все дочерние классы
        :return:
        """
        subclasses = set(base_class.__subclasses__())
        for subclass in subclasses.copy():
            subclasses.update(self._get_all_subclasses(subclass))
        return subclasses

    def initialize(self) -> None:
        """
        Инициализирует все сервисы через TaskManager
        :return: None
        """
        logger.debug("Запуск сервисов")
        if self._services is None:
            raise RuntimeError("Services are not loaded. Call 'load' first.")
        task_manager = TaskManager()
        for service in self._services:
            logger.debug(f"Запуск сервиса {service}")
            task_manager.add_task(service.initialization())

        self._is_initialized = True

    def destroy(self) -> None:
        """
        Уничтожает все сервисы
        :return: None
        """
        logger.debug("Уничтожение сервисов")
        if self._services is None:
            raise RuntimeError("Services are not loaded. Call 'load' first.")
        elif not self._is_initialized:
            raise RuntimeError("Services are not loaded. Call 'initialize' first.")

        task_manager = TaskManager()
        for service in self._services:
            logger.debug(f"Уничтожение сервиса {service}")
            task_manager.add_task(service.destroy())

        self._is_initialized = False
