from typing_extensions import override

from sampletelegrambot.src.app.bot import start_pooling, dp
from .base_service import BaseService
from .user_service import UserService
from ..core import logger


class BotService(BaseService):
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @override
    async def initialization(self):
        """
        Запуск телеграм бота
        :return:
        """
        logger.debug(f"Пользователей бота: {len(await self.user_service.get_users())}")
        return await start_pooling()

    @override
    async def destroy(self):
        await dp.stop_polling()
