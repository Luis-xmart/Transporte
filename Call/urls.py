from django.urls import path, re_path
from . import views

urlpatterns = [
    path('Call/', views.call, name='Call'),
    re_path(r'^editar/(?P<id>\d+)$', views.editar, name='editar'),

]