from django.shortcuts import render
from django.shortcuts import redirect, render
from Call.models import EnvioGuia

# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def conductor(request):
     env = EnvioGuia.objects.filter(entregado=False)
     pk = request.POST.get('id')
     if "entregado" in request.POST:
          env1 = EnvioGuia.objects.get(id = pk)
          env1.entregado = True
          env1.save()
     return render(request, 'Conductor/conductor.html', {'env': env})