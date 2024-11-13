from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor


class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=200, required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    crm = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'crm', 'password1', 'password2']
