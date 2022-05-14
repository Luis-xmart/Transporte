from django.db import models

# Create your models here.
class PreciosDocumentos(models.Model):
    valorIdoc = models.IntegerField(default=0)
    valorAdoc = models.IntegerField(default=0)
    flete = models.IntegerField(default=0)
    año = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class PreciosPaquetes(models.Model):
    valorIpaq = models.IntegerField(default=0)
    valorApaq = models.IntegerField(default=0)
    flete = models.IntegerField(default=0)
    año = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
