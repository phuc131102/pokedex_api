from django.urls import path
from PokedexApp import views

"""
Define path for HTML pages
"""

urlpatterns=[
    path("", views.home, name="home"),
    path("add_pokemon", views.add_pokemon, name="add_pokemon"),
    path("add_type", views.add_type, name="add_type"),
    path("add_ability", views.add_ability, name="add_ability"),
    
    path("gen9", views.gen9, name="gen9"),
    path("type", views.type, name="type"),
    path("ability", views.ability, name="ability"),
    path("get_form", views.get_form, name="get_form"),
]