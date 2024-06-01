from django.contrib import admin
from django.urls import path, include
from ventas import views  # Asegúrate de importar views aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
]
