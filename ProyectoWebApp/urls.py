from django.urls import path
from . import views

urlpatterns = [
    path('Base/', views.index, name='Base'),
]