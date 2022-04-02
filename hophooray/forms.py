from django import forms
from hophooray.models import Beer

class CreateForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'origin', 'beertype', 'amount', 'price']