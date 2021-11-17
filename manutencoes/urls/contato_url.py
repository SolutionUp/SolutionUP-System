from django.urls import path, include
from manutencoes.views.contato_view import *

urlpatterns = [
    path('', ContatoListView, name='listagem_contato')
]