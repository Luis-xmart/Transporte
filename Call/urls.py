from django.urls import path
from . import views

urlpatterns = [
    path('Call/', views.call, name='Call'),
]