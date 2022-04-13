from django.shortcuts import render
from .forms import FormularioRemitente, FormularioDestinatario, FormularioUnidades
from .models import EnvioGuia
# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def call(request):
    formRemi = FormularioRemitente()
    formDesti = FormularioDestinatario()
    formUnidades = FormularioUnidades()
    env = EnvioGuia.objects.all()
    if request.method == 'POST':
        formRemi = FormularioRemitente(request.POST)
        formDesti = FormularioDestinatario(request.POST)
        formUnidades = FormularioUnidades(request.POST)
        if formRemi.is_valid() and formDesti.is_valid() and formUnidades.is_valid():
            form_data1 = formRemi.cleaned_data
            tipoServicio = form_data1.get('servicio')
            numueroguia = form_data1.get('numeroguia')
            tipoIdRemitente = form_data1.get('tipoIdRemitente')
            identificacionRemi = form_data1.get('identificacionRemi')
            nombreRemi = form_data1.get('nombreRemi')
            ciudadRemi = form_data1.get('ciudadRemi')
            direccionRemi = form_data1.get('direccionRemi')
            telefonoRemi = form_data1.get('telefonoRemi')
            correoRemi = form_data1.get('correoRemi')
            form_data2 = formDesti.cleaned_data
            tipoIdDesti = form_data2.get('tipoIdDestinatario')
            identificacionDesti = form_data2.get('identificacionDesti')
            nombreDesti = form_data2.get('nombreDesti')
            ciudadDesti = form_data2.get('ciudadDesti')
            direccionDesti = form_data2.get('direccionDesti')
            telefonoDesti = form_data2.get('telefonoDesti')
            correoDesti = form_data2.get('correoDesti')
            form_data3 = formUnidades.cleaned_data
            peso = form_data3.get('peso')
            largo = form_data3.get('largo')
            ancho = form_data3.get('ancho')
            alto = form_data3.get('alto')
            contiene = form_data3.get('contiene')
            valor = form_data3.get('valor')
            formapagp = form_data3.get('forma')
            envio = EnvioGuia.objects.create(tipoServicio=tipoServicio, numueroguia=numueroguia, tipoIdRemitente=tipoIdRemitente, identificacionRemi=identificacionRemi, nombreRemi=nombreRemi, ciudadRemi=ciudadRemi, direccionRemi=direccionRemi, telefonoRemi=telefonoRemi, correoRemi=correoRemi, tipoIdDesti=tipoIdDesti, identificacionDesti=identificacionDesti, nombreDesti=nombreDesti, ciudadDesti=ciudadDesti, direccionDesti=direccionDesti, telefonoDesti=telefonoDesti, correoDesti=correoDesti, peso=peso, largo=largo, ancho=ancho, alto=alto, contiene=contiene, valor=valor, formapagp=formapagp)
    return render(request, 'Call/call.html', {'formRemi': formRemi, 'formDesti': formDesti, 'formUnidades': formUnidades, 'env': env})