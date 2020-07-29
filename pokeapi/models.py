from django.db import models


class PokeType(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type


class Pokemon(models.Model):
    pokename = models.CharField(max_length=50)
    pokeid = models.IntegerField(primary_key=True)
    poketype = models.ManyToManyField(PokeType)

    class Meta:
        ordering = ['pokeid']
