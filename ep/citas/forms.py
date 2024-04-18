from django import forms

class CitaForm(forms.Form):
    fecha_hora = forms.DateTimeField(
        required=True,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        input_formats=['%Y-%m-%dT%H:%M']  # Ajusta el formato según tus necesidades
    )
    cliente = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_fumigacion = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    empleado = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio_total = forms.DecimalField(
        max_digits=10, decimal_places=2, required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    iva_incluido = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    vendedor = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comentarios = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False
    )
