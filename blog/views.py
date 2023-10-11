from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.decorators import login_required


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
            recipe.save()
            # Redirect to the recipe detail page
            return redirect('recipes')
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


# View recipe details
def RecipeDetails(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_details.html', {'recipe': recipe})

# Edit Recipe


@login_required
def EditRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.user != recipe.author:
        pass
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe.save()
            # Redirect to the recipe detail page
            return redirect('recipe_detail', recipe_id=recipe.pk)
        else:
            form = RecipeForm(instance=recipe)
        return render(request, 'blog/edit_recipe.html', {'form': form, 'recipe': recipe})


# nevim jestli to je dobre


# @login_required
# def delete_recipe(request):
#     if request.method == 'POST':
#         form = DeleteRecipeForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirmation']:
#             recipe.delete()
#             return redirect('recipes')
#     else:
#         form = DeleteRecipeForm()

#     return render(request, 'delete_recipe.html', {'recipe': recipe, 'form': form})
