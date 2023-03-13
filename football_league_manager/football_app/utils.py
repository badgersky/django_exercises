from football_app.models import Game, Team


def load_games_data():
    filename = 'games_teams_data/games.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip('\n')
            new_lines.append(list(map(int, line.split(', '))))
        return new_lines


def load_teams_data():
    filename = 'games_teams_data/teams.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            line = line.rstrip('\n')
            new_lines.append([line.split(', ')[0], int(line.split(', ')[1])])
        return new_lines
    

if __name__ == '__main__':
    print(load_games_data())
    print(load_teams_data())
