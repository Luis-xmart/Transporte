from cmd import IDENTCHARS
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views import View
from Call.models import EnvioGuia
from Vehiculos.models import Vehiculo
from django.contrib.auth.models import User, Group
from .models import Entrega, Observaciones
from .forms import FormularioEntrega, FormularioEntrega2
from django.shortcuts import get_object_or_404
from django.db.models import Q

# from .forms import FormularioEmpresa
# from .models import Empresa 

# Create your views here.
def conductor(request):
     if request.user.groups.filter(name='CONDUCTOR').exists() or request.user.groups.filter(name='ADMINISTRADOR').exists():
          env = EnvioGuia.objects.filter(entregado=False)
          env2 = EnvioGuia.vehiculos_id = Vehiculo.objects.filter(conductor_id=request.user.id).exists()
          if env2 == True:
               env3 = EnvioGuia.vehiculos_id = Vehiculo.objects.filter(conductor_id=request.user.id).first().id
               return render(request, 'Conductor/conductor.html', {'env': env, 'env3': env3})
          if env2 == False:
               return render(request, 'Conductor/conductor.html', {'env': env})
     else:
          return redirect('sinpermiso')


def entregar(request, id):
     print('ID', id)
     obs = Observaciones.objects.filter(guia_id=id).first()
     obs2 = Observaciones.objects.filter(guia_id=id).exists()
     print(obs) 
     form = FormularioEntrega2()
     # pk = request.POST.get('id')
     # print('PK', pk)
     if request.method == 'GET':
          form = FormularioEntrega2()
     if obs2 == False:
          print('FALSE')
          form1 = FormularioEntrega2(request.POST)
          if "entregado" in request.POST:
               print('ENTREGADO')
               if form1.is_valid():
                    formdata = form1.cleaned_data
                    observacion = formdata.get('observacion')
                    Observaciones.objects.create(observacion=observacion, guia=EnvioGuia.objects.get(id=id))
                    env1 = EnvioGuia.objects.get(id = id)
                    env1.entregado = True
                    env1.save()
          if "no_entregado " in request.POST:
               print('NO ENTREGADO IF')
               if form1.is_valid():
                    formdata = form1.cleaned_data
                    observacion = formdata.get('observacion')
                    print('OBSERVACION', observacion)
                    Observaciones.objects.create(observacion=observacion, guia=EnvioGuia.objects.get(id=id))
                    env1 = EnvioGuia.objects.get(id = id)
                    env1.entregado = False
                    env1.save()
          return render(request, 'Conductor/entrega.html', { 'form': form1})
     else:
          print('EXISTE')
          form = FormularioEntrega2(request.POST, instance=obs)
          if "entregado" in request.POST:
               if form.is_valid():
                    formdata = form.cleaned_data
                    observacion = formdata.get('observacion')
                    print('ENTREGADO', observacion)
                    Observaciones.objects.filter(guia_id=id).update(observacion=observacion)
                    env1 = EnvioGuia.objects.get(id = id)
                    env1.entregado = True
                    env1.save()
          if "no_entregado" in request.POST:
               if form.is_valid():
                    formdata = form.cleaned_data
                    observacion = formdata.get('observacion')
                    print('NO ENTREGADO', observacion)
                    Observaciones.objects.filter(guia_id=id).update(observacion=observacion)
                    env2 = EnvioGuia.objects.get(id = id)
                    env2.entregado = False
                    env2.save()
          return render(request, 'Conductor/entrega.html', { 'form': form})
          
          
     


class entrega(View):
     def get(self, request):
          form = FormularioEntrega2()
          return render(request, 'Conductor/entrega.html', {'form': form})
     def post(self, request, id):
          form = FormularioEntrega2(request.POST)
          if request.method == 'POST' and 'entregado' in request.POST:
               if form.is_valid():
                    formdata = form.cleaned_data
                    observacion = formdata.get('observacion')
                    print('ENTREGADO', observacion)
                    Observaciones.objects.create(observacion=observacion, guia=EnvioGuia.objects.get(id=id))
                    env1 = EnvioGuia.objects.get(id = id)
                    env1.entregado = True
                    env1.save()
                    return render(request, 'Conductor/entrega.html', {'form': form})
          if request.method == 'POST' and 'no_entregado' in request.POST:
               if form.is_valid():
                    formdata = form.cleaned_data
                    observacion = formdata.get('observacion')
                    print('NO ENTREGADO', observacion)
                    Observaciones.objects.create(observacion=observacion, guia=EnvioGuia.objects.get(id=id))
                    env2 = EnvioGuia.objects.get(id = id)
                    env2.entregado = False
                    env2.save()
                    return render(request, 'Conductor/entrega.html', {'form': form})
          return redirect('Conductor')


# def entregar(request, id): 
#      entr = Entrega.objects.all()
#      form = FormularioEntrega()
#      if request.method == 'POST':
#           form = FormularioEntrega(request.POST)
#           if form.is_valid():
#                formdata = form.cleaned_data
#                observacion = formdata.get('observacion')
#                entrega = formdata.get('entrega')
#                Observaciones.objects.create(observacion=observacion, entrega=entrega, guia=EnvioGuia.objects.get(id=id))
#      return render(request, 'Conductor/entrega.html', {'entr': entr, 'form': form})




# def entregar(request,  id):
#      query_envio = EnvioGuia.objects.all()
#      pk = request.POST.get('id')
    
#      if request.method == 'POST':
#           form = FormularioEntrega(request.POST or None)
#           if request.method == "POST":
#                if form.is_valid():
#                     form.instance.envios = envios
#                     form.save()
#                     return redirect('Conductor')  
#                     context = {    
#                          "form": form,
#                          "envios": envios,
#                     }
#      return render(request, 'Conductor/entrega.html', form)