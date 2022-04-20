from django.shortcuts import render
from django.shortcuts import redirect, render
from Call.models import EnvioGuia
from Vehiculos.models import Vehiculo
from django.contrib.auth.models import User, Group

# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def conductor(request):
     if request.user.groups.filter(name='CONDUCTOR').exists() or request.user.groups.filter(name='ADMINISTRADOR').exists():
          env = EnvioGuia.objects.filter(entregado=False)
          env2 = Vehiculo.objects.filter(conductor_id=request.user.id)
          print(env2)
          pk = request.POST.get('id')
          if "entregado" in request.POST:
               env1 = EnvioGuia.objects.get(id = pk)
               env1.entregado = True
               env1.save()
          return render(request, 'Conductor/conductor.html', {'env': env, 'env2': env2})
     else:
          return redirect('sinpermiso')
