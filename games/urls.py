from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('index', index),
    path('category', category),
    path('games/name_of_games', name_of_games),
    path('new_search', new_search),


]