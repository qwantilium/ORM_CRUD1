from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)
    isbn = ISBNField(unique=True)

    def __str__(self):
        return self.title
