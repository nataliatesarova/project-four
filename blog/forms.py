from django import forms
from .models import Recipe
from .models import Comment
from django_bleach.forms import BleachField


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients',
                  'method', 'featured_image', 'status']

    description = BleachField(
        allowed_tags=['p', 'br', 'b', 'i', 'u', 'ul', 'li'],
        allowed_attributes={'*': ['style']}
    )
    ingredients = BleachField(
        allowed_tags=['p', 'br', 'b', 'i', 'u', 'ul', 'li'],
        allowed_attributes={'*': ['style']}
    )

    method = BleachField(
        allowed_tags=['p', 'br', 'b', 'i', 'u', 'ul', 'li'],
        allowed_attributes={'*': ['style']}
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
