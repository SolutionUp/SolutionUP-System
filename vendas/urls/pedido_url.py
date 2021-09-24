from django.urls import path, include
from vendas.views.pedido_view import *

urlpatterns = [
    path('', PedidoListView.as_view(), name='listagem_pedido'),
    path('adicionar', adicionar_pedido, name='adicionar_pedido'),
    path('<int:pk>/', PedidoDetailView.as_view(), name='detalhe_pedido'),
    path('alterar/<int:id>', alterar_pedido, name='alterar_pedido'),
    path('remover/<int:id>', remover_pedido, name='remover_pedido'),
]