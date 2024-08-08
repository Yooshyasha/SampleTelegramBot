from configparser import ConfigParser


class Config:
    SECTION = "DEFAULT"

    config = ConfigParser()
    config.read('data/config.ini')   

    bot_token = config.get(SECTION, 'bot_token')
