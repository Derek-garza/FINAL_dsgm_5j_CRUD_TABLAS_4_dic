from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal = models.PositiveIntegerField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=100)
    calle_sucursal = models.CharField(max_length=255)
    num_empleados = models.PositiveIntegerField()
    tel_sucursal = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_sucursal