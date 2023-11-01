from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients')
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title','description', 'ingredients']
    actions = ['publish_post', 'unpublish_post']

    def publish_post(self, request, queryset):
        queryset.update(status='1')

    def unpublish_post(self, request, queryset):
        queryset.update(status='0')


# Register the Recipe model with the RecipeAdmin configuration
admin.site.register(Recipe, RecipeAdmin)


class AdminComment(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('user', 'text', 'post', 'created_on', 'status')
    search_fields = ('name', 'email', 'text')
    actions = ['approve_comments', 'suspend_comments', 'delete_comments']

    def approve_comments(self, request, queryset):
        queryset.update(status='approved')

    def suspend_comments(self, request, queryset):
        queryset.update(status='pending')

    def delete_comments(self, request, queryset):
        queryset.delete()

 # Register the Comment model with the AdminComment configuration
admin.site.register(Comment, AdminComment)
