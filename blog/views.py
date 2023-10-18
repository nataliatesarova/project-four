from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .forms import CommentForm


# class RecipeList(generic.ListView):
#     model = Recipe
#     queryset = Recipe.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 9

# view to display the recipes on index.html


def RecipeList(request):
    recipe_list = Recipe.objects.all()

    return render(request, 'index.html', {'recipe_list': recipe_list})

# Creating a New Recipe


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            # Automatically generate a slug based on the recipe's title
            recipe.slug = slugify(recipe.title)
            recipe.save()

            # Redirect to the recipe detail page nevim jestli ten slug je takhle??
            return redirect('recipes',)
            # recipe_slug=recipe.slug
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


# View recipe details
# def RecipeDetails(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)

#     context = {
#         'recipe': recipe
#     }
#     return render(request, 'recipe_details.html', {'recipe': recipe})

# neivm jestli je to dobre


def RecipeDetails(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Process and save the comment
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user  # Set the user who made the comment
            comment.save()
    else:
        comment_form = CommentForm()  # Create a new CommentForm instance

    context = {
        'recipe': recipe,
        'comment_form': comment_form,  # Include the comment form in the context
    }
    return render(request, 'recipe_details.html', context)


@login_required
def EditRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.user != recipe.author:
        pass
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            # Redirect to the recipe detail page
            return redirect('recipe_detail', recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'blog/edit_recipe.html', {'form': form, 'recipe': recipe})


# nevim jestli to je dobre

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Check if user is the recipe author
    if request.user == recipe.author:
        recipe.delete()
        # Redirect to home page
        return redirect('recipes')
    else:
        return redirect('recipe_detail', recipe_id=recipe.pk)
    return render(request, 'delete_recipe.html', {'recipe': recipe, 'form': form})


# class RecipeLike(View):

#     def post(self, request, recipe_id, *args, **kwargs):
#         recipe = get_object_or_404(Recipe, pk=recipe_id)
#         if recipe.likes.filter(id=request.user.id).exists():
#             recipe.likes.remove(request.user)
#         else:
#             recipe.likes.add(request.user)

#         return HttpResponseRedirect(reverse('recipe_detail', args=[recipe_id]))
