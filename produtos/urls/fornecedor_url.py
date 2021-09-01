from django.urls import path, include
from produtos.views.fornecedor_view import FornecedorListView, FornecedorDetailView, adicionar_fornecedor, alterar_fornecedor, remover_fornecedor

urlpatterns = [
    path('', FornecedorListView.as_view(), name='listagem_fornecedor'),
    path('<int:pk>/', FornecedorDetailView.as_view(), name='detalhe_fornecedor'),
    path('adicionar', adicionar_fornecedor, name='adicionar_fornecedor'),
    path('alterar/<int:id>', alterar_fornecedor, name='alterar_fornecedor'),
    path('remover/<int:id>', remover_fornecedor, name='remover_fornecedor'),
]
