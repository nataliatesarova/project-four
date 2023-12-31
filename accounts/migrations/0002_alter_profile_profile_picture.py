# Generated by Django 3.2.21 on 2023-11-14 00:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dxtdvo8ix/image/upload/v1699821909/uwmy2pkazv6ukhsknz3m.jpg', max_length=255, verbose_name='profile_picture'),
        ),
    ]
