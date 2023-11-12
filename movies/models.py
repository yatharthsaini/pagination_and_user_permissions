from django.db import models


class Movie(models.Model):
    """
    model for creating a movie model it would store name of the movie and the rating associated with it
    """
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    rating = models.FloatField()

