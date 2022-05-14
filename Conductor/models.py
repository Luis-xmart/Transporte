from django.db import models
from Call.models import EnvioGuia

# Create your models here.

class Entrega(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

class Observaciones(models.Model):
    observacion = models.TextField()
    guia = models.ForeignKey(EnvioGuia, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

