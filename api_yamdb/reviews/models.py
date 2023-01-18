from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=50)


class Genres(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=50)


class Titles(models.Model):
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='title',
        null=True,
    )
    genre = models.ForeignKey(
        Genres,
        on_delete=models.SET_NULL,
        related_name='title',
        null=True,
    )
    name = models.CharField('Название', max_length=256)
    year = models.IntegerField('Год выпуска')
    description = models.TextField('Описание')
