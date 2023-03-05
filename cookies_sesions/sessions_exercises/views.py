from django.shortcuts import render
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
        return HttpResponse(f'active session: counter: {session_value}')


def delete_session(request):
    if 'counter' in request.session:
        del request.session['counter']
        return HttpResponse(f'Session deleted')
    else:
        return HttpResponse(f'no such session: "counter"')

