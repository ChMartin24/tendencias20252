from django.db import models

class Reservas(models.Model):
    estado_reserva = models.CharField("Estado de la reserva", max_length=50)

    def __str__(self):
        return self.estado_reserva
