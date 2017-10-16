from django.db import models

class Author(models.Model):
   name = models.CharField(max_length=30)
   born_year = models.IntegerField()


class Category(models.Model):
   title = models.CharField(max_length=20)

class Book(models.Model):
   title = models.CharField(max_length=30)
   year = models.IntegerField()
   description = models.TextField(max_length=1000)
   authors = models.ManyToManyField(Author)
   category = models.ForeignKey(Category)
