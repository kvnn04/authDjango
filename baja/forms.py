from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")