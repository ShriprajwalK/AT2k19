from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money_possesed = models.FloatField(default=10000)

    Tesla_stock = models.IntegerField(default=0)
    TataMotors_stock = models.IntegerField(default=0)
    Nissan_stock = models.IntegerField(default=0)
    JPMorgan_stock = models.IntegerField(default=0)
    BajajAllianz_stock = models.IntegerField(default=0)
    SunPharma_stock = models.IntegerField(default=0)
    GSKPfizer_stock = models.IntegerField(default=0)
    Nestle_stock = models.IntegerField(default=0)
    BHEL_stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'
