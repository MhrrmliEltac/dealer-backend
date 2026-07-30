import uuid

from tortoise import models, fields


class About(models.Model):
    id = fields.UUIDField(primary_key=True)
    about = fields.TextField()
    about_desc = fields.TextField()
    about_image = fields.TextField()
    mission = fields.TextField()
    mission_desc = fields.TextField()
    mission_image = fields.TextField()

    class Meta:
        db_table = "about"
