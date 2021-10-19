from django.urls import path, include
from vendas.views.comissao_view import *

urlpatterns = [
    path('', ComissaoPedidoListView.as_view(), name='listagem_comissoes'),
    path('adicionar', adicionar_comissao, name='adicionar_comissao'),
    path('alterar/<int:id>', alterar_comissao, name='alterar_comissao'),
    path('remover/<int:id>', remover_comissao, name='remover_comissao')
]