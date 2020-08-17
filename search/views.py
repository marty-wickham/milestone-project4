from django.shortcuts import render
from products.models import Game

# Create your views here.


def do_search(request):
    games = Game.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products/games.html", {"games": games})
