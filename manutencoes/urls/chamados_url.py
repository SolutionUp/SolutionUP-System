from django.urls import path, include
from manutencoes.views.chamado_view import *

urlpatterns = [
    path('', ChamadoListView.as_view(), name='listagem_chamado'),
    path('adicionar', adicionar_chamado, name='adicionar_chamado'),
    path('<int:pk>/', ChamadoDetailView.as_view(), name='detalhe_chamado'),
    path('alterar/<int:id>', alterar_chamado, name='alterar_chamado'),
    path('remover/<int:id>', remover_chamado, name='remover_chamado'),
]