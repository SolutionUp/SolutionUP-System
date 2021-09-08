from django.urls import path, include
from vendas.views.cliente_view import ClienteListView, ClienteDetailView, adicionar_cliente, alterar_cliente, remover_cliente

urlpatterns = [
    path('', ClienteListView.as_view(), name='listagem_cliente'),
    path('adicionar', adicionar_cliente, name='adicionar_cliente'),
    path('alterar/<int:id>', alterar_cliente, name='alterar_cliente'),
    path('remover/<int:id>', remover_cliente, name='remover_cliente'),
]
