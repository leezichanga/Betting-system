from django.forms  import ModelForm
from django import forms
from .models import Deposit, Placebet

class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        exclude = ['user']

class PlacebetForm(ModelForm):
    class Meta:
        model = Placebet
        exclude = ['user']
