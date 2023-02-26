from django.shortcuts import render
from exercises_app.utils import get_published_articles, get_band


def show_published_articles(request):
    return render(
        request,
        'exercises_app/articles.html',
        context={'articles': list(get_published_articles())}
        )


def show_band_data(request, band_id):
    band = get_band(band_id)
    band_name = band.name
    genre = band.genre
    year = band.year
    active = band.still_active
    return render(request, 'exercises_app/bands.html', context={
        'name': band_name,
        'genre': genre,
        'year': year,
        'active': active,
        })
