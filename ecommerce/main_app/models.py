from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=225)
    discount_price = models.FloatField(
        blank=True, 
        null=True, 
        default=None,
        )