from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.urls import re_path as urls

urlpatterns = [
    path('Despachador/', views.despachador, name='Despachador'),
    re_path(r'^asignar/(?P<id>\d+)$', views.asignar, name='asignar'),
    # path('asignar/<int:pk>', views.asignar, name='asignar'),
   
]