from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('crear-cita/', views.crear_cita, name='crear_cita'),
    path('listar-citas/', views.listar_citas, name='listar_citas'),
    path('editar-cita/<int:cita_id>/', views.editar_cita, name='editar_cita'),
]
