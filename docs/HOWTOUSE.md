## HOW TO USE

Этот шаблон предоставляет структуру для создания и управления сервисами с автоматическим управлением их жизненным циклом. Каждый сервис будет автоматически создавать свой экземпляр и управляться системой без дополнительных действий с вашей стороны. Следуйте приведённым ниже инструкциям для правильного использования сервисов.

### Структура сервиса

1. **Создание экземпляра (Singleton)**:
    - Каждый сервис создаётся в единственном экземпляре. Паттерн Singleton гарантирует, что сервис будет представлен только одним экземпляром в приложении.
    - Экземпляры сервисов создаются автоматически системой, и вам не нужно вручную создавать их.

2. **Инициализация**:
    - Инициализация сервиса происходит автоматически при вызове метода `initialize` в классе `ServiceLoader`.
    - Логика инициализации для каждого сервиса прописана в методе `initialization`, и она будет автоматически вызвана для каждого сервиса после загрузки.

3. **Уничтожение**:
    - Уничтожение сервиса также управляется системой. При завершении работы приложения или при необходимости освобождения ресурсов, сервисы будут корректно уничтожены через метод `destroy`.

### Создание нового сервиса

1. Для добавления нового сервиса вам нужно создать новый класс, который будет наследоваться от `BaseService`.
2. Реализуйте методы `initialization` и `destroy` для выполнения логики вашего сервиса.

Пример:

```python
from EDITTHIS.src.services.base_service import BaseService


class MyService(BaseService):
   def initialization(self):
      # Логика инициализации
      print("MyService is initialized")

   def destroy(self):
      # Логика уничтожения
      print("MyService is destroyed")
```

#### ВАЖНО: 
   - Каждый новый сервис нужно обязательно прописать в `src/services/__init__`

### Как использовать сервисы

1. **Автоматическая загрузка сервисов**:
    - Все сервисы загружаются автоматически при вызове метода `load` в классе `ServiceLoader`. Этот метод рекурсивно находит все классы, наследующие от `BaseService`, и автоматически создаёт их экземпляры.

```python
from EDITTHIS.src.core.service_loader import ServiceLoader

# Загрузите все сервисы (этот шаг выполняется автоматически при запуске приложения)
service_loader = ServiceLoader()
service_loader.load()
```
2. **Получение экземпляра сервиса**:
   - Для того, что бы получить экземпляр сервиса (напомню, что каждый сервис - Singleton) - вам нужно использовать ``.get_instance``

 ```python
from EDITTHIS.src.services.my_service import MyService

my_service = MyService.get_instance()
```

3. **Автоматическая инициализация сервисов**:
    - Для инициализации сервисов достаточно вызвать метод `initialize`. Это автоматически запустит инициализацию для каждого загруженного сервиса.

```python
# Инициализируем все сервисы (этот шаг выполняется автоматически при запуске приложения)
service_loader.initialize()
```

4. **Автоматическое уничтожение сервисов**:
    - Все сервисы будут автоматически уничтожены при завершении работы приложения. Вы можете вызвать метод `destroy` в случае, если необходимо вручную остановить сервисы.

```python
# Уничтожаем все сервисы (этот шаг выполняется автоматически при завершении работы приложения)
service_loader.destroy()
```

### Примечания

- **Автоматическое управление экземплярами**: Экземпляры сервисов создаются и уничтожаются автоматически, и вам не нужно вручную создавать или удалять их.
- **Инициализация и уничтожение**: Логика инициализации и уничтожения прописана внутри каждого сервиса. Всё, что вам нужно сделать, — это реализовать методы `initialization` и `destroy` для вашего сервиса.
- **Singleton**: Каждый сервис создаётся только один раз, и вы можете быть уверены, что его экземпляр будет уникальным в рамках всего приложения.