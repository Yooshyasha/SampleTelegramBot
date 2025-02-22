"""Copyright (c) 2025, Yooshyasha
BSD 3-Clause License
All rights reserved."""

from tortoise import Model, fields


class User(Model):
    tg_id = fields.IntField()
