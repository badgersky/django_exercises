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


def generate_multiplication_tablet(request):
    if request.method == 'GET':
        try:
            width = int(request.GET['width'])
            height = int(request.GET['height'])
        except MultiValueDictKeyError:
            return HttpResponse('Wrong data')
        else:
            multiplication_table = []
            for n1 in range(1, height + 1):
                for n2 in range(1, width + 1):
                    multiplication_table.append(n1 * n2)

            table = [multiplication_table[i:i+width] for i in range(0, len(multiplication_table), width)]
            return render(request, 'methods_app/multiplication_table.html', context={'table': table})
    else:
        return HttpResponse(f'Unknown method: {request.method}')
