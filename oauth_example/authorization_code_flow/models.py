from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    """The User model."""

    uuid = fields.UUIDField()

    username = fields.CharField(max_length=150, unique=True)

    email = fields.CharField(max_length=255, unique=True)

    picture = fields.CharField(max_length=500)

    created_at = fields.DatetimeField(auto_now_add=True)

    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"

    class PydanticMeta:
        exclude = ["id", "uuid"]


class StateCode(models.Model):
    """The StateCode model."""

    code = fields.CharField(max_length=500, unique=True)
    is_used = fields.BooleanField()


User_Pydantic = pydantic_model_creator(User, name="User")
