from typing_extensions import override

from sampletelegrambot.src.app.bot import start_pooling
from .base_service import BaseService

class BotService(BaseService):
    @override
    def __init__(self): ...

    @override
    async def initialization(self):
        """
        Запуск телеграм бота
        :return:
        """
        return await start_pooling()

    @override
    async def destroy(self): return