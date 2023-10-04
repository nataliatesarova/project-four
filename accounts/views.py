from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

# User registration page view


class RegisterView(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')



