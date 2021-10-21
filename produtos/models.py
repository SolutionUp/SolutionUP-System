from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False, unique=True)
    valor = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=30, blank=False, null=True)
    link = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='images/produtos', blank=True, null=True)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.SET_NULL, blank=False, null=True)
    categoria = models.ForeignKey('CategoriaProduto', on_delete=models.SET_NULL, blank=False, null=True)
    quantidade = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return f'{self.codigo} - {self.nome}'

class CategoriaProduto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Externo(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    ramo = models.CharField(max_length=50, blank=False, null=True)

    class Meta:
        abstract = True
        
class Contato(models.Model):
    email = models.CharField(max_length=80, blank=False, null=False)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.telefone}'

class Fornecedor(Externo, Contato):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
