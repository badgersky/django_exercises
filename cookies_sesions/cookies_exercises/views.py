from django.shortcuts import render
from django.http import HttpResponse


def set_cookie(request):
    response = HttpResponse('Setting cookie')
    response.set_cookie('user', 'Barack Obama')
    return response
