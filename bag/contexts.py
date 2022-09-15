"""Imports from django."""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from bouquets.models import Bouquet


def bag_contents(request):
    """ Function to renders the bag contents. """

    bag_items = []
    total = 0
    bouquet_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        bouquet = get_object_or_404(Bouquet, pk=item_id)
        total += quantity * bouquet.price
        bouquet_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'bouquet': bouquet,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'bouquet_count': bouquet_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
