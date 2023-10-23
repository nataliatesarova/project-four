from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, 'user/registration.html', {'form': form})

# User login view


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = 'blog/index.html'
    success_message = 'You are Logged in! Welcome'
# Profile details


@login_required
def profile_details(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile/profile.html', {'user_profile': user_profile})

# Updating user profile


@login_required
def update_profile(request, username):
    user = request.user
    user_profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            # Update the custom user's first name and last name
            if request.POST.get('first_name') is not None:
                user.first_name = request.POST.get('first_name')

            if request.POST.get('last_name') is not None:
                user.first_name = request.POST.get('last_name')

            user.save()
            # Redirect to the user's profile page
            return redirect('profile', username=username)

    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'profile/update_profile.html', {'form': form})
