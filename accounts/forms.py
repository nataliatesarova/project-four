from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Profile

# User registration form


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
# Login form


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser

# Editing user profile


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'first_name', 'last_name']
