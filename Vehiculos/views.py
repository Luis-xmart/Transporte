from django.shortcuts import render, redirect

from Conductor.views import conductor
from .forms import FormularioVehiculo, FormularioVehiculoEditar
from .models import Vehiculo
# Create your views here.
def vehiculos(request):
    if request.user.groups.filter(name='DESPACHADOR').exists() or request.user.groups.filter(name='ADMINISTRADOR').exists():
        form = FormularioVehiculo()
        vehi = Vehiculo.objects.all()
        if request.method == 'POST':
            form = FormularioVehiculo(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                placa = form_data.get('placa')
                marca = form_data.get('marca')
                tipo = form_data.get('tipo')
                conductor = form_data.get('conductor')
                veh = Vehiculo.objects.create(placa=placa, marca=marca, tipo=tipo, conductor=conductor)
        return render(request, 'Vehiculos/vehiculos.html', {'form': form, 'vehi': vehi})
    else:
        return redirect('sinpermiso')

def editarvehiculo(request, id):
    vehi = Vehiculo.objects.filter(id=id).first()
    print(vehi)
    if request.method == 'GET':
        form = FormularioVehiculoEditar(instance=vehi)
    if request.method == 'POST':
        form = FormularioVehiculoEditar(request.POST, instance=vehi)
        if form.is_valid():
            formdata2 = form.cleaned_data
            placa = formdata2.get('placa')
            print(placa)
            marca = formdata2.get('marca')
            tipo = formdata2.get('tipo')
            conductor = formdata2.get('conductor')
            print('CONDUCTOR: ', conductor)
            Vehiculo.objects.filter(id=id).update(placa=placa, marca=marca, tipo=tipo, conductor=conductor)
            return redirect('Vehiculos')
    return render(request, 'Vehiculos/editar.html', {'form': form})