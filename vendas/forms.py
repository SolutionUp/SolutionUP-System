from django.db.models.fields import DateField
from django.forms import ModelForm, DateInput, Select, EmailInput, TextInput, NumberInput, Textarea, FileInput

from .models import Clientes, Cargo, Funcionario, Pedido

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
                'placeholder': 'E-mail'
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

class FormCargo(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {      
            'nome': TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Nome do cargo'
            })
        }

class FormFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Nome do funcionario'
            }),
            'cpf': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'CPF do funcionario',
                'maxlength': 14
            }),
            'data_nascimento': DateInput( 
                format=('%Y-%m-%d'),
                attrs={
                    'class': "form-control",
                    'type': 'date'
                }),
            'percentual': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Percentual'
            }),
            'usuario': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o usuário'
            }),
            'cargo': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o cargo'
            }),
        }

class FormPedido(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'rastreio': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Rastreio'
            }),
            'comprovante': FileInput(attrs={
                'class': "form-control me-2",
                'style': 'max-width: 300px;'
            }),
            'taxa_entrega': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Insira a taxa de entrega'
            }),
            'status': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o status'
            }),
            'cliente': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione o cliente'
            }),
            'produtos': Select(attrs={
                'class': "form-select",
                'placeholder': 'Selecione os produtos'
            })
        }
