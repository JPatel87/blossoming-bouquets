"""Imports from django and the bouquet model."""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Bouquet
from django.db.models.functions import Lower


def all_bouquets(request):
    """ Function to view all bouquets.

    Sorting and search queries also
    included.
    """

    bouquets = Bouquet.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                bouquets = bouquets.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            bouquets = bouquets.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            bouquets = bouquets.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('bouquets'))
                
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            bouquets = bouquets.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    print('categories', categories)

    context = {
        'bouquets': bouquets,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'bouquets/bouquets.html', context)


def bouquet_detail(request, bouquet_id):
    """ Function to view individual bouquet detail."""

    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)

    context = {
        'bouquet': bouquet,
    }

    return render(request, 'bouquets/bouquet_detail.html', context)
