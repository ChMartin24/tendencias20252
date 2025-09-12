from django.db import models

# Create your models here.
class Roles(models.Model):
    nombre_rol = models.CharField("Nombre del rol", max_length=50)

    def __str__(self):
        return self.nombre_rol
