from django.shortcuts import render
# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def index(request):

    return render(request, 'ProyectoWebApp/base.html')

def permisos(request):
    return render(request, 'ProyectoWebApp/sinpermiso.html')
