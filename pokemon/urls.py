from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokeapi/', include('pokeapi.urls')),
    path('auth/', include('usersapi.urls')),
]
    