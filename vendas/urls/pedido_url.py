from django.urls import path, include
from vendas.views.pedido_view import PedidoListView, adicionar_pedido, alterar_pedido, remover_pedido

urlpatterns = [
    path('', PedidoListView.as_view(), name='listagem_pedido'),
    path('adicionar', adicionar_pedido, name='adicionar_pedido'),
    path('alterar/<int:id>', alterar_pedido, name='alterar_pedido'),
    path('remover/<int:id>', remover_pedido, name='remover_pedido'),
]