from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter, CommandStart, Command

from ...database.models import User


reply_router = Router()


# @reply_router.message(CallbackData("data"))
# async def start_reply(message: Message):
#     ...