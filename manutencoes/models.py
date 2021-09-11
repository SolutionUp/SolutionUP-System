from django.db import models
from produtos.models import Contato, Externo

class Terceiro(Contato, Externo):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f'{self.id} - {self.nome}'