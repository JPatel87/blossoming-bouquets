"""Imports from django and bouquet and category models."""
from django.contrib import admin
from .models import Bouquet, Category


class BouquetAdmin(admin.ModelAdmin):
    """
    bouquet model view on django admin for admin user.
    """

    list_display = (
        'name',
        'sku',
        'category',
        'price',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category model view on django admin for admin user.
    """

    list_display = (
        'name',
    )


admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Category, CategoryAdmin)
