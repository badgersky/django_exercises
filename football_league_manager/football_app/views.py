from django.shortcuts import render
from football_app.models import Team
from django.http import HttpResponse


def league_table(request):
    teams = Team.objects.all().order_by('points').reverse()
    teams_dict = {pos: team for pos, team in enumerate(teams, start=1)}
    return render(request, 'football_app/view_league_table.html', {'teams': teams_dict})
