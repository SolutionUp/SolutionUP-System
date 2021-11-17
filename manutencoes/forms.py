import datetime
from django import forms
from django.forms import ModelForm, SelectMultiple, Select, EmailInput, TextInput, NumberInput, Textarea, FileInput, DateInput, ValidationError

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
            'telefone': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Telefone'
            }),
            'celular': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira o Celular'
            }),
        }

class FormManutencao(ModelForm):
    class Meta:
        model = Manutencao
        fields = '__all__'
        widgets = {
            'data_fim': DateInput( 
                format=('%Y-%m-%d'),
                attrs={
                    'class': "form-control",
                    'type': 'date'
            }),
            'responsavel': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o responsável'
            }),
            'produto': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o produto'
            }),
            'terceiro': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o terceiro'
            }),
            'descricao':  Textarea(attrs={
                'class': "form-control mt-3 mb-3",
                'placeholder': 'Insira a descrição da manutenção...',
                'style': 'resize: None;'
            }),
        }
    
    def data_conclusao_valid(self):
        return False if self.cleaned_data['data_fim']< datetime.date.today() else True 

class FormChamado(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormChamado, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)
        if instance.id:
            if (self.initial['status'] == 'F'):
                for field in ["mensagem", "pedido", "status", "tipo", "responsavel", "data_fim"]:
                    self.fields[field].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Chamado
        fields = '__all__'
        widgets ={
            'data_fim': DateInput( 
                format=('%Y-%m-%d'),
                attrs={
                    'class': "form-control",
                    'type': 'date'
            }),
            'responsavel': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o responsável'
            }),
            'tipo': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o tipo'
            }),
            'status': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o status'
            }),                        
            'pedido': Select(attrs={
                'class': "form-select",
                'placeholder': 'Pedido'
            }),
            'mensagem':  Textarea(attrs={
                'class': "form-control mt-3 mb-3",
                'placeholder': 'Descreva a descrição do chamado...',
                'style': 'resize: None;'
            }),
        }