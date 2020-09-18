from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """Add A quantity of the specifies product to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if id in list(cart.keys()):
        if cart[id] < 3:
            cart[id] += quantity
        else:
            messages.error(request, f"Max limit 3 per title.")
    else:
        cart[id] = quantity

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def adjust_cart(request, id):
    """Adjust the quantity of a specififc product in the cart"""
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
