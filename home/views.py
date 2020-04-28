from django.shortcuts import render
from .models import Post
from products.models import Game


def index(request):
    """A view that displays the index page"""
    games = Game.objects.filter(discount=True)

    return render(request, 'home/index.html', {'games': games})


def about(request):
    """A view that displays the about page"""
    posts = Post.objects.all()

    return render(request, 'home/about.html', {'posts': posts})
