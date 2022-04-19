from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .forms import FormularioEditarUsu, RegistrationForm
from django.contrib.auth import forms  
from django.shortcuts import redirect, render  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms  import RegistrationForm
# Create your views here.
# def usuarios(request):
#     usuarios = User.objects.all()
#     form1 = crearUsuario()
#     if request == 'POST':
#         form1 = crearUsuario(request.POST)
#         if form1.is_valid():
#             formdata = form1.cleaned_data
#             username = formdata.get('username')
#             first_name = formdata.get('first_name')
#             last_name = formdata.get('last_name')
#             email = formdata.get('email')
#             password = formdata.get('password')
#             rol = formdata.get('rol')
#             print('GRUPO', formdata.get('rol'))
#             my_group = Group.objects.get(id = formdata.get('rol'))
#             usuarios.groups.add(my_group)
#             usu = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
#             return redirect('Usuarios')
#     return render(request, 'Usuarios/usuarios.html', {'usuarios': usuarios, 'form': form1})

def register(request):
    usuarios = User.objects.all()
    data = { 'form' : RegistrationForm(), 'usuarios': usuarios }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            form.save()
            usu = User.objects.get(username=formdata.get('username'))
            my_group = Group.objects.get(id = formdata.get('rol'))
            my_group.user_set.add(usu)
            
            messages.success(request, 'Usuario creado correctamente')
            return redirect('Usuarios')
        else:
            data['form'] = form
    return render(request, 'Usuarios/usuarios.html', data)

def editar(request, id):
    usuario = User.objects.filter(id=id).first()
    usuario.groups.clear() 
    if request.method == 'GET':
        form = FormularioEditarUsu(instance=usuario)
    else:
        form = FormularioEditarUsu(request.POST, instance=usuario)
        if form.is_valid():
            formdata = form.cleaned_data
            usuario.username = formdata.get('username')
            usuario.first_name = formdata.get('first_name')
            usuario.last_name = formdata.get('last_name')
            usuario.email = formdata.get('email')
            usuario1 = formdata.get('rol')
            print('GRUPO', formdata.get('rol'))
            my_group = Group.objects.get(id = formdata.get('rol'))
            my_group.user_set.add(usuario)
            
            usu1 = User.objects.filter(id=id).update(username=usuario.username, first_name=usuario.first_name, last_name=usuario.last_name, email=usuario.email)
            return redirect('Usuarios')
    return render(request, 'Usuarios/editar.html', {'usuario': usuario, 'form': form})

def eliminar(request, id):
    usuario = User.objects.filter(id=id).first()
    usuario.delete()
    return render(request, 'Usuarios/usuarios.html', {'usuario': usuario})
