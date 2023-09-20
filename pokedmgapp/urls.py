from django.urls import path
from .views import pokedmgfunc2

urlpatterns = [
    path('dmg/', pokedmgfunc2, name='pokedmg'),

]