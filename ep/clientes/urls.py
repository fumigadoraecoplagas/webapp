from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
    path('create/', views.create_cliente, name='create_cliente'),
    path('list/', views.list_clientes, name='list_clientes'),
]
