from tortoise import models, fields


class Auction(models.Model):
    id = models.IntField(primary_key=True)
    title = fields.CharField(max_length=200)
    image = fields.TextField()

    class Meta:
        db_table = "auction"
