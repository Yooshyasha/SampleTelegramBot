from configparser import ConfigParser

TORTOISE_ORM = {
    "connections": {"default": "sqlite://data/db.sqlite3"},
    "apps": {
        "models": {
            "models": ["sampletelegrambot.src.database.models"],
            "default_connection": "default",
        },
    },
}


class ApplicationConfig:
    DEFAULT_SECTION = "DEFAULT"
    APPLICATION_SECTION = "APPLICATION"

    config_parser = ConfigParser()
    config_parser.read("data/config.ini")

    #  DEFAULT
    bot_token = config_parser.get(DEFAULT_SECTION, "bot_token")

    #  APPLICATION
    shutdown_timeout = config_parser.getint(APPLICATION_SECTION, "shutdown_timeout")
