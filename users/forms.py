from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from django import forms

from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        exclude = ('first_name', 'last_name',)
       
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)