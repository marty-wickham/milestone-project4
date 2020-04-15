from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    """A view that displays the index page"""
    return render(request, 'home/index.html')


def about(request):
    """A view that displays the about page"""
    posts 
    context = {
        'posts': posts
    }
    return render(request, 'home/about.html', context)
