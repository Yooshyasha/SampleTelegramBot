from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter
from aiogram.filters.callback_data import CallbackData

from sampletelegrambot.src.app.database.models import User


callback_router = Router()


# @callback_router.callback_query_handler(CallbackData("data"))
# async def start_callback(callback_query: CallbackQuery):
#     ...
