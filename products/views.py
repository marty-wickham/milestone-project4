from django.shortcuts import render, get_object_or_404
from .models import Game

# Create your views here.


def all_games(request):
    """Create a view that will return a list of all of the games available to
    buy and render them to the games.html template"""
    games = Game.objects.all()
    return render(request, 'products/games.html', {'games': games})


def game_details(request, pk):
    """Create a view that will return a single game from the databse based on
    the primary key and render it to the game-details.html page, or return a
    404 error if not found"""
    game = get_object_or_404(Game, pk=pk)
    game.save()
    return render(request, 'products/games-details.html', {'game': game})
