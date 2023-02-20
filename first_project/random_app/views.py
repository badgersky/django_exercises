from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def view_random_number(request):
    return HttpResponse(f'Random number between 0 and 100: {randint(0, 100)}')


def view_limited_random_number(request, max_number):
    try:
        max_number = int(max_number)
    except ValueError:
        return HttpResponse(f'Invalid input: {max_number}')
    return HttpResponse(f'Random number between 0 and {max_number}: {randint(0, max_number)}')


def view_random_number_between(request, min_number, max_number):
    try:
        x = int(max([max_number, min_number]))
        y = int(min([max_number, min_number]))
    except ValueError:
        return HttpResponse(f'Invalid input: {min_number}, {max_number}')
    return HttpResponse(f'Random number between {min_number}, {max_number}: {randint(y, x)}')
