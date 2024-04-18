from django.shortcuts import render, redirect
from django.conf import settings
import pyrebase
from .forms import ClienteForm

# Configuración de Firebase
firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
db = firebase.database()

def create_cliente(request):
    if not request.session.get('uid'):
        return redirect('sign_in')
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            data = {
                'telefono': form.cleaned_data['telefono'],
                'email': form.cleaned_data.get('email', ''),
                'nombre': form.cleaned_data['nombre'],
                'descripcion': form.cleaned_data['descripcion'],
                'creador': request.session.get('email')
            }
            db.child("clientes").child(data['telefono']).set(data)
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'clientes/create_cliente.html', {'form': form})

def list_clientes(request):
    if not request.session.get('uid'):
        return redirect('sign_in')
    clientes = db.child("clientes").get().val()
    print(clientes)  # Añadir esto para depurar
    return render(request, 'clientes/list_clientes.html', {'clientes': clientes})

