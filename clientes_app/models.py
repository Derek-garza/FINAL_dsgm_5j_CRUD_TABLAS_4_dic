from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=False,blank=False)  
    correo = models.EmailField(max_length=50)  
    direccion = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()
    codigo_p = models.CharField(max_length=20) 

    def __str__(self):
        return self.nombre