from django import forms

class ClienteForm(forms.Form):
    telefono = forms.CharField(max_length=8, min_length=8, label='Teléfono')
    email = forms.EmailField(required=False, label='Email')
    nombre = forms.CharField(max_length=100, label='Nombre')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
