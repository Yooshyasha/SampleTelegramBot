import asyncio

from tortoise import Tortoise

from .src.app.bot.bot import start_pooling

from y24fw.logger.logger import logger

async def main():
    logger.info('Loading...')
    await Tortoise.init(
        db_url='sqlite://data/db.sqlite3',
        modules={'models': ['sampletelegrambot.src.app.database.models']}
    )

    await Tortoise.generate_schemas()
    logger.info('Database initialized successfully.')
    await start_pooling()

def start():
    asyncio.run(main())