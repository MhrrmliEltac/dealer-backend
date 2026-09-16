from tortoise import models, fields


class Suggestion(models.Model):
    id = fields.IntField(primary_key=True)
    fullname = fields.CharField(max_length=150)
    phone_number = fields.CharField(max_length=50)
    suggestion = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        db_table = "suggestion"
