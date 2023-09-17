from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Define possible status choices for the Recipe model.
STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts"
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    featured_image=CloudinaryField('image', default='placeholder')
    excerpt=models.TextField(blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)
    likes=models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # Define the default ordering for recipes by creation date.
    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # Create a Comment model.
    class Comment(models.Model):

        post=models.ForeignKey(
            Post, on_delete=models.CASCADE, related_name='comments')
        name=models.CharField(max_length=80)
        email=models.EmailField()
        body=models.TextField()
        # DateTimeField named 'created_on' that automatically sets the current date and time when a new comment is created.
        created_on=models.DateTimeField(auto_now_add=True)
        # Create a boolean field named 'approved' with a default value of False which can be used to indicate if the comment has been approved or not.
        approved=models.BooleanField(default=False)

        # Comments will be sorted by ascending order (oldest comments first).
        class Meta:
        ordering=['created_on']

        def __str__(self):
        return f"Comment {self.body} by {self.name}"
