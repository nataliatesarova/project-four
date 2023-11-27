from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.conf import settings
from bs4 import BeautifulSoup

# Define possible status choices for the Recipe model.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    ingredients = models.TextField()
    featured_image = CloudinaryField(
        'feature_image', default='https://res.cloudinary.com/dxtdvo8ix/image/upload/v1698401021/nc6mwhbwix6kpzfcix99.jpg')
    method = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    comments = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='Comment', related_name='recipe_comments')
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='blog_likes', blank=True)

    # Define the default ordering for recipes by creation date.
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    # Save slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Strip HTML tags for each field
        fields_to_strip = ['ingredients', 'description', 'method']

        for field_name in fields_to_strip:
            field_value = getattr(self, field_name, '')
            soup = BeautifulSoup(field_value, 'html.parser')
            setattr(self, field_name, soup.get_text())
            stripped_text = soup.get_text()

            # Preserve new lines in text
            cleaned_text = stripped_text.replace(
                '\r\n', '\n').replace('\r', '\n')
            setattr(self, field_name, cleaned_text)
        super().save(*args, **kwargs)


# Comment status choices
COMMENT_STATUS_CHOICES = [
    ('pending', 'Pending Review'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]

# Create a Comment model.


class Comment(models.Model):

    post = models.ForeignKey(
        Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    status = models.CharField(
        choices=COMMENT_STATUS_CHOICES, default='pending', max_length=20)

    # Comments will be sorted by ascending order.
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.text} by {self.user}"

    # Total comments
    def total_approved_comments(self):
        return Comment.objects.filter(post=self.post, status='approved').count()
