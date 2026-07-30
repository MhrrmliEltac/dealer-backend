import uuid

from tortoise import models, fields


class Services(models.Model):
    id = fields.UUIDField(primary_key=True)
    image = fields.TextField(null=True)
    title = fields.CharField(max_length=50)
    description = fields.TextField(null=True)

    class Meta:
        db_table = "services"
