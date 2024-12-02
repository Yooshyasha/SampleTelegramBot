from typing import List

from sampletelegrambot.src.app.database.models import User
from .base_service import BaseService


class UserService(BaseService):
    """Сервис используемый для кэширования пользователей"""

    def __init__(self) -> None:
        self._users_list: List[User] = []

    async def initialization(self):
        self._users_list = await User.all()

    async def destroy(self):
        del self._users_list

    @staticmethod
    async def get_users() -> List[User]:
        return await User.all()

    def add_user(self, user: User):
        self._users_list.append(user)

    async def remove_user(self, user: User):
        self._users_list.remove(user)
        await user.delete()

    async def get_user(self, user_tg_id: int) -> User:
        for user in self._users_list:
            if user.tg_id == user_tg_id:
                return user

        return await User.get(tg_id=user_tg_id)
