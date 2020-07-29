from rest_framework import serializers
from .models import Pokemon, PokeType


class PokemonSerializer(serializers.ModelSerializer):
    poketype = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = ('pokeid', 'pokename', 'poketype')


class PokeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokeType
        fields = ('id', 'type')
        