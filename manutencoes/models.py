from django.db import models
from datetime import datetime
from produtos.models import Contato, Externo, Produto
from vendas.models import Funcionario
from vendas.models import Pedido
from vendas.models import Clientes

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

class Chamado(models.Model):
    STATUS_CHAMADO = (
        ('E', 'Em andamento'),
        ('F', 'Finalizado'),
        ('R', 'Recebido')
    )
    TIPO_CHAMADO = (
        ('C', 'Contato'),
        ('D', 'Devolução'),
        ('S', 'Suporte'),
        ('O', 'Outros'),
    )
    id = models.AutoField(primary_key=True)
    mensagem = models.TextField(blank=True, null=False, verbose_name='Mensagem')
    data_abertura = models.DateField(auto_now_add=True)
    data_fim = models.DateField(auto_now=False, blank=False, null=False)
    status = models.CharField(max_length=30, choices=STATUS_CHAMADO, verbose_name='Status', blank=False, null=False)
    pedido = models.ForeignKey(Pedido, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Pedido')
    responsavel = models.ForeignKey(Funcionario, null=False, blank=False, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=TIPO_CHAMADO, verbose_name='Tipo de chamado')

    def __str__(self):
        return f'{self.id} - {self.tipo}'