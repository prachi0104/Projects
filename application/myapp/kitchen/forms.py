from django import forms 
from .models import *





class Userinventory(forms.ModelForm):
    class Meta:
        model=ItemModel
        fields='__all__'
    


class MonthlyForm(forms.ModelForm):
    class Meta:
        model=MonthlyList
        fields = ['year', 'month', 'product', 'qty','unit']
        widgets = {
            'year': forms.Select(choices=YEAR),
            'month': forms.Select(choices=MONTH),
        }

