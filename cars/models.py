from tortoise import models, fields


class Cars(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    description = fields.TextField()
    vincode = fields.CharField(max_length=17, unique=True)

    class Meta:
        db_table = "cars"
