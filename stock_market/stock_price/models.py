from django.conf import settings
from django.db import models
from django.utils import timezone

#Info on the company for the database.


class Company(models.Model):

    name = models.CharField(max_length=100)
    opening_price = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    percentage_change = models.FloatField(default=0)
    day_high = models.FloatField(default=0)
    day_low = models.FloatField(default=0)


    def __str__(self):
        return self.name


class ForBuy(models.Model):
    amount = models.IntegerField(default = 0)
    name = models.CharField(max_length=1000)
