from football_app.views import league_table, games_played, add_game
from django.urls import path


urlpatterns = [
    path('table/', league_table),
    path('games/<team_id>/', games_played, name='played_games'),
    path('add-game/', add_game)
]
