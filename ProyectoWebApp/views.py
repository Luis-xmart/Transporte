from django.shortcuts import render
# from .forms import FormularioEmpresa
# from .models import Empresa

# Create your views here.
def index(request):
    # formularioEmpresa = FormularioEmpresa()
    # emp = Empresa.objects.all()
    # if request.method == 'POST':
    #     formularioEmpresa = FormularioEmpresa(request.POST)
    #     if formularioEmpresa.is_valid():
    #         form_data = formularioEmpresa.cleaned_data
    #         nombre = form_data.get('nombre')
    #         direccion = form_data.get('direccion')
    #         telefono = form_data.get('telefono')
    #         representante = form_data.get('representante')
    #         web = form_data.get('web')
    #         empresa = Empresa.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, representante=representante, web=web)
    return render(request, 'ProyectoWebApp/base.html')
