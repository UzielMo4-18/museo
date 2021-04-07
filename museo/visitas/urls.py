from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('Entrada', Entrada.as_view(), name='Entrada'),
    path('Salida', Salida.as_view(), name='Salida'),
]