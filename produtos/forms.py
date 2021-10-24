from django import forms
from django.forms import ModelForm, SelectMultiple, Select, EmailInput, TextInput, NumberInput, Textarea, FileInput

from .models import *

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do produto'
            }),
            'quantidade': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Quantidade',
                'step' : 1
            }),
            'custo': NumberInput(attrs={
                'class': "form-control", 
                'placeholder': 'R$',
                'step' : 0.01,
                'min' : 0
            }), 
            'valor': NumberInput(attrs={
                'class': "form-control", 
                'placeholder': 'R$',
                'step' : 0.01,
                'min' : 0
            }),
            'descricao':  Textarea(attrs={
                'class': "form-control mt-3 mb-3",
                'placeholder': 'Insira a descrição do produto...',
                'style': 'resize: None;'
            }),
            'marca': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Marca do produto'
            }),
            'link': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o link do produto'
            }), 
            'imagem': FileInput(attrs={
                'class': "form-control me-2",
                'style': 'max-width: 300px;'
            }),
            'fornecedor': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o fornecedor'
            }),
            'categoria': Select(attrs={
                'class': "form-select",
            }),
            
        }       

class FormCategoriaProduto(ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = '__all__'
        widgets = {      
            'nome': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Nome da categoria'
            })
        }


class FormFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do fornecedor'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'E-mail'
            }),
            'ramo': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Ramo'
            }),
            'telefone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Telefone',
            }),
            'celular': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Celular',
            }),
        }
