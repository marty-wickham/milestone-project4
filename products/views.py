from django.shortcuts import render
from .models import Game

# Create your views here.


def all_games(request):
    games = Game.objects.all()
    return render(request, "games.html", {'games': games})
