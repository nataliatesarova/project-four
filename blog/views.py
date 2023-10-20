from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .forms import RecipeForm, CommentEditForm
from .models import Recipe, Comment
from django.contrib.auth.decorators import login_required


def RecipeList(request):
    recipe_list = Recipe.objects.filter(status=1).order_by("-created_on")

    return render(request, 'blog/index.html', {'recipe_list': recipe_list})

# Creating a New Recipe


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            # Redirect to the recipe detail page
            return redirect('recipes',)
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


# Recipe details


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = Comment.objects.filter(post=recipe)

    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(post=recipe, user=request.user, text=text)
        return redirect('recipe_detail', slug=slug)

    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe, 'comments': comments})

# Edit recipe


@login_required
def EditRecipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            # Redirect to the recipe detail page
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'blog/edit_recipe.html', {'form': form, 'recipe': recipe})


# Delete recipe

@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    # Check if user is the recipe author
    if request.user == recipe.author:
        if request.method == 'POST':
            # Delete the recipe
            recipe.delete()
            # Redirect to home page
            return redirect('recipes')
    else:
        return redirect('recipe_detail', slug=recipe.slug)
    return render(request, 'recipe/delete_recipe.html', {'recipe': recipe})

    # Likes
    @login_required
    def like_recipe(request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if request.user in recipe.likes.all():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return redirect('recipe_detail', slug=slug)
