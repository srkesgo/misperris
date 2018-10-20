from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        #le diremos al formulario que debe guardar los datos
        #utilizando el modelo User
        model = User
        #le diremos al formulario en que orden mostrar cada campo
        fields = (
            'username',
         'first_name',
          'last_name',
          'email',
          'password1',
          'password2'
          )