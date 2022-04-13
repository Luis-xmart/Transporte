from django.urls import path
from . import views

urlpatterns = [
    path('Vehiculos/', views.vehiculos, name='Vehiculos'),
]