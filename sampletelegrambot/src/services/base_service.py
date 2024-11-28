from abc import ABC, abstractmethod

from sampletelegrambot.src.core.utils import SingletonABCMeta


class BaseService(ABC, metaclass=SingletonABCMeta):
    @abstractmethod
    def __init__(self):
        """Создание экземпляра сервиса"""

    @abstractmethod
    async def initialization(self):
        """
        Инициализирует сервис
        :return: None
        """
        pass

    @abstractmethod
    async def destroy(self):
        """
        Уничтожает сервис
        :return: None
        """
        pass