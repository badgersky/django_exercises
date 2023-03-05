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


def add_to_cookie(request):
    if request.method == 'GET':
        return render(request, 'cookies_exercises/add_to_cookie.html')
    if request.method == 'POST':
        response = render(request, 'cookies_exercises/add_to_cookie.html')
        cookie_name = request.POST['key']
        cookie_value = request.POST['value']
        response.set_cookie(cookie_name, cookie_value)
        return response


def view_all_cookies(request):
    user_cookies = request.COOKIES
    return render(request, 'cookies_exercises/show_all_cookies.html', context={'cookies': user_cookies})
