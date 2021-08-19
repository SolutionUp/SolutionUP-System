from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea

from .models import Produto

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Nome do produto'
            }),
            'valor': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'R$',
                'step' : 0.01,
                'min' : 0
            }),
            'tipo': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insira o tipo'
            }),
            'descricao':  Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insira a descrição'
            }),
            'marca': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Marca do produto'
            }),
            'link': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Insira o link do produto'
            })   
        }       
