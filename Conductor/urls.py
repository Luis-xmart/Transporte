from django.urls import path, re_path
from . import views

urlpatterns = [
    path('Conductor/', views.conductor, name='Conductor'),
    re_path(r'^entregar/(?P<id>\d+)$', views.entregar, name='entregar'),
    # path('entregar/', views.entregar, name='entregar'),
]