from django.urls import path, include
from vendas.views.funcionario_view import *

urlpatterns = [
    path('', FuncionarioListView.as_view(), name='listagem_funcionario'),
    path('adicionar', adicionar_funcionario, name='adicionar_funcionario'),
    path('alterar/<int:id>', alterar_funcionario, name='alterar_funcionario'),
    path('remover/<int:id>', remover_funcionario, name='remover_funcionario'),
    path('cargo/adicionar', adicionar_cargo, name='adicionar_cargo')
]