from django.db import models

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    valor = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=30, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=30, blank=False, null=False)
    link = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='images/produtos', blank=True, null=True)

    def __str__(self):
        return self.nome

class EntidadeExterna(models.Model): #Classe base, só as filhas terão tabela no banco de dados
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    ramo = models.CharField(max_length=50, blank=False, null=False)
    class Meta:
        abstract = True
        
class Fornecedor(EntidadeExterna):
    fornecedor_telefone = models.ManyToManyField("TelefoneFornecedor",verbose_name="Fornecedor Telefone",related_name="telefone_fornecedor")#N pra N 

    def __str__(self):
        return f"{self.id} - {self.nome}"

class TelefoneFornecedor(models.Model):
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.telefone

class Categoria(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome
