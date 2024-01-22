from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'py-2 px-2 rounded'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'py-2 px-2 rounded'}))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username', 'class': 'py-2 px-2 rounded'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'py-2 px-2 rounded'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password', 'class': 'py-2 px-2 rounded'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your password', 'class': 'py-2 px-2 rounded'}))
