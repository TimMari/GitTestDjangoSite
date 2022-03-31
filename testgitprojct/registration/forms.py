from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegUserForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'text_input'}))
    email = forms.EmailField(label='Ваш email', required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'pass_input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput({'class': 'pass_input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
