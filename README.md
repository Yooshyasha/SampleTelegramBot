How to use:

### Install poetry
```bash
pipx install poetry 1.8.3
```

### Edit project
- - Edit pyproject.toml (edit name)
- - Edit package name (sampletelegrambot)
- - Edit tortoise models path (main.py)
```python
await Tortoise.init(
    db_url='sqlite://data/db.sqlite3',
    modules={'models': ['sampletelegrambot.src.app.database.models']}
)
```

### Start
```bash
poetry run main
```
