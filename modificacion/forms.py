from django import forms

class ModifyNombreApellido(forms.Form):
    nombre = forms.CharField(max_length=50, min_length=1, required=True, label='Nombre')
    apellido = forms.CharField(max_length=50, min_length=1, required=True, label='Apellido')