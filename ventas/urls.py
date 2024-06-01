from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-cita/', views.crear_cita, name='crear_cita'),
]
