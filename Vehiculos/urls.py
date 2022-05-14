from django.urls import path, re_path
from . import views

urlpatterns = [
    path('Vehiculos/', views.vehiculos, name='Vehiculos'),
    re_path(r'^editar/(?P<id>\d+)/$', views.editarvehiculo, name='editarvehiculo'),
]