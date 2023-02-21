from random import randint, choice


def load_bands():
    file_name = '/home/badgersky/Desktop/bands.txt'
    with open(file_name, 'r') as f:
        bands = f.read()
        return bands.split(',')


def generate_bands_data():
    year = randint(1960, 2010)
    genre = randint(0, 6)
    still_active = choice(['True', 'False'])
    return year, still_active, genre


if __name__ == '__main__':
    pass
