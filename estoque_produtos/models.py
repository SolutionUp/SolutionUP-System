from django.db import models

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    valor = models.DecimalField(blank=False, null=False, max_digits=7, decimal_places=2)
    tipo = models.CharField(max_length=30, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=30, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='images/produtos', blank=True, null=True)

    def __str__(self):
        return self.nome