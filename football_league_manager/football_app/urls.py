from football_app.views import league_table
from django.urls import path


urlpatterns = [
    path('table/', league_table),
]
