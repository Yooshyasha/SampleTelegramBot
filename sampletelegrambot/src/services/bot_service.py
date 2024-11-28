from sampletelegrambot.src.app.bot.bot import start_pooling
from .base_service import BaseService

class BotService(BaseService):
    async def initialization(self):
        return await start_pooling()

    async def destroy(self): return