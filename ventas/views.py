from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CitaForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'ventas/login.html', {'form': form})

@login_required
def home(request):
    print(request.user.is_authenticated)  # Debería imprimir True si el usuario está autenticado
    return render(request, 'ventas/index.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CitaForm()
    return render(request, 'ventas/crear_cita.html', {'form': form})

@login_required
def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'ventas/listar_citas.html', {'citas': citas})

@login_required
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'ventas/editar_cita.html', {'form': form, 'cita_id': cita.id})