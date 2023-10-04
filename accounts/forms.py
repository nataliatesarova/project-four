from django import forms
from django.contrib.auth.forms import UserCreationForm

# User registration form


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



