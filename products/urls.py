from django.urls import path
from .views import all_games, game_details

urlpatterns = [
    path('', all_games, name='all_games'),
    path('<int:pk>/', game_details, name='game_details'),
]
