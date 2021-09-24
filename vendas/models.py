from django.db import models
from produtos.models import Contato, Produto
from users.models import User

class Clientes(Contato):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)

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
    percentual = models.DecimalField(max_digits=5, decimal_places=2)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Pedido(models.Model):
    STATUS_PEDIDO = (
        ("E", "Enviado"),
        ("R", "Realizado"),
        ("F", "Finalizado"),
        ("C", "Cancelado")
    )
    id = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rastreio = models.CharField(max_length=30, blank=False, null=False)
    comprovante = models.ImageField(upload_to='images/comprovantes', blank=True, null=True)
    taxa_entrega = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_PEDIDO, blank=False, null=False)   
    cliente = models.ForeignKey(Clientes, related_name='pedido_cliente', null=False, blank=False, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produto, related_name='pedido_produto', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} - {self.cliente}'