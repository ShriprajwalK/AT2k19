from django.forms import ModelForm
from django import forms

from stock_price.models import Company,ForBuy
from users.models import Profile

class BuyForm(forms.Form):
    name = forms.CharField(label='Company name', max_length=100)
    amount = forms.IntegerField(label='Number of stock you want to buy?')



class SellForm(forms.Form):
    name = forms.CharField(label='Company name', max_length=100)
    amount = forms.IntegerField(label='Number of stock you want to sell?')
