from django.shortcuts import render
from .models import Post
from products.models import Game


def index(request):
    """A view that displays the index page"""
    games = Game.objects.exclude(sale_price=0.00)
    posts = Post.objects.all()

    args = {'games': games,
            'posts': posts}

    return render(request, 'home/index.html', args)


def about(request):
    """A view that displays the about page"""
    posts = Post.objects.all()

    return render(request, 'home/about.html')
