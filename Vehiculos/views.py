from django.shortcuts import render
from .forms import FormularioVehiculo
from .models import Vehiculo
# Create your views here.
def vehiculos(request):
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