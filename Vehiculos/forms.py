from django import forms
from .models import TipoVehiculo, Vehiculo
from django.contrib.auth.models import Group

class FormularioVehiculo (forms.Form):
    placa = forms.CharField(max_length=7, label="Placa")
    marca = forms.CharField(max_length=50, label="Marca")
    tipo = forms.ModelChoiceField(queryset=TipoVehiculo.objects.all(), label="Tipo")
    conductor = forms.ModelChoiceField(queryset=Group.objects.get(name="CONDUCTOR").user_set.all(), label="Conductor")
    