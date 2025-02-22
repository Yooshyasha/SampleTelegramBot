"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from typing_extensions import override

from EDITTHIS.src.app.bot import start_pooling, dp
from .base_service import BaseService


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
