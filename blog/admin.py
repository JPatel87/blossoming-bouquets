from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """
    Post model view on django admin for admin user.
    """

    list_display = (
        'title',
        'slug',
        'date',
    )


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    """
    Comment model view on django admin for admin user.
    """

    list_display = (
        'post',
        'author',
        'date',
        'updated',
    )


admin.site.register(Comment, CommentAdmin)
