from django.shortcuts import render
from manage_movies.utils import load_movies


def view_listed_movies(request):
    movies = load_movies()
    return render(request, 'manage_movies/list_movies.html', context={'movies': movies})
