from django.urls import path
from . import views
 
urlpatterns = [
    # O caminho vazio ('') será nossa página inicial
    path('', views.lista_colaboradores, name='lista_colaboradores'),
]