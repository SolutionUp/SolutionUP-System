from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from produtos.models import Contato, Produto
from users.models import User

class Clientes(Contato):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    data_nascimento = models.DateField()
    percentual_comissao = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Pedido(models.Model):
    STATUS_PEDIDO = (
        ("E", "Enviado"),
        ("R", "Realizado"),
        ("F", "Finalizado")
    )
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rastreio = models.CharField(max_length=30, blank=True, null=False)
    comprovante = models.ImageField(upload_to='images/comprovantes', blank=True, null=True)
    taxa_entrega = models.DecimalField(blank=True , null=True, default=0.00, max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_PEDIDO, blank=False, null=False)   
    cliente = models.ForeignKey(Clientes, related_name='pedido_cliente', null=False, blank=False, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return f'{self.id} - {self.cliente.nome}'

    def get_total_itens(self):
        itens = PedidoItem.objects.filter(pedido=self)
        return sum([item.get_total() for item in itens])

    def get_total(self):
        return float(self.get_total_itens() or 0) + float(self.taxa_entrega or 0)

    def get_valor_comissao(self):
        return float(self.funcionario.percentual_comissao or 0) / 100 * float(self.get_total_itens() or 0)

class PedidoItem(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=None, null=None)
    produto = models.ForeignKey(Produto, on_delete=DO_NOTHING, blank=None, null=None)
    quantidade = models.IntegerField(blank=False, null=False)
    
    def get_total(self):
        return self.produto.valor * self.quantidade

class ComissaoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    valor_comissao = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=False, blank=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.id} - {self.funcionario.nome}'