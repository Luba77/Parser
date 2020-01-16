import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://127.0.0.1/games'

def index(request):
    return render(request, 'main.html')

def category(request):
        return render(request, 'category.html')

def name_of_games(request):
        return render(request, 'name_of_games.html')

#Функция парсера
def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    # print(data)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'games/new_search.html', stuff_for_frontend)







