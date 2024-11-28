from typing import Callable, Awaitable, Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject

from ...database.models import User


class UserMiddleware(BaseMiddleware):
    def __init__(self):
        ...

    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]) -> Any:

        user, created = await User.get_or_create(tg_id=event.from_user.id)
        data.update({"user": user, "user_first_start": created})

        return await handler(event, data)