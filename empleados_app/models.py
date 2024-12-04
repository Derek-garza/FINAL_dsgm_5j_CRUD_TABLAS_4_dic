from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.PositiveIntegerField(primary_key=True)
    curp = models.CharField(max_length=18)  # CURP tiene 18 caracteres
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    fecha_nac = models.DateField(null=False,blank=False)
    sexo = models.CharField(max_length=10)  # Ejemplo: 'Masculino', 'Femenino'
    id_sucursal=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre