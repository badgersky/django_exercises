from django.shortcuts import render
from manage_movies.utils import load_movies, load_move_by_id


def view_listed_movies(request):
    movies = load_movies()
    return render(request, 'manage_movies/list_movies.html', context={'movies': movies})


def view_movie_details(request, movie_id):
    movie = load_move_by_id(movie_id)
    return render(request, 'manage_movies/movie_details.html', context={'movie': movie})
