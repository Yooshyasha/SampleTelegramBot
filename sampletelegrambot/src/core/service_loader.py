import inspect
from typing import Type, Dict

from sampletelegrambot.src.core import logger
from sampletelegrambot.src.core.task_manager import TaskManager
from sampletelegrambot.src.core.utils import SingletonMeta
from sampletelegrambot.src.services.base_service import BaseService


class ServiceLoader(metaclass=SingletonMeta):
    _services: Dict[Type[BaseService], BaseService] = {}
    _is_initialized: bool = False

    def load(self) -> "ServiceLoader":
        """
        Загружает сервисы, создавая их экземпляры с разрешением зависимостей.
        :return: ServiceLoader
        """
        for service_class in self._get_all_subclasses(BaseService):
            if service_class not in self._services:
                self._services[service_class] = self._create_service(service_class)
        return self

    def _create_service(self, service_class: Type[BaseService]) -> BaseService:
        """
        Создаёт экземпляр сервиса, разрешая его зависимости.
        :param service_class: Класс сервиса.
        :return: Экземпляр сервиса.
        """
        constructor = inspect.signature(service_class.__init__)
        dependencies = {}

        for name, param in constructor.parameters.items():
            if name == "self":
                continue

            dependency_type = param.annotation
            if dependency_type == param.empty:
                raise ValueError(f"Dependency '{name}' in {service_class} is missing a type annotation")

            if dependency_type not in self._services:
                self._services[dependency_type] = self._create_service(dependency_type)

            dependencies[name] = self._services[dependency_type]

        return service_class(**dependencies)

    def _get_all_subclasses(self, base_class) -> set[Type[BaseService]]:
        """
        Рекурсивно возвращает все дочерние классы.
        :param base_class: Класс, у которого ищутся все дочерние классы.
        :return: Набор классов.
        """
        subclasses = set(base_class.__subclasses__())
        for subclass in subclasses.copy():
            subclasses.update(self._get_all_subclasses(subclass))
        return subclasses

    def initialize(self) -> None:
        """
        Инициализирует все сервисы через TaskManager.
        """
        logger.debug("Запуск сервисов")
        if not self._services:
            raise RuntimeError("Services are not loaded. Call 'load' first.")

        task_manager = TaskManager()
        for service in self._services.values():
            logger.debug(f"Запуск сервиса {service}")
            task_manager.add_task(service.initialization())

        self._is_initialized = True

    def destroy(self) -> None:
        """
        Уничтожает все сервисы.
        """
        logger.debug("Уничтожение сервисов")
        if not self._services:
            raise RuntimeError("Services are not loaded. Call 'load' first.")
        elif not self._is_initialized:
            raise RuntimeError("Services are not initialized. Call 'initialize' first.")

        task_manager = TaskManager()
        for service in self._services.values():
            logger.debug(f"Уничтожение сервиса {service}")
            task_manager.add_task(service.destroy())

        self._is_initialized = False
