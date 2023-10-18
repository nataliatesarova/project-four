from django.shortcuts import render
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile, CustomUser
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.

# User registration page view


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user automatically
            login(request, user)
            # Create user profile
            Profile.objects.create(user=user)
            # Redirect to the homepage
            return redirect('recipes')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

# User login view


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = 'index.html'
