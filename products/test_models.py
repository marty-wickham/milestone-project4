from django.test import TestCase
from .models import Game, Review
from accounts.models import User
from django.utils import timezone


def create_game(self, name="Test Game",
                description="Test to create a Game object.", price=5,
                genre="Action", works_on="Windows",
                release_date="2012-12-12", company="Test",
                video_url="some url."):

    return Game.objects.create(name=name, description=description,
                               price=price, genre=genre, works_on=works_on,
                               release_date=release_date, company=company,
                               video_url=video_url)


def create_user(self, username="Test User", password="test password"):
    return User.objects.create_user(username=username, password=password)


def create_review(self, title="Test title",
                  content="Test to create a Review object.", rating=5):

    user = create_user(self)

    game = create_game(self)

    return Review.objects.create(title=title, content=content,
                                 rating=rating, date_posted=timezone.now(),
                                 user=user, game=game)


class TestUserModel(TestCase):

    def test_can_create_user(self):
        user = create_user(self)
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.username, "Test User")


class TestGameModel(TestCase):

    def test_can_create_game(self):
        game = create_game(self)
        self.assertTrue(isinstance(game, Game))
        self.assertEqual(game.__str__(), game.name)


class TestReviewModel(TestCase):

    def test_create_review(self):
        review = create_review(self)
        self.assertTrue(isinstance(review, Review))
        self.assertEqual(review.__str__(), review.title)
