from django.shortcuts import get_object_or_404
from products.models import Game

def cart_contents(request):
    """ Ensure that cart contents are available when rendering every page"""

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        game = get_object_or_404(Game, pk=id)

        if game.sale_price:
            total += quantity * game.sale_price
        else:
            total += quantity * game.price

        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'game': game})

    return ({'cart_items': cart_items, 'total': total, 'product_count': product_count})
