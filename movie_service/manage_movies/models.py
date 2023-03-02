from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, related_name='director', on_delete=models.CASCADE)
    screenplay = models.ForeignKey(Person, related_name='screenplay', on_delete=models.CASCADE)
    starring = models.ManyToManyField(Person, through='PersonMovie')


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.ManyToManyField(Genre)
