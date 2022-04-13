from django.urls import path
from . import views

urlpatterns = [
    path('Conductor/', views.conductor, name='Conductor'),
]