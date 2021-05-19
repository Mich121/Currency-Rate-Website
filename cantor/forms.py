from django import forms
from .models import Currency

class BuyCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency', 'price', 'owner')

        widgets = {
            'currency': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),           
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of dollars...', 'min':0.00}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'id':'elder', 'type':'hidden'}),
        } 

class SellCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency', 'price')

        widgets = {
            'currency': forms.TextInput(attrs={'class':'form-control'}),           
            'price': forms.NumberInput(attrs={'class':'form-control', 'min':0.00}),
        } 