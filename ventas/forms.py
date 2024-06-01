from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['canton', 'provincia', 'nombre', 'telefono', 'precio_colones', 'fecha_inicio', 'fecha_fin', 'color_ruta', 'servicios']
