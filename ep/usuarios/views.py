from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import pyrebase

# Configuración de Firebase
firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
auth = firebase.auth()

# Decoradores
def add_user_email_to_context(view_func):
    def wrapper(request, *args, **kwargs):
        context = kwargs.pop('context', {})
        user_email = None
        if 'uid' in request.session:
            user_email = request.session.get('email')
        context['user_email'] = user_email
        return view_func(request, *args, context=context, **kwargs)
    return wrapper

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'uid' not in request.session:
            return redirect('sign_in')  # Redirige al sign in si no hay uid en la sesión
        return view_func(request, *args, **kwargs)
    return wrapper

# Vista de inicio de sesión
def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['idToken']
            request.session['email'] = user['email']
            return redirect('home')
        except:
            messages.error(request, "Correo electrónico o contraseña incorrectos")
            return render(request, 'usuarios/error.html', {'message': 'Correo electrónico o contraseña incorrectos'})
    else:
        return render(request, 'usuarios/sign_in.html')

# Vista de la página principal
@add_user_email_to_context
@login_required
def home(request, context):
    return render(request, 'usuarios/home.html', context)

# Función para cerrar sesión
@login_required
def log_out(request):
    # Elimina el usuario y otros datos de la sesión
    request.session.flush()
    # Redirige al usuario a la página de inicio de sesión
    return redirect('sign_in')