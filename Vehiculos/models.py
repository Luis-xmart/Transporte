from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    conductor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conductor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.placa