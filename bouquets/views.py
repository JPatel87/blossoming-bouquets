"""Imports from django and the bouquet model."""
from django.shortcuts import render, get_object_or_404
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


def bouquet_detail(request, bouquet_id):
    """ Function to view individual bouquet detail."""

    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)

    context = {
        'bouquet': bouquet,
    }

    return render(request, 'bouquets/bouquet_detail.html', context)
