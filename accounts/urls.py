from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<str:username>/', views.profile_details, name='profile'),
    path('profile/update/<str:username>/', views.update_profile, name='edit_profile'),
]
