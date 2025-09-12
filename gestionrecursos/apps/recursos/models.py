from django.db import models

# Create your models here.
class Recursos(models.Model):
    nombre_recurso = models.CharField("Nombre del recurso", max_length=50)

    def __str__(self):
        return self.nombre_recurso
