from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Review
from products.test_models import create_game, create_user


class TestViews(TestCase):

    def test_get_games_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/games.html")

    def test_get_game_details_page(self):
        game = create_game(self)

        page = self.client.get("/products/{0}/".format(game.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/game-details.html")

    def test_get_game_details_page_for_game_that_does_not_exist(self):
        page = self.client.get("/products/1/")
        self.assertEqual(page.status_code, 404)

    def test_post_create_review(self):
        game = create_game(self)
        user = create_user(self)

        response = self.client.post("/products/{0}/".format(game.id),
                                    data={"title": "Test Post Review",
                                          "content": "Here is some test content",
                                          "rating": 5, "game": game,
                                          "user": user})

        # review = get_object_or_404(Review, pk=1)
        # self.assertEqual(review.title, "Test Post Review")
        self.assertEqual(response.status_code, 200)
