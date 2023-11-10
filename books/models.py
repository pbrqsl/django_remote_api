from collections.abc import Iterable
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250)
    # author = models.CharField(max_length=50)
    authors = ArrayField(
        models.CharField(max_length=100, blank=True, default=0, null=True), null=True
    )
    published_date = models.CharField(max_length=10, null=True)
    categories = ArrayField(models.CharField(max_length=150, null=True), null=True)
    thumbnail = models.URLField(null=True)
    average_rating = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    ratings_count = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if not Book.objects.filter(title=self.title):
            super().save(*args, **kwargs)


# "categories": [
#        "Baggins, Bilbo (Fictitious character)"
#      ],
#    "average_rating": 5,
#    "ratings_count": 2,
#    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
