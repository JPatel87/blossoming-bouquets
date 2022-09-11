"""Imports from django and the bouquet model."""
from django.shortcuts import render
from .models import Bouquet


def all_bouquets(request):
    """ Function to view all bouquets.

    Sorting and search queries will also
    be included.
    """

    bouquets = Bouquet.objects.all()

    context = {
        'bouquets': bouquets,
    }

    return render(request, 'bouquets/bouquets.html', context)
