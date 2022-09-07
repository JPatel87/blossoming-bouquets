"""Imports from django."""
from django.db import models


class Category(models.Model):
    """
    Category model for bouquets.
    """

    class Meta:
        """
        Method to display category model as categories in admin view.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Bouquet(models.Model):
    """
    Bouquet model for bouquets.
    """
    category = models.ForeignKey(
        'Category', null=True,
        blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Method to display bouquet instance by its name.
        """
        return str(self.name)
