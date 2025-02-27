"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from abc import ABCMeta


class SingletonMeta(type):
    """
    Метакласс для реализации Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        return cls.get_instance(*args, **kwargs)

    def get_instance(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Создаем единственный экземпляр
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonABCMeta(ABCMeta, SingletonMeta):
    pass
