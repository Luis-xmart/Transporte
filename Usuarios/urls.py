from django.urls import path, re_path
from . import views

urlpatterns = [
    path('Usuarios/', views.register, name='Usuarios'),
    path('Precios/', views.precios, name='Precios'),
    re_path(r'^editarusu/(?P<id>\d+)$', views.editar, name='editarusu'),
    re_path(r'^editarprec/(?P<id>\d+)$', views.preciosEditar, name='editarprec'),
    re_path(r'^editarprecpaq/(?P<id>\d+)$', views.preciosEditarPaquete, name='editarprecpaq'),

    re_path(r'^eliminar/(?P<id>\d+)$', views.eliminar, name='eliminar'),
]