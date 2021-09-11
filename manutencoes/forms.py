from django import forms
from django.forms import ModelForm, SelectMultiple, Select, EmailInput, TextInput, NumberInput, Textarea, FileInput

from .models import *

class FormTerceiro(ModelForm):
    class Meta:
        model = Terceiro
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
            'telefone': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Telefone'
            }),
            'celular': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Celular'
            }),
        }