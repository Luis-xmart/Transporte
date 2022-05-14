from django.shortcuts import render, redirect
from .forms import FormularioRemitente, FormularioRemitente2, FormularioDestinatario,  FormularioDestinatario2, FormularioUnidades, FormularioUnidades2
from .models import EnvioGuia
from Usuarios.models import PreciosDocumentos, PreciosPaquetes
from datetime import datetime
# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def call(request):
    if request.user.groups.filter(name='CALL CENTER').exists() or request.user.groups.filter(name='ADMINISTRADOR').exists():
        formRemi = FormularioRemitente()
        formDesti = FormularioDestinatario()
        formUnidades = FormularioUnidades()
        guias = EnvioGuia.objects.all().count()
        print('GUIAS', guias)
        rs =  datetime.today().strftime('%Y%m%d') + str((guias + 1)) 
        print('RS', rs)
        env = EnvioGuia.objects.all()
        if request.method == 'POST':
            formRemi = FormularioRemitente(request.POST)
            formDesti = FormularioDestinatario(request.POST)
            formUnidades = FormularioUnidades(request.POST)
            if formRemi.is_valid() and formDesti.is_valid() and formUnidades.is_valid():
                form_data1 = formRemi.cleaned_data
                tipoServicio = form_data1.get('servicio')
                print(tipoServicio)
                if str(tipoServicio) == 'Documentos':
                    numueroguia = rs
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
                    form_data4 = formUnidades.cleaned_data
                    peso = form_data4.get('peso')
                    print('PESO: ', peso)
                    print(peso)
                    form_data3 = formUnidades.cleaned_data
                    peso = form_data3.get('peso')
                    if peso < 5:
                        valorIdoc = PreciosDocumentos.objects.get(año=2022).valorIdoc
                        print('VALOR IDOC: ', valorIdoc)
                        valor = valorIdoc
                    else:
                        valorIdoc = PreciosDocumentos.objects.get(año=2022).valorIdoc
                        print('VALOR IDOC: ', valorIdoc)
                        valorAdoc = PreciosDocumentos.objects.get(año=2022).valorAdoc
                        print('VALOR ADOC: ', valorAdoc)
                        flete = PreciosDocumentos.objects.get(año=2022).flete
                        print('FLETE: ', flete)
                        total = (valorIdoc + valorAdoc + flete)
                        valor = total
                    largo = form_data4.get('largo')
                    ancho = form_data4.get('ancho')
                    alto = form_data4.get('alto')
                    contiene = form_data4.get('contiene')
                    formapagp = form_data4.get('forma')
                    largo = form_data3.get('largo')
                    ancho = form_data3.get('ancho')
                    alto = form_data3.get('alto')
                    contiene = form_data3.get('contiene')
                    formapagp = form_data3.get('forma')
                    EnvioGuia.objects.create(tipoServicio=tipoServicio, numueroguia=numueroguia, tipoIdRemitente=tipoIdRemitente, identificacionRemi=identificacionRemi, nombreRemi=nombreRemi, ciudadRemi=ciudadRemi, direccionRemi=direccionRemi, telefonoRemi=telefonoRemi, correoRemi=correoRemi, tipoIdDesti=tipoIdDesti, identificacionDesti=identificacionDesti, nombreDesti=nombreDesti, ciudadDesti=ciudadDesti, direccionDesti=direccionDesti, telefonoDesti=telefonoDesti, correoDesti=correoDesti, peso=peso, largo=largo, ancho=ancho, alto=alto, contiene=contiene, valor=valor, formapagp=formapagp)
                else:
                    numueroguia = rs
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
                    print('PESO 2', peso)
                    if peso < 50:
                        valorIpaq = PreciosPaquetes.objects.get(año=2022).valorIpaq
                        print('VALOR IPaq: ', valorIpaq)
                        valor = valorIpaq
                    else:
                        valorIpaq = PreciosPaquetes.objects.get(año=2022).valorIpaq
                        print('VALOR IPaq: ', valorIpaq)
                        valorApaq = PreciosPaquetes.objects.get(año=2022).valorApaq
                        print('VALOR APaq: ', valorApaq)
                        flete = PreciosPaquetes.objects.get(año=2022).flete
                        print('FLETE: ', flete)
                        total = (valorIpaq + valorApaq + flete)
                        valor = total
                    largo = form_data3.get('largo')
                    ancho = form_data3.get('ancho')
                    alto = form_data3.get('alto')
                    contiene = form_data3.get('contiene')
                    formapagp = form_data3.get('forma')
                    EnvioGuia.objects.create(tipoServicio=tipoServicio, numueroguia=numueroguia, tipoIdRemitente=tipoIdRemitente, identificacionRemi=identificacionRemi, nombreRemi=nombreRemi, ciudadRemi=ciudadRemi, direccionRemi=direccionRemi, telefonoRemi=telefonoRemi, correoRemi=correoRemi, tipoIdDesti=tipoIdDesti, identificacionDesti=identificacionDesti, nombreDesti=nombreDesti, ciudadDesti=ciudadDesti, direccionDesti=direccionDesti, telefonoDesti=telefonoDesti, correoDesti=correoDesti, peso=peso, largo=largo, ancho=ancho, alto=alto, contiene=contiene, valor=valor, formapagp=formapagp)
        return render(request, 'Call/call.html', {'formRemi': formRemi, 'formDesti': formDesti, 'formUnidades': formUnidades, 'env': env})
    else:
        return redirect('sinpermiso')

def editar(request, id):
    env = EnvioGuia.objects.filter(id=id).first()
    print(env)
    if request.method == 'GET':
        formRemi = FormularioRemitente2(instance=env)
        formDesti = FormularioDestinatario2(instance=env)
        fromC = FormularioUnidades2(instance=env)
    else:
        formRemi = FormularioRemitente2(request.POST, instance=env)
        formDesti = FormularioDestinatario2(request.POST, instance=env)
        fromC = FormularioUnidades2(request.POST, instance=env)
        if formRemi.is_valid() and formDesti.is_valid() and fromC.is_valid():
            form_data1 = formRemi.cleaned_data
            print(form_data1)
            tipoServicio = form_data1.get('tipoServicio')
            print(str(tipoServicio) == "Documento")
            print(str(tipoServicio))
            if str(tipoServicio) == 'Documentos':
                form_data4 = fromC.cleaned_data
                peso = int(form_data4.get('peso'))
                print('PESO:', peso)
                print(type(peso))
                print(peso < 5)
                if peso < 5:
                    valorIdoc = PreciosDocumentos.objects.get(año=2022).valorIdoc
                    valor = valorIdoc
                else:
                    valorIdoc = PreciosDocumentos.objects.get(año=2022).valorIdoc
                    valorAdoc = PreciosDocumentos.objects.get(año=2022).valorAdoc
                    flete = PreciosDocumentos.objects.get(año=2022).flete
                    total = (valorIdoc + valorAdoc + flete)
                    valor = total
                env1 = EnvioGuia.objects.filter(id=id).update(peso=peso, valor = valor)
            else:
                form_data3 = fromC.cleaned_data
                peso = int(form_data3.get('peso'))
                print(type(peso))
                print('PESO 2', peso)
                print(peso < 50)
                if peso < 50:
                    valorIpaq = PreciosPaquetes.objects.get(año=2022).valorIpaq
                    print('VALOR IPaq: ', valorIpaq)
                    valor = valorIpaq
                else:
                    valorIpaq = PreciosPaquetes.objects.get(año=2022).valorIpaq
                    print('VALOR IPaq: ', valorIpaq)
                    valorApaq = PreciosPaquetes.objects.get(año=2022).valorApaq
                    print('VALOR APaq: ', valorApaq)
                    flete = PreciosPaquetes.objects.get(año=2022).flete
                    print('FLETE: ', flete)
                    total = (valorIpaq + valorApaq + flete)
                    valor = total
                env1 = EnvioGuia.objects.filter(id=id).update(peso=peso, valor = valor)
                return redirect('Call')
    return render(request, 'Call/editar.html', context ={'formRemi': formRemi, 'formDesti': formDesti,'fromC': fromC, 'env': env})
