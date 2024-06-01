from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['provincia', 'distrito', 'cliente', 'inicio', 'duracion', 'color', 'precio', 'iva', 'descripcion', 'telefono', 'direccion']
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'duracion': forms.Select(choices=[(i, f"{i} minutos") for i in range(1, 481)]),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'telefono': forms.TextInput(attrs={'maxlength': 8}),
        }
