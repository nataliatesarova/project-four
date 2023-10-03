from django.shortcuts import render
from django.views import generic
from .models import Recipe


# class RecipeList(generic.ListView):
#     model = Recipe
#     queryset = Recipe.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 9

# view to display the recipes on index.html
def RecipeList(request):
    recipe_list = Recipe.objects.all()

    return render(request, 'index.html', {'recipe_list' : recipe_list})


