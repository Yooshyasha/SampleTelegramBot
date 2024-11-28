import asyncio

from tortoise import Tortoise

from sampletelegrambot.src.app.bot.bot import start_pooling
from sampletelegrambot.src.core.application_config import TORTOISE_ORM
from sampletelegrambot.src.core import logger


async def main():
    logger.info("Loading...")
    await Tortoise.init(config=TORTOISE_ORM)

    await Tortoise.generate_schemas()
    logger.info("Database initialized successfully.")
    await start_pooling()


def start():
    asyncio.run(main())
