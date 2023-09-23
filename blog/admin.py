from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']


# Register the Recipe model with the RecipeAdmin configuration
admin.site.register(Recipe, RecipeAdmin)


class AdminComment(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


 # Register the Comment model with the AdminComment configuration
admin.site.register(Comment, AdminComment)
