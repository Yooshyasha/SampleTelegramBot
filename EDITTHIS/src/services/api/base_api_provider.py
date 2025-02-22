"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from abc import abstractmethod

from EDITTHIS.src.core.utils import SingletonABCMeta


class BaseAPIProvider(metaclass=SingletonABCMeta):
    """Класс, для инкапсулирования логики, связанной со сторонними API"""
    _is_initialized: bool = False

    async def initialize(self):
        """Инициализация API провайдера"""
        if not self._is_initialized:
            self._is_initialized = True
            return await self._initialize()

    @abstractmethod
    async def _initialize(self):
        raise NotImplementedError

    @abstractmethod
    async def destroy(self):
        """Метод, в котором будут проходить запросы, связанные с дисконнектом от API."""
        raise NotImplementedError
