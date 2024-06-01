from django.db import models

class Venta(models.Model):
    canton = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    precio_colones = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    color_ruta = models.CharField(max_length=20, choices=[
        ('Verde', 'Verde'),
        ('Morada', 'Morada'),
        ('Amarilla', 'Amarilla'),
        ('Naranja', 'Naranja'),
        ('Celeste', 'Celeste'),
        ('Rosada', 'Rosada'),
        ('Café', 'Café')
    ])
    servicios = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
