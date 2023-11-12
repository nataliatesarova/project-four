from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.contrib.auth import get_user_model


# create a custom user
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

# create user profile


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('profile_picture', default='https://res.cloudinary.com/dxtdvo8ix/image/upload/v1699821909/uwmy2pkazv6ukhsknz3m.jpg')
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
# return the username

    def __str__(self):
        return str(self.user.username)
# check current user

    def check_user(self):
        return self.get.object().user == self.request.user
