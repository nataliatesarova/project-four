from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(Recipe, RecipeAdmin)
