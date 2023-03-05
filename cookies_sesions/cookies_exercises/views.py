from django.shortcuts import render
from django.http import HttpResponse


def set_cookie(request):
    response = HttpResponse('Setting cookie')
    response.set_cookie('user', 'Barack Obama')
    return response


def view_cookie(request):
    if 'user' in request.COOKIES:
        user_cookie = request.COOKIES['user']
        return HttpResponse(f'Here is your cookie: {user_cookie}')
    else:
        return HttpResponse(f'No cookie named "user"')


def delete_cookie(request):
    response = HttpResponse('deleting you cookie')
    if 'user' in request.COOKIES:
        response.delete_cookie('user')
        return response
