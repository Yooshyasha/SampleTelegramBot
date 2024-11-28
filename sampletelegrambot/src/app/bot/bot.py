from aiogram import Bot, Dispatcher

from .handlers.callback import callback_router
from .handlers.reply import reply_router

from .modules.middlewares import UserMiddleware

from sampletelegrambot.src.core import logger, ApplicationConfig


async def start_pooling():
    dp = Dispatcher()

    dp.message.middleware(UserMiddleware())
    dp.callback_query.middleware(UserMiddleware())

    dp.include_routers(
        callback_router,
        reply_router
    )

    logger.info('Starting bot pooling...')

    await dp.start_polling(Bot(token=ApplicationConfig().bot_token))
