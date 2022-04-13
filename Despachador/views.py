from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from Call.models import EnvioGuia
from django.contrib.auth.models import Group
from .forms import FormularioConductores
from Call.models import EnvioGuia
from Vehiculos.models import Vehiculo

# Create your views here.
def despachador(request):
    env = EnvioGuia.objects.filter(asignado=False)
    return render(request, 'Despachador/despachador.html', {'env': env})



def asignar(request, id):
    env = EnvioGuia.objects.filter(vehiculos_id=id).first()
    pk = request.POST.get('id')
    print(pk)
    if "asignado" in request.POST:
        env1 = EnvioGuia.objects.get(id = id)
        env1.asignado = True
        env1.save()
    if request.method == 'GET':
        fromC = FormularioConductores(instance=env)
    else:
        fromC = FormularioConductores(request.POST, instance=env)
        if fromC.is_valid():
            form_data = fromC.cleaned_data
            vehiculo = form_data.get('secretdocs')
            env1 = EnvioGuia.objects.filter(id=id).update(vehiculos_id=vehiculo)
            return redirect('Despachador')
    return render(request, 'Despachador/asignar.html', context ={'fromC': fromC, 'env': env})