from football_app.models import Game, Team


def load_games_data():
    filename = '/home/badgersky/workspace/django_exercises/football_league_manager/football_app/games_teams_data/games.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip('\n')
            new_lines.append(list(map(int, line.split(', '))))
        return new_lines


def load_teams_data():
    filename = '/home/badgersky/workspace/django_exercises/football_league_manager/football_app/games_teams_data/teams.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip('\n')
            new_lines.append([line.split(', ')[0], int(line.split(', ')[1])])
        return new_lines


def insert_teams_data():
    for team in load_teams_data():
        Team.objects.create(name=team[0], points=team[1])


def insert_game_data():
    for game in load_games_data():
        Game.objects.create(
            team_home_id=game[0],
            team_home_goals=game[1],
            team_away_id=game[2],
            team_away_goals=game[3]
            )


if __name__ == '__main__':
    insert_game_data()
    insert_teams_data()
