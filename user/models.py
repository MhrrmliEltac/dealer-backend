from tortoise import models, fields
from utils.hashing import Hash


class User(models.Model):
    id = fields.IntField(primary_key=True)
    fullname = fields.CharField(max_length=150)
    phone_number = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=255)
    monthly_volume = fields.IntField()
    suggestion = fields.CharField(max_length=255)

    def set_password(self, raw_password: str):
        hash_pass = Hash.encrypt(raw_password)
        self.password = hash_pass

    class Meta:
        table_name = 'users'
        db_table = 'users'
