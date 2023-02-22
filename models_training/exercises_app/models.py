from django.db import models


class Band(models.Model):

    class Genre(models.IntegerChoices):
        NOT_DEFINED = -1
        ROCK = 0
        METAL = 1
        POP = 2
        HIP_HOP = 3
        ELECTRONIC = 4
        REGGAE = 5
        OTHER = 6

    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(null=True)
    genre = models.IntegerField(choices=Genre.choices, default=-1)

    def __str__(self):
        return f'{self.pk}, {self.name}, {self.year}'


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):

    class Status(models.IntegerChoices):
        STILL_WRITING = 0
        AWAITS_REVIEW = 1
        PUBLISHED = 2

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=Status.choices, default=0)
    start_date = models.DateField(null=True)
    stop_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.title}, {self.author}'


class Album(models.Model):

    class Rating(models.TextChoices):
        ZERO = ''
        ONE = '*'
        TWO = '*' * 2
        THREE = '*' * 3
        FOUR = '*' * 4
        FIVE = '*' * 5

    title = models.CharField(max_length=64)
    year = models.IntegerField()
    rating = models.CharField(choices=Rating.choices, max_length=5)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.rating}'
