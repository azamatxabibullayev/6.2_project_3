from django.db import models


# Create your models here.


class EBook(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'EBook'

    def __str__(self):
        return self.name, self.author


class Manga(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'Manga'

    def __str__(self):
        return self.name, self.author
