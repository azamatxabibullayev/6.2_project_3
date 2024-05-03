from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.name, self.author


class Comic(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'Comics'

    def __str__(self):
        return self.name, self.author
