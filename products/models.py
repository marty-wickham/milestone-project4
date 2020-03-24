from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Game(models.Model):
    """Model migration for game product"""
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    INDIE = 'Indie'
    FANATASY = 'Fantasy'
    RPG = 'RPG'
    SIMULATOR = 'Simulator'
    SHOOTER = 'Shooter'
    SPORTS_AND_RACING = 'Sports and racing'
    STRATEGY = 'Strategy'

    WINDOWS = 'Windows'
    LINUX = 'Linux'
    MAC = 'Mac'

    GENRE_CHOICES = [
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (INDIE, 'Indie'),
        (FANATASY, 'Fantasy'),
        (RPG, 'RPG'),
        (SIMULATOR, 'Simulator'),
        (SHOOTER, 'Shooter'),
        (SPORTS_AND_RACING, 'Sports and racing'),
        (STRATEGY, 'Strategy')
    ]

    WORKS_ON_CHOICES = [
        (WINDOWS, 'Windows')
        (LINUX, 'Linux')
        (MAC, 'Mac')
    ]

    PEGI_RATING_CHOICES = [
        
    ]

    game = models.CharField(max_length=120, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images')
    genre = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=False)
    genre_two = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    genre_three = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    works_on = models.CharField(max_length=7, choices=WORKS_ON_CHOICES, blank=False)
    release_date = models.DateField()
    company = models.CharField(max_length=30)
    size = models.DecimalField(max_digits=3, decimal_places=1)
    pegi_rating = models.IntegerField()

    def avg_rating(self):
        sum = 0
        ratings = Review.objects.filter(Product=self)
        for rating in ratings:
            sum += rating

            return sum
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

        return total_ratings

    def __str__(self):
        return self.name


class Review(models.Model):
    """Model migration design for votes"""
    game = models.ForeignKey(Product, null=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(MinValueValidator(1), MaxValueValidator(5))
