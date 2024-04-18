from django.db import models
from django.conf import settings

class Cita(models.Model):
    fecha_hora = models.DateTimeField(verbose_name="Fecha y hora de la cita")
    cliente = models.CharField(max_length=255, verbose_name="Cliente")
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    tipo_fumigacion = models.CharField(max_length=100, verbose_name="Tipo de Fumigación")
    empleado = models.CharField(max_length=100, verbose_name="Empleado Asignado")
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Total")
    iva_incluido = models.BooleanField(default=False, verbose_name="IVA Incluido")
    comentarios = models.TextField(blank=True, verbose_name="Comentarios")
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Vendedor")

    def __str__(self):
        return f"Cita para {self.cliente} el {self.fecha_hora}"
