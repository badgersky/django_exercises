from manage_movies.models import Person, Genre, Movie, PersonMovie


def generate_person_data():
    for i in range(15):
        first = 'name' + str(i)
        last = 'surname' + str(i)
        Person.objects.create(first_name=first, last_name=last)


def generate_genre_data():
    for i in range(15):
        genre_name = 'genre' + str(i)
        Genre.objects.create(name=genre_name)


def load_movies():
    movies = Movie.objects.order_by('year').reverse()
    return movies


def load_move_by_id(movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return movie
