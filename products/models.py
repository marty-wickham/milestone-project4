from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Game(models.Model):
    """Model migration for game product"""
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Indie', 'Indie'),
        ('Fantasy', 'Fantasy'),
        ('RPG', 'RPG'),
        ('Simulator', 'Simulator'),
        ('Shooter', 'Shooter'),
        ('Sports and racing', 'Sports and racing'),
        ('Strategy', 'Strategy')
    ]

    WORKS_ON_CHOICES = [
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac', 'Mac'),
    ]

    PEGI_RATING_CHOICES = [
        ('3', '3'),
        ('7', '7'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18'),
    ]

    DISCOUNT_CHOICES = [(i, i) for i in range(5, 96, 5)]

    name = models.CharField(max_length=120, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images')
    genre = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=False)
    genre_two = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    genre_three = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    works_on = models.CharField(max_length=7, choices=WORKS_ON_CHOICES, blank=False)
    release_date = models.DateField()
    company = models.CharField(max_length=30)
    pegi_rating = models.CharField(max_length=2, choices=PEGI_RATING_CHOICES, blank=True)
    sale = models.BooleanField(blank=True, default=False)
    discount = models.IntegerField(blank=True, choices=DISCOUNT_CHOICES)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Model migration design for reviews"""
    STAR_CHOICES = [(i, i) for i in range(1, 6)]

    game = models.ForeignKey(Game, null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(choices=STAR_CHOICES, blank=False)

    def __str__(self):
        return self.title
