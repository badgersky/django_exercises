from football_app.views import league_table, games_played
from django.urls import path


urlpatterns = [
    path('table/', league_table),
    path('games/<team_id>/', games_played)
]
