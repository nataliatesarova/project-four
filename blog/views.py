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
            messages.success(request, 'Recipe created successfully.')
        

            # Redirect to the recipe detail page
            return redirect('recipes')
        else:
            messages.error(request, 'Recipe creation failed. Make sure You have filled in all the fields.')

    else:
        form = RecipeForm()

    return render(request, 'blog/create_recipe.html', {'form': form})


# Recipe details


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = Comment.objects.filter(post=recipe, status="approved")
    # Approved comments for the recipe
    total_approved_comments = comments.count()
    total_pending_comments = 0
    is_logged_in = request.user.is_authenticated
    owner = False
    
    if is_logged_in:
        if request.user == recipe.author:
            owner = True

        if request.method == 'POST':
            text = request.POST.get('comment_text')
            Comment.objects.create(post=recipe, user=request.user, text=text, status='pending')
            messages.success(request, 'Your comment has been created successfully. It will be visible once the admin approves.')
            return redirect('recipe_detail', slug=slug)

        # Pending comments for the current user and recipe
        pending_comments = Comment.objects.filter(post=recipe, user=request.user, status='pending')
        total_pending_comments = pending_comments.count()  


    return render(request, 'blog/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'owner': owner, 'total_approved_comments': total_approved_comments, 'total_pending_comments': total_pending_comments })

# Edit recipe


@login_required
def EditRecipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'Recipe {recipe.title} was updated successfully.')
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
            messages.success(request, f'Recipe "{recipe.title}" was deleted successfully.')
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


# Todo Update and Delete Comments