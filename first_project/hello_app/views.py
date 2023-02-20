from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello Django!')


def say_personalized_hello(request, name):
    return HttpResponse(f'Hello, {name.title()}!')
