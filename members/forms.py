from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from cantor.models import Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'profile_picture')
        widgets = {
                'phone': forms.TextInput(attrs={'class':'form-control'}),
        }