from tortoise import Model, fields


class User(Model):
    tg_id = fields.IntField()
