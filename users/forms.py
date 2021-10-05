from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'

class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        exclude = ('first_name', 'last_name',)
       
