from django.urls import path
from PokedexApp import views

"""
Define path for HTML pages
"""

urlpatterns=[
    path("", views.home, name="home"),
    path("add_pokemon", views.add_pokemon, name="add_pokemon"),
    path("add_type", views.add_type, name="add_type"),
    path("gen9", views.gen9, name="gen9"),
]