from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


admin.site.register(Recipe, RecipeAdmin)
