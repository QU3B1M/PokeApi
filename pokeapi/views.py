from rest_framework import viewsets
from rest_framework.response import Response
from .models import Pokemon, PokeType
from .serializers import PokemonSerializer, PokeTypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokeTypesViewSet(viewsets.ModelViewSet):
    queryset = PokeType.objects.all()
    serializer_class = PokeTypeSerializer
