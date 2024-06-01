from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VentaForm
from .models import Venta

@login_required
def home(request):
    return render(request, 'ventas/index.html')

@login_required
def crear_cita(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VentaForm()
    return render(request, 'ventas/formulario_cita.html', {'form': form})
