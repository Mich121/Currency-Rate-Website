from django import forms
from django.forms.models import model_to_dict
from matplotlib.pyplot import cla
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

class SellSomeCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency', 'price')

        widgets = {
            'currency': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),           
            'price': forms.NumberInput(attrs={'class':'form-control', 'min':0.00, 'id':'amount'}),
        } 
        labels = {
            'price': ('Amount'),
        }

class SellAllCurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency', 'price')

class BarTypeForm(forms.Form):
    CHART_CHOICES=(
        ('#1','Bar chart'),
        ('#2','Pie chart'),
        )
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, label="", widget=forms.Select(attrs={'class': 'form-control'}))