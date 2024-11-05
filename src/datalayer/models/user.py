from tortoise.models import Model
from tortoise import fields

# Model User
class UserModel(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=140)
    email = fields.CharField(max_length=140)
    password = fields.TextField()