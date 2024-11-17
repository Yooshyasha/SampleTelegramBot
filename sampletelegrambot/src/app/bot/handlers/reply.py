from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter, CommandStart, Command

from sampletelegrambot.src.app.database.models import User
from sampletelegrambot.src.core.json_answer import JsonAnswer

reply_router = Router()


@reply_router.message(CommandStart())
async def start_reply(message: Message):
    await message.answer(text=await JsonAnswer.get("start"))
