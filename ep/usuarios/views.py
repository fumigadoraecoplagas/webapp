from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import pyrebase

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)  # Corrección aquí

auth = firebase.auth()

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Intenta autenticar al usuario con Firebase
            user = auth.sign_in_with_email_and_password(email, password)
            # Guarda el token del usuario en la sesión
            request.session['uid'] = user['idToken']
            # Redirige a la página principal si el inicio de sesión es exitoso
            return redirect('home')  # Asegúrate de tener una URL con nombre 'home'
        except:
            # Si hay un error (credenciales inválidas, por ejemplo), muestra un mensaje
            messages.error(request, "Correo electrónico o contraseña incorrectos")
            return render(request, 'usuarios/error.html', {'message': 'Correo electrónico o contraseña incorrectos'})
    else:
        # Si no es una solicitud POST, simplemente renderiza la página de inicio de sesión
        return render(request, 'usuarios/sign_in.html')

def home(request):
    return render(request, 'usuarios/home.html')
