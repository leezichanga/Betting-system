from django  import forms
from .models import Deposit, get_placebet

class DepositForm(forms.ModelForm):
    class Meta:
        model = DepositForm
        exclude ['name']

class PlacebetForm(forms.ModelForm):
    class Meta:
        model = PlacebetForm
        exclude = ['user']
