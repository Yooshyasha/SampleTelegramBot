## Здесь используется [шаблон](https://github.com/Yooshyasha/SampleTelegramBot) / Here used [template](https://github.com/Yooshyasha/SampleTelegramBot)

### Основная идея шаблона / Main idea of the template
- **Сервисы и внутренняя магия / Services and internal magic**  
  Шаблон построен на использовании сервисов с легкой "внутренней магией", упрощающей логику приложения.  
  The template is built using services with light "internal magic" that simplifies the application logic.

- **DI и IoC / DI and IoC**  
  В шаблоне реализованы Dependency Injection (DI) и Inversion of Control (IoC). Подробности смотрите в директории `/docs`.  
  The template implements Dependency Injection (DI) and Inversion of Control (IoC). For details, see the `/docs` directory.

- **Неразрушаемое ядро / Non-destructive core**  
  Директория `/src/core` содержит важную внутреннюю логику, которая обеспечивает магию шаблона. Рекомендуется не редактировать файлы в этой папке.  
  The `/src/core` directory contains important internal logic that powers the magic of the template. It is recommended not to edit files in this folder.

- **Наследование сервисов / Service inheritance**  
  Все сервисы должны наследоваться от класса `BaseService`.  
  All services should inherit from the `BaseService` class.

- **Настройка проекта / Project setup**  
  Если вы только начинаете работу, отредактируйте слово `EDITTHIS` в названии проекта. Не забудьте внести изменения в файлы `pyproject.toml` и `docker-compose`.  
  If you are just starting, edit the word `EDITTHIS` in the project name. Don't forget to make changes in `pyproject.toml` and `docker-compose`.

---

### Структура проекта / Project structure

- **`/data`**  
  Изменяемые данные. Здесь уже находятся конфигурация и база данных (если не переключились с sqlite3).  
  Editable data. Configuration and database (if you didn't switch from sqlite3) are already here.

- **`EDITTHIS/src`**  
  Корневая директория, откуда начинается весь проект.  
  The root directory where the entire project starts.

- **`/src/app`**  
  Приложение. Здесь располагаются файлы, связанные с Telegram-ботом.  
  Application folder. Here are the files related to the Telegram bot.

- **`/src/core`**  
  Ядро проекта. Содержит реализацию магии для сервисов, утилиты и другие важные классы. Редактировать не рекомендуется.  
  Core logic. Contains the implementation of the magic for services, utilities, and other important classes. It is recommended not to edit.

- **`/src/database`**  
  База данных проекта. В этой папке находятся модели и другая логика, связанная с БД.  
  Database folder. This folder contains models and other DB-related logic.

- **`/src/services`**  
  Модуль для сервисов и их API.  
  Services module and their APIs.

---

### Рекомендации / Recommendations

- **Работа с API / Work with API**  
  Пишите или интегрируйте классы, отвечающие за связь с API, в `/src/services/api`. Это касается только API провайдеров.  
  Write or integrate classes that handle API interactions in `/src/services/api`. This applies only to API providers.

- **Избегание цикличных импортов / Avoid cyclic imports**  
  Если возникает цикличный импорт, попробуйте использовать отложенный импорт или отказаться от лишних импортов. Это довольно распространённая проблема в данном шаблоне.  
  If you run into cyclic imports, try using deferred imports or avoid unnecessary imports. This is a common problem in this template.

- **Полные пути при импорте / Full import paths**  
  Импортируйте сервисы по полному пути, без сокращений в файле `__init__.py`, чтобы избежать циклических зависимостей.  
  Import services by their full path, without shortcuts in `__init__.py`, to avoid cyclic dependencies.

---

Эта структура и рекомендации помогут вам быстрее освоиться с шаблоном и создать стабильное приложение, используя всю "магическую" силу, заложенную в его основу.  
This structure and recommendations will help you get up to speed with the template and create a stable application using all the "magical" powers built into its core.

> Важно! Использование этого шаблона требует сохранения указания автора в коде и документации.  
> Important! Using this template requires maintaining the author's credits in the code and documentation.
