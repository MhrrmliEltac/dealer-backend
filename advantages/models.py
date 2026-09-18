from tortoise import models, fields


class Advantages(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=150)
    description = fields.TextField()
    image = fields.TextField(null=True)

    class Meta:
        db_table = "advantages"
