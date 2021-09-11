from django.urls import path, include
from manutencoes.views.terceiro_view import TerceiroListView, adicionar_terceiro, alterar_terceiro, remover_terceiro

urlpatterns = [
    path('', TerceiroListView.as_view(), name='listagem_terceiro'),
    path('adicionar', adicionar_terceiro, name='adicionar_terceiro'),
    path('alterar/<int:id>', alterar_terceiro, name='alterar_terceiro'),
    path('remover/<int:id>', remover_terceiro, name='remover_terceiro'),
]