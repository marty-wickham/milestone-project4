from django.test import TestCase
from .models import Game, Review


class TestGameModel(TestCase):

    def test_can_create_game(self):
        game = Game(name="game", description="some text")
        game.save()
        self.assertEqual(name="game")