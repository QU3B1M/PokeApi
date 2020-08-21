from django.db import models
from django.core.validators import MinValueValidator


class PokeType(models.Model):
    type = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type


class Pokemon(models.Model):
    pokename = models.CharField(max_length=50)
    poketype = models.ManyToManyField(PokeType)
    pokeid = models.IntegerField(
        validators=[MinValueValidator(0)],
        primary_key=True)

    class Meta:
        ordering = ['pokeid']

    def __str__(self):
        return self.pokename
