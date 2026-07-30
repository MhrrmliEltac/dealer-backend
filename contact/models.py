from tortoise import models, fields


class Contact(models.Model):
    id = fields.IntField(primary_key=True)
    location = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=100)

    class Meta:
        db_table = "contact"
