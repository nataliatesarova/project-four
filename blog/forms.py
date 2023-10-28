from django import forms
from .models import Recipe
from .models import Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'content', 'featured_image', 'excerpt',
                  'status',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
