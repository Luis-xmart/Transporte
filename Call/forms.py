from django import forms
from .models import TipoServicio, TipoIdentificacion, FormaPago, Municipio
# from Cotizaciones.models import Municipio

class FormularioRemitente(forms.Form):
    servicio = forms.ModelChoiceField(queryset=TipoServicio.objects.all())
    numeroguia = forms.CharField(max_length=50, label='Número de Guía')
    tipoIdRemitente = forms.ModelChoiceField(queryset=TipoIdentificacion.objects.all(), label = 'Tipo de Identificación')
    identificacionRemi = forms.CharField(label='Identificación', max_length=100, required=True)
    nombreRemi = forms.CharField(label='Nombre', max_length=100, required=True)
    ciudadRemi = forms.ModelChoiceField(queryset=Municipio.objects.all(), label = 'Ciudad')
    direccionRemi = forms.CharField(label='Dirección', max_length=100, required=True)
    telefonoRemi = forms.CharField(label='Teléfono', max_length=100, required=True)
    correoRemi = forms.CharField(label='Correo', max_length=100, required=True)

class FormularioDestinatario(forms.Form):
    tipoIdDestinatario = forms.ModelChoiceField(queryset=TipoIdentificacion.objects.all(), label = 'Tipo de Identificación')
    identificacionDesti = forms.CharField(label='Identificación', max_length=100, required=True)
    nombreDesti = forms.CharField(label='Nombre', max_length=100, required=True)
    ciudadDesti = forms.ModelChoiceField(queryset=Municipio.objects.all(), label = 'Ciudad')
    direccionDesti = forms.CharField(label='Dirección', max_length=100, required=True)
    telefonoDesti = forms.CharField(label='Teléfono', max_length=100, required=True)
    correoDesti = forms.CharField(label='Correo', max_length=100, required=True)


class FormularioUnidades(forms.Form):
    peso = forms.CharField(label='Peso Real', max_length=100, required=True)
    largo = forms.CharField(label='Largo', max_length=100, required=True)
    ancho = forms.CharField(label='Ancho', max_length=100, required=True)
    alto = forms.CharField(label='Alto', max_length=100, required=True)
    contiene = forms.CharField(label='Contiene', max_length=100, required=True)
    valor = forms.CharField(label='Valor', max_length=100, required=True)
    forma = forms.ModelChoiceField(queryset=FormaPago.objects.all(), label='Forma de Pago')

