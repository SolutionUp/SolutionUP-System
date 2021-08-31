from django.urls import path, include
from estoque_produtos.views.produtos_view import ProdutoListView, ProdutoDetailView, adicionar_produto, alterar_produto, remover_produto

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listagem_produto'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('adicionar', adicionar_produto, name='adicionar_produto'),
    path('alterar/<int:codigo>', alterar_produto, name='alterar_produto'),
    path('remover/<int:codigo>', remover_produto, name='remover_produto'),
]