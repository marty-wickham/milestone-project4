from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Game, Review
from products.test_models import TestReviewModel


test_review_model = TestReviewModel


class TestViews(TestCase):

    def test_get_games_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/games.html")

    def test_get_game_details_page(self):
        game = Game.objects.create(name="Test Game", price=5,
                                   release_date="2012-12-12")

        page = self.client.get("/products/{0}/".format(game.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products/game-details.html")

    def test_get_game_details_page_for_game_that_does_not_exist(self):
        page = self.client.get("/products/1/")
        self.assertEqual(page.status_code, 404)

    # def test_valid_form(self):
    #     review = test_review_model.create_review()

    def test_create_review(self):
        response = self.client.post("/products/game-details/",
                                    {"title": "Test Review"})
        review = get_object_or_404(Review, pk=1)
        self.assertEqual(review.title, "Test Review")
