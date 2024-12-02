# **DI - Аутсорсинг внедрения зависимостей**

С помощью этой базы вы можете **легко прописывать зависимости между классами** и удобно их инжектировать, минимизируя
нужду в ручной настройке зависимостей.

## Пример использования

```python
class UserService(BaseService):
    """Сервис, используемый для кэширования пользователей"""

    def __init__(self) -> None:
        self._users_list: List[User] = []

    async def initialization(self):
        """Загружает всех пользователей"""
        self._users_list = await User.all()

    async def destroy(self):
        """Очищает кэш пользователей"""
        del self._users_list

    @staticmethod
    async def get_users() -> List[User]:
        """Возвращает всех пользователей"""
        return await User.all()

    def add_user(self, user: User):
        """Добавляет пользователя в кэш"""
        self._users_list.append(user)

    async def remove_user(self, user: User):
        """Удаляет пользователя из кэша"""
        self._users_list.remove(user)
        await user.delete()

    async def get_user(self, user_tg_id: int) -> User:
        """Получает пользователя по его Telegram ID"""
        for user in self._users_list:
            if user.tg_id == user_tg_id:
                return user

        return await User.get(tg_id=user_tg_id)
```

```python
class BotService(BaseService):
    """Сервис для управления ботом"""

    def __init__(self, user_service: UserService):
        """Инжектируем UserService в BotService"""
        self.user_service = user_service

    @override
    async def initialization(self):
        """
        Запуск телеграм-бота
        """
        logger.debug(f"Пользователей бота: {len(await self.user_service.get_users())}")
        return await start_pooling()

    @override
    async def destroy(self):
        """Останавливаем бота"""
        await dp.stop_polling()
```

### Как это работает?

1. Мы создаем сервис **UserService**, который инкапсулирует бизнес-логику, связанную с пользователями. Он управляет их
   кэшированием, добавлением, удалением и получением данных.

2. Затем, мы легко внедряем **UserService** в **BotService**. Для этого достаточно указать зависимость через конструктор
   и использовать её в методах сервиса.

3. Внедрение зависимостей (DI) автоматически обработается с помощью **ServiceLoader**, который создаст и
   проинициализирует все сервисы, а также их зависимости.

---

### Преимущества

- **Простота**: Внедрение зависимостей становится максимально простым, без лишних настроек.
- **Модульность**: Логика сервисов разделена на маленькие, легко тестируемые блоки.
- **Гибкость**: Легко менять зависимости между сервисами без изменения их интерфейсов.

---

**ServiceLoader** возьмет на себя все необходимые действия по загрузке и инициализации сервисов, вам не нужно заботиться
о сложных настройках или порядке зависимостей.
