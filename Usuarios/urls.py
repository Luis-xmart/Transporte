from django.urls import path
from . import views

urlpatterns = [
    path('Usuarios/', views.usuarios, name='Usuarios'),
]