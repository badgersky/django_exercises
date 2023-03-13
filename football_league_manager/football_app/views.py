from django.shortcuts import render
from football_app.models import Team, Game
from django.http import HttpResponse


def league_table(request):
    teams = Team.objects.all().order_by('points').reverse()
    teams_dict = {pos: team for pos, team in enumerate(teams, start=1)}
    return render(request, 'football_app/view_league_table.html', {'teams': teams_dict})


def games_played(request, team_id):
    games_home = Game.objects.filter(team_home_id=team_id)
    games_away = Game.objects.filter(team_away_id=team_id)
    return render(request, 'football_app/view_played_games.html', {
        'games_home': games_home,
        'games_away': games_away,
        })

