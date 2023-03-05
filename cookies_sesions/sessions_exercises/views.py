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
    if request.method == 'GET':
        return render(request, 'session_exercises/delete_session.html')
    elif request.method == 'POST':
        session_name = request.POST['session']
        if session_name in request.session:
            del request.session[session_name]
            return HttpResponse(f'Session deleted')
        else:
            return HttpResponse(f'no such session: {session_name}')


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


def add_session(request):
    if request.method == 'GET':
        return render(request, 'session_exercises/add_session.html')
    elif request.method == 'POST':
        session_key = request.POST['key']
        session_value = request.POST['value']
        if session_key in request.session:
            return HttpResponse(f'session already exists')
        else:
            request.session[session_key] = session_value
            return HttpResponse(f'session created')


def show_multi_sessions(request):
    if len(dict(request.session)) == 0:
        return redirect('add_session')
    else:
        sessions = request.session
        return render(request, 'session_exercises/show-sessions.html', context={'sessions': sessions})