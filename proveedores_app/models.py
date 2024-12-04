from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    producto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    id_sucursal = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre