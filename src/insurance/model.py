from tortoise import fields
from tortoise.models import Model

class Rate(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField()
    cargo_type = fields.CharField(max_length=50)
    rate = fields.FloatField()

    class Meta:
        table = "insurance_price" 