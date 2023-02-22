from random import randint, choice
from exercises_app.models import Band
from string import ascii_lowercase


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


def get_bands_without_year():
    return Band.objects.filter(year=None)


def get_bands_without_genre():
    return Band.objects.filter(genre=-1)


def generate_article_content():
    content = [choice(ascii_lowercase) for _ in range(3000)]
    return ''.join(content)


def generate_title():
    name = [choice(ascii_lowercase) for _ in range(25)]
    return ''.join(name).title()


def generate_author_name():
    author_name = [choice(ascii_lowercase) for _ in range(20)]
    return ''.join(author_name).title()


if __name__ == '__main__':
    pass
