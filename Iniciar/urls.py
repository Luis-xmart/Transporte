from django.urls import path

from ProyectoWebApp import views
from . import views

urlpatterns = [
    path('', views.login1, name="login"),
]