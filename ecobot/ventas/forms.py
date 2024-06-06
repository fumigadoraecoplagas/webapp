from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'provincia', 'distrito', 'cliente', 'inicio', 'duracion', 'color', 
            'precio', 'iva', 'descripcion', 'telefono', 'direccion', 'comisionistas'
        ]
        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'distrito': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'duracion': forms.Select(attrs={'class': 'form-control'}, choices=[(i, f"{i} minutos") for i in range(1, 481)]),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'iva': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 8}),
            'direccion': forms.URLInput(attrs={'class': 'form-control'}),
            'comisionistas': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
