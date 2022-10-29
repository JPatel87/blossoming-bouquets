"""Imports from django, bouquet and category models."""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Bouquet, Category

@admin.register(Bouquet)
class BouquetAdmin(ModelAdmin):
    """
    bouquet model view for admin user.
    """

    list_display = (
        'name',
        'sku',
        'category',
        'price',
    )

    ordering = ('category',)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    """
    Category model view for admin user.
    """

    list_display = (
        'name',
    )
