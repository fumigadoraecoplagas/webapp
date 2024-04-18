from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.sign_in, name='sign_in'),  # Establece sign_in como la página de inicio
    # Incluye las URLs de otras aplicaciones si es necesario
    path('usuarios/', include('usuarios.urls')),
    path('clientes/', include('clientes.urls')),
    path('citas/', include('citas.urls')),  # Asegúrate de que 'citas.urls' es el path correcto a tu app 'citas'


]