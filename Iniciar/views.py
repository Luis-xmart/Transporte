from tokenize import group
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
# Create your views here.
def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            contraseña = form.cleaned_data['password']
            usuario = authenticate(username=username, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('Base/')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    form = AuthenticationForm()
    return render(request, 'Iniciar/iniciar.html', {'form': form})