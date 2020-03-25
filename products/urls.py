from django.conf.urls import url
from .views import all_games

urlpatterns = [
    url(r'^$', all_games, name='all_games'),
]
