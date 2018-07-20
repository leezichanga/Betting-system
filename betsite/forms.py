from django  import forms
from .models import Deposit, Placebet

class DepositForm(forms.ModelForm):
    class Meta:
        model = DepositForm
        exclude ['name, user']

class PlacebetForm(forms.ModelForm):
    class Meta:
        model = PlacebetForm
        exclude = ['user']
