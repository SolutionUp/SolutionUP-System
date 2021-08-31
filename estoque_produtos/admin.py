from django.contrib import admin
from .models import *

class FornecedorAdmin(admin.ModelAdmin):
    ...

class TelefoneFornecedorAdmin(admin.ModelAdmin):
    ...

class CategoriaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(TelefoneFornecedor, TelefoneFornecedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)