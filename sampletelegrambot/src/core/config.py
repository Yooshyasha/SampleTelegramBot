from configparser import ConfigParser

TORTOISE_ORM = {
    "connections": {"default": "sqlite://data/db.sqlite3"},
    "apps": {
        "models": {
            "models": ["sampletelegrambot.src.app.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


class Config:
    SECTION = "DEFAULT"

    config = ConfigParser()
    config.read("data/config.ini")

    bot_token = config.get(SECTION, "bot_token")
