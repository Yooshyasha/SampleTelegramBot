from abc import ABC, abstractmethod

from sampletelegrambot.src.core.utils import SingletonABCMeta


class BaseService(ABC, metaclass=SingletonABCMeta):
    @abstractmethod
    async def initialization(self): ...

    @abstractmethod
    async def destroy(self): ...