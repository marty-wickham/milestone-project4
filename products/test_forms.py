from django.test import TestCase
from .forms import ReviewForm
from .models import Review
from .test_models import create_game, create_user, create_review


class TestReviewForm(TestCase):

    def test_valid_form(self):
        review = create_review(self)
        data = {"title": review.title, "content": review.content,
                "rating": review.rating, "date_posted": review.date_posted,
                "game": review.game, "user": review.user}

        form = ReviewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        user = create_user(self)
        game = create_game(self)

        review = Review.objects.create(title="Test Title", content="",
                                       rating=5, user=user, game=game)

        data = {"title": review.title, "content": review.content,
                "rating": review.rating, "date_posted": review.date_posted,
                "game": review.game, "user": review.user}

        form = ReviewForm(data=data)
        self.assertFalse(form.is_valid())

    def test_correct_error_message_for_missing_content(self):
        user = create_user(self)
        game = create_game(self)
        data = {"title": "Test Review Form", "content": "", "rating": 5,
                "game": game, "user": user}
        form = ReviewForm(data=data)
        self.assertEqual(form.errors['content'], [u"This field is required."])
