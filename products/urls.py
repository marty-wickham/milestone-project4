from django.conf.urls import url
from .views import all_games, game_details

urlpatterns = [
    url(r'^$', all_games, name='all_games'),
    url(r'^(?P<pk>\d+)/$', game_details, name='game_details'),
]
