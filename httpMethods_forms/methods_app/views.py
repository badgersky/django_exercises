from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def generate_number(request):
    if request.method == 'GET':
        try:
            start = int(request.GET['start'])
            end = int(request.GET['end'])
            bigger = max(start, end)
            smaller = min(start, end)
        except MultiValueDictKeyError:
            return HttpResponse('podałeś niepoprawne dane.')
        else:
            return HttpResponse(', '.join(str(i) for i in range(smaller, bigger + 1)))
    else:
        return HttpResponse(f'Nie rozumiem metody http: {request.method}')
