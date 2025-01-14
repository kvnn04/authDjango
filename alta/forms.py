from django import forms
from django.core.exceptions import ValidationError
import re

class SignUp(forms.Form):
    username = forms.CharField(max_length=50, min_length=2, label='username', required=True)
    email = forms.CharField(max_length=100, min_length=2, label='email', required=True)
    pwd = forms.CharField(min_length=8, widget=forms.PasswordInput, required=True, label='Contraseña')
    verifyPwd = forms.CharField(min_length=8, widget=forms.PasswordInput,required=True, label='Contraseña')

    def clean_pwd(self):
        password = self.cleaned_data.get('pwd')

        # Validación de seguridad de la contraseña
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'\d', password):  # Al menos un número
            raise ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[A-Z]', password):  # Al menos una letra mayúscula
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Al menos un carácter especial
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")
        
        return password
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise ValidationError("El correo electrónico debe contener un '@'.")
        return email
    
    def clean(self):
        cleanedData = super().clean()
        password = cleanedData.get("pwd")
        confirmPassword = cleanedData.get("verifyPwd")

        if password and confirmPassword and password != confirmPassword:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
        
        return cleanedData

class Login(forms.Form):
    email = forms.CharField(max_length=100, min_length=2, label='email', required=True)
    pwd = forms.CharField(min_length=8, widget=forms.PasswordInput, required=True, label='Contraseña')

    def clean_pwd(self):
        password = self.cleaned_data.get('pwd')

        # Validación de seguridad de la contraseña
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'\d', password):  # Al menos un número
            raise ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[A-Z]', password):  # Al menos una letra mayúscula
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Al menos un carácter especial
            raise ValidationError("La contraseña debe contener al menos un carácter especial.")
        
        return password
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if '@' not in email:
    #         raise ValidationError("El correo electrónico debe contener un '@'.")
    #     return email
    