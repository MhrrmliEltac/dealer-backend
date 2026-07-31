import uuid

from tortoise import models, fields


class ServiceInfo(models.Model):
    id = fields.UUIDField(primary_key=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    tags = fields.JSONField(default=list)
    image = fields.TextField(null=True)

    class Meta:
        db_table = 'serviceInformation'
