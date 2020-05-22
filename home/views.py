from django.shortcuts import render
from .models import Post
from products.models import Game


def index(request):
    """A view that displays the index page"""
    games = Game.objects.exclude(sale_price=0.00)

    return render(request, 'home/index.html', {'games': games})


def about(request):
    """A view that displays the about page"""
    posts = Post.objects.all()

    return render(request, 'home/about.html', {'posts': posts})
