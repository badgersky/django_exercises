from django.shortcuts import render
from exercises_app.utils import get_published_articles


def show_published_articles(request):
    return render(
        request,
        'exercises_app/articles.html',
        context={'articles': list(get_published_articles())}
        )
