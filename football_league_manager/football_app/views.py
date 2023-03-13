from django.shortcuts import render, redirect
from football_app.models import Team, Game
from django.utils.datastructures import MultiValueDictKeyError
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


def add_game(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        return render(request, 'football_app/add_game.html', {'teams': teams})
    elif request.method == 'POST':
        try:
            team_home_name = request.POST['team_home']
            team_away_name = request.POST['team_away']
            if team_home_name == team_away_name:
                return HttpResponse('Team cannot play against itself')
            else:
                team_home = Team.objects.get(name=team_home_name)
                team_away = Team.objects.get(name=team_away_name)
                home_goals = int(request.POST['home_goals'])
                away_goals = int(request.POST['away_goals'])
        except MultiValueDictKeyError:
            return HttpResponse('Invalid input data')
        else:
            Game.objects.create(
                team_home=team_home,
                team_away=team_away,
                team_home_goals=home_goals,
                team_away_goals=away_goals
            )
            if home_goals > away_goals:
                team_home.points += 3
                team_home.save()
            elif home_goals == away_goals:
                team_home.points += 1
                team_away.points += 1
                team_home.save()
                team_away.save()
            elif away_goals > home_goals:
                team_away.points += 3
                team_away.save()
            return redirect('played_games', team_id=team_home.id)
