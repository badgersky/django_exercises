from django.shortcuts import render
from exercises_app.utils import get_published_articles, get_band
from django.views import View
from exercises_app.models import Band
from django.http import HttpResponse


def show_published_articles(request):
    return render(
        request,
        'exercises_app/articles.html',
        context={'articles': list(get_published_articles())}
        )


def show_band_data(request, band_id):
    band = get_band(band_id)
    return render(request, 'exercises_app/bands.html', context={
        'band': band,
        })


class AddBand(View):
    def get(self, request):
        genres = Band.Genre
        return render(request, 'exercises_app/get_band_info.html', context={'genres': genres})

    def post(self, request):
        name = request.POST['name']
        year = int(request.POST['year'])
        is_active = request.POST['still_active']
        if is_active == 'True':
            still_active = True
        else:
            still_active = False
        genre = request.POST['genre']
        Band.objects.create(name=name, year=year, still_active=still_active, genre=genre)
        return HttpResponse(f'Band added')
