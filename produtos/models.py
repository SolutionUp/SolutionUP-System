from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    valor = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=30, blank=False, null=True)
    link = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='images/produtos', blank=True, null=True)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.SET_NULL, blank=False, null=True)
    categoria = models.ForeignKey('CategoriaProduto', on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class CategoriaProduto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class Externo(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    ramo = models.CharField(max_length=50, blank=False, null=True)
    class Meta:
        abstract = True
        
class Fornecedor(Externo):

    def __str__(self):
        return f'{self.id} - {self.nome}'

class TelefoneFornecedor(models.Model):
    fornecedor = ForeignKey('Fornecedor', on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.telefone
