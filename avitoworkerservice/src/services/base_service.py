"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from abc import ABC, abstractmethod
from typing import Any

from avitoworkerservice.src.core.utils import SingletonABCMeta


class BaseService(ABC, metaclass=SingletonABCMeta):
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Создание экземпляра сервиса."""
        raise NotImplementedError

    @abstractmethod
    async def initialization(self) -> Any:
        """
        Инициализирует сервис
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    async def destroy(self) -> Any:
        """
        Уничтожает сервис
        :return: None
        """
        raise NotImplementedError
