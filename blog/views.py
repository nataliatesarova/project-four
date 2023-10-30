from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .forms import RecipeForm, CommentForm
from .models import Recipe, Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from django.contrib import messages


def RecipeList(request):
    recipe_list = Recipe.objects.filter(status=1).order_by("-created_on")
    # Recipe Pages
    # Recipe Pages
    recipes_per_page = 9
    paginator = Paginator(recipe_list, recipes_per_page)
    page_number = request.GET.get('page')

    try:
        current_page = paginator.page(page_number)
    # show the first page if the page number is not an integer
    except PageNotAnInteger:
        current_page = paginator.page(1)
    # Empty page error
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'current_page': current_page})

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

    return render(request, 'blog/create_recipe.html', {'form': form})


# Recipe details


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = Comment.objects.filter(post=recipe, status="approved")

    owner = False
    if request.user == recipe.author:
        owner = True

    if request.method == 'POST':
        text = request.POST.get('comment_text')
        Comment.objects.create(post=recipe, user=request.user, text=text)
        return redirect('recipe_detail', slug=slug)

    return render(request, 'blog/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'owner': owner})

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
    return render(request, 'blog/delete_recipe.html', {'recipe': recipe})

# Likes


@login_required
def like_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect('recipe_detail', slug=slug)

# Comments


def post_comment(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    user_featured_image_url = request.user.featured_image.url

    if request.method == 'POST':
        text = request.POST.get('comment_text')
        # Comments are pending by default
        Comment.objects.create(
            post=recipe, user=request.user, text=text, status='pending')

        comments = Comment.objects.filter(post=recipe)

        return render(request, 'blog/recipe_detail.html', {'recipe': recipe, 'comments': comments,  'user_featured_image_url': user_featured_image_url})
    return redirect('recipe:recipe_detail', slug=slug, recipe=recipe, commmets=comments)
