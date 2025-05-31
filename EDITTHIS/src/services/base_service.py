"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from abc import ABC, abstractmethod

from EDITTHIS.src.core.utils import SingletonABCMeta


class BaseService(ABC, metaclass=SingletonABCMeta):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """Создание экземпляра сервиса."""
        raise NotImplementedError

    @abstractmethod
    async def initialization(self):
        """
        Инициализирует сервис
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    async def destroy(self):
        """
        Уничтожает сервис
        :return: None
        """
        raise NotImplementedError
