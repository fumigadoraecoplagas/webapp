from django.urls import path
from . import views
from .views import crear_cita

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('crear-cita/', crear_cita, name='crear_cita'),
]
