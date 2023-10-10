from django.shortcuts import render
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

    return render(request, 'blog/create_recipe.html', {'form': form})
