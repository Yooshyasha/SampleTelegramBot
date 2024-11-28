from configparser import ConfigParser

TORTOISE_ORM = {
    "connections": {"default": "sqlite://data/db.sqlite3"},
    "apps": {
        "models": {
            "models": ["sampletelegrambot.src.app.database.models"],
            "default_connection": "default",
        },
    },
}


class Config:
    SECTION = "DEFAULT"

    config_parser = ConfigParser()
    config_parser.read("data/config.ini")

    bot_token = config_parser.get(SECTION, "bot_token")
