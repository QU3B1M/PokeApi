from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import PokemonViewSet, PokeTypesViewSet

router = routers.DefaultRouter()
# router.register('users', UserViewSet)
router.register('pokemons', PokemonViewSet)
router.register('poketypes', PokeTypesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
