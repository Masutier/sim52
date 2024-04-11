from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class EnterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        exclude = ['username', 'password1', 'password2']

