from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money_possesed = models.FloatField(default=10000)

    Stark_stock = models.IntegerField(default=0)
    Wayne_stock = models.IntegerField(default=0)
    Daily_stock = models.IntegerField(default=0)
    Big_stock = models.IntegerField(default=0)
    Lex_stock = models.IntegerField(default=0)
    Parker_stock = models.IntegerField(default=0)
    Queen_stock = models.IntegerField(default=0)
    Oscorp_stock = models.IntegerField(default=0)
    Shield_stock = models.IntegerField(default=0)
    Xavier_stock = models.IntegerField(default=0)
    Ramon_stock = models.IntegerField(default=0)
    Banner_stock = models.IntegerField(default=0)
    Wakanda_stock = models.IntegerField(default=0)
    Nonsense_stock = models.IntegerField(default=0)
    Strange_stock = models.IntegerField(default=0)
    Murdork_stock = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'
