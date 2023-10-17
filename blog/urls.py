from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RecipeList, name='recipes'),
    # Create recipe
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    # Recipe Detail
    path('recipe/<int:recipe_id>/', views.RecipeDetails, name='recipe_detail'),
    # Edit recipe
    path('edit_recipe/<int:recipe_id>/', views.EditRecipe, name='edit_recipe'),
    # Delete recipe
    path('recipe/<int:recipe_id>/delete/',
         views.delete_recipe, name='delete_recipe'),
    # Likes
    # path('recipe_like/<int:recipe_id>/',
    #      RecipeLike.as_view(), name='recipe_like'),
    # path('recipes/<slug:recipe_slug>/',
    #      views.recipe_detail, name='recipe_detail'),
]
