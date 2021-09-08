from django import forms
from django.forms import ModelForm, SelectMultiple, Select, EmailInput, TextInput, NumberInput, Textarea, FileInput

from .models import Clientes

class FormCliente(ModelForm):

    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do cliente'
            }),
            'cpf': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'CPF do cliente'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'E-mail',
            }),        
            'telefone': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Telefone'
            }),
            'celular': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Celular'
            })
        }
