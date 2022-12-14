""" Imports from django and bouquet model. """
from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
)
from django.contrib import messages
from bouquets.models import Bouquet


def view_bag(request):
    """
    Render bag contents page.
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add quantity of the specified bouquet to bag.
    """

    bouquet = get_object_or_404(Bouquet, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {bouquet.name} quantity to {bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {bouquet.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust quantity of specified bouquet to specified amount.
    """

    bouquet = get_object_or_404(Bouquet, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {bouquet.name} quantity to {bag[item_id]}'
            )
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {bouquet.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove bouquet from bag.
    """

    try:
        bouquet = get_object_or_404(Bouquet, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {bouquet.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
