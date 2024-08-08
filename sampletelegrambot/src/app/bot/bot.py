from aiogram import Bot, Dispatcher

from .handlers.callback import callback_router
from.handlers.reply import reply_router

from .modules.middlewares import UserMiddleware

from y24fw.aiogram.fsm import FSMMiddleware
from y24fw.logger.logger import logger

from ...core.config import Config


async def start_pooling():
    dp = Dispatcher()

    dp.message.middleware(UserMiddleware())
    dp.callback_query.middleware(UserMiddleware())

    dp.message.middleware(FSMMiddleware())  # can remove

    logger.info('Starting bot pooling...')

    await dp.start_polling(Bot(token=Config().bot_token))    
