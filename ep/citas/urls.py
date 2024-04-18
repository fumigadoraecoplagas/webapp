from django.urls import path
from . import views

app_name = 'citas'  # Namespace para las URLs de la aplicación

urlpatterns = [
    path('crear/', views.crear_cita, name='crear_cita'),
    path('ver/', views.ver_citas, name='ver_citas'),
]
