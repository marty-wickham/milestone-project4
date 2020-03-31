from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add A quantity of the specifies product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] += int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('all_games'))


def adjust_cart(request, id):
    """Adjust the quantity of a specififc product in the cart"""
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if cart[id] > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
