from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pokemon, PokeType
from .serializers import PokemonSerializer, PokeTypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        re = request.data
        if not PokeType.objects.filter(type=re["poketype"]).exists():
            ptype = PokeType(type=re["poketype"])
            ptype.save()

        pokemon = Pokemon.objects.create(pokeid=re["pokeid"], pokename=re["pokename"])
        pokemon.poketype.add(PokeType.objects.get(type=re["poketype"]))
        serializer = PokemonSerializer(pokemon)
        response = {"message": "Your pokemon was created", "result": serializer.data}

        return Response(response, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        self.destroy(self.get_object())
        re = request.data

        if not PokeType.objects.filter(type=request.data["poketype"]).exists():
            ptype = PokeType(type=request.data["poketype"])
            ptype.save()
        else:
            ptype = PokeType.objects.get(type=request.data["poketype"])

        pokemon = Pokemon.objects.create(pokeid=re["pokeid"], pokename=re["pokename"])
        pokemon.poketype.add(PokeType.objects.get(type=re["poketype"]))
        serializer = PokemonSerializer(pokemon)
        response = {"message": "Your pokemon was updated", "result": serializer.data}

        return Response(response, status=status.HTTP_200_OK)


class PokeTypesViewSet(viewsets.ModelViewSet):
    queryset = PokeType.objects.all()
    serializer_class = PokeTypeSerializer
