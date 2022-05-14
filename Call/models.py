from django.db import models
from Vehiculos.models import Vehiculo

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicios'

class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Tipo de Identificación'
        verbose_name_plural = 'Tipos de Identificación'

class FormaPago(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'


class EnvioGuia(models.Model):
    numueroguia = models.CharField(max_length=50)
    tipoServicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    tipoIdRemitente = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE, related_name='tipoIdRemitente')
    identificacionRemi = models.CharField(max_length=50)
    nombreRemi = models.CharField(max_length=50)
    ciudadRemi = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='ciudadRemi')
    direccionRemi = models.TextField()
    telefonoRemi = models.CharField(max_length=50)
    correoRemi = models.EmailField(max_length=254)
    tipoIdDesti = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE, related_name='tipoIdDesti')
    identificacionDesti  = models.CharField(max_length=50)
    nombreDesti = models.CharField(max_length=50)
    ciudadDesti = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='ciudadDesti')
    direccionDesti = models.TextField()
    telefonoDesti = models.CharField(max_length=50)
    correoDesti = models.EmailField(max_length=254)
    peso = models.CharField(max_length=50)
    alto = models.CharField(max_length=50)
    ancho = models.CharField(max_length=50)
    largo = models.CharField(max_length=50)
    contiene = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    formapagp = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    vehiculos = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='vehiculos', null=True, blank=True)
    entregado = models.BooleanField(default=False)
    asignado = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.numueroguia
    class Meta:
        db_table = 'EnvioGuia'
        verbose_name = 'Envio de Guia'
        verbose_name_plural = 'Envios de Guias'