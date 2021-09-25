from django.urls import path, include
from manutencoes.views.manutencao_view import *

urlpatterns = [
    path('', ManutencaoListView.as_view(), name='listagem_manutencao'),
    path('adicionar', adicionar_manutencao, name='adicionar_manutencao'),
    path('<int:pk>/', ManutencaoDetailView.as_view(), name='detalhe_manutencao'),
    path('alterar/<int:id>', alterar_manutencao, name='alterar_manutencao'),
    path('remover/<int:id>', remover_manutencao, name='remover_manutencao'),
]