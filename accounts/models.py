from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.contrib.auth import get_user_model


# create a custom user
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.Charfield(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


