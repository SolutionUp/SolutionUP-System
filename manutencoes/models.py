from django.db import models
from produtos.models import Contato, Externo, Produto
from vendas.models import Funcionario

class Terceiro(Contato, Externo):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f'{self.id} - {self.nome}'

class Manutencao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(auto_now=False, blank=False, null=False)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, blank=False, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=False, null=True)
    terceiro = models.ForeignKey(Terceiro, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.produto}'