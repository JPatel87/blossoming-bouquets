""" Imports from django and post and comment models. """
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(ModelAdmin):
    """
    Post model view on django admin.
    """

    list_display = (
        'title',
        'slug',
        'date',
    )


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    """
    Comment model view on django admin.
    """

    list_display = (
        'post',
        'author',
        'date',
        'updated',
    )
