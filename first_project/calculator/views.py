from django.shortcuts import render
from django.http import HttpResponse


def add(request, number1, number2):
    try:
        return HttpResponse(f'{number1} + {number2} = {int(number1) + int(number2)}')
    except ValueError:
        return HttpResponse(f'invalid input: {number1}, {number2}')


def subtract(request, number1, number2):
    try:
        return HttpResponse(f'{number1} - {number2} = {int(number1) - int(number2)}')
    except ValueError:
        return HttpResponse(f'invalid input: {number1}, {number2}')


def multiply(request, number1, number2):
    try:
        return HttpResponse(f'{number1} * {number2} = {int(number1) * int(number2)}')
    except ValueError:
        return HttpResponse(f'invalid input: {number1}, {number2}')


def divide(request, number1, number2):
    try:
        return HttpResponse(f'{number1} / {number2} = {int(number1) / int(number2)}')
    except ValueError:
        return HttpResponse(f'invalid input: {number1}, {number2}')
    except ZeroDivisionError:
        return HttpResponse(f'You cannot divide by 0.')
