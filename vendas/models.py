from django.db import models
from produtos.models import Contato
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