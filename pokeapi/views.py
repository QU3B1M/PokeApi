from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pokemon, PokeType
from .serializers import PokemonSerializer, PokeTypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    # def update(self, request, *args, **kwargs):
    #     req_poketype = request.data['poketype']
    #     if req_poketype not in PokeType.objects.all():
    #         poketype = PokeType.objects.create(type=req_poketype)
    #         serializer = PokeTypeSerializer(poketype)

    #     pokemon = Pokemon.objects.get(pokeid=request.data['pokeid'])
    #     pokemon.poketype = request.data['poketype']
    #     pokemon.pokename = request.data['pokename']
    #     pokemon.pokeid = request.data['pokeid']
    #     pokemon.save()
    #     serializer = PokemonSerializer(pokemon)

    #     response = {
    #         'message': 'Your pokemon were updated',
    #         'result': serializer.data
    #         }

    #     return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        poketype = request.data["poketype"]

        if poketype not in PokeType.objects.all():
            ptype = PokeType(type=poketype)
            ptype.save()
            pokemon = Pokemon.objects.create(
                pokeid=request.data["pokeid"], pokename=request.data["pokename"]
            )
            pokemon.poketype.add(ptype)

        serializer = PokemonSerializer(pokemon)
        response = {"message": "Your pokemon were created", "result": serializer.data}

        return Response(response, status=status.HTTP_201_CREATED)


class PokeTypesViewSet(viewsets.ModelViewSet):
    queryset = PokeType.objects.all()
    serializer_class = PokeTypeSerializer
