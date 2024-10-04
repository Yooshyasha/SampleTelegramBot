import asyncio

from tortoise import Tortoise

from sampletelegrambot.src.app.bot.bot import start_pooling
from sampletelegrambot.src.core.config import TORTOISE_ORM

from aerich import Command

from y24fw.logger.logger import logger


async def migration():
    try:
        migration_command = Command(tortoise_config=TORTOISE_ORM)
        await migration_command.init()
        await migration_command.migrate()
    except Exception as ex:
        logger.error(ex)


async def main():
    logger.info("Loading...")
    await Tortoise.init(config=TORTOISE_ORM)

    await Tortoise.generate_schemas()
    logger.info("Database initialized successfully.")
    await start_pooling()


def start():
    asyncio.run(main())
