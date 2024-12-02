from typing_extensions import override

from sampletelegrambot.src.app.bot import start_pooling, dp
from .base_service import BaseService
from .user_service import UserService
from ..core import logger


class BotService(BaseService):
    def __init__(self):
        pass

    @override
    async def initialization(self):
        """
        Запуск телеграм бота
        :return:
        """
        return await start_pooling()

    @override
    async def destroy(self):
        await dp.stop_polling()
