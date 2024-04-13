from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('home/', views.home, name='home'),
    # Añade más rutas según sea necesario
]