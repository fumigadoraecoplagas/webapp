from django.db import models

class Cita(models.Model):
    PROVINCIAS = [
        ('San José', 'San José'),
        ('Alajuela', 'Alajuela'),
        ('Cartago', 'Cartago'),
        ('Heredia', 'Heredia'),
        ('Guanacaste', 'Guanacaste'),
        ('Puntarenas', 'Puntarenas'),
        ('Limón', 'Limón'),
    ]
    
    COLORES = [
        ('Azul', 'Azul'),
        ('Rojo', 'Rojo'),
        ('Verde', 'Verde'),
        ('Amarillo', 'Amarillo'),
        ('Naranja', 'Naranja'),
        ('Morado', 'Morado'),
        ('Rosa', 'Rosa'),
        ('Marrón', 'Marrón'),
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
    ]
    
    provincia = models.CharField(max_length=20, choices=PROVINCIAS)
    distrito = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    duracion = models.IntegerField()  # Duración en minutos
    color = models.CharField(max_length=20, choices=COLORES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.BooleanField(default=False)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=8)
    direccion = models.URLField()

    def __str__(self):
        return f"Cita con {self.cliente} en {self.provincia}, {self.distrito} - {self.inicio}"

    def save(self, *args, **kwargs):
        self.fin = self.inicio + timedelta(minutes=self.duracion)
        super().save(*args, **kwargs)
