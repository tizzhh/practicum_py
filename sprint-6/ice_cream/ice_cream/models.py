from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Категории
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)


# Топпинги
class Topping(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


# Обёртки
class Wrapper(models.Model):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)


# Сорта мороженого
class IceCream(models.Model):
    is_published = models.BooleanField(default=True)
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
