from cProfile import label
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form 
from django.contrib.auth.models import Group

# class crearUsuario(forms.Form):
#     username = forms.CharField(label='Nombre de usuario', max_length=100, required=True)
#     first_name = forms.CharField(label='Nombre', max_length=100, required=True)
#     last_name = forms.CharField(label='Apellido', max_length=100, required=True)
#     email = forms.EmailField(label='Correo electrónico', max_length=100, required=True)
#     password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, max_length=100, required=True)
#     rol = forms.ModelChoiceField(label='Rol', queryset=Group.objects.all(), required=True)
class RegistrationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=[(rol.id, rol.name) for rol in Group.objects.all()])
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'rol')

        # def save(self, commit=True):
        #     user = super(RegistrationForm, self).save(commit=False)
        #     user.first_name = self.cleaned_data['first_name']
        #     user.last_name = self.cleaned_data['last_name']
        #     user.email = self.cleaned_data['email']

        #     if commit:
        #         user.save()

        #     return user 

class FormularioEditarUsu(forms.ModelForm):
    rol = forms.ChoiceField(choices=[(rol.id, rol.name) for rol in Group.objects.all()])
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rol']
        labels = { 'username': 'Nombre de usuario', 'first_name': 'Nombre', 'last_name': 'Apellidos', 'email': 'Correo electrónico', 'rol': 'Rol' }
        widgets = { 'username': forms.TextInput(attrs={'class': 'form-control'}), 
        'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
        'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
        'email': forms.TextInput(attrs={'class': 'form-control'}), 
        'rol': forms.Select(attrs={'class': 'form-control'}), }