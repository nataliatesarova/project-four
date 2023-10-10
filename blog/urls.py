from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RecipeList, name='recipes'),
    # Create recipe
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    # Recipe Detail
    # path('recipe/<int:recipe_id>/', views.RecipeDetails, name='recipe_detail'),
]
