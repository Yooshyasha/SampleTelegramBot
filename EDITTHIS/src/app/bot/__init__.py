"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from aiogram import Bot, Dispatcher

from EDITTHIS.src.core import logger, config
from .handlers.reply import reply_router
from .modules.middlewares import UserMiddleware

dp = Dispatcher()
bot = Bot(token=config.bot_token)

async def start_pooling():
    dp.message.middleware(UserMiddleware())
    dp.callback_query.middleware(UserMiddleware())

    dp.include_routers(
        reply_router,
    )

    logger.info('Starting bot pooling...')

    await dp.start_polling(bot)
