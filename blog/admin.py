from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Comment)

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
