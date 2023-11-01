from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile, CustomUser
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

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
    return render(request, 'accounts/registration/registration.html', {'form': form})

# User login view


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/registration/login.html', {'form': form})

# Profile details


@login_required
def profile_details(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    return render(request, 'accounts/profile/profile.html', {'user_profile': user_profile})

# update profile


@login_required
def update_profile(request, username):
    user = request.user  # Get the current user
    user_profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = EditProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            user.save()
            messages.success(
                request, "Profile information Updated Successfully.")

            # Redirect to the user's profile page
            return redirect('profile', username=username)

    else:
        form = EditProfileForm(instance=user_profile)
    form.fields['first_name'].initial = user.first_name
    form.fields['last_name'].initial = user.last_name
    return render(request, 'accounts/profile/update_profile.html', {'form': form})
