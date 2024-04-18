from django.urls import path
from . import views
from .views import cita_detalle

app_name = 'citas'  # Namespace para las URLs de la aplicación

urlpatterns = [
    path('crear/', views.crear_cita, name='crear_cita'),
    path('api/citas/', views.citas_json, name='citas_json'),  # Verifica que esta línea esté presente
    path('ver-citas/', views.ver_citas, name='ver_citas'),  # Asegúrate de que el nombre y la vista coincidan
    path('detalle/<str:cita_id>/', views.cita_detalle, name='cita_detalle'),  # Ruta para detalles de cita específica



]
