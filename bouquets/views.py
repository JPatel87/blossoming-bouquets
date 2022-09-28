"""Imports from django and the bouquet and category model."""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Bouquet
from .forms import BouquetForm


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


def add_bouquet(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = BouquetForm(request.POST, request.FILES)
        if form.is_valid():
            bouquet = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('bouquet_detail', args=[bouquet.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')    
    
    else:
        form = BouquetForm()
       
    template = 'bouquets/add_bouquet.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_bouquet(request, bouquet_id):
    """ Edit a product in the store """
    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)
    if request.method == 'POST':
        form = BouquetForm(request.POST, request.FILES, instance=bouquet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('bouquet_detail', args=[bouquet.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = BouquetForm(instance=bouquet)
        messages.info(request, f'You are editing {bouquet.name}')

    template = 'bouquets/edit_bouquet.html'
    context = {
        'form': form,
        'bouquet': bouquet,
    }

    return render(request, template, context)


def delete_bouquet(request, bouquet_id):
    """ Delete a product from the store """
    bouquet = get_object_or_404(Bouquet, pk=bouquet_id)
    bouquet.delete()
    messages.success(request, 'Bouquet deleted!')
    return redirect(reverse('bouquets'))