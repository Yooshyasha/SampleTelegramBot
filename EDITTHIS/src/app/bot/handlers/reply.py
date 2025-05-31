"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from EDITTHIS.src.core.json_answer import JsonAnswer

reply_router = Router()


@reply_router.message(CommandStart())
async def start_reply(message: Message):
    await message.answer(text=await JsonAnswer.get("start"))
