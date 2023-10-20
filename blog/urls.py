from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RecipeList, name='recipes'),
    # Create recipe
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    # Recipe Detail
    path('recipe/<str:slug>/', views.recipe_detail, name='recipe_detail'),
    # Edit recipe
    path('edit_recipe/<str:slug>/', views.EditRecipe, name='edit_recipe'),
    # Delete recipe
    path('delete_recipe/<str:slug>/delete/',
         views.delete_recipe, name='delete_recipe'),
    # Likes
    path('recipes/<str:slug>/like/', views.like_recipe,
         name='like_recipe'),
    # Comments
    path('recipes/<str:slug>/comment/',
         views.post_comment, name='post_comment'),
]
