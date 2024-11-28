# Пример использования: PaymentService

## Описание

`PaymentService` — это сервис для обработки платежей с использованием Telegram бота. Сервис проверяет статус платежей и выполняет соответствующие действия (подтверждение или отмену платежа) в цикле, с использованием асинхронных задач. Он предоставляет методы для создания платежей, проверки их статуса и генерации данных о платеже.

## Структура

- `__init__(self)` — Инициализирует сервис с ботом и необходимыми данными (например, токен провайдера).
- `create_payment(self, payment: Payment) -> Payment` — Создает новый платеж и запускает процесс проверки его статуса.
- `is_payed(self, payment: Payment) -> bool` — Проверяет, был ли платеж успешно произведен.
- `get_all_unpaid_payments_wait(self) -> List[Coroutine]` — Получает все непогашенные платежи и создает задачи для их обработки.
- `wait_payment_payed(self, payment: Payment) -> bool` — Асинхронно ожидает подтверждения оплаты или истечения времени действия платежа.
- `_payment_success(self, payment: Payment) -> bool` — Обрабатывает успешный платеж.
- `_payment_failure(self, payment: Payment) -> bool` — Обрабатывает неуспешный платеж.
- `generate_data(self, payment: Payment) -> dict` — Генерирует данные о платеже для дальнейшего использования.
- `initialization(self)` — Точка входа, где запускается цикл обработки платежей и проверки их статуса.

## Пример кода
В качестве примера дам реальный кейс
```python
class PaymentService(BaseService):
    def __init__(self):
        self.bot = bot
        self.provider_token = config.provider_token
        
        self.payment_processors = {
            'telegram': TelegramPaymentProcessor(bot, self.provider_token),
        }

        self.payment_life_time = timedelta(days=1)
        self.check_interval = timedelta(seconds=10)

    def get_payment_processor(self, payment_type: str):
        """Возвращает процессор для указанного метода оплаты."""
        processor = self.payment_processors.get(payment_type)
        if not processor:
            raise ValueError(f"Нет процессора для метода оплаты: {payment_type}")
        return processor

    async def create_payment(self, payment: Payment) -> Payment:
        payment.amount *= MULTIPLIER
        await payment.save()

        processor = self.get_payment_processor(payment.type)
        payment = await processor.create_payment(payment)

        TaskManager().add_task(self.wait_payment_payed(payment))
        return payment

    async def is_payed(self, payment: Payment) -> bool:
        processor = self.get_payment_processor(payment.type)
        return await processor.is_payed(payment)

    async def get_all_unpaid_payments_wait(self) -> List[Coroutine]:
        unpaid_payments = await Payment.filter(status="open")  # Замените на актуальные статусы
        unpaid_payments_wait = []

        for unpaid_payment in unpaid_payments:
            unpaid_payments_wait.append(self.wait_payment_payed(unpaid_payment))

        return unpaid_payments_wait

    async def wait_payment_payed(self, payment: Payment) -> bool:
        while True:
            payment = await Payment.get_or_none(id=payment.id)
            if not payment:
                logger.error(f"Платеж {payment.id} не найден.")
                return False

            current_time = datetime.now(timezone.utc)
            if current_time - payment.created_at >= self.payment_life_time:
                try:
                    return await self._payment_failure(payment)
                except Exception as e:
                    logger.error(str(e))

            if await self.is_payed(payment):
                try:
                    return await self._payment_success(payment)
                except Exception as e:
                    logger.error(str(e))

            await asyncio.sleep(self.check_interval.seconds)

    async def _payment_success(self, payment: Payment) -> bool:
        payment.status = "payed"  # Замените на актуальные статусы
        await payment.save()

        user = await payment.user

        user.balance += payment.amount
        await user.save()

        logger.debug(f"Баланс юзера {user.tg_id} изменен на {user.balance}")

        try:
            await self.bot.send_message(
                user.tg_id,
                "Оплата прошла успешно!"
            )
        except Exception as e:
            logger.error(str(e))

        return True

    async def _payment_failure(self, payment: Payment) -> bool:
        payment.status = "failed"  # Замените на актуальные статусы
        await payment.save()

        logger.debug(f"Платеж {payment.id} истек")

        processor = self.get_payment_processor(payment.type)
        await processor.cancel_payment(payment)

        user = await payment.user

        try:
            await self.bot.send_message(
                user.tg_id,
                "Оплата не прошла!"
            )
        except Exception as e:
            logger.error(str(e))

        return True

    async def generate_data(self, payment: Payment) -> dict:
        return {"payment_id": payment.id, "status": payment.status}

    async def initialization(self):
        """
        Инициализация сервисов: тут запускается цикл проверки платежей
        и выполнение всех задач, связанных с мониторингом состояний.
        """
        print("Инициализация PaymentService началась...")

        # Пример асинхронного выполнения: Проверка всех непогашенных платежей
        unpaid_payments = await self.get_all_unpaid_payments_wait()

        for payment_task in unpaid_payments:
            # Добавление задач в менеджер задач
            TaskManager().add_task(payment_task)

        # Дальше вы можете реализовать логику которая может быть циклична

    async def destroy(self): ...
```

## Как это работает

- Сервис `PaymentService` предназначен для обработки и мониторинга платежей.
- Он использует асинхронные задачи для цикличной проверки статуса платежей.
- Метод `initialization` запускает основной цикл проверки платежей, который на момент запуска не являются оплаченными, добавляя задачи в `TaskManager` для выполнения.
- В случае успешного или неудачного платежа сервис отправляет уведомления пользователям через Telegram.

## Примечания

1. Все данные и статус платежей должны быть правильно настроены в вашем проекте (например, `Payment` и `PaymentStatuses`).
2. Для работы с Telegram ботом используйте библиотеку `aiogram` и убедитесь, что ваш бот настроен корректно.
3. Для цикла мониторинга и выполнения задач используется асинхронное ожидание (`asyncio.sleep`) для эффективной работы.
4. Конкретно этот сервис не цикличен в `initializstion`, но может быть таким
