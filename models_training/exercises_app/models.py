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
