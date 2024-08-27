from django import forms
from django.


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm password')
        if p1 and p2 and p1 != p2:
            raise