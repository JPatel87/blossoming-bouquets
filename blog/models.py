"""Imports from django."""
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model for post database."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """Display post with most recent one first."""
        ordering = ['-date']

    def __str__(self):
        """Method to display post instance by its title."""
        return str(self.title)

    def snippet(self):
        """Display snippet of post instance."""
        return self.body[:50] + '...'


class Comment(models.Model):
    """Comment model for comment database."""
    post = models.ForeignKey(
        Post, related_name='comments',
        on_delete=models.CASCADE
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, default=None)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Display comment with oldest one first."""
        ordering = ['date']

    def __str__(self):
        """Display comment instance as comment title and author."""
        return f"{self.post.title} | {self.author}"
