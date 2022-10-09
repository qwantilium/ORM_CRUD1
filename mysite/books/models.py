from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    publisher = models.CharField(max_length=100)
    isbn = ISBNField()

    def __str__(self):
        return self.title
