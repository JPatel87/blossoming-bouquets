"""Imports from django and the bouquet model."""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Bouquet


def all_bouquets(request):
    """ Function to view all bouquets.

    Sorting and search queries also
    included.
    """

    bouquets = Bouquet.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('bouquets'))
            
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        bouquets = bouquets.filter(queries)
    
    context = {
        'bouquets': bouquets,
        'search_term': query,
    }

    return render(request, 'bouquets/bouquets.html', context)


def bouquet_detail(request, bouquet_id):
    """ Function to view individual bouquet detail."""

    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)

    context = {
        'bouquet': bouquet,
    }

    return render(request, 'bouquets/bouquet_detail.html', context)
