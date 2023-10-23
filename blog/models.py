from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.conf import settings


# Define possible status choices for the Recipe model.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField("Title", max_length=200, unique=True)
    slug = models.SlugField("Slug", max_length=200, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('feature_image', default='placeholder')
    excerpt = models.TextField(blank=True)
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
        super(Recipe, self).save(*args, **kwargs)


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
    # DateTimeField named 'created_on' that automatically sets the current date and time when a new comment is created.
    created_on = models.DateTimeField(auto_now_add=True)
    # Create a boolean field named 'approved' with a default value of False which can be used to indicate if the comment has been approved or not.
    is_edited = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    status = models.CharField(
        choices=COMMENT_STATUS_CHOICES, default='pending', max_length=20)

    # Comments will be sorted by ascending order (oldest comments first).
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    # Total comments
    def total_comments(self):
        return self.comments.count()
