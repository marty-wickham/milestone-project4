from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Review
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.


def all_games(request):
    """Create a view that will return a list of all of the games available to
    buy and render them to the games.html template"""
    games = Game.objects.all()
    return render(request, 'products/games.html', {'games': games})


def game_details(request, pk):
    """Create a view that will return a single game from the databse based on
    the primary key and render it to the game-details.html page, or return a
    404 error if not found. This view will also return a list of reviews for
    this specific game, as well as a review form for users to add a their own
    review"""
    game = get_object_or_404(Game, pk=pk)
    reviews = Review.objects.filter(game=game)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=request.game)

        if review_form.is_valid():
            review_form.save()
            messages.success(request, f'Your review has been created!')
            return redirect('game_details')
    else:
        review_form = ReviewForm()

    return render(request, 'products/game-details.html', {
        'game': game,
        'reviews': reviews,
        'review_form': review_form
    })
