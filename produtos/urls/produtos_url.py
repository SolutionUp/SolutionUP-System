from django.urls import path, include
from produtos.views.produtos_view import *

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listagem_produto'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('adicionar', adicionar_produto, name='adicionar_produto'),
    path('alterar/<int:codigo>', alterar_produto, name='alterar_produto'),
    path('remover/<int:codigo>', remover_produto, name='remover_produto'),
    path('categoria/adicionar', adicionar_categoria, name='adicionar_categoria'),
    path('relatorio/pdf', gerar_relatorio_pdf, name='relatorio_pdf'),
    path('relatorio/csv', gerar_relatorio_csv, name='relatorio_csv'),
]