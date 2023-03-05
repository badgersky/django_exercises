from django.shortcuts import render, redirect
from django.http import HttpResponse


def set_session(request):
    if 'counter' in request.session:
        return HttpResponse('session already active')
    else:
        request.session['counter'] = 0
        return HttpResponse('session active')


def show_session(request):
    if 'counter' not in request.session:
        return HttpResponse(f'no session named: "counter"')
    else:
        session_value = request.session['counter']
        request.session['counter'] += 1
        return HttpResponse(f'active session: counter: {session_value}')


def delete_session(request):
    if 'counter' in request.session:
        del request.session['counter']
        return HttpResponse(f'Session deleted')
    else:
        return HttpResponse(f'no such session: "counter"')


def log_greet_user(request):
    if request.method == 'GET':
        if 'LoggedUser' in request.session:
            return HttpResponse(f'Hello again {request.session["LoggedUser"]}')
        else:
            return render(request, 'session_exercises/login.html')
    elif request.method == 'POST':
        name = request.POST['name']
        request.session['LoggedUser'] = name
        return HttpResponse(f'Hello {name.title}')
