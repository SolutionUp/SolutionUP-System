from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name="index"),
    path('adicionar', views.adicionar_produto, name="adicionar_produto"),
    path('alterar/<int:codigo>', views.alterar_produto, name="alterar_produto"),
    path('remover/<int:codigo>', views.remover_produto, name='remover_produto'),
]