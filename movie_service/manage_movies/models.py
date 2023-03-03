from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, related_name='director', on_delete=models.CASCADE)
    screenplay = models.ForeignKey(Person, related_name='screenplay', on_delete=models.CASCADE)
    starring = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField(null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    genre = models.ManyToManyField(Genre)


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.person.first_name
