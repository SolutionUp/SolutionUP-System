from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea, FileInput 

from .models import Produto

class FormProduto(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do produto'
            }),
            'valor': NumberInput(attrs={
                'class': "form-control", 
                'placeholder': 'R$',
                'step' : 0.01,
                'min' : 0
            }),
            'tipo': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o tipo'
            }),
            'descricao':  Textarea(attrs={
                'class': "form-control mt-3",
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
                'class': "form-control mb-3",
                'style': 'max-width: 300px;',
            }) 
        }       
